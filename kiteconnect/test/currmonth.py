import datetime

# Get the current date

# Get the abbreviated name of the current month in uppercase
current_month_abbr_upper = datetime.datetime.now().strftime('%b').upper()

print("Current month:", current_month_abbr_upper)

