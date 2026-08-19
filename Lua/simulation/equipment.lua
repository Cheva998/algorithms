local Flux = require('Lua.simulation.fluxes')

---@class Equipment Parent class for other equipments
local Equipment = {}

---Method to instantiate a equipment class
---@param o table Empty table
---@return table equipment New object of the equipment class  
function Equipment:new(o)
	o = o or {}
	self.__index = self
	setmetatable(o, self)
	return o
end

---Method with the differential equation (this is meant to be overwritten by the children classes)
---@param x number Point at which the diff eq is evaluated
---@return number x Value of the diff equation
function Equipment:diffEquation(x)
	return x
end

---Method to solve the differential equation
---@param distance number The distance to solve the diff eq
function Equipment:solve(distance)
	local deltaT = 0.001
	local diff = 0
	local prop = 0
	for i=0,distance,deltaT do
		diff = self:diffEquation(i)
		prop = prop + diff * deltaT
	end
end

---@class HeatExchanger: Equipment
local HeatExchanger = Equipment:new()

function HeatExchanger:new(o)
	o = o or {}
	self.__index = self
	setmetatable(o, self)

	self.U = self.U or 10 --Overall heat transfer coefficient
	self.perimeter = self.perimeter or 1 --Perimeter of heat exchanger
	self.hot_flux_in = o.hot_flux
	self.cold_flux_in = o.cold_flux
	local data = self.hot_flux_in:copy_flux()
	self.hot_flux_out = Flux:new(data)
	data = self.cold_flux_in:copy_flux()
	self.cold_flux_out = Flux:new(data)
	--------------------
	self.Cpc = self.cold_flux_out:get_cp() or 4.18 --Calorific capacity of cold fluid
	self.Cph = self.hot_flux_out:get_cp() or 4.18 --Calorific capacity of hot fluid
	self.mc = self.cold_flux_out:get_total_flux() or 1 --Mass flow rate of cold fluid
	self.mh = self.hot_flux_out:get_total_flux() or 1 -- Mass flow rate of hot fluid
	self.Tc = self.cold_flux_out:get_temperature() or 20 --Initial temperature of cold fluid
	self.Th = self.hot_flux_out:get_temperature() or 300 --Initial temperature of hot fluid
	----------------------------------
	return o
end

function HeatExchanger:diffEquation()
	local ah = self.U * self.perimeter / (self.Cph * self.mh)
	local ac = self.U * self.perimeter / (self.Cpc * self.mc)
	local dt = self.Th - self.Tc
	local diffT = {
		dth = - ah * dt,
		dtc = ac * dt
	}
	return diffT
end

function HeatExchanger:solve(distance)
	local deltaT = 0.001
	local diffT = 0
	local prop = 0
	for i=0, distance, deltaT do
		diffT = self:diffEquation()
		self.Th = self.Th + diffT.dth * deltaT
		self.Tc = self.Tc + diffT.dtc * deltaT
	end
	self.hot_flux_out:set_temperature(self.Th)
	self.cold_flux_out:set_temperature(self.Tc)
	return self.hot_flux_out, self.cold_flux_out
end

---@class PFR: Equipment
local PFR = Equipment:new()

function PFR:new(o)
	o = o or {}
	self.__index = self
	setmetatable(o, self)
	self.k = self.k or 0.1 --Reaction rate constant
	self.u = self.u or 1 --Flow velocity
	--------------------------------------
	self.flux_in = o.flux_in
	local data = self.flux_in:copy_flux()
	self.flux_out = Flux:new(self.flux_in)
	--------------------------------------
	self.CN2 = self.CN2 or 1 --Initial concentration of reactant N2
	self.CH2 = self.CH2 or 3 --Initial concentration of product H2
	self.CNH3 = self.CNH3 or 0 --Initial concentration of product NH3
	return o
end

function PFR:diffEquation()
	----Constants specific for Ammonia Synthesis----
	local A = 3.64 * 10 ^ 10 -- s^-1
	local Ea = 160000 -- J / mol
	------------------------------------------------
	local R = 8.314 -- J / (mol . K)
	local T = self.flux_out:get_temperature()
	local k = A * math.exp(-Ea / (R * T))
	local r = k * self.CN2 * self.CH2 ^ 3 --Reaction rate
	local dCN2 = - r / self.u
	local dCH2 = - 3 * r / self.u
	local dCNH3 = 2 * r / self.u
	local diffC = {
		dCN2 = dCN2,
		dCH2 = dCH2,
		dCNH3 = dCNH3
	}
	return diffC
end

function PFR:solve(distance)
	local deltaX = 0.001
	local diffC = {}
	for i=0,distance,deltaX do
		diffC = self:diffEquation()
		self.CN2 = self.CN2 + diffC.dCN2 * deltaX
		self.CH2 = self.CH2 + diffC.dCH2 * deltaX
		self.CNH3 = self.CNH3 + diffC.dCNH3 * deltaX
	end
end


local flux1n2h2 = Flux:new({compounds = {H2 = 3, N2 = 1}, temperature = 30 + 273.15, pressure = 1})
local flux2n2h2 = Flux:new({compounds = {H2 = 3, N2 = 1}, temperature = 300 + 273.15, pressure = 1})


local heat = HeatExchanger:new({hot_flux=flux2n2h2, cold_flux=flux1n2h2})
local flux3n2h2, flux4n2h2 = heat:solve(1)
print('-----Heat Exchanger-----')
print('Temp hot flux:', flux3n2h2:get_temperature(), 'K')
print('Temp cold flux:', flux4n2h2:get_temperature(), 'K')

----------------------
flux4n2h2:set_temperature(500 + 273.15)
---------------------

local pfr = PFR:new({flux_in = flux4n2h2})
pfr:solve(1)
print('\n---------Reactor---------')
print('Flux N2: ', pfr.CN2)
print('Flux H2: ', pfr.CH2)
print('Flux NH3:', pfr.CNH3)


