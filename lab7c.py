#!/usr/bin/env python3
# Student ID: hzhao99
class Time:
    """Simple object type for time of the day.
    data attributes: hour, minute, second
    """
    def __init__(self,hour=12,minute=0,second=0):
        """constructor for time object""" 
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times(t1, t2):
    """Add two time objests and return the sum."""
    t1_sec = time_to_sec(t1)
    t2_sec = time_to_sec(t2)
    sum = sec_to_time(t1_sec + t2_sec)

    # sum = Time(0,0,0)
    # sum.hour = t1.hour + t2.hour
    # sum.minute = t1.minute + t2.minute
    # sum.second = t1.second + t2.second

    # # Carry seconds to minutes first when seconds exceeds 60.
    # while sum.second > 60:
    #     sum.minute += 1
    #     sum.second -= 60
    
    # #Carry minutes to hours when minutes exceeds 60.
    # while sum.minute > 60:
    #     sum.hour += 1
    #     sum.minute -= 60
    
    return sum

def valid_time(t):
    """check for the validity of the time object attributes:
        24 > hour > 0, 60 > minute > 0, 60 > second > 0 """
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60 or t.hour >= 24:
        return False
    return True

def change_time(time, seconds):
    """Modifies time object by increasing it by the number
    of seconds specified."""
    t_sec = time_to_sec(time)
    t_sec += seconds
    time = sec_to_time(t_sec) 

    # time.second += seconds
    # if valid_time(time) != True:
    #     while time.second >= 60:
    #         time.second -= 60
    #         time.minute += 1
    #     while time.minute >= 60:
    #         time.minute -= 60
    #         time.hour += 1

    # # If seconds is negative
    # while time.second < 0:
    #     time.minute -= 1
    #     time.second += 60
    # while time.minute < 0:
    #     time.hour -= 1
    #     time.minute += 60
        
    return None

def time_to_sec(time):
    '''convert a time object to a single integer representing the number of seconds from mid-night'''
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def sec_to_time(seconds):   
    '''convert a given number of seconds to a time object in hour,minute,second format'''
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes,60)
    return time