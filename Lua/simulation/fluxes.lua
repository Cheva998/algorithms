-- Define the flux class, and the functions to get properties
local database = {
    cp = {
        H2 = 14.3, --KJ/kg K
        N2 = 1.04, --KJ/kg K
    }
}

---Get the colorific capacity for the compound, at a temperature and pressure
---@param compound string The name or code for the compound
---@param temperature number The temperature of the compound
---@param pressure number The pressure of the compound
---@return number cp The colorific capacity of the compound
local function get_cp(compound, temperature, pressure)
    return database.cp[compound]
end

---@class Flux
---@field private compounds table Table with the name or code of the compounds
---@field private temperature number Temperature of the flux
---@field private pressure number Pressure of the flux
local Flux = {}

---Method to instantiate a flux class
---@param o table Information of the flux
---@return Flux o Flux object
function Flux:new(o)
    self.__index = self
    setmetatable(o, self)
    self.compounds = o.compounds
    self.temperature = o.temperature
    self.pressure = o.pressure
    return o
end

---Method to return the compounds' table
---@return table compounds The table with the compounds:mass flux
function Flux:get_compounds()
    local new_compounds = {}
    for k, v in pairs(self.compounds) do
        new_compounds[k] = v
    end
    return new_compounds
end

---Method to return the temperature
---@return number temperature Temperature of the flux
function Flux:get_temperature()
    return self.temperature
end

---Method to return the pressure
---@return number pressure Pressure of the flux
function Flux:get_pressure()
    return self.pressure
end

---Method to set the new temperature
---@param t number New temperature
function Flux:set_temperature(t)
    self.temperature = t
end

---Method to set the new pressure
---@param p number New pressure
function Flux:set_pressure(p)
    self.pressure = p
end

---Method to set the new composition of the flux
---@param c table New composition
function Flux:set_compounds(c)
    self.compounds = c
end

---Method to get the calorific capacity of the flux
---@return number cp Calculated calorific capacity
function Flux:get_cp()
    local total_mass = 0
    local cp = 0
    for _, mass_flow in pairs(self.compounds) do
        total_mass = total_mass + mass_flow
    end
    
    for compound, mass_flow in pairs(self.compounds) do
        local cpi = get_cp(compound, self.temperature, self.pressure)
        cp = cp + cpi * (mass_flow / total_mass)
    end
    return cp
end

---Copy the values of a flux and returns a new flux with the same values
---@return table new_flux A new copy of the flux
function Flux:copy_flux()
    local new_data = {
        temperature = self.temperature,
        presure = self.pressure,
        compounds = self:get_compounds()
    }
    return new_data
end

local flux1 = Flux:new({compounds = {H2 = 3, N2 = 1}, temperature = 300, pressure = 1})
local data = flux1:copy_flux()
local flux2 = Flux:new(data)
flux2.compounds.H2 = 23
flux2.temperature = 1
return Flux