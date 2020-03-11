week = 3
time_wakeup = "08:00"
step = 15
minutes = 0
hour = 0

try:
    week = int(week)
    hour, minutes = time_wakeup.split(":")
    hour = int(hour)
    minutes = int(minutes)
    if 24 < hour or hour < 0 or 60 < minutes or minutes < 0:
        print("Ви ввели неіснуючий час")
        exit()
except ValueError:
    print("Ви ввели неіснуючий час")
    exit()
day_of_week = ["Понеділок", "Вівторок", "Середа", "Четвер", "Пятниця", "Субота", "Неділя"]
for i in range(3):
    j = 0
    for j in range(7):
        if j == 5 or j == 6:
            output_minutes = minutes or "00"
            print(f"{day_of_week[j]} {hour}" + ":" + f"{output_minutes}") #saturday,sunday
            continue

        minutes = minutes - step

        if minutes < 0:
            hour = hour - 1
            minutes += 60

        output_minutes = minutes or "00"
        print(f"{day_of_week[j]} {hour}" + ":" + f"{output_minutes}")
