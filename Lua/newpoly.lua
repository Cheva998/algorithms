local function newpoly(coefs)
	return function (x)
			local sum = coefs[1]
			local xn = 1
			for i=2, #coefs do
				xn = xn * x
				sum = sum + coefs[i] * xn
			end
			return sum
		end
end

local p1 = newpoly({1,1,1})
print(p1(2)) --> 7
local p2 = newpoly({1,0,1})
print(p2(2)) --> 5