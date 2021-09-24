from datetime import datetime
import pytz

cal = pytz.timezone('us/pacific')
cali = datetime.now(cal)

h = str(cali.strftime("%H"))
m = str(cali.strftime("%M"))
data = str(cali.strftime("%D"))
if str(h) == '01':
    hour = 12
    apm = 'am'
elif str(h) == '02':
    hour = 1
    apm = 'am'
elif str(h) == '03':
    hour = 2
    apm = 'am'
elif str(h) == '04':
    hour = 3
    apm = 'am'
elif str(h) == '05':
    hour = 4
    apm = 'am'
elif str(h) == '06':
    hour = 5
    apm = 'am'
elif str(h) == '07':
    hour = 6
    apm = 'am'
elif str(h) == '08':
    hour = 7
    apm = 'am'
elif str(h) == '09':
    hour = 8
    apm = 'am'
elif str(h) == '10':
    hour = 9
    apm = 'am'
elif str(h) == '11':
    hour = 10
    apm = 'am'
elif str(h) == '12':
    hour = 11
    apm = 'pm'
elif str(h) == '13':
    hour = 12
    apm = 'pm'
elif str(h) == '14':
    hour = 1
    apm = 'pm'
elif str(h) == '15':
    hour = 2
    apm = 'pm'
elif str(h) == '16':
    hour = 3
    apm = 'pm'
elif str(h) == '17':
    hour = 4
    apm = 'pm'
elif str(h) == '18':
    hour = 5
    apm = 'pm'
elif str(h) == '19':
    hour = 6
    apm = 'pm'
elif str(h) == '20':
    hour = 7
    apm = 'pm'
elif str(h) == '21':
    hour = 8
    apm = 'pm'
elif str(h) == '22':
    hour = 9
    apm = 'pm'
elif str(h) == '23':
    hour = 10
    apm = 'pm'
elif str(h) == '24':
    hour = 11
    apm = 'pm'
hour = hour + 1

timezone = str(hour) + ":" + str(m) + apm + " on " + data
