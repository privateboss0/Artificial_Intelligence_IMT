import calendar
import datetime
import time
import re
import shutil

# Get the current year and month
current_year = datetime.date.today().year
current_month = datetime.date.today().month
current_day = datetime.date.today().day
calendar.setfirstweekday(6)

# Create regular expression patterns
bdayb = r'\b{current_day}\b'.format(current_day=current_day)
bdayac = r"\033[34m\033[1m{current_day}\033[0m".format(current_day=current_day)

# Replace the current day with blue colored text
calendar_text = calendar.month(current_year, current_month)
calendar_text = re.sub(bdayb, bdayac, calendar_text)

#output to the screen
terminal_size = shutil.get_terminal_size((80, 24))
centered_text = calendar_text.rjust(terminal_size[1])

print(centered_text)