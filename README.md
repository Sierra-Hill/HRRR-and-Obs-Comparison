# HRRR-and-Obs-Comparison
Welcome to the host code for my Summer 2024 REU project. All code (except when noted) was written by me in python. A lot of the code is specified towards the specific project. I tried to generalize it when it proved useful and did not require too much rewriting. For example, a lot of the date ranges require the user to find the date range in the list then call the range needed within the list by the position of the range. If you as the user do what I did an trusted chatgpt to write out all of that instead of copy pasting 8*24 times, don't do it.....chatgpt changes the ranges on whim, even when you ask it ever so kindly not to. There are other quirks, and some quirks are in depth, so double check list lengths match and that the np.nan exclusion is working well if errors start to occur. Now, if you wanted to recreate the project how would you do that...
1) First you need a linux shell that can handle a lot of data depending on how much time you want to cover. Open python in the terminal and create an environment with the required python modules by Herbie (think numpy, netcdf4, stuff like that). Sometimes it likes to throw EECODES errors, basically it is running a depricated version of something, but it so far works as of February 2025. After this open up the **RHdownload.py** (initially written by Kevin Fletcher for other purposes, then heavily edited by me) script. Alter the date ranges to what you want it to be, and make sure to change the file path so that it pushes the data to your linux server and not mine :). A lot more in-depth information on how Herbie works is found on Brian Blaylock's, site, there is a whole host of how to call variables. The format follows a loose algorithm, but capitalization etc changes from variable to variable. Hit run and watch the magic happen. It should spend 5- 10 seconds per hour of HRRR data it is pulling. For my situation it took about 30 minutes to pull June 1st through August 31st. If it runs any faster than that it is not actually pulling any data, you need to go back to the script and fix something.
2) Now that you have the data in netcdf4 form you can use it like that, but it is nicer to deal with in csv form. The script **RHextract.py** (initially written by Kevin Fletcher for other purposes, then heavily edited by me) will pull the data into one csv that has stations as the rows and date:time in the columns. Now you can close your linux situation and open up jupyter notebooks (make sure you downloaded the csv files to a workspace that can be accessed by jupyter)
3) In my code I wrote a quick **csvtranspose.ipynb** script that allowed the user to transpose the csv so that it was easier to deal with. At this point in my coding knowledge I only knew how to call pandas dataframes by columns, so I needed the stations to be in columns and the date:time to be in the row. Run your files through this, making sure that you know where the resulting files are being stored and that you can call them back for future scripts.
4) To be continued....
