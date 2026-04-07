local function stopwords_list()
	-- Load stopwords from file into a table for quick lookup
	local stopwords = {}
	local file = io.open("./Lua/files/stopwords.txt", 'r')
	for word in file:lines() do
		stopwords[word] = 1
	end
	return stopwords
end

local function count_words(text)
	--[[ Count the frequency of each word in the text, excluding stopwords,
	and print them sorted by frequency and alphabetically.
	]]
	local count = {}
	local words = {}
	local stopwords = stopwords_list()
	for word in string.gmatch(text, "[%a']+") do
		count[word] = (count[word] or 0) + 1
	end
	for word in pairs(count) do
		if stopwords[word] == nil then
			words[#words + 1] = word
		end
	end
	table.sort(words, function(w1, w2)
		return count[w1] > count[w2] or
			count[w1] == count[w2] and w1 < w2
	end)
	
	for _, word in pairs(words) do
		print(word .. ': ' .. count[word])
	end
end

local text = "hello world, hi there, hello again, this isn't a test"
count_words(text)