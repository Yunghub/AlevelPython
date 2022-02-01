import time
from datetime import datetime

def timeInputs(car):
    if car == 1:
        carNum = "1st"
    elif car == 2:
        carNum = "2nd"
    while True:
        try:
            time = input("Please enter the time of the {} car driving by in the format: DD/MM/YYYY HH:MM:SS: ".format(carNum))
            if time[2] != "/" and time [5] != "/" and time[10]!= " " and time[13] != ":" and time[16] != ":":
                raise ValueError
            elif int(time[6]+time[7]+time[8]+time[9]) > 9999 or int(time[6]+time[7]+time[8]+time[9]) < 0:
                raise ValueError
            elif int(time[3]+time[4]) > 12 or int(time[3]+time[4]) < 0:
                raise ValueError
            elif int(time[0]+time[1]) > 31 or int(time[0]+time[1]) < 0:
                raise ValueError
            elif int(time[11]+time[12]) > 24 or int(time[11]+time[12]) < 0:
                raise ValueError
            elif int(time[14]+time[15]) > 60 or int(time[14]+time[15]) < 0:
                raise ValueError
            elif int(time[17]+time[18]) > 60 or int(time[17]+time[18]) < 0:
                raise ValueError
            break
        except ValueError:
            print("You have not entered the correct format, please try again.")
        except IndexError:
            print("You have not entered the correct format, please try again.")

            
    return(time)

def speedCalculation(time1, time2):
    years1 = time1[6]+time1[7]+time1[8]+time1[9]
    months1 = time1[3]+time1[4]
    days1 = time1[0]+time1[1]
    hours1 = time1[11]+time1[12]
    minutes1 = time1[14]+time1[15]
    seconds1 = time1[17]+time1[18]

    years2 = time2[6]+time2[7]+time2[8]+time2[9]
    months2 = time2[3]+time2[4]
    days2 = time2[0]+time2[1]
    hours2 = time2[11]+time2[12]
    minutes2 = time2[14]+time2[15]
    seconds2 = time2[17]+time2[18]

    time1 = '{}/{}/{} {}:{}:{}'.format(days1,months1,years1,hours1,minutes1,seconds1)
    time2 = '{}/{}/{} {}:{}:{}'.format(days2,months2,years2,hours2,minutes2,seconds2)

    try:
        timeStamp1 = time.mktime(datetime.strptime(time1, "%d/%m/%Y %H:%M:%S").timetuple())
        timeStamp2 = time.mktime(datetime.strptime(time2, "%d/%m/%Y %H:%M:%S").timetuple())
    except ValueError:
        print("The date you have entered is not calculatable by the currrent sytem, restarting...")
        return(None)

    totalDifference = (timeStamp2 - timeStamp1)/3600

    averageSpeed = 1/totalDifference

    print ("The car is doing an average of {}MPH".format(averageSpeed))

    return(averageSpeed,time1,time2)

def licenseChecker(): #AA00 000
    while True:
        try:
            license = input("Please enter the license plate of the vehicle: ")
            if license[0].isalpha() == False:
                validPlate = False
            elif license[1].isalpha() == False:
                validPlate = False
            elif license[2].isnumeric() == False:
                validPlate = False
            elif license[3].isnumeric() == False:
                validPlate = False
            elif license[4] != " ":
                validPlate = False
            elif license[5].isnumeric() == False:
                validPlate = False
            elif license[6].isnumeric() == False:
                validPlate = False
            elif license[7].isnumeric() == False:
                validPlate = False
            else:
                validPlate = True
            break
        except IndexError:
            validPlate = False
            break

    if validPlate == True:
        print ("The plate is valid")
    else: 
        print ("The plate is invalid")

    return (license,validPlate)

def store(averageSpeed,plate,valid,time1,time2):
    store = False
    if averageSpeed > 70:
        store = True
    elif valid == False:
        store = True
    
    if store == True:
        f = open("storedCars.txt", "a")
        f.write("Plate: {0}, Speed: {1}MPH, Time In: {2}, Time Out: {3}\n".format(plate,averageSpeed,time1,time2))
        f.close()
        print ("The car has been successfully saved.")


def main():
    print ("="*105)
    print (" "*40, " Speed Tracker by Yung ")
    print (" 1. Enter the time of the cars")
    print (" 2. Calculates average miles per hour")
    print (" 3. License plate pattern checker")
    print (" 4. Stores over speed or invalid license plates")
    print ("="*105)
    input("Press enter to continue...")

    averageSpeed = None
    while averageSpeed == None:
        time1 = timeInputs(1)
        time2 = timeInputs(2)
        averageSpeed = speedCalculation(time1,time2)


    licenseReturn = licenseChecker()
    plate = licenseReturn[0]
    valid = licenseReturn[1]

    store(averageSpeed[0],plate,valid,averageSpeed[1],averageSpeed[2])

while True:
    main()
    print ("="*105)
    while True:
        try:
            repeat = input("Do you want enter again? (y/n): ")
            if repeat not in ("y","n"):
                raise ValueError
            if repeat == "y":
                break
            else:
                exit(0)
        except ValueError:
            print ("Your choice is not valid...")
    
