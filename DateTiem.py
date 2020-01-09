import datetime
import pytz

print("...................Working with datetime functions with 'format' string method......................")

# working with datetime module using 'format' method
# if you use datetime.datetime function, you can print all Year,month,date,Hrs,Min.Sec
# my_date = datetime.datetime(2020, 4, 21, 12, 30, 45) # do not mention '0' with the date
# print(my_date)

# Change to March 05, 2019 date type
# tdy = '{:%B %d, %Y}'.format(my_date) # '%B- month / %d- date / %Y- Year'
# print(tdy)

# Ex: to find (April 21, 2020) fell on which day of the week and the year
# {:%A} = day of the week & {:%j} = day of the year
# tdy = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)
# if you run above command you will get an error coz, there are three place orders but we are passing on
# only one value to our format, so you have to index '0' with place orders in order to get it right
# print(tdy)
# print("")
print(".....................Working with datetime functions with 'f' string method.........................")
# working with datetime module using 'format' method
# Birth_day = datetime.datetime(1982, 11, 29)
# sentence = f'John has his B-day on {Birth_day:%B %d, %Y}'
# print(sentence)
# print("")
print(".....................Working with DateTime Module.........................")
# if you want to print out today's date
# print("Lets see the datetime.date function")
# if you use datetime.date function, you can print only Year,month,date
# tday = datetime.date.today()
# tday = f'{tday:%B %d, %Y}'
# print(tday)
# print(tday.year)# print out only the year
# print(tday.day)# print out only the date
# to print out the nuber of the date of the week (weekday =0-6 / isoweekday = 1-7)
# print(tday.weekday()) # we get vale '0' because in python Monday is '0' and Sunday is '6'
# print(tday.isoweekday())# in 'isoweekday' monday is '1' and Sunday is '7'
# print("")
# to check the differance between the dates or weeks using ('timedelta') command
# print("")
# print("Check what's the date from 7 days from today!!!")
# tday = datetime.date.today()
# tdelta = datetime.timedelta(days=7)
# print(tday + tdelta)
# print("Check what's the date from one week ago!!!")
# print(tday - tdelta)
# print("")
#date2 = date1 +/- timedelta 
#timedelta = date1 +/- date2 
# Ex: lets see howmany days left for my B-day
# bday = datetime.date(2020, 11, 29)
# till_bday = bday - tday
# print(till_bday)
# if you want only the days
# print(till_bday.days)
# if you want total seconds
# print(till_bday.total_seconds())
# print("")
# print("Lets see the datetime.time function")
# if you use datetime.time function, you can print only the Hrs,Mins.Secs
# lets set up fake local time elements are {Hrs.Min.Sec.Milsec}
# dt = datetime.time(10, 35, 22, 100000)
# print(dt)
# print(dt.hour)
# Lets continue with datetime module more further 
# it's better to use below function instead of accessing time & Date function seperately
# dt1 = datetime.datetime(2020, 1, 5, 10, 35, 22, 100000)
# tdelta = datetime.timedelta(hours=12, seconds=2)
# print(dt1 + tdelta)
# print("")
# dt_today = datetime.datetime.today() 	# returns current local datetime with a timezone of none
# dt_now = datetime.datetime.now() 		# gives an option to pass on to the timezone
# dt_utcnow = datetime.datetime.utcnow()	# UTC means Coordinated Universal Time, give current UTC time, but UTC
										# info is set none 
# print(dt_today)
# print(dt_now)
# print(dt_utcnow)
# print("")
# print(".....................Working with TimeZone with 'pytz' module.........................")
# dt1 = datetime.datetime(2020, 1, 5, 10, 35, 22, tzinfo = pytz.UTC)
# print(dt1) # you can see in the return valu there is a +00.00 with the datetime, it is UTC offset
# lets get the current UTC time that is also timezone aware
# One method with 'dt_now = datetime.datetime.now()'
# dt_now = datetime.datetime.now(tz = pytz.UTC)
# print(dt_now) # Now you can see current UTC time and some miliseconds add on there
# Second method with 'dt_utcnow = datetime.datetime.utcnow()'
# dt_utcnow = datetime.datetime.utcnow().replace(tzinfo = pytz.UTC)
# print(dt_utcnow) # You can see that you will get the same return as above
# print("")
# Lets first see all the timezones in all around the world using 'for' loop
# for tz in pytz.all_timezones:
# 	print(tz)

# lets see how we convert into a different timezone in 'utsnow'
# dt_utcnow = datetime.datetime.now(tz = pytz.UTC)
# print(dt_utcnow)
# dt_col = dt_utcnow.astimezone(pytz.timezone('Asia/Colombo'))
# print(dt_col)# you can see the my local time and UTC time  
# dt_QTR = dt_utcnow.astimezone(pytz.timezone('Etc/GMT+3'))
# print(dt_QTR)
# what exactly we did here is we took a timezone aware datetime and set to UTC and we converted that to my
# Time zone whatever it is
# what if we have naive datetime and set it to timezone aware 
'''
We call them "naive" because this datetime representation does not have a time zone. 
This means the datetime may not actually exist in certain areas in the world even though it is valid. 
For example, when daylight saving changes are applied by a region, the clock typically moves 
forward or backward by one hour.
'''
# dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
# print(dt_utcnow)
# dt_col = datetime.datetime.now()
# print(dt_col) # You can see i got my local time but not timezone aware means there is no timezone information
# but if i try to convert toanother timezoe, it gives me an error or not giving a expected result
# My be you might get an error saying that astimezone() cannot be applied to a naive datetime
# dt_lisbon = dt_col.astimezone(pytz.timezone('Europe/Lisbon'))
# print(dt_col)
# print("")
# In order to get it done, you have to 'localize you naive datetiem timezone aware' lets see how it goes
dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
# print(dt_utcnow)

dt_col = datetime.datetime.now()
col_tz = pytz.timezone('Asia/Colombo')

dt_col = col_tz.localize(dt_col)

dt_USC = dt_col.astimezone(pytz.timezone('US/Central'))
print(dt_col)# now you can see it's been localized where before it was a naive timezone aware 
print(dt_USC)	# you can see the timezone of US Central -6.00 Hrs behind where as colombo is +5.30 Hrs 
				# means (US Central is 11.30 Hrs behind Colombo Timezone)
				 
# lets print out the datetime with 'ISO format' or any format you like 
dt_col = datetime.datetime.now(tz=pytz.timezone('Asia/Colombo'))
print(dt_col.strftime('%B %d, %Y'))
# lets see the otherway arround means you have a tring and want to convert it to datetime
dt_str = 'May 25, 2019'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt) # You can see it converted into the datetime again
# strftime = Datetime to a string
# strptime = String to a Datetime

