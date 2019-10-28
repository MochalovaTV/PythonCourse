import datetime


def work_days(first_day, second_day):
    """Считает количество рабочих дней между двумя датами."""
    i = 0
    f_date = datetime.date(first_day[0], first_day[1], first_day[2])
    s_date = datetime.date(second_day[0], second_day[1], second_day[2])
    day_count = (s_date - f_date).days + 1
    for single_date in (f_date + datetime.timedelta(n) for n in range(day_count)):
        x = single_date.isoweekday()
        if x in range(1, 6):
            i += 1
        else:
            continue
    return i


print(work_days((2019, 10, 1), (2019, 10, 20)))




