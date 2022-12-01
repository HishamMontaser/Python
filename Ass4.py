import pynmea2
import csv

Variable = pynmea2.parse("$GPGGA,184353.07,1929.045,S,02410.506,E,1,04,2.6,100.00,M,-33.9,M,,0000*6D", check=True)
print(Variable.latitude)
print(Variable.longitude)
print(Variable.lat_dir)
print(Variable.lon_dir)
print(Variable.timestamp)
print(Variable.gps_qual)
print(Variable.num_sats)
print(Variable.horizontal_dil)
print(Variable.altitude)
print(Variable.geo_sep)
print(Variable.ref_station_id)    



f1 = open ("GPS1.csv" , "a+" , newline="")

Field_Description = ("Position" , "Latitude" , "Longitude" , "Lat_dir" , "Lon_dir" , "timestamp" , "gpa_qual" , "num_stats" , "horizontal_dil" , "altitude" , "geo_sep" , "ref_station_id" )

writer = csv.writer(f1)

writer.writerow(Field_Description)

Row_1 = (0 , -19.4840833333334 , 24.1751 , 'S' , 'E' , '18:43:53.070000' , 1 , '04' , 2.6 , 100.0 , -33.9 , 0000)

writer.writerow(Row_1)
