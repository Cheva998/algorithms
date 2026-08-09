local database = {
    cp = {
        H2 = 14.3, --KJ/kg K
        N2 = 1.04, --KJ/kg K
    }
}

local function get_cp(compound, temperature, pressure)
    return database.cp[compound]
end

local Flux = {}

function Flux:new(o)
    self.__index = self
    setmetatable(o, self)
    self.compounds = o.compounds
    self.temperature = o.temperature
    self.pressure = o.pressure
    return o
end

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


local flux1 = Flux:new({compounds = {H2 = 3}, temperature = 300, pressure = 1})

print(flux1:get_cp())

local flux2 = Flux:new({compounds = {H2 = 3, N2 = 1}, temperature = 300, pressure = 1})

print(flux2:get_cp())