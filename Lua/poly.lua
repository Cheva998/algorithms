local function poly(coefs, x)
  local sum = coefs[1]
  local xn = 1
  for i=2, #coefs do
    xn = xn * x
    sum = sum + coefs[i] * xn
  end
  return sum
end

print(poly({1,1,1}, 2)) --> 7
print(poly({1,0,1}, 3)) --> 10
print(poly({1,2,3}, 4)) --> 57