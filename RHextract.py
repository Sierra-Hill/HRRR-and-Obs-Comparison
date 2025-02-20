import netCDF4 as nc
import numpy as np

monthlist=['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
dataarray=np.empty([22,2208]) #number of sites plus 4 , number of hours of hrrr data
dataarray[:]=np.nan

counter=0
yearstr=str(2024)          
for i in range(6, 9):
    currentmonth = monthlist[i-1]
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
            try:

              fricvdata=nc.Dataset('/eddy/s0/srh6060/data/hrrrRH12/'+yearstr+monthstr+daystring+'/'+hourstr+'Z'+daystring+currentmonth+yearstr+'.nc')
              fricvdata=np.array(fricvdata['r2'])
              fricv_INc=(fricvdata[627, 1494])
              fricv_INg=(fricvdata[627, 1492])
              fricv_INa=(fricvdata[626, 1494])
              fricv_INe=(fricvdata[626, 1491])
              fricv_INb=(fricvdata[625, 1494])
              fricv_INj=(fricvdata[627, 1491])
          #fricv_INi=(fricvdata[627, 1494])
              fricv_INp=(fricvdata[632, 1489])
              fricv_BWa=(fricvdata[621, 1485])
              fricv_BWb=(fricvdata[625, 1491])
              fricv_a=(fricvdata[626, 1493])
              fricv_b=(fricvdata[629, 1492])
              fricv_d=(fricvdata[625, 1489])
              fricv_e=(fricvdata[626, 1492])
              fricv_f=(fricvdata[628, 1491])
              fricv_g=(fricvdata[625, 1495])
              fricv_h=(fricvdata[628, 1495])
              fricv_c=(fricvdata[628, 1494])
              fricv_i=(fricvdata[627, 1493])
              dataarray[0,counter]=fricv_INc
          
              dataarray[1,counter]=fricv_INg
          
              dataarray[2,counter]=fricv_INa
          
              dataarray[3,counter]=fricv_INe
          
              dataarray[4,counter]=fricv_INb
          
              dataarray[5,counter]=fricv_INj
          
          #dataarray[6,counter]=fricv_INi
          
              dataarray[6,counter]=fricv_INp
          
          
              dataarray[7,counter]=fricv_BWa
          
              dataarray[8,counter]=fricv_BWb
              dataarray[9,counter]=fricv_a
          
              dataarray[10,counter]=fricv_b
          
              dataarray[11,counter]=fricv_d
          
              dataarray[12,counter]=fricv_e
          
              dataarray[13,counter]=fricv_f
          
              dataarray[14,counter]=fricv_g

              dataarray[15,counter]=fricv_h
          
              dataarray[16,counter]=fricv_c
              dataarray[17,counter]=fricv_i
          
              dataarray[18,counter]=yearstr
              dataarray[19,counter]=i
              dataarray[20,counter]=day
              dataarray[21,counter]=hour
              counter+=1
          
          
            except Exception as e:
              print(e)
              dataarray[18,counter]=yearstr
              dataarray[19,counter]=i
              dataarray[20,counter]=day
              dataarray[21,counter]=hour
              counter+=1
              continue


np.savetxt('/eddy/s0/srh6060/data/hrrrRH12csv.csv',dataarray,delimiter=',')
