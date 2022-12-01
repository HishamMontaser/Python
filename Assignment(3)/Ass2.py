import csv


f1 = open ("GPS.csv" , "a+" , newline="")

Field_Description = ("Position" , "Field Name" , "Example Data" , "Description")

writer = csv.writer(f1)

writer.writerow(Field_Description)

Row_1 = (0 , "Sentence Type Identifier" , " $GPGGA " , "GGA Protocol header")

writer.writerow(Row_1)

Row_2 = (1 , " Time" , 170241 , "17:02:41 UTC")


writer.writerow(Row_2)

Row_3 = (2 , "Latiude" , 3401.21189 , "ddmm.mmmm format converts to 34.020196")


writer.writerow(Row_3)

Row_4 = (3,"Longitude Hempisphere" , "W" , "W=West , E=East")

writer.writerow(Row_4)

Row_5 = (4,"Number of Satellites" , "06" , "6 Satellites are in view")

writer.writerow(Row_5)
    







