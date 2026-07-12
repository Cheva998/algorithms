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

local heat = HeatExchanger:new({})
heat:solve(1)
print(heat.Th, heat.Tc)