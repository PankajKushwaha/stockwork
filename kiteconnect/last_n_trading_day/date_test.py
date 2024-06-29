from datetime import date, timedelta
from nsepython import *
from pynse import *

nse = Nse()

#['26-Jan-2021', '19-Feb-2021', '11-Mar-2021', '29-Mar-2021', '01-Apr-2021', '02-Apr-2021', '13-Apr-2021', '14-Apr-2021', '21-Apr-2021', '25-Apr-2021', '01-May-2021', '13-May-2021', '26-May-2021', '21-Jul-2021', '15-Aug-2021', '16-Aug-2021', '19-Aug-2021', '10-Sep-2021', '02-Oct-2021', '15-Oct-2021', '19-Oct-2021', '04-Nov-2021', '05-Nov-2021', '19-Nov-2021', '25-Dec-2021']

month_str_to_num = {
        "Jan":"01",
        "Feb":"02",
        "Mar":"03",
        "Apr":"04",
        "May":"05",
        "Jun":"06",
        "Jul":"07",
        "Aug":"08",
        "Sep":"09",
        "Oct":"10",
        "Nov":"11",
        "Dec":"12",
        }

def get_month_from_date(dt):
    for month in month_str_to_num.keys():
        if month in dt:
            return month

def is_time_greater_330():
    current_time = datetime.datetime.now()
    print(current_time.hour)
    print(current_time.minute)
    if current_time.hour>=3 and current_time.minute>30:
        return True
    else:
        return False


def last_3_valid_date():
    base_date = date.today()
    if is_time_greater_330():
        base_date = base_date - timedelta(days = 1)
    if date.today().strftime("%A") == "Saturday" :
        base_date = base_date - timedelta(days = 1)
    if date.today().strftime("%A") == "Sunday" :
        base_date = base_date - timedelta(days = 2)


def get_holiday_list():
    tmp_holiday_list = []
    holiday_list = []
    #today = date.today()
    #yesterday = today - timedelta(days = 1)
    #print(fnolist())
    for date in nse_holidays()['CBM']:
        tmp_holiday_list.append(date['tradingDate'])
    for date in tmp_holiday_list:
        mon = get_month_from_date(date)
        tmp_str_date = date.replace(mon, month_str_to_num[mon])
        tmp_str_date = "-".join(reversed(tmp_str_date.split("-")))
        holiday_list.append(tmp_str_date.replace(mon, month_str_to_num[mon]))
    return holiday_list


def main_function():
    isIncludeToday = True

holiday_list = get_holiday_list()
print(holiday_list)

today = date.today()
print("Today's date:", str(today))
yesterday = date.today() - timedelta(days=1)
p = nse.bhavcopy(yesterday)
print(p)

base_date = date.today()
print(base_date.strftime("%A"))
