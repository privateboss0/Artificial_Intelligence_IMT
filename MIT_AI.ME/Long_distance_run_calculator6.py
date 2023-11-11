def time_to_complete_actual_run(mile_time, distance):
    
  if not isinstance(mile_time, float):
    raise TypeError("mile_time must be a float")
  if not isinstance(distance, float):
    raise TypeError("distance must be a float")

  total_seconds = distance * 60 * mile_time
  hours = total_seconds // 3600
  minutes = total_seconds // 60 % 60
  seconds = total_seconds % 60

  return "%02d:%02d:%02.2f" % (hours, minutes, seconds)


print(time_to_complete_actual_run(4.50, 27.3))