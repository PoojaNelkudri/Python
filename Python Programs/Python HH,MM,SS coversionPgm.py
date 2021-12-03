#Defining constant minute and hour
SECONDS_PER_MINUTE = 60
SECONDS_PER_HOUR= 3600
# taking number of seconds  as input from user 
seconds= int(input("Enter number of seconds:"))
#Calculating
hours= seconds /SECONDS_PER_HOUR
seconds = seconds % SECONDS_PER_HOUR
minutes = seconds / SECONDS_PER_MINUTE
seconds = seconds % SECONDS_PER_MINUTE
#printing in form of HH:MM:SS
print("The duration is: ",":%02d:%02d:%02d"%(hours,minutes,seconds))         
