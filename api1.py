import urllib.request as internet
import json
import mysql.connector
import datetime

pb = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="hardcore96",
	database="agro1"
)
mycursor = pb.cursor()

key = 'a573f34f1a2eb5dbdd1827f4de060e19'
polkey = '5db8f447ae8d9e0013fc226b'

url_uvi = 'http://api.agromonitoring.com/agro/1.0/uvi?appid=a573f34f1a2eb5dbdd1827f4de060e19&polyid=5db8f447ae8d9e0013fc226b'
call_uvi = internet.urlopen(url_uvi)
data_uvi = json.load(call_uvi)

url_temp = 'http://api.agromonitoring.com/agro/1.0/weather?polyid=5db8f447ae8d9e0013fc226b&appid=a573f34f1a2eb5dbdd1827f4de060e19'
call_temp = internet.urlopen(url_temp)
data_temp = json.load(call_temp)

url_soil = 'http://api.agromonitoring.com/agro/1.0/soil?polyid=5db8f447ae8d9e0013fc226b&appid=a573f34f1a2eb5dbdd1827f4de060e19'
call_soil = internet.urlopen(url_soil)
data_soil = json.load(call_soil)

dt = data_soil['dt']
dt_local = datetime.datetime.utcfromtimestamp(dt) - datetime.timedelta(hours=5, minutes=0)
uvi = data_uvi['uvi']
temp_live = data_temp['main']
tempf = (temp_live['temp']-273.15)
t10 = (data_soil['t10']-273.15)
t0 = (data_soil['t0']-273.15)
ms = data_soil['moisture']



try:
	ffdb = 'INSERT INTO interne(tfinca_ID,Date,temp,uvi,t10,moisture,t0) VALUES(1,%s,%s,%s,%s,%s,%s)'
	vals = [dt_local,tempf,uvi,t10,ms,t0]
	mycursor.execute(ffdb,vals)
	pb.commit()
	print('insert complete')
except: 
	print('error')
