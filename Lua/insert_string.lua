local function insert_string(word, pos, str_to_insert)
	return word:sub(0, pos - 1) .. str_to_insert .. word:sub(pos, -1)
end

print(insert_string("hello", 1, "X: ")) --> prints "X: hello"
print(insert_string("hello", 2, "X: ")) --> prints "hX: ello"
print(insert_string("hello", 3, "X: ")) --> prints "heX: llo"
print(insert_string("hello", 4, "X: ")) --> prints "helX: lo"
print(insert_string("hello", 5, "X: ")) --> prints "hellX: o"
print(insert_string("hello", 6, "X: ")) --> prints "helloX:
