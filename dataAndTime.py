import time
localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)



import calendar
cal = calendar.month(2023, 4)
print ("Here is the calendar:")
print (cal)