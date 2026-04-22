

local function hamming(n)
	-- Function to calculate the number of ones in the binary representation of
	-- a positive integer
	if n < 0 then
		return 'Not a positive integer'
	end
	local hamming = 0
	while n > 0 do
		hamming = hamming + (n & 1)
		n = n >> 1
	end
	return hamming
end

print(hamming(1)) --> 1
print(hamming(7)) --> 3
print(hamming(-7)) --> Not a positive integer