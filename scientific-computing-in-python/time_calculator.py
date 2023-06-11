def add_time(start, duration, DayOfTheWeek=None):
  #normalize the optional input, inizialize Week and create splits for managing minutes and hours   
  new_time = ""
  if DayOfTheWeek == None:
    DayOfTheWeek = ""
  DayOfTheWeek = DayOfTheWeek.capitalize()
  start = start.strip()
  start = start.replace(" ", ":")
  start_spl = start.split(":")
  duration_spl = duration.split(":")
  Week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
  hoursS = int(start_spl[0])
  minutesS = int(start_spl[1])
  hoursD = int(duration_spl[0])
  minutesD = int(duration_spl[1])

  #add result hours by summing up minutesD (Duration) and minutesS (Start)
  if minutesS + minutesD >= 60:
    hoursS += 1
    minutesS = minutesS + minutesD - 60
  else:
    minutesS = minutesS + minutesD

  #calculate the number of days that will pass by adding Duration, by summing up both hours and dividing by 24 (hours of a day) -> 
  #if you are in PM, you need to normalize the timetable by adding 12 ( for exambple 8 PM = 20:00
  if start_spl[2] == "AM":
    DaysLater = int((hoursS + hoursD)/24)
  elif start_spl[2] == "PM":
    DaysLater = int((hoursS + 12 + hoursD)/24)

  #different possible situations: 12 <= hours sum <= 24 (- 12 for normalize the result hour between 0 - 12)
  #hours sum < 12 (dont need to normalize because it is already between 0 - 12)
  #hours sum > 24 (that condition says that if your number has odd or even number of +12 in his sum (like 36 has 3 +12), u have to switch or not AM/PM)
  if hoursS + hoursD >= 12 and hoursS + hoursD <= 24:
    hoursS = hoursS + hoursD - 12
    if start_spl[2] == "PM":
        start_spl[2] = "AM"
    elif start_spl[2] == "AM":
        start_spl[2] = "PM"
  elif hoursS + hoursD < 12:
    hoursS = hoursS + hoursD
  elif hoursS + hoursD > 24:
    if ( ( (hoursS + hoursD) - ( (hoursS + hoursD) % 12) )/12 ) % 2 != 0 :
      if start_spl[2] == "PM":
        start_spl[2] = "AM"
      elif start_spl[2] == "AM":
        start_spl[2] = "PM"
    hoursS = (hoursS + hoursD) % 12 #the rest operation allow to take the remaining hours after /12 (37 hours later means 3 days and 1 HOUR later, 37 % 12 = 1)

  if DayOfTheWeek in Week:
    position = (Week.index(DayOfTheWeek) + DaysLater) % 7 #calculate, by using DaysLater, in what week day we will stop (same logic like before for %7, ->
                                                          # -> u can skip useless iterations inside "Week" list)

  #building the precise and correct output for tests
  if minutesS < 10:
    minutesS = "0" + str(minutesS)
  else:
    minutesS = str(minutesS)

  if hoursS < 1:
    hoursS = "12" + ":" + minutesS + " " + str(start_spl[2])
  elif hoursS < 10:
    hoursS = str(hoursS) + ":" + minutesS + " " + str(start_spl[2])
  else:
    hoursS = str(hoursS) + ":" + minutesS + " " + str(start_spl[2])

  if DaysLater > 1:
    DaysLater = " (" + str(DaysLater) + " days later)"
  elif DaysLater == 1:
    DaysLater = " (next day)"
  elif DaysLater == 0:
    DaysLater = ""

  if len(DayOfTheWeek) == 0:
    new_time = hoursS + DaysLater
  else:
    new_time = hoursS + ", " + Week[position] + DaysLater
 
  return new_time
print(add_time(1,1,3))