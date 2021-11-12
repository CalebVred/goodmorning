import crypto_writer
import pyttsx3
import time
import datetime


def main():

    #TODO: Find some way for the user to input this time instead of just a hard-coded value
    alarm_time = "05:30:00"

    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now_str = current_time.strftime("%H:%M:%S")

        if now_str == alarm_time:
            engine = pyttsx3.init()

            hour = current_time.hour
            if hour > 12:
                engine.say("Good Afternoon")
  
            else:
                engine.say("Good Morning")

            engine.say("It is ")
            engine.say(time_to_string())

            #TODO: Find some way for the user to select news sources
            engine.say(crypto_writer.crypto_stat_string(
                    ['bitcoin', 'ethereum'], 'usd'))
            engine.runAndWait()
            engine.stop()
            break

'''
time_to_string()
@output: t_string - The string representation of the current date and time.
'''
def time_to_string():

    t_string = ""

    seconds = time.time()
    local_time = time.localtime(seconds)
    dotw = local_time.tm_wday
    dotw_str = ""
    if(dotw == 6):
        dotw_str = "Sunday"
    elif(dotw == 0):
        dotw_str = "Monday"
    elif(dotw == 1):
        dotw_str = "Tuesday"
    elif(dotw == 2):
        dotw_str = "Wednesday"
    elif(dotw == 3):
        dotw_str = "Thursday"
    elif(dotw == 4):
        dotw_str = "Friday"
    elif(dotw == 5):
        dotw_str = "Saturday"

    t_string += dotw_str
    t_string += ", "

    month = local_time.tm_mon
    month_str = ""
    if(month == 1):
        month_str = "January"
    elif(month == 2):
        month_str = "February"
    elif(month == 3):
        month_str = "March"
    elif(month == 4):
        month_str = "April"
    elif(month == 5):
        month_str = "May"
    elif(month == 6):
        month_str = "June"
    elif(month == 7):
        month_str = "July"
    elif(month == 8):
        month_str = "August"
    elif(month == 9):
        month_str = "September"
    elif(month == 10):
        month_str = "October"
    elif(month == 11):
        month_str = "November"
    elif(month == 12):
        month_str = "December"

    t_string += month_str
    t_string += " "

    dotm = local_time.tm_mday
    t_string += str(dotm)
    t_string += " "

    hour = local_time.tm_hour
    meridian = ""
    if hour > 12:
        meridian = "PM"
    else:
        meridian = "AM"

    if hour != 12:
        hour = hour % 12

    t_string += str(hour)
    t_string += " "

    minute = local_time.tm_min
    if minute < 10:
        t_string += "o'"
    t_string += str(minute)
    t_string += " "

    t_string += meridian
    t_string += "."
    return t_string


main()
