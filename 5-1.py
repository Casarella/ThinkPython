# Exercise 5-1
# Transform epoch time to human readable current time.
# Format: HH:MM:SS + days since epoch

import time
time.time()
print('Epoch time:',time.time())

def num_days(time):
  """
  Determination of number of days since epoch, time divided by number of seconds in a day.
  """
  return int(time.time()/(24*3600))

print(num_days(time),'days have passed since epoch (1 Jan 1970)')

def current_year_check(time):
  return int(1970+num_days(time)/365.25)

print('CURRENT YEAR:',current_year_check(time))

def local_time(time):
  """
  Calculation of local time of particular day
  """
  return time.time()%(24*3600)
#print(local_time(time))
offset=int(input('Enter current GMT offset'))
def time_format(time):
  HH=int(local_time(time)/3600)
  MM=int((local_time(time)-HH*3600)/60)
  SS=int(local_time(time)-HH*3600-MM*60)
  print(HH+offset,':',MM,':',SS, 'GMT',offset)
  
time_format(time)

