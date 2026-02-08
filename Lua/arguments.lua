local function arguments(...)
	print('vars ... ', ...)
	local a, b, c = ...
	print('a: ', a, 'b: ', b, 'c: ', c)
	local arg = table.pack(...)
	print('arg pack: ', arg)
	print('arg unpack', table.unpack(arg))
	return select(2, ...)
end

local function unpack(t, i, f)
	i = i or 1
	f = f or #t
	if i <= f then
		return t[i], unpack(t, i + 1, f)
	end
end
print('Testing arguments function')
print(arguments(1, 2, 3, 4))
print('\nTesting unpack functions')
print(unpack({1, 2, 3, 4}, 1, 3)) --> 1 2 3
print(unpack({1, 2, 3, 4}, 2, 4)) --> 2 3 4