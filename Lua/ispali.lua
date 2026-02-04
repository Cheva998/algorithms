local function ispali(text)
	for i = 1, #text // 2 do
		if text:sub(i,i) ~= text:sub(-i,-i) then
			return false
		end
	end
	return true
end

print(ispali("step on no pets")) --> true
print(ispali("hello")) --> false
print(ispali("racecar")) --> true