week_day = 1
month_week = 1
month_day = 1
month = 1
year = 1901

months = [[31,1],[28,2],[31,3],[30,4],[31,5],[30,6],[31,7],[31,8],[30,9],[31,10],[30,11],[31,12]]
count = 0
while year < 2001:
	week_day += 1
	if week_day == 8:
		week_day = 1
		month_week += 1
	month_day += 1
	if month_day > months[month-1][0]:
		if year%400 == 0 and month == 2:
			week_day += 1
		month += 1
		if month > 12:
			month = 1
			year += 1
			month_week = 1
		month_day = 1
		if week_day == 7:
			count += 1

print count

