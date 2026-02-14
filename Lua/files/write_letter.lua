local function write_letter(filename, content)
	local file = io.open(filename, "w")
	if file then
		file:write(content)
		file:close()
		print("Letter written to " .. filename)
	else
		print("Error opening file: " .. filename)
	end
end

local date = os.date("%Y-%m-%d")
local letter_content = [[
Some text goes here.
Best regards,
]]
local letter = date .. "\n\n" .. letter_content
local file_name = "./Lua/files/letter.txt"
return {
	write_letter = write_letter,
	file_name = file_name,
	letter = letter
}