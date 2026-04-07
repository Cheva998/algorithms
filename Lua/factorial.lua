local function factorial (n)
	-- Calculate the factorial of n using recursion
	if n == 0 then
		return 1
	elseif n > 0 then
		return n * factorial(n - 1)
	else
		return n * factorial(n + 1)
	end
end

print("enter a number:")
local a = io.read("*n") -- reads a number
print(factorial(a))
