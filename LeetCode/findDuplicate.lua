local a = {5, 1, 4, 2, 3, 3}

local function findDuplicate(array)
  --[[Find if the array has duplicates
  No extra memory used and no modifying the initial input
  ]]
  for i = 1, #a do
    for j = i + 1 , #a do
      if a[i] == a[j] then
        return true
      end
    end
  end
  return false
end

print(findDuplicate(a))