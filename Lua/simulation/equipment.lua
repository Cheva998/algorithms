local Equipment = {}

function Equipment:new(o)
	o = o or {}
	self.__index = self
	setmetatable(o, self)
	return o
end

function Equipment:diffEquation(x)
	return x
end

function Equipment:solve(distance)
	local deltaT = 0.001
	local diffT = {}
	for i=0,distance,deltaT do
		diffT = self:diffEquation()
		self.Th = self.Th + diffT.dth * deltaT
		self.Tc = self.Tc + diffT.dtc * deltaT
	end
end

local HeatExchanger = Equipment:new()

function HeatExchanger:new(o)
	o = o or {}
	self.__index = self

	setmetatable(o, self)
	self.U = self.U or 10 --Overall heat transfer coefficient
	self.Cpc = self.Cpc or 4.18 --Calorific capacity of cold fluid
	self.Cph = self.Cph or 4.18 --Calorific capacity of hot fluid
	self.mh = self.mh or 1 -- Mass flow rate of hot fluid
	self.mc = self.mc or 1 --Mass flow rate of cold fluid
	self.P = self.P or 1 --Perimeter of heat exchanger
	self.Th = self.Th or 300 --Initial temperature of hot fluid
	self.Tc = self.Tc or 20 --Initial temperature of cold fluid
	return o
end

function HeatExchanger:diffEquation()
	local ah = self.U * self.P / (self.Cph * self.mh)
	local ac = self.U * self.P / (self.Cpc * self.mc)
	local dt = self.Th - self.Tc
	local diffT = {
		dth = - ah * dt,
		dtc = ac * dt
	}
	return diffT
end




local PFR = Equipment:new()

function PFR:new(o)
	o = o or {}
	self.__index = self
	setmetatable(o, self)
	self.k = self.k or 0.1 --Reaction rate constant
	self.u = self.u or 1 --Flow velocity
	self.CN2 = self.CN2 or 1 --Initial concentration of reactant N2
	self.CH2 = self.CH2 or 3 --Initial concentration of product H2
	self.CNH3 = self.CNH3 or 0 --Initial concentration of product NH3
	return o
end

function PFR:diffEquation()
	local r = self.k * self.CN2 * self.CH2 ^ 3 --Reaction rate
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


local heat = HeatExchanger:new({})
heat:solve(1)
print(heat.Th, heat.Tc)

local pfr = PFR:new({})
pfr:solve(1)
print(pfr.CN2, pfr.CH2, pfr.CNH3)