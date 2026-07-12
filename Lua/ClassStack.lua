local ClassStack = {}

function ClassStack:new(o)
	o = o or {}
	self.stack = {}
	self.__index = self
	setmetatable(o, self)
	return o
end

function ClassStack:isEmpty()
	return #self.stack == 0
end

function ClassStack:push(item)
	table.insert(self.stack, item)
end

function ClassStack:pop()
	local item = self.stack[#self.stack]
	table.remove(self.stack, #self.stack)
	return item
end

local stack = ClassStack:new()

print(stack:isEmpty()) -- true
stack:push(2)
stack:push(1)
print(stack:pop()) --1
print(stack:isEmpty()) --false
print(stack:pop()) --2