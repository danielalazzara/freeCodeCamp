def add_time(start, duration, day=None):
    week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    start_time, am_pm = start.split()
    start_hour, start_minute = start_time.split(':')
    duration_hour, duration_minute = duration.split(':')

    start_hour = int(start_hour)
    start_minute = int(start_minute)
    duration_hour = int(duration_hour)
    duration_minute = int(duration_minute)

    total_minute = start_minute + duration_minute
    total_hour = start_hour + duration_hour
    total_day = 0

    while (total_minute >= 60) or (total_hour >= 12):
        # Empty the minute bucket
        # Empty the hour bucket

        # Organizing bucket
        # Empty minutes bucket
        if total_minute >= 60:
            total_hour += 1
            total_minute -= 60

        # Empty hour bucket
        if total_hour >= 12:
            total_hour -= 12
            if am_pm == "AM":
                am_pm = "PM"
            else:
                am_pm = "AM"
                total_day += 1

    if day:
        # n = (total_day // 7) + 1
        # week_days_total = week_days * n
        # end_day = week_days_total[total_day]
        day = day.lower().capitalize()
        day_index = week_days.index(day)
        new_index = (day_index + total_day) % 7
        end_day = week_days[new_index]
        week_days_string = f", {end_day}"
    else:
        week_days_string = ""

    if total_hour == 0:
        total_hour = 12

    if total_day == 0:
        result = f"{total_hour}:{total_minute:>02d} {am_pm}{week_days_string}"
    elif total_day == 1:
        result = f"{total_hour}:{total_minute:>02d} {am_pm}{week_days_string} (next day)"
    else:
        result = f"{total_hour}:{total_minute:>02d} {am_pm}{week_days_string} ({total_day} days later)"

    return result

