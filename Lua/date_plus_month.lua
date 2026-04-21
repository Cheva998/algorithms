
local function date_plus_one_month(year, month, day, hour, min, sec)
	-- Add one month to the given date and return the new date as a formatted string
	month = month + 1
	print(year, month, day, hour, min, sec)
	local time = os.time({year = year,
		month = month,
		day = day,
		hour = hour,
		min = min,
		sec = sec
	})
	return os.date("%A %d/%m/%Y - %H:%M:%S", time)
end

print(date_plus_one_month(2025, 4, 30, 15, 30, 36)) --> Friday 30/05/2025 - 15:30:36