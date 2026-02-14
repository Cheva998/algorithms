local function read_all(handle)
	local lines = {}
	for line in handle:lines() do
		table.insert(lines, line)
	end
	return lines
end

local function write_all(handle, lines)
	for _, l in ipairs(lines) do
		handle:write(l, '\n')
	end

end

local function order_lines(read_file, write_file)
	local in_handle = io.stdin
	local out_handle = io.stdout
	if read_file then
		in_handle = io.open(read_file, 'r')
	else
		os.exit(1)
	end
	local lines = read_all(in_handle)
	table.sort(lines)
	if write_file then
		out_handle = io.open(write_file, 'w')
	end
	write_all(out_handle, lines)
end
local wl = require("./Lua/files/write_letter")
wl.write_letter(wl.file_name, wl.letter)
local out_file = "./Lua/files/sorted.txt"
order_lines(wl.file_name)
order_lines(wl.file_name, out_file)