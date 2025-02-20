from herbie import Herbie
import pandas as pd
import os

monthlist = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
yearstr = str(2024)

for i in range(6, 9):
    currentmonth = monthlist[i-1]
    print(currentmonth)
    if i < 10:
        monthstr = '0' + str(i)
    else:
        monthstr = str(i)

    # Adjust days based on month
    if i in [1, 3, 5, 7, 8, 10, 12]:  # Months with 31 days
        days_in_month = 31
    elif i == 2:  # February handling (not checking for leap year here)
        days_in_month = 28
    else:  # Months with 30 days
        days_in_month = 30

    for day in range(1, days_in_month + 1):
        if day < 10:
            daystring = '0' + str(day)
        else:
            daystring = str(day)
            
        for hour in range(0, 24):
            if hour < 10:
                hourstr = '0' + str(hour)
            else:
                hourstr = str(hour)
                
            print(yearstr, monthstr, daystring, hourstr)
            

            H = Herbie(yearstr+'-'+monthstr+'-'+daystring+' '+hourstr+':00',model='hrrr',product='sfc',fxx=12,save_dir='/eddy/s0/srh6060/data')
            H.inventory()   
            H.download("RH:2 m")
            dataset=H.xarray("RH:2 m")
            dataset.to_netcdf('/eddy/s0/srh6060/data/hrrr/'+yearstr+monthstr+daystring+'/'+hourstr+'Z'+daystring+currentmonth+yearstr+'.nc')
          #dataset.to_netcdf('/eddy/s0/srh6060/data/hrrr/'+yearstr+monthstr+daystring+'/'+hourstr+'Z'+daystring+monthlist[monthlist-1]+yearstr+'.nc')
