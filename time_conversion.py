def timeConversion(s):
    if s[-2:] == "AM" and s[:2] == "12": 
        return "00" + s[2:-2] 
    elif s[-2:] == "AM": 
        return s[:-2]
    elif s[-2:] == "PM" and s[:2] == "12": 
        return s[:-2] 
    else:
       converse = int(s[:2]) + 12
       return str(str(converse) + s[2:len(s)-2]) 
s = input()
result = timeConversion(s)
print(result)
       
    




# Sample Input 0
# 07:05:45PM

# Sample Output 0
# 19:05:45

# Example: s="12:01:00PM", return=> "12:01:00"
        #  s="12:01:00AM", return=>"00:01:00"


# Given a time in -hour AM/PM format, convert it to military (24-hour) time.

# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.