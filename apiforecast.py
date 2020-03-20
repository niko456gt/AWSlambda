import urllib.request as internet
import json
import mysql.connector as sql
import datetime


pb = sql.connect(
	host="localhost",
	user="root",
	passwd="hardcore96",
	database="agro1"
)
mycursor = pb.cursor()

key = 'a573f34f1a2eb5dbdd1827f4de060e19'
polkey = '5db8f447ae8d9e0013fc226b'

url_fore = 'http://api.agromonitoring.com/agro/1.0/weather/forecast?appid=a573f34f1a2eb5dbdd1827f4de060e19&polyid=5db8f447ae8d9e0013fc226b'
call_fore = internet.urlopen(url_fore)
data_fore = json.load(call_fore)

url_temp = 'http://api.agromonitoring.com/agro/1.0/weather?polyid=5db8f447ae8d9e0013fc226b&appid=a573f34f1a2eb5dbdd1827f4de060e19'
call_temp = internet.urlopen(url_temp)
data_temp = json.load(call_temp)


dt0 = data_temp['dt']
#dt_local = time.strftime("%Y %b %d  %H:%M:%S ", time.localtime(dt0))
dt_local = datetime.datetime.utcfromtimestamp(dt0) - datetime.timedelta(hours=5, minutes=0)
main0 = data_temp['main']

dt3 = data_fore[0]
main3 = dt3['main']

dt6 = data_fore[1]
main6 = dt6['main']

dt9 = data_fore[2]
main9 = dt9['main']

dt12 = data_fore[3]
main12 = dt12['main']

dt15 = data_fore[4]
main15 = dt15['main']


#print(data_fore)

cel0 = main0['temp']-273.15
cel3 = main3['temp']-273.15
cel6 = main6['temp']-273.15
cel9 = main9['temp']-273.15
cel12 = main12['temp']-273.15
cel15 = main15['temp']-273.15




#0K − 273.15 = -273.1°C

print(dt_local)




try:
	ffdb = 'INSERT INTO forecast(finca_ID,date,current_temp,3h,6h,9h,12h,15h) VALUES(1,%s,%s,%s,%s,%s,%s,%s)'
	vals = [dt_local,cel0,cel3,cel6,cel9,cel12,cel15]
	mycursor.execute(ffdb,vals)
	pb.commit()
	print('insert complete')
except: 
	print('error')

