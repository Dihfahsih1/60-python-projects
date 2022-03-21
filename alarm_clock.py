from datetime import datetime
from playsound import playsound

alarm_time = input('Enter the time of the alarm to set: HH:MM:SS\n')
alarm_hour=alarm_time[0:2]#store hours part of the input from index 0 to index 2(not inclusive)
alarm_minute=alarm_time[3:5]#range or sequence from index 3 to 4 only 
alarm_seconds=alarm_time[6:8]
alarm_period =alarm_time[9:11].upper() 
print("Setting up alarm..")

while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minutes = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")
    if(alarm_period==current_period):
        if(alarm_hour==current_hour):
            if(alarm_minute==current_minutes):
                if(alarm_seconds==current_seconds):
                    print("wake up please")
                    playsound('tone.mp3')
                    break