
local function split(text)
	local array = {}
	for word in string.gmatch(text, '%a+') do
		array[#array + 1] = word
	end
	return array
end

local text = 'Hello world, 21/02/2026'
print(string.sub(text, 7, 11)) --> world
print(string.find(text, 'world')) --> 7 11
print(string.match(text, 'world')) --> world
print(string.gsub(text, 'world', 'Lua')) --> Hello Lua, 21/02/2026 1 [The last number is the number of substitutions]
for word in string.gmatch(text, '%a+') do
	print(word)
end

local result = split(text)
for idx, word in ipairs(result) do
	print(idx, word)
end