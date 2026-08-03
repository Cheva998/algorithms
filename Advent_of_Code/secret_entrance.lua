

local function read_file(filename)
	local file = assert(io.open(filename, 'r'))
	return function()
		local line = file:read('*l')
		if line == nil then
			file:close()
		end
		return line
	end
end

local function get_code(filename)
	local code = 0
	local pos = 50
	local maxNumber = 100
	local conversion = {L=-1, R=1}
	local change
	local filename = filename or 'test_code.txt'
	for line in read_file(filename) do
		change = conversion[string.sub(line, 1, 1)] * tonumber(string.sub(line, 2))
		pos = (pos + change) % maxNumber
		if pos == 0 then
			code = code + 1
		end
		--print(line, pos)
	end
	return code
end

local function get_code_function_0x434C49434B(filename)
	local code = 0
	local pos = 50
	local maxNumber = 100
	local conversion = {L=-1, R=1}
	local sign, change
	local filename = filename or 'test_code.txt'
	for line in read_file(filename) do
		sign = conversion[string.sub(line, 1, 1)]
		change =  tonumber(string.sub(line, 2))
		local passes_0 = change // maxNumber
		local normalized_pos = pos
		local new_pos = (pos + (sign * change)) % maxNumber
		if pos ~= 0 then
			if sign > 0 then
				if (change % maxNumber) + pos >= maxNumber then
					passes_0 = passes_0 + 1
				end
			else
				if change % maxNumber >= pos then
					passes_0 = passes_0 + 1
				end
			end
		end
		pos = new_pos
		code = code + passes_0
	end
	return code
end

local code = get_code('./Advent_of_Code/codes/code.txt')

print(code)

local code_func = get_code_function_0x434C49434B('./Advent_of_Code/codes/code.txt')
print(code_func)

