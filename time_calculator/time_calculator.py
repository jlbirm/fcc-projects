def add_time(start, duration, day = None):
  period = ('AM', 'PM')

  # Set up start time for calculation
  start_sp = start.replace(':', ' ')
  start_f = start_sp.split()

  start_hr = int(start_f[0])
  start_min = int(start_f[1])
  start_period = period.index(start_f[2].upper())

  # Set up duration for calculation
  duration_f = duration.split(':')

  dur_hour = int(duration_f[0])
  dur_min = int(duration_f[1])

  # Calculate minutes
  minutes = start_min + dur_min
  hour_add = 0

  while minutes >= 60:
    minutes -= 60
    hour_add += 1

  # Calculate hours
  hours = start_hr + dur_hour + hour_add
  change = 0

  while hours > 12:
    hours -= 12
    change += 1
  
  if hours == 12: change += 1

  # AM vs PM
  if change >= 1:
    period_change = start_period + change
  else:
    period_change = start_period

  new_period = period[(period_change) % 2]

  # Calculate day change
  if change == 1 and start_period == 0:
    num_days = 0
  elif change % 2 == 0:
    num_days = int(change / 2)
  else:
    change -= 1
    num_days = int(change / 2) + 1

  if num_days == 1: 
    nxt_day = '(next day)'
  elif num_days == 0:
    nxt_day = None
  else:
    nxt_day = f"({num_days} days later)"

  if day:
    day_f = day.title()
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    cur_day = days.index(day_f)
    new_day = cur_day + num_days
    
    while new_day > 6:
      new_day -= 7

    if nxt_day:
      new_time = f"{hours}:{str(minutes).zfill(2)} {new_period}, {days[new_day]} {nxt_day}"
    else:
      new_time = f"{hours}:{str(minutes).zfill(2)} {new_period}, {days[new_day]}"

  else:
    if nxt_day:
      new_time = f"{hours}:{str(minutes).zfill(2)} {new_period} {nxt_day}"
    else:
      new_time = f"{hours}:{str(minutes).zfill(2)} {new_period}"

  return new_time
