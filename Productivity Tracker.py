from tkinter import *
import customtkinter as CTk
import time
import datetime
import json
from plyer import notification
import threading
import os
import csv
import discord
from dotenv import load_dotenv
import platform

tracking = False
pomodoro_break = False
readytostart = True
paused = False
p_string_store = ""
focus_time = 1500
break_time = 300
long_break_time = 900
p_focus_time = 1500
p_break_time = 300
p_long_break_time = 900
p_cycle_count = 1
start_time = 0
time_passed = 0
timer_id = ""

file_path = "variables.json"
# Check if the file exists
if not os.path.isfile(file_path):
    with open(file_path, 'w') as file:
        file.write("{}")

file_path = "punches.json"
# Check if the file exists
if not os.path.isfile(file_path):
    with open(file_path, 'w') as file:
        file.write("{}")

# file_path = "walking.json"
# # Check if the file exists
# if not os.path.isfile(file_path):
#     with open(file_path, 'w') as file:
#         file.write("{}")

file_path = "description.json"
# Check if the file exists
if not os.path.isfile(file_path):
    with open(file_path, 'w') as file:
        file.write("{}")

file_path = "must_clear.json"
# Check if the file exists
if not os.path.isfile(file_path):
    with open(file_path, 'w') as file:
        file.write("{}")

file_path = ".env"
# Check if the file exists
if not os.path.isfile(file_path):
    with open(".env", "w", newline='') as file:
        file.write("Discord_Webhook='None'")

file_path = "current_week.json"
# Check if the file exists
if not os.path.isfile(file_path):
    with open(file_path, 'w') as file:
        file.write("{}")

# Open the JSON file
with open("variables.json", "r") as file:
    # Load the JSON data
    data = json.load(file)

if ("thursday_programming_time" not in data):
    data = {
            "thursday_programming_time": 0,
            "friday_programming_time": 0,
            "saturday_programming_time": 0,
            "sunday_programming_time": 0,
            "monday_programming_time": 0,
            "tuesday_programming_time": 0,
            "wednesday_programming_time": 0,
            "total_programming_time": 0
            }

thursday_programming_time = data["thursday_programming_time"]
friday_programming_time = data["friday_programming_time"]
saturday_programming_time = data["saturday_programming_time"]
sunday_programming_time = data["sunday_programming_time"]
monday_programming_time = data["monday_programming_time"]
tuesday_programming_time = data["tuesday_programming_time"]
wednesday_programming_time = data["wednesday_programming_time"]
total_programming_time = data["total_programming_time"]

# Open the JSON file
with open("punches.json", "r") as file:
    # Load the JSON data
    data = json.load(file)

if ("thursday_punches" not in data):
    data = {
            "thursday_punches": ["None"],
            "friday_punches": ["None"],
            "saturday_punches": ["None"],
            "sunday_punches": ["None"],
            "monday_punches": ["None"],
            "tuesday_punches": ["None"],
            "wednesday_punches": ["None"],
            }

thursday_punches = data["thursday_punches"]
friday_punches = data["friday_punches"]
saturday_punches = data["saturday_punches"]
sunday_punches = data["sunday_punches"]
monday_punches = data["monday_punches"]
tuesday_punches = data["tuesday_punches"]
wednesday_punches = data["wednesday_punches"]

# # Open the JSON file
# with open("walking.json", "r") as file:
#     # Load the JSON data
#     data = json.load(file)

# if ("thursday_walking_time" not in data):
#     data = {
#             "thursday_weight": 0,
#             "friday_weight": 0,
#             "saturday_weight": 0,
#             "sunday_weight": 0,
#             "monday_weight": 0,
#             "tuesday_weight": 0,
#             "wednesday_weight": 0,
#             "total_weight_lost": 0,

#             "thursday_walking_time": 0,
#             "friday_walking_time": 0,
#             "saturday_walking_time": 0,
#             "sunday_walking_time": 0,
#             "monday_walking_time": 0,
#             "tuesday_walking_time": 0,
#             "wednesday_walking_time": 0,
#             "total_walking_time": 0,

#             "thursday_walking_distance": 0,
#             "friday_walking_distance": 0,
#             "saturday_walking_distance": 0,
#             "sunday_walking_distance": 0,
#             "monday_walking_distance": 0,
#             "tuesday_walking_distance": 0,
#             "wednesday_walking_distance": 0,
#             "total_walking_distance": 0,

#             "thursday_walking_steps": 0,
#             "friday_walking_steps": 0,
#             "saturday_walking_steps": 0,
#             "sunday_walking_steps": 0,
#             "monday_walking_steps": 0,
#             "tuesday_walking_steps": 0,
#             "wednesday_walking_steps": 0,
#             "total_walking_steps": 0,

#             "thursday_calories": 0,
#             "friday_calories": 0,
#             "saturday_calories": 0,
#             "sunday_calories": 0,
#             "monday_calories": 0,
#             "tuesday_calories": 0,
#             "wednesday_calories": 0,
#             "total_calories": 0
#             }

# thursday_weight = data["thursday_weight"]
# friday_weight = data["friday_weight"]
# saturday_weight = data["saturday_weight"]
# sunday_weight = data["sunday_weight"]
# monday_weight = data["monday_weight"]
# tuesday_weight = data["tuesday_weight"]
# wednesday_weight = data["wednesday_weight"]
# total_weight_lost = data["total_weight_lost"]

# thursday_walking_time = data["thursday_walking_time"]
# friday_walking_time = data["friday_walking_time"]
# saturday_walking_time = data["saturday_walking_time"]
# sunday_walking_time = data["sunday_walking_time"]
# monday_walking_time = data["monday_walking_time"]
# tuesday_walking_time = data["tuesday_walking_time"]
# wednesday_walking_time = data["wednesday_walking_time"]
# total_walking_time = data["total_walking_time"]

# thursday_walking_distance = data["thursday_walking_distance"]
# friday_walking_distance = data["friday_walking_distance"]
# saturday_walking_distance = data["saturday_walking_distance"]
# sunday_walking_distance = data["sunday_walking_distance"]
# monday_walking_distance = data["monday_walking_distance"]
# tuesday_walking_distance = data["tuesday_walking_distance"]
# wednesday_walking_distance = data["wednesday_walking_distance"]
# total_walking_distance = data["total_walking_distance"]

# thursday_walking_steps = data["thursday_walking_steps"]
# friday_walking_steps = data["friday_walking_steps"]
# saturday_walking_steps = data["saturday_walking_steps"]
# sunday_walking_steps = data["sunday_walking_steps"]
# monday_walking_steps = data["monday_walking_steps"]
# tuesday_walking_steps = data["tuesday_walking_steps"]
# wednesday_walking_steps = data["wednesday_walking_steps"]
# total_walking_steps = data["total_walking_steps"]

# thursday_calories = data["thursday_calories"]
# friday_calories = data["friday_calories"]
# saturday_calories = data["saturday_calories"]
# sunday_calories = data["sunday_calories"]
# monday_calories = data["monday_calories"]
# tuesday_calories = data["tuesday_calories"]
# wednesday_calories = data["wednesday_calories"]
# total_calories = data["total_calories"]

# Open the JSON file
with open("description.json", "r") as file:
    # Load the JSON data
    data = json.load(file)

if ("description" not in data):
    data = {
        "description": ""
    }

description = data["description"]

# Open the JSON file
with open("must_clear.json", "r") as file:
    # Load the JSON data
    data = json.load(file)

if ("must_clear" not in data):
    data = {
        "must_clear": False,
        "current_week": -1
    }

must_clear = data["must_clear"]
current_week = data["current_week"]

# Open the JSON file
with open("current_week.json", "r") as file:
    # Load the JSON data
    data = json.load(file)

if ("current_week_str" not in data):
    data = {
        "curr_week_str": ""
    }

curr_week_str = data["curr_week_str"]

# current_weight = 0

can_clear = True

webhook_locked = False

def lock_webhook():
    global webhook_locked
    if (webhook_locked == False):
        if (app.webhook_entry.get() != ""):
            with open(".env", "w", newline='') as file:
                env_str = "Discord_Webhook=" + "'" + app.webhook_entry.get() + "'"
                file.write(env_str)
            app.webhook_entry.configure(state="disabled")
            app.webhook_entry_lock_button.configure(text="Unlock")
            webhook_locked = True
    else:
        app.webhook_entry.configure(state="normal")
        app.webhook_entry_lock_button.configure(text="Lock")
        webhook_locked = False

def center_window(window, window_width, window_height):
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    window.geometry("+{}+{}".format(x, y))

def get_date_range_for_current_week():
    """
    Returns the date range for the current week in the format 'MMM d(st/nd/rd/th) yyyy - MMM d(st/nd/rd/th) yyyy'.
    The week starts on Sunday and ends on Saturday.
    """
    today = datetime.date.today()
    current_weekday = today.isoweekday()

    # Calculate the start date (Sunday)
    start_date = today - datetime.timedelta(days=current_weekday % 7)

    # Calculate the end date (Saturday)
    end_date = start_date + datetime.timedelta(days=6)

    start_date_str = start_date.strftime("%b %d")
    end_date_str = end_date.strftime("%b %d")

    # Add proper day suffix
    start_date_str += get_day_suffix(int(start_date.strftime("%d")))
    end_date_str += get_day_suffix(int(end_date.strftime("%d")))

    # Add year to the date strings
    start_date_str += f" {start_date.year}"
    end_date_str += f" {end_date.year}"

    date_range = f"{start_date_str} - {end_date_str}"
    return date_range

def get_day_suffix(day):
    """
    Returns the proper day suffix (st, nd, rd, th) for the given day.
    """
    if 4 <= day <= 20 or 24 <= day <= 30:
        suffix = "th"
    else:
        suffix = ["th", "st", "nd", "rd"][day % 10 - 1]
    return suffix

def send_data_modal():
    modal_dialog = CTk.CTkToplevel(app)
    modal_dialog.iconbitmap("icon4.ico")
    modal_dialog.grab_set()  # Make the dialog modal
    modal_dialog.geometry("800x490")
    modal_dialog.title("Send Data")
    modal_dialog.iconbitmap("icon4.ico")
    center_window(modal_dialog, 800, 490)

    # Add your dialog content here
    label = CTk.CTkLabel(modal_dialog, text="Preview of data to be sent:")
    label.grid(row=0, column=0, pady=(10,0))

    # tab_view = CTk.CTkTabview(modal_dialog, fg_color="transparent")
    # tab_view.add("Programming Data")
    # tab_view.add("Exercise Data")
    # tab_view.grid(row=1, column=0, columnspan=4, sticky="we")

    current_week_range = ""
    if (curr_week_str != ""):
        current_week_range = curr_week_str
    else:
        current_week_range = get_date_range_for_current_week()

    # Time Worked Each Day
    text_to_send = ""
    text_to_send += "DATES:\n"
    text_to_send += current_week_range
    text_to_send += "\n\nTIME WORKED EACH DAY:"
    text_to_send += "\nSunday - Time Worked: "
    sunday_str_time_worked = ""
    if (app.weekly_daily_tabs.weekly_tab.sunday_hour_entry.get() != ""):
        text_to_send += app.weekly_daily_tabs.weekly_tab.sunday_hour_entry.get()
        sunday_str_time_worked = app.weekly_daily_tabs.weekly_tab.sunday_hour_entry.get()
    else: 
        text_to_send += "00:00:00"
        sunday_str_time_worked = "00:00:00"
    text_to_send += ", Punches: "
    count = 0
    sunday_str_punches = ""
    for i in app.weekly_daily_tabs.weekly_tab.sunday_punches_entry._values:
        count += 1
        text_to_send += i
        sunday_str_punches += i
        if (count != len(app.weekly_daily_tabs.weekly_tab.sunday_punches_entry._values)): 
            text_to_send += ", "
            sunday_str_punches += ", "

    monday_str_time_worked = ""
    text_to_send += "\nMonday - Time Worked: "
    if (app.weekly_daily_tabs.weekly_tab.monday_hour_entry.get() != ""):
        text_to_send += app.weekly_daily_tabs.weekly_tab.monday_hour_entry.get()
        monday_str_time_worked = app.weekly_daily_tabs.weekly_tab.monday_hour_entry.get()
    else: 
        text_to_send += "00:00:00"
        monday_str_time_worked = "00:00:00"
    text_to_send += ", Punches: "
    count = 0
    monday_str_punches = ""
    for i in app.weekly_daily_tabs.weekly_tab.monday_punches_entry._values:
        count += 1
        text_to_send += i
        monday_str_punches += i
        if (count != len(app.weekly_daily_tabs.weekly_tab.monday_punches_entry._values)): 
            text_to_send += ", "
            monday_str_punches += ", "

    tuesday_str_time_worked = ""
    text_to_send += "\nTuesday - Time Worked: "
    if (app.weekly_daily_tabs.weekly_tab.tuesday_hour_entry.get() != ""):
        text_to_send += app.weekly_daily_tabs.weekly_tab.tuesday_hour_entry.get()
        tuesday_str_time_worked = app.weekly_daily_tabs.weekly_tab.tuesday_hour_entry.get()
    else: 
        text_to_send += "00:00:00"
        tuesday_str_time_worked = "00:00:00"
    text_to_send += ", Punches: "
    count = 0
    tuesday_str_punches = ""
    for i in app.weekly_daily_tabs.weekly_tab.tuesday_punches_entry._values:
        count += 1
        text_to_send += i
        tuesday_str_punches += i
        if (count != len(app.weekly_daily_tabs.weekly_tab.tuesday_punches_entry._values)): 
            text_to_send += ", "
            tuesday_str_punches += ", "

    wednesday_str_time_worked = ""
    text_to_send += "\nWednesday - Time Worked: "
    if (app.weekly_daily_tabs.weekly_tab.wednesday_hour_entry.get() != ""):
        text_to_send += app.weekly_daily_tabs.weekly_tab.wednesday_hour_entry.get()
        wednesday_str_time_worked = app.weekly_daily_tabs.weekly_tab.wednesday_hour_entry.get()
    else: 
        text_to_send += "00:00:00"
        wednesday_str_time_worked = "00:00:00"
    text_to_send += ", Punches: "
    count = 0
    wednesday_str_punches = ""
    for i in app.weekly_daily_tabs.weekly_tab.wednesday_punches_entry._values:
        count += 1
        text_to_send += i
        wednesday_str_punches += i
        if (count != len(app.weekly_daily_tabs.weekly_tab.wednesday_punches_entry._values)): 
            text_to_send += ", "
            wednesday_str_punches += ", "

    thursday_str_time_worked = ""
    text_to_send += "\nThursday - Time Worked: "
    if (app.weekly_daily_tabs.weekly_tab.thursday_hour_entry.get() != ""):
        text_to_send += app.weekly_daily_tabs.weekly_tab.thursday_hour_entry.get()
        thursday_str_time_worked = app.weekly_daily_tabs.weekly_tab.thursday_hour_entry.get()
    else: 
        text_to_send += "00:00:00"
        thursday_str_time_worked = "00:00:00"
    text_to_send += ", Punches: "
    count = 0
    thursday_str_punches = ""
    for i in app.weekly_daily_tabs.weekly_tab.thursday_punches_entry._values:
        count += 1
        text_to_send += i
        thursday_str_punches += i
        if (count != len(app.weekly_daily_tabs.weekly_tab.thursday_punches_entry._values)): 
            text_to_send += ", "
            thursday_str_punches += ", "

    friday_str_time_worked = ""
    text_to_send += "\nFriday - Time Worked: "
    if (app.weekly_daily_tabs.weekly_tab.friday_hour_entry.get() != ""):
        text_to_send += app.weekly_daily_tabs.weekly_tab.friday_hour_entry.get()
        friday_str_time_worked = app.weekly_daily_tabs.weekly_tab.friday_hour_entry.get()
    else: 
        text_to_send += "00:00:00"
        friday_str_time_worked = "00:00:00"
    text_to_send += ", Punches: "
    count = 0
    friday_str_punches = ""
    for i in app.weekly_daily_tabs.weekly_tab.friday_punches_entry._values:
        count += 1
        text_to_send += i
        friday_str_punches += i
        if (count != len(app.weekly_daily_tabs.weekly_tab.friday_punches_entry._values)): 
            text_to_send += ", "
            friday_str_punches += ", "

    saturday_str_time_worked = ""
    text_to_send += "\nSaturday - Time Worked: "
    if (app.weekly_daily_tabs.weekly_tab.saturday_hour_entry.get() != ""):
        text_to_send += app.weekly_daily_tabs.weekly_tab.saturday_hour_entry.get()
        saturday_str_time_worked = app.weekly_daily_tabs.weekly_tab.saturday_hour_entry.get()
    else: 
        text_to_send += "00:00:00"
        saturday_str_time_worked = "00:00:00"
    text_to_send += ", Punches: "
    count = 0
    saturday_str_punches = ""
    for i in app.weekly_daily_tabs.weekly_tab.saturday_punches_entry._values:
        count += 1
        text_to_send += i
        saturday_str_punches += i
        if (count != len(app.weekly_daily_tabs.weekly_tab.saturday_punches_entry._values)): 
            text_to_send += ", "
            saturday_str_punches += ", "

    #Total Time Worked
    text_to_send += "\n\nTOTAL TIME WORKED:\n"
    total_str_time_worked = ""
    if (app.totals_frame.time_programming_entry.get() != ""):
        text_to_send += app.totals_frame.time_programming_entry.get()
        total_str_time_worked = app.totals_frame.time_programming_entry.get()
    else:
        text_to_send += "00:00:00"
        total_str_time_worked = "00:00:00"

    #Description
    description_str = ""
    text_to_send += "\n\nDESCRIPTION:\n"
    if (description != ""):
        text_to_send += description
        description_str = description
    else:
        text_to_send += "No description given..."
        description_str = "No description given..."

    print(description)
    print(description_str)
    textbox = CTk.CTkTextbox(modal_dialog, wrap="word", height=350, width=750)
    textbox.grid(row=0, column=0, pady=(50, 0))
    textbox.insert(1.0, text_to_send)
    textbox.configure(state="disabled")

    # text_to_send_exercise = ""
    # text_to_send_exercise += "DATES:\n"
    # text_to_send_exercise += current_week_range
    # #Exercise Daily Statistics
    # text_to_send_exercise += "\n\nEXERCISE DAILY STATISTICS:"
    # text_to_send_exercise += "\nSunday - Weight: "
    # sunday_str_weight = ""
    # if (app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_weight_entry.get() != ""):
    #     text_to_send_exercise += app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_weight_entry.get()
    #     sunday_str_weight = app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_weight_entry.get()
    # else: 
    #     text_to_send_exercise += "None Given"
    #     sunday_str_weight = "None Given"
    # text_to_send_exercise += ", Time Walked: "
    # sunday_str_time_walked = ""
    # if (app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_time_walked_entry.get() != ""):
    #     text_to_send_exercise += app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_time_walked_entry.get()
    #     sunday_str_time_walked = app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_time_walked_entry.get()
    # else: 
    #     text_to_send_exercise += "00:00:00"
    #     sunday_str_time_walked = "00:00:00"
    # text_to_send_exercise += ", Distance: "
    # sunday_str_distance = ""
    # if (app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_distance_entry.get() != ""):
    #     text_to_send_exercise += app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_distance_entry.get()
    #     sunday_str_distance = app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_distance_entry.get()
    # else: 
    #     text_to_send_exercise += "0"
    #     sunday_str_distance = "0"
    # text_to_send_exercise += ", Steps: "
    # sunday_str_steps = ""
    # if (app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_steps_entry.get() != ""):
    #     text_to_send_exercise += app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_steps_entry.get()
    #     sunday_str_steps = app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_steps_entry.get()
    # else: 
    #     text_to_send_exercise += "0"
    #     sunday_str_steps = "0"
    # text_to_send_exercise += ", Calories Burned: "
    # sunday_str_calories = ""
    # if (app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_calories_entry.get() != ""):
    #     text_to_send_exercise += app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_calories_entry.get()
    #     sunday_str_calories = app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_calories_entry.get()
    # else: 
    #     text_to_send_exercise += "0"
    #     sunday_str_calories = "0"
    # text_to_send_exercise += "\nMonday - Weight: "
    # monday_str_weight = ""
    # if (app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_weight_entry.get() != ""):
    #     text_to_send_exercise += app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_weight_entry.get()
    #     monday_str_weight = app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_weight_entry.get()
    # else: 
    #     text_to_send_exercise += "None Given"
    #     monday_str_weight = "None Given"
    # text_to_send_exercise += ", Time Walked: "
    # monday_str_time_walked = ""
    # if (app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_time_walked_entry.get() != ""):
    #     text_to_send_exercise += app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_time_walked_entry.get()
    #     monday_str_time_walked = app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_time_walked_entry.get()
    # else: 
    #     text_to_send_exercise += "00:00:00"
    #     monday_str_time_walked = "00:00:00"
    # text_to_send_exercise += ", Distance: "
    # monday_str_distance = ""
    # if (app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_distance_entry.get() != ""):
    #     text_to_send_exercise += app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_distance_entry.get()
    #     monday_str_distance = app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_distance_entry.get()
    # else: 
    #     text_to_send_exercise += "0"
    #     monday_str_distance = "0"
    # text_to_send_exercise += ", Steps: "
    # monday_str_steps = ""
    # if (app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_steps_entry.get() != ""):
    #     text_to_send_exercise += app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_steps_entry.get()
    #     monday_str_steps = app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_steps_entry.get()
    # else: 
    #     text_to_send_exercise += "0"
    #     monday_str_steps = "0"
    # text_to_send_exercise += ", Calories Burned: "
    # monday_str_calories = ""
    # if (app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_calories_entry.get() != ""):
    #     text_to_send_exercise += app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_calories_entry.get()
    #     monday_str_calories = app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_calories_entry.get()
    # else: 
    #     text_to_send_exercise += "0"
    #     monday_str_calories = "0"
    # text_to_send_exercise += "\nTuesday - Weight: "
    # tuesday_str_weight = ""
    # if (app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_weight_entry.get() != ""):
    #     text_to_send_exercise += app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_weight_entry.get()
    #     tuesday_str_weight = app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_weight_entry.get()
    # else: 
    #     text_to_send_exercise += "None Given"
    #     tuesday_str_weight = "None Given"
    # text_to_send_exercise += ", Time Walked: "
    # tuesday_str_time_walked = ""
    # if (app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_time_walked_entry.get() != ""):
    #     text_to_send_exercise += app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_time_walked_entry.get()
    #     tuesday_str_time_walked = app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_time_walked_entry.get()
    # else: 
    #     text_to_send_exercise += "00:00:00"
    #     tuesday_str_time_walked = "00:00:00"
    # text_to_send_exercise += ", Distance: "
    # tuesday_str_distance = "0"
    # if (app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_distance_entry.get() != ""):
    #     text_to_send_exercise += app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_distance_entry.get()
    #     tuesday_str_distance = app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_distance_entry.get()
    # else: 
    #     text_to_send_exercise += "0"
    #     tuesday_str_distance = "0"
    # text_to_send_exercise += ", Steps: "
    # tuesday_str_steps = ""
    # if (app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_steps_entry.get() != ""):
    #     text_to_send_exercise += app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_steps_entry.get()
    #     tuesday_str_steps = app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_steps_entry.get()
    # else: 
    #     text_to_send_exercise += "0"
    #     tuesday_str_steps = "0"
    # text_to_send_exercise += ", Calories Burned: "
    # tuesday_str_calories = ""
    # if (app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_calories_entry.get() != ""):
    #     text_to_send_exercise += app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_calories_entry.get()
    #     tuesday_str_calories = app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_calories_entry.get()
    # else: 
    #     text_to_send_exercise += "0"
    #     tuesday_str_calories = "0"
    # text_to_send_exercise += "\nWednesday - Weight: "
    # wednesday_str_weight = ""
    # if (app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_weight_entry.get() != ""):
    #     text_to_send_exercise += app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_weight_entry.get()
    #     wednesday_str_weight = app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_weight_entry.get()
    # else: 
    #     text_to_send_exercise += "None Given"
    #     wednesday_str_weight = "None Given"
    # text_to_send_exercise += ", Time Walked: "
    # wednesday_str_time_walked = ""
    # if (app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_time_walked_entry.get() != ""):
    #     text_to_send_exercise += app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_time_walked_entry.get()
    #     wednesday_str_time_walked = app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_time_walked_entry.get()
    # else: 
    #     text_to_send_exercise += "00:00:00"
    #     wednesday_str_time_walked = "00:00:00"
    # text_to_send_exercise += ", Distance: "
    # wednesday_str_distance = ""
    # if (app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_distance_entry.get() != ""):
    #     text_to_send_exercise += app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_distance_entry.get()
    #     wednesday_str_distance = app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_distance_entry.get()
    # else: 
    #     text_to_send_exercise += "0"
    #     wednesday_str_distance = "0"
    # text_to_send_exercise += ", Steps: "
    # wednesday_str_steps = ""
    # if (app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_steps_entry.get() != ""):
    #     text_to_send_exercise += app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_steps_entry.get()
    #     wednesday_str_steps = app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_steps_entry.get()
    # else: 
    #     text_to_send_exercise += "0"
    #     wednesday_str_steps = "0"
    # text_to_send_exercise += ", Calories Burned: "
    # wednesday_str_calories = ""
    # if (app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_calories_entry.get() != ""):
    #     text_to_send_exercise += app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_calories_entry.get()
    #     wednesday_str_calories = app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_calories_entry.get()
    # else: 
    #     text_to_send_exercise += "0"
    #     wednesday_str_calories = "0"
    # text_to_send_exercise += "\nThursday - Weight: "
    # thursday_str_weight = ""
    # if (app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_weight_entry.get() != ""):
    #     text_to_send_exercise += app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_weight_entry.get()
    #     thursday_str_weight = app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_weight_entry.get()
    # else: 
    #     text_to_send_exercise += "None Given"
    #     thursday_str_weight = "None Given"
    # text_to_send_exercise += ", Time Walked: "
    # thursday_str_time_walked = ""
    # if (app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_time_walked_entry.get() != ""):
    #     text_to_send_exercise += app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_time_walked_entry.get()
    #     thursday_str_time_walked = app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_time_walked_entry.get()
    # else: 
    #     text_to_send_exercise += "00:00:00"
    #     thursday_str_time_walked = "00:00:00"
    # text_to_send_exercise += ", Distance: "
    # thursday_str_distance = "0"
    # if (app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_distance_entry.get() != ""):
    #     text_to_send_exercise += app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_distance_entry.get()
    #     thursday_str_distance = app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_distance_entry.get()
    # else: 
    #     text_to_send_exercise += "0"
    #     thursday_str_distance = "0"
    # text_to_send_exercise += ", Steps: "
    # thursday_str_steps = ""
    # if (app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_steps_entry.get() != ""):
    #     text_to_send_exercise += app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_steps_entry.get()
    #     thursday_str_steps = app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_steps_entry.get()
    # else: 
    #     text_to_send_exercise += "0"
    #     thursday_str_steps = "0"
    # text_to_send_exercise += ", Calories Burned: "
    # thursday_str_calories = ""
    # if (app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_calories_entry.get() != ""):
    #     text_to_send_exercise += app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_calories_entry.get()
    #     thursday_str_calories = app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_calories_entry.get()
    # else: 
    #     text_to_send_exercise += "0"
    #     thursday_str_calories = "0"
    # text_to_send_exercise += "\nFriday - Weight: "
    # friday_str_weight = ""
    # if (app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_weight_entry.get() != ""):
    #     text_to_send_exercise += app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_weight_entry.get()
    #     friday_str_weight = app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_weight_entry.get()
    # else: 
    #     text_to_send_exercise += "None Given"
    #     friday_str_weight = "None Given"
    # text_to_send_exercise += ", Time Walked: "
    # friday_str_time_walked = ""
    # if (app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_time_walked_entry.get() != ""):
    #     text_to_send_exercise += app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_time_walked_entry.get()
    #     friday_str_time_walked = app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_time_walked_entry.get()
    # else: 
    #     text_to_send_exercise += "00:00:00"
    #     friday_str_time_walked = "00:00:00"
    # text_to_send_exercise += ", Distance: "
    # friday_str_distance = ""
    # if (app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_distance_entry.get() != ""):
    #     text_to_send_exercise += app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_distance_entry.get()
    #     friday_str_distance = app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_distance_entry.get()
    # else: 
    #     text_to_send_exercise += "0"
    #     friday_str_distance = "0"
    # text_to_send_exercise += ", Steps: "
    # friday_str_steps = "0"
    # if (app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_steps_entry.get() != ""):
    #     text_to_send_exercise += app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_steps_entry.get()
    #     friday_str_steps = app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_steps_entry.get()
    # else: 
    #     text_to_send_exercise += "0"
    #     friday_str_steps = "0"
    # text_to_send_exercise += ", Calories Burned: "
    # friday_str_calories = ""
    # if (app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_calories_entry.get() != ""):
    #     text_to_send_exercise += app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_calories_entry.get()
    #     friday_str_calories = app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_calories_entry.get()
    # else: 
    #     text_to_send_exercise += "0"
    #     friday_str_calories = "0"
    # text_to_send_exercise += "\nSaturday - Weight: "
    # saturday_str_weight = ""
    # if (app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_weight_entry.get() != ""):
    #     text_to_send_exercise += app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_weight_entry.get()
    #     saturday_str_weight = app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_weight_entry.get()
    # else: 
    #     text_to_send_exercise += "None Given"
    #     saturday_str_weight = "None Given"
    # text_to_send_exercise += ", Time Walked: "
    # saturday_str_time_walked = ""
    # if (app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_time_walked_entry.get() != ""):
    #     text_to_send_exercise += app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_time_walked_entry.get()
    #     saturday_str_time_walked = app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_time_walked_entry.get()
    # else: 
    #     text_to_send_exercise += "00:00:00"
    #     saturday_str_time_walked = "00:00:00"
    # text_to_send_exercise += ", Distance: "
    # saturday_str_distance = ""
    # if (app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_distance_entry.get() != ""):
    #     text_to_send_exercise += app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_distance_entry.get()
    #     saturday_str_distance = app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_distance_entry.get()
    # else: 
    #     text_to_send_exercise += "0"
    #     saturday_str_distance = "0"
    # text_to_send_exercise += ", Steps: "
    # saturday_str_steps = ""
    # if (app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_steps_entry.get() != ""):
    #     text_to_send_exercise += app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_steps_entry.get()
    #     saturday_str_steps = app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_steps_entry.get()
    # else: 
    #     text_to_send_exercise += "0"
    #     saturday_str_steps = "0"
    # text_to_send_exercise += ", Calories Burned: "
    # saturday_str_calories = ""
    # if (app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_calories_entry.get() != ""):
    #     text_to_send_exercise += app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_calories_entry.get()
    #     saturday_str_calories = app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_calories_entry.get()
    # else: 
    #     text_to_send_exercise += "0"
    #     saturday_str_calories = "0"

    # #Exercise Total Statistics
    # text_to_send_exercise += "\n\nEXERCISE TOTAL STATISTICS:"
    # text_to_send_exercise += "\nWeight Lost: "
    # total_str_weight = ""
    # if (app.totals_frame.total_weight_lost_entry.get() != ""):
    #     text_to_send_exercise += app.totals_frame.total_weight_lost_entry.get()
    #     total_str_weight = app.totals_frame.total_weight_lost_entry.get()
    # else: 
    #     text_to_send_exercise += "0"
    #     total_str_weight = "0"
    # text_to_send_exercise += ", Time Walked: "
    # total_str_time_walked = ""
    # if (app.totals_frame.time_walked_entry.get() != ""):
    #     text_to_send_exercise += app.totals_frame.time_walked_entry.get()
    #     total_str_time_walked = app.totals_frame.time_walked_entry.get()
    # else: 
    #     text_to_send_exercise += "00:00:00"
    #     total_str_time_walked = "00:00:00"
    # text_to_send_exercise += ", Distance: "
    # total_str_distance = ""
    # if (app.totals_frame.distance_entry.get() != ""):
    #     text_to_send_exercise += app.totals_frame.distance_entry.get()
    #     total_str_distance = app.totals_frame.distance_entry.get()
    # else: 
    #     text_to_send_exercise += "0"
    #     total_str_distance = "0"
    # text_to_send_exercise += ", Steps: "
    # total_str_steps = ""
    # if (app.totals_frame.steps_entry.get() != ""):
    #     text_to_send_exercise += app.totals_frame.steps_entry.get()
    #     total_str_steps = app.totals_frame.steps_entry.get()
    # else: 
    #     text_to_send_exercise += "0"
    #     total_str_steps = "0"
    # text_to_send_exercise += ", Calories Burned: "
    # total_str_calories = ""
    # if (app.totals_frame.calories_burned_entry.get() != ""):
    #     text_to_send_exercise += app.totals_frame.calories_burned_entry.get()
    #     total_str_calories = app.totals_frame.calories_burned_entry.get()
    # else: 
    #     text_to_send_exercise += "0"
    #     total_str_calories = "0"

    # textbox2 = CTk.CTkTextbox(tab_view.tab("Exercise Data"), wrap="word", height=350, width=750)
    # textbox2.pack()
    # textbox2.insert(1.0, text_to_send_exercise)
    # textbox2.configure(state="disabled")

    button_frame = CTk.CTkFrame(modal_dialog, fg_color="transparent")
    button_frame.grid(row=12, column=0, pady=(30,10))

    def send_code_data_and_close():
        with open('work.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            # Dates
            writer.writerow(["Dates"])
            writer.writerow([current_week_range])
            writer.writerow([""])
            # Time Worked Each Day
            writer.writerow(["Day of the Week", "Time Worked Each Day", "Punches for Each Day"])
            writer.writerow(["Sunday", sunday_str_time_worked, sunday_str_punches])
            writer.writerow(["Monday", monday_str_time_worked,  monday_str_punches])
            writer.writerow(["Tuesday", tuesday_str_time_worked, tuesday_str_punches])
            writer.writerow(["Wednesday", wednesday_str_time_worked, wednesday_str_punches])
            writer.writerow(["Thursday", thursday_str_time_worked, thursday_str_punches])
            writer.writerow(["Friday", friday_str_time_worked, friday_str_punches])
            writer.writerow(["Saturday", saturday_str_time_worked, saturday_str_punches])
            writer.writerow([""])
            # Total Time Worked
            writer.writerow(["Total Time Worked"])
            writer.writerow([total_str_time_worked])
            writer.writerow([""])
            # Description
            writer.writerow(["Description"])
            writer.writerow([description_str])

        load_dotenv(".env", override=True)
        discord_webhook = os.environ.get("Discord_Webhook")
        print(discord_webhook)
        if (discord_webhook == "None"):
            pass
        else:
            try:
                print(discord_webhook)
                webhook = discord.SyncWebhook.from_url('https://discord.com/api/webhooks/https://discord.com/api/webhooks/' + discord_webhook) # Initializing webhook

                with open(file='work.csv', mode='rb') as f:
                    my_file = discord.File(f)

                webhook.send(text_to_send, file=my_file)
            except:
                modal_dialog.destroy()

        modal_dialog.destroy()

    # def send_exerice_data_and_close():
    #     with open('exercise.csv', 'w', newline='') as file:
    #         writer = csv.writer(file)
    #         # Dates
    #         writer.writerow(["Dates"])
    #         writer.writerow([current_week_range])
    #         writer.writerow([""])
    #         # Time Worked Each Day
    #         writer.writerow(["Exercise Daily Statistics"])
    #         writer.writerow(["Day of the Week", "Weight", "Time Walked", "Distance", "Steps", "Calories Burned"])
    #         writer.writerow(["Sunday", sunday_str_weight, sunday_str_time_walked, sunday_str_distance, sunday_str_steps, sunday_str_calories])
    #         writer.writerow(["Monday", monday_str_weight, monday_str_time_walked, monday_str_distance, monday_str_steps, monday_str_calories])
    #         writer.writerow(["Tuesday", tuesday_str_weight, tuesday_str_time_walked, tuesday_str_distance, tuesday_str_steps, tuesday_str_calories])
    #         writer.writerow(["Wednesday", wednesday_str_weight, wednesday_str_time_walked, wednesday_str_distance, wednesday_str_steps, wednesday_str_calories])
    #         writer.writerow(["Thursday", thursday_str_weight, thursday_str_time_walked, thursday_str_distance, thursday_str_steps, thursday_str_calories])
    #         writer.writerow(["Friday", friday_str_weight, friday_str_time_walked, friday_str_distance, friday_str_steps, friday_str_calories])
    #         writer.writerow(["Saturday", saturday_str_weight, saturday_str_time_walked, saturday_str_distance, saturday_str_steps, saturday_str_calories])
    #         writer.writerow([""])
    #         # Total Time Worked
    #         writer.writerow(["Exercise Total Statistics"])
    #         writer.writerow(["Total Weight Lost", "Total Time Walked", "Total Distance", "Total Steps", "Total Calories Burned"])
    #         writer.writerow([total_str_weight, total_str_time_walked, total_str_distance, total_str_steps, total_str_calories])

    #         load_dotenv(".env")
    #         webhook_arr = os.environ.get("Exercise_Webhooks")
    #         if (webhook_arr == "None"):
    #             pass
    #         else:
    #             webhook_arr = webhook_arr.split(",")
    #             for i in webhook_arr:
    #                 webhook_str = i

    #                 webhook = discord.SyncWebhook.from_url('https://discord.com/api/webhooks/https://discord.com/api/webhooks/' + webhook_str) # Initializing webhook

    #                 with open(file='exercise.csv', mode='rb') as f:
    #                     my_file = discord.File(f)

    #                 webhook.send(text_to_send_exercise, file=my_file)

    #         modal_dialog.destroy()

    button = CTk.CTkButton(button_frame, text="Send Work Data", command=send_code_data_and_close)
    button.grid(row=0, column=0, padx=(0,5))

    # button = CTk.CTkButton(button_frame, text="Send Exercise Data", command=send_exerice_data_and_close)
    # button.grid(row=0, column=1, padx=(5,5))

    button = CTk.CTkButton(button_frame, text="Cancel", command=modal_dialog.destroy)
    button.grid(row=0, column=1, padx=(5,0))

    modal_dialog.grid_columnconfigure(0, weight=1)

    app.wait_window(modal_dialog)  # Wait for the modal dialog to be closed

def clear_data_modal():
    modal_dialog = CTk.CTkToplevel(app)
    modal_dialog.grab_set()  # Make the dialog modal
    modal_dialog.geometry("400x150")
    modal_dialog.title("Clear Data")
    modal_dialog.iconbitmap("icon4.ico")
    center_window(modal_dialog, 400, 150)

    # Add your dialog content here
    first_label = CTk.CTkLabel(modal_dialog, text="Make sure that all data is sent beforehand.")
    first_label.grid(row=0, column=0)
    
    second_label = CTk.CTkLabel(modal_dialog, text="All data not sent will be permanently lost!")
    second_label.grid(row=1, column=0)

    third_label = CTk.CTkLabel(modal_dialog, text="Are you sure you want to clear your data?")
    third_label.grid(row=2, column=0)

    button_frame = CTk.CTkFrame(modal_dialog, fg_color="transparent")
    button_frame.grid(row=3, column=0, pady=(15,0))

    def clear_data_and_close():
        clear_data()
        modal_dialog.destroy()

    button = CTk.CTkButton(button_frame, text="Clear Data", command=clear_data_and_close)
    button.grid(row=0, column=0, padx=(0,5))

    button = CTk.CTkButton(button_frame, text="Cancel", command=modal_dialog.destroy)
    button.grid(row=0, column=1, padx=(5,0))

    modal_dialog.grid_columnconfigure(0, weight=1)
    app.wait_window(modal_dialog)  # Wait for the modal dialog to be closed

def new_week_modal():
    modal_dialog = CTk.CTkToplevel(app)
    modal_dialog.grab_set()  # Make the dialog modal
    modal_dialog.geometry("700x200")
    modal_dialog.title("Clear Data")
    modal_dialog.iconbitmap("icon4.ico")
    center_window(modal_dialog, 700, 200)

    # Add your dialog content here
    first_label = CTk.CTkLabel(modal_dialog, text="You have been clocked out due to being clocked in during a new week without clearing first.")
    first_label.grid(row=0, column=0)

    second_label = CTk.CTkLabel(modal_dialog, text="Your program has been locked except for the description box, send weekly data button and clear weekly data button.")
    second_label.grid(row=1, column=0)

    third_label = CTk.CTkLabel(modal_dialog, text="Please send your data and then clear your data to unlock your program.")
    third_label.grid(row=2, column=0)
    
    fourth_label = CTk.CTkLabel(modal_dialog, text="All data not sent will be permanently lost!")
    fourth_label.grid(row=3, column=0)

    button_frame = CTk.CTkFrame(modal_dialog, fg_color="transparent")
    button_frame.grid(row=4, column=0, pady=(15,0))

    button = CTk.CTkButton(button_frame, text="Close", command=modal_dialog.destroy)
    button.grid(row=0, column=1)

    modal_dialog.grid_columnconfigure(0, weight=1)
    app.wait_window(modal_dialog)  # Wait for the modal dialog to be closed

def save_description(event):
    data = {
        "description": app.weekly_daily_tabs.weekly_tab.description_textbox.get("1.0", "end-1c")
        }
    write_description_to_file(data)
    global description
    description = data["description"]

# thursday_weight_as_float = 0
# def validate_thursday_weight_float(event):
#     global thursday_weight_as_float
#     try:
#         thursday_weight_as_float = float(app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_weight_entry.get())
#         thursday_weight = thursday_weight_as_float
#     except ValueError:
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_weight_entry.delete(0, "end")
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_weight_entry.insert(0, str(thursday_weight_as_float))

# friday_weight_as_float = 0
# def validate_friday_weight_float(event):
#     global friday_weight_as_float
#     try:
#         friday_weight_as_float = float(app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_weight_entry.get())
#         friday_weight = friday_weight_as_float
#     except ValueError:
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_weight_entry.delete(0, "end")
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_weight_entry.insert(0, str(friday_weight_as_float))

# saturday_weight_as_float = 0
# def validate_saturday_weight_float(event):
#     global saturday_weight_as_float
#     try:
#         saturday_weight_as_float = float(app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_weight_entry.get())
#         saturday_weight = saturday_weight_as_float
#     except ValueError:
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_weight_entry.delete(0, "end")
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_weight_entry.insert(0, str(saturday_weight_as_float))

# sunday_weight_as_float = 0
# def validate_sunday_weight_float(event):
#     global sunday_weight_as_float
#     try:
#         sunday_weight_as_float = float(app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_weight_entry.get())
#         sunday_weight = sunday_weight_as_float
#     except ValueError:
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_weight_entry.delete(0, "end")
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_weight_entry.insert(0, str(sunday_weight_as_float))

# monday_weight_as_float = 0
# def validate_monday_weight_float(event):
#     global monday_weight_as_float
#     try:
#         monday_weight_as_float = float(app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_weight_entry.get())
#         monday_weight = monday_weight_as_float
#     except ValueError:
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_weight_entry.delete(0, "end")
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_weight_entry.insert(0, str(monday_weight_as_float))

# tuesday_weight_as_float = 0
# def validate_tuesday_weight_float(event):
#     global tuesday_weight_as_float
#     try:
#         tuesday_weight_as_float = float(app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_weight_entry.get())
#         tuesday_weight = tuesday_weight_as_float
#     except ValueError:
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_weight_entry.delete(0, "end")
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_weight_entry.insert(0, str(tuesday_weight_as_float))

# wednesday_weight_as_float = 0
# def validate_wednesday_weight_float(event):
#     global wednesday_weight_as_float
#     try:
#         wednesday_weight_as_float = float(app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_weight_entry.get())
#         wednesday_weight = wednesday_weight_as_float
#     except ValueError:
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_weight_entry.delete(0, "end")
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_weight_entry.insert(0, str(wednesday_weight_as_float))

def start_end():
    # start
    global start_time
    global tracking
    global readytostart
    global paused
    global thursday_punches
    global friday_punches
    global saturday_punches
    global sunday_punches
    global monday_punches
    global tuesday_punches
    global wednesday_punches
    global can_clear
    global must_clear
    global current_week
    global curr_week_str
    if (current_week != datetime.datetime.now().strftime("%U %Y") and current_week != -1):
        app.weekly_daily_tabs.daily_tab.start_end_button.configure(state="disabled")
        # Create a notification
        notification.notify(
            title="You've been clocked out!",
            message="You've been clocked out due to being clocked in during a new week without clearing first.",
            app_name="Productivity Tracker",
            app_icon="icon4.ico",
            timeout=10  # Duration to display the notification in seconds
        )
        app.attributes("-topmost", True)
        app.attributes("-topmost", False)
        new_week_modal()
    else:
        can_clear = False
        app.buttons_frame.send_weekly_data_button.configure(state="disabled")
        app.buttons_frame.clear_weekly_data_button.configure(state="disabled")
        app.weekly_daily_tabs.weekly_tab.description_textbox.configure(state="disabled")
        # app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_weight_entry.configure(state="disabled")
        # app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_weight_entry.configure(state="disabled")
        # app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_weight_entry.configure(state="disabled")
        # app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_weight_entry.configure(state="disabled")
        # app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_weight_entry.configure(state="disabled")
        # app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_weight_entry.configure(state="disabled")
        # app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_weight_entry.configure(state="disabled")
        if (readytostart):
            readytostart = False
            start_time = time.time()
            tracking = True
            app.weekly_daily_tabs.daily_tab.start_end_button.configure(text="End")
            app.weekly_daily_tabs.daily_tab.pause_resume_button.configure(state="normal")
            
            #global wednesday_punches
            day = datetime.datetime.now().strftime("%A")
            if (day == "Thursday"):
                thursday_punches.append("Start: " + str(datetime.datetime.now().strftime("%I:%M:%S %p")))
                if (thursday_punches[0] == "None"):
                    thursday_punches.pop(0)
                app.weekly_daily_tabs.weekly_tab.thursday_punches_entry.configure(values=thursday_punches)
            elif (day == "Friday"):
                friday_punches.append("Start: " + str(datetime.datetime.now().strftime("%I:%M:%S %p")))
                if (friday_punches[0] == "None"):
                    friday_punches.pop(0)
                app.weekly_daily_tabs.weekly_tab.friday_punches_entry.configure(values=friday_punches)
            elif (day == "Saturday"):
                saturday_punches.append("Start: " + str(datetime.datetime.now().strftime("%I:%M:%S %p")))
                if (saturday_punches[0] == "None"):
                    saturday_punches.pop(0)
                app.weekly_daily_tabs.weekly_tab.saturday_punches_entry.configure(values=saturday_punches)
            elif (day == "Sunday"):
                sunday_punches.append("Start: " + str(datetime.datetime.now().strftime("%I:%M:%S %p")))
                if (sunday_punches[0] == "None"):
                    sunday_punches.pop(0)
                app.weekly_daily_tabs.weekly_tab.sunday_punches_entry.configure(values=sunday_punches)
            elif (day == "Monday"):
                monday_punches.append("Start: " + str(datetime.datetime.now().strftime("%I:%M:%S %p")))
                if (monday_punches[0] == "None"):
                    monday_punches.pop(0)
                app.weekly_daily_tabs.weekly_tab.monday_punches_entry.configure(values=monday_punches)
            elif (day == "Tuesday"):
                tuesday_punches.append("Start: " + str(datetime.datetime.now().strftime("%I:%M:%S %p")))
                if (tuesday_punches[0] == "None"):
                    tuesday_punches.pop(0)
                app.weekly_daily_tabs.weekly_tab.tuesday_punches_entry.configure(values=tuesday_punches)
            else:
                wednesday_punches.append("Start: " + str(datetime.datetime.now().strftime("%I:%M:%S %p")))
                if (wednesday_punches[0] == "None"):
                    wednesday_punches.pop(0)
                app.weekly_daily_tabs.weekly_tab.wednesday_punches_entry.configure(values=wednesday_punches)

            data = {
                "thursday_punches": thursday_punches,
                "friday_punches": friday_punches,
                "saturday_punches": saturday_punches,
                "sunday_punches": sunday_punches,
                "monday_punches": monday_punches,
                "tuesday_punches": tuesday_punches,
                "wednesday_punches": wednesday_punches,
            }

            threading.Thread(target=write_punches_to_file, args=(data,)).start()

            if (curr_week_str == ""):
                curr_week_str = get_date_range_for_current_week()
                data = {
                    "curr_week_str": curr_week_str
                }
                threading.Thread(target=write_current_week_to_file, args=(data,)).start()

            if (current_week == -1):
                current_week = datetime.datetime.now().strftime("%U %Y")
                data = {
                    "must_clear": must_clear,
                    "current_week": current_week
                }
                threading.Thread(target=write_must_clear_to_file, args=(data,)).start()
            
            # Flush out timer if one is set and start clock
            if (timer_id != ""):
                app.after_cancel(timer_id)
            update_time(True)
        else:
            global p_focus_time
            global p_break_time
            global p_long_break_time
            global p_cycle_count
            can_clear = True
            app.buttons_frame.send_weekly_data_button.configure(state="normal")
            app.buttons_frame.clear_weekly_data_button.configure(state="normal")
            app.weekly_daily_tabs.weekly_tab.description_textbox.configure(state="normal")
            # day = datetime.datetime.now().strftime("%A")
            # if (day == "Thursday"):
            #     app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_weight_entry.configure(state="normal")
            # elif (day == "Friday"):
            #     app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_weight_entry.configure(state="normal")
            # elif (day == "Saturday"):
            #     app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_weight_entry.configure(state="normal")
            # elif (day == "Sunday"):
            #     app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_weight_entry.configure(state="normal")
            # elif (day == "Monday"):
            #     app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_weight_entry.configure(state="normal")
            # elif (day == "Tuesday"):
            #     app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_weight_entry.configure(state="normal")
            # else:
            #     app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_weight_entry.configure(state="normal")

            # app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_weight_entry.configure(state="normal")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_weight_entry.configure(state="normal")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_weight_entry.configure(state="normal")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_weight_entry.configure(state="normal")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_weight_entry.configure(state="normal")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_weight_entry.configure(state="normal")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_weight_entry.configure(state="normal")
            app.weekly_daily_tabs.daily_tab.start_end_button.configure(text="Start")
            app.weekly_daily_tabs.daily_tab.pause_resume_button.configure(state="disabled")
            app.weekly_daily_tabs.daily_tab.total_time_label.configure(text="00:00:00")
            app.weekly_daily_tabs.daily_tab.pomodoro_time_label.configure(text="00:25:00")
            app.weekly_daily_tabs.daily_tab.pause_resume_button.configure(text="Pause")
            app.weekly_daily_tabs.daily_tab.pomodoro_count_label.configure(text="#1")
            app.weekly_daily_tabs.daily_tab.pomodoro_focus_label.configure(text="Focus")
            readytostart = True
            paused = False
            p_focus_time = focus_time
            p_break_time = break_time
            p_long_break_time = long_break_time
            p_cycle_count = 1

            #global wednesday_punches
            day = datetime.datetime.now().strftime("%A")
            if (day == "Thursday"):
                thursday_punches.append("End: " + str(datetime.datetime.now().strftime("%I:%M:%S %p")))
                if (thursday_punches[0] == "None"):
                    thursday_punches.pop(0)
                app.weekly_daily_tabs.weekly_tab.thursday_punches_entry.configure(values=thursday_punches)
            elif (day == "Friday"):
                friday_punches.append("End: " + str(datetime.datetime.now().strftime("%I:%M:%S %p")))
                if (friday_punches[0] == "None"):
                    friday_punches.pop(0)
                app.weekly_daily_tabs.weekly_tab.friday_punches_entry.configure(values=friday_punches)
            elif (day == "Saturday"):
                saturday_punches.append("End: " + str(datetime.datetime.now().strftime("%I:%M:%S %p")))
                if (saturday_punches[0] == "None"):
                    saturday_punches.pop(0)
                app.weekly_daily_tabs.weekly_tab.saturday_punches_entry.configure(values=saturday_punches)
            elif (day == "Sunday"):
                sunday_punches.append("End: " + str(datetime.datetime.now().strftime("%I:%M:%S %p")))
                if (sunday_punches[0] == "None"):
                    sunday_punches.pop(0)
                app.weekly_daily_tabs.weekly_tab.sunday_punches_entry.configure(values=sunday_punches)
            elif (day == "Monday"):
                monday_punches.append("End: " + str(datetime.datetime.now().strftime("%I:%M:%S %p")))
                if (monday_punches[0] == "None"):
                    monday_punches.pop(0)
                app.weekly_daily_tabs.weekly_tab.monday_punches_entry.configure(values=monday_punches)
            elif (day == "Tuesday"):
                tuesday_punches.append("End: " + str(datetime.datetime.now().strftime("%I:%M:%S %p")))
                if (tuesday_punches[0] == "None"):
                    tuesday_punches.pop(0)
                app.weekly_daily_tabs.weekly_tab.tuesday_punches_entry.configure(values=tuesday_punches)
            else:
                wednesday_punches.append("End: " + str(datetime.datetime.now().strftime("%I:%M:%S %p")))
                if (wednesday_punches[0] == "None"):
                    wednesday_punches.pop(0)
                app.weekly_daily_tabs.weekly_tab.wednesday_punches_entry.configure(values=wednesday_punches)

            data = {
                "thursday_punches": thursday_punches,
                "friday_punches": friday_punches,
                "saturday_punches": saturday_punches,
                "sunday_punches": sunday_punches,
                "monday_punches": monday_punches,
                "tuesday_punches": tuesday_punches,
                "wednesday_punches": wednesday_punches,
            }

            threading.Thread(target=write_punches_to_file, args=(data,)).start()

            app.after_cancel(timer_id)

def pause_resume():
    global tracking
    global paused
    # pause resume switch
    if (not paused):
        paused = True
        tracking = False
        app.weekly_daily_tabs.daily_tab.pause_resume_button.configure(text="Resume")
        app.after_cancel(timer_id)
    else:
        paused = False
        tracking = True
        app.weekly_daily_tabs.daily_tab.pause_resume_button.configure(text="Pause")
        # Flush out timer and resume clock
        app.after_cancel(timer_id)
        update_time(True)

def pomodoro():
    global pomodoro_break
    global p_cycle_count
    global p_string_store
    # If Elif Else for determining pomodoro states
    if (app.weekly_daily_tabs.daily_tab.pomodoro_switch.get() == 1):
        if (not pomodoro_break):
            # 25 min
            global p_focus_time
            p_focus_time = p_focus_time - 1
            hours = p_focus_time // 3600
            minutes = (p_focus_time % 3600) // 60
            seconds = p_focus_time % 60
            p_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            # Sets label text to current time left
            app.weekly_daily_tabs.daily_tab.pomodoro_time_label.configure(text=p_string)
            
        elif (pomodoro_break and p_cycle_count % 4 == 0):
            # 15 min
            global p_long_break_time
            p_long_break_time = p_long_break_time - 1
            hours = p_long_break_time // 3600
            minutes = (p_long_break_time % 3600) // 60
            seconds = p_long_break_time % 60
            p_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            # Sets label text to current time left
            app.weekly_daily_tabs.daily_tab.pomodoro_time_label.configure(text=p_string)
            
        else:
            # 5 min
            global p_break_time
            p_break_time = p_break_time - 1
            hours = p_break_time // 3600
            minutes = (p_break_time % 3600) // 60
            seconds = p_break_time % 60
            p_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            # Sets label text to current time left
            app.weekly_daily_tabs.daily_tab.pomodoro_time_label.configure(text=p_string)
            

        # If for on pomodoro state end (time reaches 00:00:00)
        if (app.weekly_daily_tabs.daily_tab.pomodoro_time_label._text == "00:00:00"):
            # Swap break state and increment cycle count if break
            if (pomodoro_break):
                p_cycle_count = p_cycle_count + 1
                app.weekly_daily_tabs.daily_tab.pomodoro_count_label.configure(text="#" + str(p_cycle_count))
                app.weekly_daily_tabs.daily_tab.pomodoro_focus_label.configure(text="Focus")
                pomodoro_break = False
            else:
                app.weekly_daily_tabs.daily_tab.pomodoro_focus_label.configure(text="Break")
                pomodoro_break = True
            
            # Reset Pomodoro vars
            global break_time
            global long_break_time
            global focus_time
            p_break_time = break_time
            p_focus_time = focus_time
            p_long_break_time = long_break_time

            # Pause and reset label
            pause_resume()

            # If Elif Else for determining pomodoro states
            if (app.weekly_daily_tabs.daily_tab.pomodoro_switch.get() == 1):
                if (not pomodoro_break):
                    # 25 min
                    # Create a notification
                    notification.notify(
                        title="Focus",
                        message="Focus for 25 minutes.",
                        app_name="Productivity Tracker",
                        app_icon="icon4.ico",
                        timeout=10  # Duration to display the notification in seconds
                    )
                    app.attributes("-topmost", True)
                    app.attributes("-topmost", False)
                    hours = p_focus_time // 3600
                    minutes = (p_focus_time % 3600) // 60
                    seconds = p_focus_time % 60
                    p_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
                    # Sets label text to current time left
                    app.weekly_daily_tabs.daily_tab.pomodoro_time_label.configure(text=p_string)
                
                elif (pomodoro_break and p_cycle_count % 4 == 0):
                    # 15 min
                    # Create a notification
                    notification.notify(
                        title="Long Break",
                        message="Break for 15 minutes.",
                        app_name="Productivity Tracker",
                        app_icon="icon4.ico",
                        timeout=10  # Duration to display the notification in seconds
                    )
                    app.attributes("-topmost", True)
                    app.attributes("-topmost", False)
                    hours = p_long_break_time // 3600
                    minutes = (p_long_break_time % 3600) // 60
                    seconds = p_long_break_time % 60
                    p_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
                    # Sets label text to current time left
                    app.weekly_daily_tabs.daily_tab.pomodoro_time_label.configure(text=p_string)
                    
                else:
                    # 5 min
                    # Create a notification
                    notification.notify(
                        title="Short Break",
                        message="Break for 5 minutes.",
                        app_name="Productivity Tracker",
                        app_icon="icon4.ico",
                        timeout=10  # Duration to display the notification in seconds
                    )
                    app.attributes("-topmost", True)
                    app.attributes("-topmost", False)
                    hours = p_break_time // 3600
                    minutes = (p_break_time % 3600) // 60
                    seconds = p_break_time % 60
                    p_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
                    # Sets label text to current time left
                    app.weekly_daily_tabs.daily_tab.pomodoro_time_label.configure(text=p_string)

# def calc_weight_loss():
#     first_weight = 0
#     last_weight = 0

#     #Get First Weight
#     if (first_weight == 0 and app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_weight_entry.get() != ""):
        
#         first_weight = app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_weight_entry.get()
        
#     elif (first_weight == 0 and app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_weight_entry.get() != ""):
        
#         first_weight = app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_weight_entry.get()

#     elif (first_weight == 0 and app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_weight_entry.get() != ""):
        
#         first_weight = app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_weight_entry.get()

#     elif (first_weight == 0 and app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_weight_entry.get() != ""):
        
#         first_weight = app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_weight_entry.get()

#     elif (first_weight == 0 and app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_weight_entry.get() != ""):
        
#         first_weight = app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_weight_entry.get()

#     elif (first_weight == 0 and app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_weight_entry.get() != ""):
        
#         first_weight = app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_weight_entry.get()

#     elif (first_weight == 0 and app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_weight_entry.get() != ""):
        
#         first_weight = app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_weight_entry.get()

#     #Get Last Weight, set weigh in count, and set vars
#     weigh_in_count = 0
#     global sunday_weight
#     global monday_weight
#     global tuesday_weight
#     global wednesday_weight
#     global thursday_weight
#     global friday_weight
#     global saturday_weight
#     global sunday_weight
#     global total_weight_lost
#     global current_weight
#     if (app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_weight_entry.get() != ""):
        
#         last_weight = app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_weight_entry.get()
#         weigh_in_count = weigh_in_count + 1
#         sunday_weight = last_weight
#         current_weight = last_weight
        
#     if (app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_weight_entry.get() != ""):
        
#         last_weight = app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_weight_entry.get()
#         weigh_in_count = weigh_in_count + 1
#         monday_weight = last_weight
#         current_weight = last_weight

#     if (app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_weight_entry.get() != ""):
        
#         last_weight = app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_weight_entry.get()
#         weigh_in_count = weigh_in_count + 1
#         tuesday_weight = last_weight
#         current_weight = last_weight

#     if (app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_weight_entry.get() != ""):
        
#         last_weight = app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_weight_entry.get()
#         weigh_in_count = weigh_in_count + 1
#         wednesday_weight = last_weight
#         current_weight = last_weight

#     if (app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_weight_entry.get() != ""):
        
#         last_weight = app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_weight_entry.get()
#         weigh_in_count = weigh_in_count + 1
#         thursday_weight = last_weight
#         current_weight = last_weight

#     if (app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_weight_entry.get() != ""):
        
#         last_weight = app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_weight_entry.get()
#         weigh_in_count = weigh_in_count + 1
#         friday_weight = last_weight
#         current_weight = last_weight

#     if (app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_weight_entry.get() != ""):
        
#         last_weight = app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_weight_entry.get()
#         weigh_in_count = weigh_in_count + 1
#         saturday_weight = last_weight
#         current_weight = last_weight

#     # Calculate Weight Lost
#     weight_lost = 0
#     weight_lost_str = 0
#     #Check to make sure both vars are not equal
#     if (first_weight != last_weight):
#         weight_lost = float(first_weight) - float(last_weight)
#         weight_lost = round(weight_lost, 2)
#         app.totals_frame.total_weight_lost_entry.configure(state="normal")
#         weight_lost_str = ""
#         # Choose whether to display positive or negative value depending on subtraction
#         if (weight_lost > 0):
#             weight_lost_str = "-" + str(weight_lost)
#         elif (weight_lost < 0):
#             weight_lost_str = "+" + str(abs(weight_lost))
#         app.totals_frame.total_weight_lost_entry.delete(0, "end")
#         app.totals_frame.total_weight_lost_entry.insert(0, weight_lost_str)
#         app.totals_frame.total_weight_lost_entry.configure(state="disabled")
#     # Check to make sure both vars set
#     elif ((first_weight != 0 or last_weight != 0) and weigh_in_count > 1):
#         app.totals_frame.total_weight_lost_entry.configure(state="normal")
#         app.totals_frame.total_weight_lost_entry.delete(0, "end")
#         app.totals_frame.total_weight_lost_entry.insert(0, "0")
#         app.totals_frame.total_weight_lost_entry.configure(state="disabled")

#     # Set total_weight_lost
#     total_weight_lost = weight_lost_str

# def walking():
#     if (app.weekly_daily_tabs.daily_tab.walking_switch.get() == 1):
#         global thursday_walking_time
#         global friday_walking_time
#         global saturday_walking_time
#         global sunday_walking_time
#         global monday_walking_time
#         global tuesday_walking_time
#         global wednesday_walking_time
#         global total_walking_time

#         day = datetime.datetime.now().strftime("%A")
#         if (day == "Thursday"):
#             thursday_walking_time = thursday_walking_time + 1
#             hours = thursday_walking_time // 3600
#             minutes = (thursday_walking_time % 3600) // 60
#             seconds = thursday_walking_time % 60
#             walking_time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
#             app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_time_walked_entry.configure(state="normal")
#             app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_time_walked_entry.delete(0, "end")
#             app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_time_walked_entry.insert(0, walking_time_string)
#             app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_time_walked_entry.configure(state="disabled")
#         elif (day == "Friday"):
#             friday_walking_time = friday_walking_time + 1
#             hours = friday_walking_time // 3600
#             minutes = (friday_walking_time % 3600) // 60
#             seconds = friday_walking_time % 60
#             walking_time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
#             app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_time_walked_entry.configure(state="normal")
#             app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_time_walked_entry.delete(0, "end")
#             app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_time_walked_entry.insert(0, walking_time_string)
#             app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_time_walked_entry.configure(state="disabled")
#         elif (day == "Saturday"):
#             saturday_walking_time = saturday_walking_time + 1
#             hours = saturday_walking_time // 3600
#             minutes = (saturday_walking_time % 3600) // 60
#             seconds = saturday_walking_time % 60
#             walking_time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
#             app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_time_walked_entry.configure(state="normal")
#             app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_time_walked_entry.delete(0, "end")
#             app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_time_walked_entry.insert(0, walking_time_string)
#             app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_time_walked_entry.configure(state="disabled")
#         elif (day == "Sunday"):
#             sunday_walking_time = sunday_walking_time + 1
#             hours = sunday_walking_time // 3600
#             minutes = (sunday_walking_time % 3600) // 60
#             seconds = sunday_walking_time % 60
#             walking_time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
#             app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_time_walked_entry.configure(state="normal")
#             app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_time_walked_entry.delete(0, "end")
#             app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_time_walked_entry.insert(0, walking_time_string)
#             app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_time_walked_entry.configure(state="disabled")
#         elif (day == "Monday"):
#             monday_walking_time = monday_walking_time + 1
#             hours = monday_walking_time // 3600
#             minutes = (monday_walking_time % 3600) // 60
#             seconds = monday_walking_time % 60
#             walking_time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
#             app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_time_walked_entry.configure(state="normal")
#             app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_time_walked_entry.delete(0, "end")
#             app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_time_walked_entry.insert(0, walking_time_string)
#             app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_time_walked_entry.configure(state="disabled")
#         elif (day == "Tuesday"):
#             tuesday_walking_time = tuesday_walking_time + 1
#             hours = tuesday_walking_time // 3600
#             minutes = (tuesday_walking_time % 3600) // 60
#             seconds = tuesday_walking_time % 60
#             walking_time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
#             app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_time_walked_entry.configure(state="normal")
#             app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_time_walked_entry.delete(0, "end")
#             app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_time_walked_entry.insert(0, walking_time_string)
#             app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_time_walked_entry.configure(state="disabled")
#         else:
#             wednesday_walking_time = wednesday_walking_time + 1
#             hours = wednesday_walking_time // 3600
#             minutes = (wednesday_walking_time % 3600) // 60
#             seconds = wednesday_walking_time % 60
#             walking_time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
#             app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_time_walked_entry.configure(state="normal")
#             app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_time_walked_entry.delete(0, "end")
#             app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_time_walked_entry.insert(0, walking_time_string)
#             app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_time_walked_entry.configure(state="disabled")
        
#         total_walking_time = thursday_walking_time + friday_walking_time + saturday_walking_time + sunday_walking_time + monday_walking_time + tuesday_walking_time + wednesday_walking_time
#         hours = total_walking_time // 3600
#         minutes = (total_walking_time % 3600) // 60
#         seconds = total_walking_time % 60
#         walking_time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
#         app.totals_frame.time_walked_entry.configure(state="normal")
#         app.totals_frame.time_walked_entry.delete(0, "end")
#         app.totals_frame.time_walked_entry.insert(0, walking_time_string)
#         app.totals_frame.time_walked_entry.configure(state="disabled")

# def update_walking_stats():
#     global thursday_walking_distance
#     global friday_walking_distance
#     global saturday_walking_distance
#     global sunday_walking_distance
#     global monday_walking_distance
#     global tuesday_walking_distance
#     global wednesday_walking_distance

#     global thursday_walking_steps
#     global friday_walking_steps
#     global saturday_walking_steps
#     global sunday_walking_steps
#     global monday_walking_steps
#     global tuesday_walking_steps
#     global wednesday_walking_steps

#     global thursday_calories
#     global friday_calories
#     global saturday_calories
#     global sunday_calories
#     global monday_calories
#     global tuesday_calories
#     global wednesday_calories

#     day = datetime.datetime.now().strftime("%A")
#     if (day == "Thursday"):
#         time_in_seconds = thursday_walking_time
#         speed_in_mph = 2
#         steps_per_mile = 2000
#         met = 2.9
#         if current_weight != 0:
#             weight_in_pounds = float(current_weight)
#         else:
#             weight_in_pounds = 150

#         # Step 1: Convert time from seconds to hours
#         time_in_hours = time_in_seconds / 3600

#         # Step 2: Calculate the distance traveled in miles
#         distance_in_miles = time_in_hours * speed_in_mph

#         # Round the result to two decimal places
#         distance_in_miles_rounded = round(distance_in_miles, 2)

#         # Print the result
#         thursday_walking_distance = distance_in_miles_rounded
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_distance_entry.configure(state="normal")
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_distance_entry.delete(0, "end")
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_distance_entry.insert(0, str(distance_in_miles_rounded))
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_distance_entry.configure(state="disabled")

#         # Step 4: Calculate the number of steps
#         steps = distance_in_miles * steps_per_mile

#         # Round the number of steps to the nearest integer
#         steps_rounded = round(steps)

#         # Print the result
#         thursday_walking_steps = steps_rounded
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_steps_entry.configure(state="normal")
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_steps_entry.delete(0, "end")
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_steps_entry.insert(0, str(steps_rounded))
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_steps_entry.configure(state="disabled")

#         # Step 5: Calculate the calories burned
#         weight_in_kilograms = weight_in_pounds / 2.205
#         time = distance_in_miles/speed_in_mph
#         calories_burned = met * weight_in_kilograms * time

#         # Round the calories burned to two decimal places
#         calories_burned_rounded = round(calories_burned, 2)

#         # Print the result
#         thursday_calories = calories_burned_rounded
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_calories_entry.configure(state="normal")
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_calories_entry.delete(0, "end")
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_calories_entry.insert(0, str(calories_burned_rounded))
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_calories_entry.configure(state="disabled")

#         thursday_walking_distance = distance_in_miles_rounded
#         thursday_walking_steps = steps_rounded
#         thursday_calories = calories_burned_rounded

#     elif (day == "Friday"):
#         time_in_seconds = friday_walking_time
#         speed_in_mph = 2
#         steps_per_mile = 2000
#         met = 2.9
#         if current_weight != 0:
#             weight_in_pounds = float(current_weight)
#         else:
#             weight_in_pounds = 150

#         # Step 1: Convert time from seconds to hours
#         time_in_hours = time_in_seconds / 3600

#         # Step 2: Calculate the distance traveled in miles
#         distance_in_miles = time_in_hours * speed_in_mph

#         # Round the result to two decimal places
#         distance_in_miles_rounded = round(distance_in_miles, 2)

#         # Print the result
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_distance_entry.configure(state="normal")
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_distance_entry.delete(0, "end")
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_distance_entry.insert(0, str(distance_in_miles_rounded))
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_distance_entry.configure(state="disabled")

#         # Step 4: Calculate the number of steps
#         steps = distance_in_miles * steps_per_mile

#         # Round the number of steps to the nearest integer
#         steps_rounded = round(steps)

#         # Print the result
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_steps_entry.configure(state="normal")
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_steps_entry.delete(0, "end")
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_steps_entry.insert(0, str(steps_rounded))
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_steps_entry.configure(state="disabled")

#         # Step 5: Calculate the calories burned
#         weight_in_kilograms = weight_in_pounds / 2.205
#         time = distance_in_miles/speed_in_mph
#         calories_burned = met * weight_in_kilograms * time

#         # Round the calories burned to two decimal places
#         calories_burned_rounded = round(calories_burned, 2)

#         # Print the result
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_calories_entry.configure(state="normal")
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_calories_entry.delete(0, "end")
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_calories_entry.insert(0, str(calories_burned_rounded))
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_calories_entry.configure(state="disabled")

#         friday_walking_distance = distance_in_miles_rounded
#         friday_walking_steps = steps_rounded
#         friday_calories = calories_burned_rounded

#     elif (day == "Saturday"):
#         time_in_seconds = saturday_walking_time
#         speed_in_mph = 2
#         steps_per_mile = 2000
#         met = 2.9
#         if current_weight != 0:
#             weight_in_pounds = float(current_weight)
#         else:
#             weight_in_pounds = 150

#         # Step 1: Convert time from seconds to hours
#         time_in_hours = time_in_seconds / 3600

#         # Step 2: Calculate the distance traveled in miles
#         distance_in_miles = time_in_hours * speed_in_mph

#         # Round the result to two decimal places
#         distance_in_miles_rounded = round(distance_in_miles, 2)

#         # Print the result
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_distance_entry.configure(state="normal")
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_distance_entry.delete(0, "end")
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_distance_entry.insert(0, str(distance_in_miles_rounded))
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_distance_entry.configure(state="disabled")

#         # Step 4: Calculate the number of steps
#         steps = distance_in_miles * steps_per_mile

#         # Round the number of steps to the nearest integer
#         steps_rounded = round(steps)

#         # Print the result
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_steps_entry.configure(state="normal")
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_steps_entry.delete(0, "end")
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_steps_entry.insert(0, str(steps_rounded))
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_steps_entry.configure(state="disabled")

#         # Step 5: Calculate the calories burned
#         weight_in_kilograms = weight_in_pounds / 2.205
#         time = distance_in_miles/speed_in_mph
#         calories_burned = met * weight_in_kilograms * time

#         # Round the calories burned to two decimal places
#         calories_burned_rounded = round(calories_burned, 2)

#         # Print the result
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_calories_entry.configure(state="normal")
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_calories_entry.delete(0, "end")
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_calories_entry.insert(0, str(calories_burned_rounded))
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_calories_entry.configure(state="disabled")

#         saturday_walking_distance = distance_in_miles_rounded
#         saturday_walking_steps = steps_rounded
#         saturday_calories = calories_burned_rounded

#     elif (day == "Sunday"):
#         time_in_seconds = sunday_walking_time
#         speed_in_mph = 2
#         steps_per_mile = 2000
#         met = 2.9
#         if current_weight != 0:
#             weight_in_pounds = float(current_weight)
#         else:
#             weight_in_pounds = 150

#         # Step 1: Convert time from seconds to hours
#         time_in_hours = time_in_seconds / 3600

#         # Step 2: Calculate the distance traveled in miles
#         distance_in_miles = time_in_hours * speed_in_mph

#         # Round the result to two decimal places
#         distance_in_miles_rounded = round(distance_in_miles, 2)

#         # Print the result
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_distance_entry.configure(state="normal")
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_distance_entry.delete(0, "end")
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_distance_entry.insert(0, str(distance_in_miles_rounded))
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_distance_entry.configure(state="disabled")

#         # Step 4: Calculate the number of steps
#         steps = distance_in_miles * steps_per_mile

#         # Round the number of steps to the nearest integer
#         steps_rounded = round(steps)

#         # Print the result
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_steps_entry.configure(state="normal")
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_steps_entry.delete(0, "end")
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_steps_entry.insert(0, str(steps_rounded))
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_steps_entry.configure(state="disabled")

#         # Step 5: Calculate the calories burned
#         weight_in_kilograms = weight_in_pounds / 2.205
#         time = distance_in_miles/speed_in_mph
#         calories_burned = met * weight_in_kilograms * time

#         # Round the calories burned to two decimal places
#         calories_burned_rounded = round(calories_burned, 2)

#         # Print the result
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_calories_entry.configure(state="normal")
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_calories_entry.delete(0, "end")
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_calories_entry.insert(0, str(calories_burned_rounded))
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_calories_entry.configure(state="disabled")
        
#         sunday_walking_distance = distance_in_miles_rounded
#         sunday_walking_steps = steps_rounded
#         sunday_calories = calories_burned_rounded

#     elif (day == "Monday"):
#         time_in_seconds = monday_walking_time
#         speed_in_mph = 2
#         steps_per_mile = 2000
#         met = 2.9
#         if current_weight != 0:
#             weight_in_pounds = float(current_weight)
#         else:
#             weight_in_pounds = 150

#         # Step 1: Convert time from seconds to hours
#         time_in_hours = time_in_seconds / 3600

#         # Step 2: Calculate the distance traveled in miles
#         distance_in_miles = time_in_hours * speed_in_mph

#         # Round the result to two decimal places
#         distance_in_miles_rounded = round(distance_in_miles, 2)

#         # Print the result
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_distance_entry.configure(state="normal")
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_distance_entry.delete(0, "end")
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_distance_entry.insert(0, str(distance_in_miles_rounded))
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_distance_entry.configure(state="disabled")

#         # Step 4: Calculate the number of steps
#         steps = distance_in_miles * steps_per_mile

#         # Round the number of steps to the nearest integer
#         steps_rounded = round(steps)

#         # Print the result
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_steps_entry.configure(state="normal")
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_steps_entry.delete(0, "end")
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_steps_entry.insert(0, str(steps_rounded))
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_steps_entry.configure(state="disabled")

#         # Step 5: Calculate the calories burned
#         weight_in_kilograms = weight_in_pounds / 2.205
#         time = distance_in_miles/speed_in_mph
#         calories_burned = met * weight_in_kilograms * time

#         # Round the calories burned to two decimal places
#         calories_burned_rounded = round(calories_burned, 2)

#         # Print the result
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_calories_entry.configure(state="normal")
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_calories_entry.delete(0, "end")
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_calories_entry.insert(0, str(calories_burned_rounded))
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_calories_entry.configure(state="disabled")

#         monday_walking_distance = distance_in_miles_rounded
#         monday_walking_steps = steps_rounded
#         monday_calories = calories_burned_rounded

#     elif (day == "Tuesday"):
#         time_in_seconds = tuesday_walking_time
#         speed_in_mph = 2
#         steps_per_mile = 2000
#         met = 2.9
#         if current_weight != 0:
#             weight_in_pounds = float(current_weight)
#         else:
#             weight_in_pounds = 150

#         # Step 1: Convert time from seconds to hours
#         time_in_hours = time_in_seconds / 3600

#         # Step 2: Calculate the distance traveled in miles
#         distance_in_miles = time_in_hours * speed_in_mph

#         # Round the result to two decimal places
#         distance_in_miles_rounded = round(distance_in_miles, 2)

#         # Print the result
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_distance_entry.configure(state="normal")
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_distance_entry.delete(0, "end")
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_distance_entry.insert(0, str(distance_in_miles_rounded))
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_distance_entry.configure(state="disabled")

#         # Step 4: Calculate the number of steps
#         steps = distance_in_miles * steps_per_mile

#         # Round the number of steps to the nearest integer
#         steps_rounded = round(steps)

#         # Print the result
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_steps_entry.configure(state="normal")
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_steps_entry.delete(0, "end")
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_steps_entry.insert(0, str(steps_rounded))
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_steps_entry.configure(state="disabled")

#         # Step 5: Calculate the calories burned
#         weight_in_kilograms = weight_in_pounds / 2.205
#         time = distance_in_miles/speed_in_mph
#         calories_burned = met * weight_in_kilograms * time

#         # Round the calories burned to two decimal places
#         calories_burned_rounded = round(calories_burned, 2)

#         # Print the result
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_calories_entry.configure(state="normal")
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_calories_entry.delete(0, "end")
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_calories_entry.insert(0, str(calories_burned_rounded))
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_calories_entry.configure(state="disabled")

#         tuesday_walking_distance = distance_in_miles_rounded
#         tuesday_walking_steps = steps_rounded
#         tuesday_calories = calories_burned_rounded
        
#     else:
#         time_in_seconds = wednesday_walking_time
#         speed_in_mph = 2
#         steps_per_mile = 2000
#         met = 2.9
#         if current_weight != 0:
#             weight_in_pounds = float(current_weight)
#         else:
#             weight_in_pounds = 150

#         # Step 1: Convert time from seconds to hours
#         time_in_hours = time_in_seconds / 3600

#         # Step 2: Calculate the distance traveled in miles
#         distance_in_miles = time_in_hours * speed_in_mph

#         # Round the result to two decimal places
#         distance_in_miles_rounded = round(distance_in_miles, 2)

#         # Print the result
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_distance_entry.configure(state="normal")
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_distance_entry.delete(0, "end")
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_distance_entry.insert(0, str(distance_in_miles_rounded))
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_distance_entry.configure(state="disabled")

#         # Step 4: Calculate the number of steps
#         steps = distance_in_miles * steps_per_mile

#         # Round the number of steps to the nearest integer
#         steps_rounded = round(steps)

#         # Print the result
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_steps_entry.configure(state="normal")
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_steps_entry.delete(0, "end")
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_steps_entry.insert(0, str(steps_rounded))
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_steps_entry.configure(state="disabled")

#         # Step 5: Calculate the calories burned
#         weight_in_kilograms = weight_in_pounds / 2.205
#         time = distance_in_miles/speed_in_mph
#         calories_burned = met * weight_in_kilograms * time

#         # Round the calories burned to two decimal places
#         calories_burned_rounded = round(calories_burned, 2)

#         # Print the result
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_calories_entry.configure(state="normal")
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_calories_entry.delete(0, "end")
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_calories_entry.insert(0, str(calories_burned_rounded))
#         app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_calories_entry.configure(state="disabled")

#         wednesday_walking_distance = distance_in_miles_rounded
#         wednesday_walking_steps = steps_rounded
#         wednesday_calories = calories_burned_rounded

#     total_walking_distance = thursday_walking_distance + friday_walking_distance + saturday_walking_distance + sunday_walking_distance + monday_walking_distance + tuesday_walking_distance + wednesday_walking_distance
#     total_walking_steps = thursday_walking_steps + friday_walking_steps + saturday_walking_steps + sunday_walking_steps + monday_walking_steps + tuesday_walking_steps + wednesday_walking_steps
#     total_calories = thursday_calories + friday_calories + saturday_calories + sunday_calories + monday_calories + tuesday_calories + wednesday_calories

#     total_walking_distance = round(total_walking_distance, 2)
#     total_walking_steps = round(total_walking_steps, 2)
#     total_calories = round(total_calories, 2)

#     # Print the result
#     app.totals_frame.distance_entry.configure(state="normal")
#     app.totals_frame.distance_entry.delete(0, "end")
#     app.totals_frame.distance_entry.insert(0, str(total_walking_distance))
#     app.totals_frame.distance_entry.configure(state="disabled")

#     # Print the result
#     app.totals_frame.steps_entry.configure(state="normal")
#     app.totals_frame.steps_entry.delete(0, "end")
#     app.totals_frame.steps_entry.insert(0, str(total_walking_steps))
#     app.totals_frame.steps_entry.configure(state="disabled")

#     # Print the result
#     app.totals_frame.calories_burned_entry.configure(state="normal")
#     app.totals_frame.calories_burned_entry.delete(0, "end")
#     app.totals_frame.calories_burned_entry.insert(0, str(total_calories))
#     app.totals_frame.calories_burned_entry.configure(state="disabled")

#     data = {
#         "thursday_weight": thursday_weight,
#         "friday_weight": friday_weight,
#         "saturday_weight": saturday_weight,
#         "sunday_weight": sunday_weight,
#         "monday_weight": monday_weight,
#         "tuesday_weight": tuesday_weight,
#         "wednesday_weight": wednesday_weight,
#         "total_weight_lost": total_weight_lost,

#         "thursday_walking_time": thursday_walking_time,
#         "friday_walking_time": friday_walking_time,
#         "saturday_walking_time": saturday_walking_time,
#         "sunday_walking_time": sunday_walking_time,
#         "monday_walking_time": monday_walking_time,
#         "tuesday_walking_time": tuesday_walking_time,
#         "wednesday_walking_time": wednesday_walking_time,
#         "total_walking_time": total_walking_time,

#         "thursday_walking_distance": thursday_walking_distance,
#         "friday_walking_distance": friday_walking_distance,
#         "saturday_walking_distance": saturday_walking_distance,
#         "sunday_walking_distance": sunday_walking_distance,
#         "monday_walking_distance": monday_walking_distance,
#         "tuesday_walking_distance": tuesday_walking_distance,
#         "wednesday_walking_distance": wednesday_walking_distance,
#         "total_walking_distance": total_walking_distance,

#         "thursday_walking_steps": thursday_walking_steps,
#         "friday_walking_steps": friday_walking_steps,
#         "saturday_walking_steps": saturday_walking_steps,
#         "sunday_walking_steps": sunday_walking_steps,
#         "monday_walking_steps": monday_walking_steps,
#         "tuesday_walking_steps": tuesday_walking_steps,
#         "wednesday_walking_steps": wednesday_walking_steps,
#         "total_walking_steps": total_walking_steps,

#         "thursday_calories": thursday_calories,
#         "friday_calories": friday_calories,
#         "saturday_calories": saturday_calories,
#         "sunday_calories": sunday_calories,
#         "monday_calories": monday_calories,
#         "tuesday_calories": tuesday_calories,
#         "wednesday_calories": wednesday_calories,
#         "total_calories": total_calories
#     }

#     threading.Thread(target=write_walking_variables_to_file, args=(data,)).start()

def update_time(firstpass):
    global tracking
    global start_time
    global time_passed
    global timer_id
    global current_week
    global must_clear
    if (current_week == -1):
        current_week = datetime.datetime.now().strftime("%U %Y")
        data = {
            "must_clear": must_clear,
            "current_week": current_week
        }
        threading.Thread(target=write_must_clear_to_file, args=(data,)).start()
    else:
        week_num = datetime.datetime.now().strftime("%U %Y")
        if (current_week != week_num):
            # The user has been clocked in passed Saturday 11:59:59
            # Clock User Out
            global can_clear
            can_clear = True
            app.buttons_frame.send_weekly_data_button.configure(state="normal")
            app.buttons_frame.clear_weekly_data_button.configure(state="normal")
            app.weekly_daily_tabs.weekly_tab.description_textbox.configure(state="normal")
            app.weekly_daily_tabs.daily_tab.start_end_button.configure(text="Start")
            app.weekly_daily_tabs.daily_tab.start_end_button.configure(state="disabled")
            app.weekly_daily_tabs.daily_tab.pause_resume_button.configure(state="disabled")
            app.weekly_daily_tabs.daily_tab.total_time_label.configure(text="00:00:00")
            app.weekly_daily_tabs.daily_tab.pomodoro_time_label.configure(text="00:25:00")
            app.weekly_daily_tabs.daily_tab.pause_resume_button.configure(text="Pause")
            app.weekly_daily_tabs.daily_tab.pomodoro_count_label.configure(text="#1")
            app.weekly_daily_tabs.daily_tab.pomodoro_focus_label.configure(text="Focus")
            global readytostart
            global paused
            global p_focus_time
            global p_break_time
            global p_long_break_time
            global p_cycle_count
            readytostart = True
            paused = False
            p_focus_time = focus_time
            p_break_time = break_time
            p_long_break_time = long_break_time
            p_cycle_count = 1

            # Forge Punchout
            saturday_punches.append("End: 11:59:59 PM")
            if (saturday_punches[0] == "None"):
                saturday_punches.pop(0)
            app.weekly_daily_tabs.weekly_tab.saturday_punches_entry.configure(values=saturday_punches)

            data = {
            "thursday_punches": thursday_punches,
            "friday_punches": friday_punches,
            "saturday_punches": saturday_punches,
            "sunday_punches": sunday_punches,
            "monday_punches": monday_punches,
            "tuesday_punches": tuesday_punches,
            "wednesday_punches": wednesday_punches,
            }

            threading.Thread(target=write_punches_to_file, args=(data,)).start()

            # Create a notification
            notification.notify(
                title="You've been clocked out!",
                message="You've been clocked out due to being clocked in during a new week without clearing first.",
                app_name="Productivity Tracker",
                app_icon="icon4.ico",
                timeout=10  # Duration to display the notification in seconds
            )
            app.attributes("-topmost", True)
            app.attributes("-topmost", False)

            new_week_modal()

            # Break out of time tracker
            tracking = False

            must_clear = True

            data = {
                "must_clear": must_clear,
                "current_week": current_week
            }

            threading.Thread(target=write_must_clear_to_file, args=(data,)).start()

            app.after_cancel(timer_id)

    if (tracking):
        # Allows for 1 second buffer
        if (firstpass):
            firstpass = False
        else:
            label_text = app.weekly_daily_tabs.daily_tab.total_time_label._text
            hours, minutes, seconds = map(int, label_text.split(":"))
            label_value = hours * 3600 + minutes * 60 + seconds
            label_value = label_value + 1
            hours = int(label_value // 3600)
            minutes = int((label_value % 3600) // 60)
            seconds = int(label_value % 60)
            time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            app.weekly_daily_tabs.daily_tab.total_time_label.configure(text=time_string)
            pomodoro()
            # calc_weight_loss()
            # walking()
            # update_walking_stats()
            global thursday_programming_time
            global friday_programming_time
            global saturday_programming_time
            global sunday_programming_time
            global monday_programming_time
            global tuesday_programming_time
            global wednesday_programming_time
            day = datetime.datetime.now().strftime("%A")
            if (day == "Thursday"):
                thursday_programming_time = thursday_programming_time + 1
                hours = thursday_programming_time // 3600
                minutes = (thursday_programming_time % 3600) // 60
                seconds = thursday_programming_time % 60
                programming_time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
                app.weekly_daily_tabs.weekly_tab.thursday_hour_entry.configure(state="normal")
                app.weekly_daily_tabs.weekly_tab.thursday_hour_entry.delete(0, "end")
                app.weekly_daily_tabs.weekly_tab.thursday_hour_entry.insert(0, programming_time_string)
                app.weekly_daily_tabs.weekly_tab.thursday_hour_entry.configure(state="disabled")
            elif (day == "Friday"):
                friday_programming_time = friday_programming_time + 1
                hours = friday_programming_time // 3600
                minutes = (friday_programming_time % 3600) // 60
                seconds = friday_programming_time % 60
                programming_time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
                app.weekly_daily_tabs.weekly_tab.friday_hour_entry.configure(state="normal")
                app.weekly_daily_tabs.weekly_tab.friday_hour_entry.delete(0, "end")
                app.weekly_daily_tabs.weekly_tab.friday_hour_entry.insert(0, programming_time_string)
                app.weekly_daily_tabs.weekly_tab.friday_hour_entry.configure(state="disabled")
            elif (day == "Saturday"):
                saturday_programming_time = saturday_programming_time + 1
                hours = saturday_programming_time // 3600
                minutes = (saturday_programming_time % 3600) // 60
                seconds = saturday_programming_time % 60
                programming_time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
                app.weekly_daily_tabs.weekly_tab.saturday_hour_entry.configure(state="normal")
                app.weekly_daily_tabs.weekly_tab.saturday_hour_entry.delete(0, "end")
                app.weekly_daily_tabs.weekly_tab.saturday_hour_entry.insert(0, programming_time_string)
                app.weekly_daily_tabs.weekly_tab.saturday_hour_entry.configure(state="disabled")
            elif (day == "Sunday"):
                sunday_programming_time = sunday_programming_time + 1
                hours = sunday_programming_time // 3600
                minutes = (sunday_programming_time % 3600) // 60
                seconds = sunday_programming_time % 60
                programming_time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
                app.weekly_daily_tabs.weekly_tab.sunday_hour_entry.configure(state="normal")
                app.weekly_daily_tabs.weekly_tab.sunday_hour_entry.delete(0, "end")
                app.weekly_daily_tabs.weekly_tab.sunday_hour_entry.insert(0, programming_time_string)
                app.weekly_daily_tabs.weekly_tab.sunday_hour_entry.configure(state="disabled")
            elif (day == "Monday"):
                monday_programming_time = monday_programming_time + 1
                hours = monday_programming_time // 3600
                minutes = (monday_programming_time % 3600) // 60
                seconds = monday_programming_time % 60
                programming_time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
                app.weekly_daily_tabs.weekly_tab.monday_hour_entry.configure(state="normal")
                app.weekly_daily_tabs.weekly_tab.monday_hour_entry.delete(0, "end")
                app.weekly_daily_tabs.weekly_tab.monday_hour_entry.insert(0, programming_time_string)
                app.weekly_daily_tabs.weekly_tab.monday_hour_entry.configure(state="disabled")
            elif (day == "Tuesday"):
                tuesday_programming_time = tuesday_programming_time + 1
                hours = tuesday_programming_time // 3600
                minutes = (tuesday_programming_time % 3600) // 60
                seconds = tuesday_programming_time % 60
                programming_time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
                app.weekly_daily_tabs.weekly_tab.tuesday_hour_entry.configure(state="normal")
                app.weekly_daily_tabs.weekly_tab.tuesday_hour_entry.delete(0, "end")
                app.weekly_daily_tabs.weekly_tab.tuesday_hour_entry.insert(0, programming_time_string)
                app.weekly_daily_tabs.weekly_tab.tuesday_hour_entry.configure(state="disabled")
            else:
                wednesday_programming_time = wednesday_programming_time + 1
                hours = wednesday_programming_time // 3600
                minutes = (wednesday_programming_time % 3600) // 60
                seconds = wednesday_programming_time % 60
                programming_time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
                app.weekly_daily_tabs.weekly_tab.wednesday_hour_entry.configure(state="normal")
                app.weekly_daily_tabs.weekly_tab.wednesday_hour_entry.delete(0, "end")
                app.weekly_daily_tabs.weekly_tab.wednesday_hour_entry.insert(0, programming_time_string)
                app.weekly_daily_tabs.weekly_tab.wednesday_hour_entry.configure(state="disabled")
        
            total_programming_time = thursday_programming_time + friday_programming_time + saturday_programming_time + sunday_programming_time + monday_programming_time + tuesday_programming_time + wednesday_programming_time
            hours = total_programming_time // 3600
            minutes = (total_programming_time % 3600) // 60
            seconds = total_programming_time % 60
            programming_time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            app.totals_frame.time_programming_entry.configure(state="normal")
            app.totals_frame.time_programming_entry.delete(0, "end")
            app.totals_frame.time_programming_entry.insert(0, programming_time_string)
            app.totals_frame.time_programming_entry.configure(state="disabled")

            data = {
                "thursday_programming_time": thursday_programming_time,
                "friday_programming_time": friday_programming_time,
                "saturday_programming_time": saturday_programming_time,
                "sunday_programming_time": sunday_programming_time,
                "monday_programming_time": monday_programming_time,
                "tuesday_programming_time": tuesday_programming_time,
                "wednesday_programming_time": wednesday_programming_time,
                "total_programming_time": total_programming_time,
            }

            threading.Thread(target=write_variables_to_file, args=(data,)).start()

        # global thursday_punches
        # global friday_punches
        # global saturday_punches
        # global sunday_punches
        # global monday_punches
        # global tuesday_punches
        # global wednesday_punches

        # if (str(datetime.datetime.now().strftime("%I:%M:%S %p")) == "11:59:59 PM"):
        #     #Clock Out
        #     if (day == "Thursday"):
        #         thursday_punches.append("End: " + str(datetime.datetime.now().strftime("%I:%M:%S %p")))
        #     elif (day == "Friday"):
        #         friday_punches.append("End: " + str(datetime.datetime.now().strftime("%I:%M:%S %p")))
        #     elif (day == "Saturday"):
        #         saturday_punches.append("End: " + str(datetime.datetime.now().strftime("%I:%M:%S %p")))
        #     elif (day == "Sunday"):
        #         sunday_punches.append("End: " + str(datetime.datetime.now().strftime("%I:%M:%S %p")))
        #     elif (day == "Monday"):
        #         monday_punches.append("End: " + str(datetime.datetime.now().strftime("%I:%M:%S %p")))
        #     elif (day == "Tuesday"):
        #         tuesday_punches.append("End: " + str(datetime.datetime.now().strftime("%I:%M:%S %p")))
        #     else:
        #         wednesday_punches.append("End: " + str(datetime.datetime.now().strftime("%I:%M:%S %p")))

        #     data = {
        #     "thursday_punches": thursday_punches,
        #     "friday_punches": friday_punches,
        #     "saturday_punches": saturday_punches,
        #     "sunday_punches": sunday_punches,
        #     "monday_punches": monday_punches,
        #     "tuesday_punches": tuesday_punches,
        #     "wednesday_punches": wednesday_punches,
        #     }

        #     threading.Thread(target=write_punches_to_file, args=(data,)).start()
                
        # if (str(datetime.datetime.now().strftime("%I:%M:%S %p")) == "12:00:00 AM"):
        #     if (day == "Thursday"):
        #         thursday_punches.append("Start: " + str(datetime.datetime.now().strftime("%I:%M:%S %p")))
        #     elif (day == "Friday"):
        #         friday_punches.append("Start: " + str(datetime.datetime.now().strftime("%I:%M:%S %p")))
        #     elif (day == "Saturday"):
        #         saturday_punches.append("Start: " + str(datetime.datetime.now().strftime("%I:%M:%S %p")))
        #     elif (day == "Sunday"):
        #         sunday_punches.append("Start: " + str(datetime.datetime.now().strftime("%I:%M:%S %p")))
        #     elif (day == "Monday"):
        #         monday_punches.append("Start: " + str(datetime.datetime.now().strftime("%I:%M:%S %p")))
        #     elif (day == "Tuesday"):
        #         tuesday_punches.append("Start: " + str(datetime.datetime.now().strftime("%I:%M:%S %p")))
        #     else:
        #         wednesday_punches.append("Start: " + str(datetime.datetime.now().strftime("%I:%M:%S %p")))

        #     data = {
        #     "thursday_punches": thursday_punches,
        #     "friday_punches": friday_punches,
        #     "saturday_punches": saturday_punches,
        #     "sunday_punches": sunday_punches,
        #     "monday_punches": monday_punches,
        #     "tuesday_punches": tuesday_punches,
        #     "wednesday_punches": wednesday_punches,
        #     }

        #     threading.Thread(target=write_punches_to_file, args=(data,)).start()

        timer_id = app.after(1000, update_time, False)

def write_variables_to_file(data):
    try:
        with open("variables.json", "w") as file:
            json.dump(data, file)
    except Exception as e:
        write_variables_to_file(data)

# def write_walking_variables_to_file(data):
#     try:
#         with open("walking.json", "w") as file:
#             json.dump(data, file)
#     except Exception as e:
#         write_walking_variables_to_file(data)

def write_punches_to_file(data):
    try:
        with open("punches.json", "w") as file:
            json.dump(data, file)
    except Exception as e:
        write_punches_to_file(data)

def write_description_to_file(data):
    try:
        with open("description.json", "w") as file:
            json.dump(data, file)
    except Exception as e:
        write_description_to_file(data)

def write_must_clear_to_file(data):
    try:
        with open("must_clear.json", "w") as file:
            json.dump(data, file)
    except Exception as e:
        write_must_clear_to_file(data)

def write_current_week_to_file(data):
    try:
        with open("current_week.json", "w") as file:
            json.dump(data, file)
    except Exception as e:
        write_current_week_to_file(data)

def clear_data():
    # Check if files exist
    variables_path = "variables.json"
    punches_path = "punches.json"
    # walking_path = "walking.json"
    description_path = "description.json"
    must_clear_path = "must_clear.json"
    current_week_path = "current_week.json"
    # Check if the file exists
    if (os.path.isfile(variables_path) and os.path.isfile(punches_path) and os.path.isfile(description_path) and os.path.isfile(must_clear_path) and os.path.isfile(current_week_path)):
        # Check that not tracking (this needs to be fixed, currently it only works on boot)
        if (can_clear):
            # Empty all data from files
            data = {}
            write_variables_to_file(data)
            # write_walking_variables_to_file(data)
            write_punches_to_file(data)
            write_description_to_file(data)
            write_current_week_to_file(data)
            write_must_clear_to_file(data)
            
            # Reset all UI fields

            # Time Programming Fields
            app.weekly_daily_tabs.weekly_tab.thursday_hour_entry.configure(state="normal")
            app.weekly_daily_tabs.weekly_tab.thursday_hour_entry.delete(0, "end")
            app.weekly_daily_tabs.weekly_tab.thursday_hour_entry.configure(placeholder_text="00:00:00")
            app.weekly_daily_tabs.weekly_tab.thursday_hour_entry.configure(state="disabled")

            app.weekly_daily_tabs.weekly_tab.friday_hour_entry.configure(state="normal")
            app.weekly_daily_tabs.weekly_tab.friday_hour_entry.delete(0, "end")
            app.weekly_daily_tabs.weekly_tab.friday_hour_entry.configure(placeholder_text="00:00:00")
            app.weekly_daily_tabs.weekly_tab.friday_hour_entry.configure(state="disabled")

            app.weekly_daily_tabs.weekly_tab.saturday_hour_entry.configure(state="normal")
            app.weekly_daily_tabs.weekly_tab.saturday_hour_entry.delete(0, "end")
            app.weekly_daily_tabs.weekly_tab.saturday_hour_entry.configure(placeholder_text="00:00:00")
            app.weekly_daily_tabs.weekly_tab.saturday_hour_entry.configure(state="disabled")

            app.weekly_daily_tabs.weekly_tab.sunday_hour_entry.configure(state="normal")
            app.weekly_daily_tabs.weekly_tab.sunday_hour_entry.delete(0, "end")
            app.weekly_daily_tabs.weekly_tab.sunday_hour_entry.configure(placeholder_text="00:00:00")
            app.weekly_daily_tabs.weekly_tab.sunday_hour_entry.configure(state="disabled")

            app.weekly_daily_tabs.weekly_tab.monday_hour_entry.configure(state="normal")
            app.weekly_daily_tabs.weekly_tab.monday_hour_entry.delete(0, "end")
            app.weekly_daily_tabs.weekly_tab.monday_hour_entry.configure(placeholder_text="00:00:00")
            app.weekly_daily_tabs.weekly_tab.monday_hour_entry.configure(state="disabled")

            app.weekly_daily_tabs.weekly_tab.tuesday_hour_entry.configure(state="normal")
            app.weekly_daily_tabs.weekly_tab.tuesday_hour_entry.delete(0, "end")
            app.weekly_daily_tabs.weekly_tab.tuesday_hour_entry.configure(placeholder_text="00:00:00")
            app.weekly_daily_tabs.weekly_tab.tuesday_hour_entry.configure(state="disabled")

            app.weekly_daily_tabs.weekly_tab.wednesday_hour_entry.configure(state="normal")
            app.weekly_daily_tabs.weekly_tab.wednesday_hour_entry.delete(0, "end")
            app.weekly_daily_tabs.weekly_tab.wednesday_hour_entry.configure(placeholder_text="00:00:00")
            app.weekly_daily_tabs.weekly_tab.wednesday_hour_entry.configure(state="disabled")

            # Punches Fields
            global thursday_punches
            global friday_punches
            global saturday_punches
            global sunday_punches
            global monday_punches
            global tuesday_punches
            global wednesday_punches

            thursday_punches = ["None"]
            app.weekly_daily_tabs.weekly_tab.thursday_punches_entry.configure(values=thursday_punches)

            friday_punches = ["None"]
            app.weekly_daily_tabs.weekly_tab.friday_punches_entry.configure(values=friday_punches)

            saturday_punches = ["None"]
            app.weekly_daily_tabs.weekly_tab.saturday_punches_entry.configure(values=saturday_punches)

            sunday_punches = ["None"]
            app.weekly_daily_tabs.weekly_tab.sunday_punches_entry.configure(values=sunday_punches)

            monday_punches = ["None"]
            app.weekly_daily_tabs.weekly_tab.monday_punches_entry.configure(values=monday_punches)

            tuesday_punches = ["None"]
            app.weekly_daily_tabs.weekly_tab.tuesday_punches_entry.configure(values=tuesday_punches)

            wednesday_punches = ["None"]
            app.weekly_daily_tabs.weekly_tab.wednesday_punches_entry.configure(values=wednesday_punches)

            # # Weight Fields
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_weight_entry.configure(state="normal")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_weight_entry.delete(0, "end")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_weight_entry.configure(placeholder_text="Enter Weight")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_weight_entry.configure(state="disabled")

            # app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_weight_entry.configure(state="normal")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_weight_entry.delete(0, "end")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_weight_entry.configure(placeholder_text="Enter Weight")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_weight_entry.configure(state="disabled")

            # app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_weight_entry.configure(state="normal")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_weight_entry.delete(0, "end")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_weight_entry.configure(placeholder_text="Enter Weight")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_weight_entry.configure(state="disabled")

            # app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_weight_entry.configure(state="normal")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_weight_entry.delete(0, "end")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_weight_entry.configure(placeholder_text="Enter Weight")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_weight_entry.configure(state="disabled")

            # app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_weight_entry.configure(state="normal")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_weight_entry.delete(0, "end")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_weight_entry.configure(placeholder_text="Enter Weight")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_weight_entry.configure(state="disabled")

            # app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_weight_entry.configure(state="normal")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_weight_entry.delete(0, "end")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_weight_entry.configure(placeholder_text="Enter Weight")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_weight_entry.configure(state="disabled")

            # app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_weight_entry.configure(state="normal")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_weight_entry.delete(0, "end")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_weight_entry.configure(placeholder_text="Enter Weight")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_weight_entry.configure(state="disabled")

            # # Time Walked Fields
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_time_walked_entry.configure(state="normal")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_time_walked_entry.delete(0, "end")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_time_walked_entry.configure(placeholder_text="00:00:00")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_time_walked_entry.configure(state="disabled")

            # app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_time_walked_entry.configure(state="normal")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_time_walked_entry.delete(0, "end")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_time_walked_entry.configure(placeholder_text="00:00:00")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_time_walked_entry.configure(state="disabled")

            # app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_time_walked_entry.configure(state="normal")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_time_walked_entry.delete(0, "end")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_time_walked_entry.configure(placeholder_text="00:00:00")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_time_walked_entry.configure(state="disabled")

            # app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_time_walked_entry.configure(state="normal")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_time_walked_entry.delete(0, "end")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_time_walked_entry.configure(placeholder_text="00:00:00")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_time_walked_entry.configure(state="disabled")

            # app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_time_walked_entry.configure(state="normal")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_time_walked_entry.delete(0, "end")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_time_walked_entry.configure(placeholder_text="00:00:00")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_time_walked_entry.configure(state="disabled")

            # app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_time_walked_entry.configure(state="normal")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_time_walked_entry.delete(0, "end")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_time_walked_entry.configure(placeholder_text="00:00:00")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_time_walked_entry.configure(state="disabled")

            # app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_time_walked_entry.configure(state="normal")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_time_walked_entry.delete(0, "end")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_time_walked_entry.configure(placeholder_text="00:00:00")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_time_walked_entry.configure(state="disabled")

            # # Distance Fields
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_distance_entry.configure(state="normal")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_distance_entry.delete(0, "end")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_distance_entry.configure(placeholder_text="0")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_distance_entry.configure(state="disabled")

            # app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_distance_entry.configure(state="normal")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_distance_entry.delete(0, "end")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_distance_entry.configure(placeholder_text="0")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_distance_entry.configure(state="disabled")

            # app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_distance_entry.configure(state="normal")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_distance_entry.delete(0, "end")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_distance_entry.configure(placeholder_text="0")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_distance_entry.configure(state="disabled")

            # app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_distance_entry.configure(state="normal")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_distance_entry.delete(0, "end")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_distance_entry.configure(placeholder_text="0")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_distance_entry.configure(state="disabled")

            # app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_distance_entry.configure(state="normal")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_distance_entry.delete(0, "end")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_distance_entry.configure(placeholder_text="0")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_distance_entry.configure(state="disabled")

            # app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_distance_entry.configure(state="normal")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_distance_entry.delete(0, "end")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_distance_entry.configure(placeholder_text="0")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_distance_entry.configure(state="disabled")

            # app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_distance_entry.configure(state="normal")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_distance_entry.delete(0, "end")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_distance_entry.configure(placeholder_text="0")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_distance_entry.configure(state="disabled")

            # # Steps Fields
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_steps_entry.configure(state="normal")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_steps_entry.delete(0, "end")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_steps_entry.configure(placeholder_text="0")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_steps_entry.configure(state="disabled")

            # app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_steps_entry.configure(state="normal")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_steps_entry.delete(0, "end")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_steps_entry.configure(placeholder_text="0")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_steps_entry.configure(state="disabled")

            # app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_steps_entry.configure(state="normal")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_steps_entry.delete(0, "end")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_steps_entry.configure(placeholder_text="0")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_steps_entry.configure(state="disabled")

            # app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_steps_entry.configure(state="normal")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_steps_entry.delete(0, "end")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_steps_entry.configure(placeholder_text="0")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_steps_entry.configure(state="disabled")

            # app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_steps_entry.configure(state="normal")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_steps_entry.delete(0, "end")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_steps_entry.configure(placeholder_text="0")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_steps_entry.configure(state="disabled")

            # app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_steps_entry.configure(state="normal")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_steps_entry.delete(0, "end")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_steps_entry.configure(placeholder_text="0")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_steps_entry.configure(state="disabled")

            # app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_steps_entry.configure(state="normal")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_steps_entry.delete(0, "end")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_steps_entry.configure(placeholder_text="0")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_steps_entry.configure(state="disabled")

            # # Calories Burned Fields
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_calories_entry.configure(state="normal")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_calories_entry.delete(0, "end")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_calories_entry.configure(placeholder_text="0")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.thursday_calories_entry.configure(state="disabled")

            # app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_calories_entry.configure(state="normal")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_calories_entry.delete(0, "end")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_calories_entry.configure(placeholder_text="0")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.friday_calories_entry.configure(state="disabled")

            # app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_calories_entry.configure(state="normal")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_calories_entry.delete(0, "end")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_calories_entry.configure(placeholder_text="0")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_calories_entry.configure(state="disabled")

            # app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_calories_entry.configure(state="normal")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_calories_entry.delete(0, "end")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_calories_entry.configure(placeholder_text="0")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.sunday_calories_entry.configure(state="disabled")

            # app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_calories_entry.configure(state="normal")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_calories_entry.delete(0, "end")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_calories_entry.configure(placeholder_text="0")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.monday_calories_entry.configure(state="disabled")

            # app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_calories_entry.configure(state="normal")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_calories_entry.delete(0, "end")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_calories_entry.configure(placeholder_text="0")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.tuesday_calories_entry.configure(state="disabled")

            # app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_calories_entry.configure(state="normal")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_calories_entry.delete(0, "end")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_calories_entry.configure(placeholder_text="0")
            # app.weekly_daily_tabs.weekly_tab.exercise_frame.wednesday_calories_entry.configure(state="disabled")

            # Totals Fields
            app.totals_frame.time_programming_entry.configure(state="normal")
            app.totals_frame.time_programming_entry.delete(0, "end")
            app.totals_frame.time_programming_entry.configure(placeholder_text="00:00:00")
            app.totals_frame.time_programming_entry.configure(state="disabled")

            # app.totals_frame.total_weight_lost_entry.configure(state="normal")
            # app.totals_frame.total_weight_lost_entry.delete(0, "end")
            # app.totals_frame.total_weight_lost_entry.configure(placeholder_text="0")
            # app.totals_frame.total_weight_lost_entry.configure(state="disabled")

            # app.totals_frame.time_walked_entry.configure(state="normal")
            # app.totals_frame.time_walked_entry.delete(0, "end")
            # app.totals_frame.time_walked_entry.configure(placeholder_text="00:00:00")
            # app.totals_frame.time_walked_entry.configure(state="disabled")

            # app.totals_frame.distance_entry.configure(state="normal")
            # app.totals_frame.distance_entry.delete(0, "end")
            # app.totals_frame.distance_entry.configure(placeholder_text="0")
            # app.totals_frame.distance_entry.configure(state="disabled")

            # app.totals_frame.steps_entry.configure(state="normal")
            # app.totals_frame.steps_entry.delete(0, "end")
            # app.totals_frame.steps_entry.configure(placeholder_text="0")
            # app.totals_frame.steps_entry.configure(state="disabled")

            # app.totals_frame.calories_burned_entry.configure(state="normal")
            # app.totals_frame.calories_burned_entry.delete(0, "end")
            # app.totals_frame.calories_burned_entry.configure(placeholder_text="0")
            # app.totals_frame.calories_burned_entry.configure(state="disabled")

            global must_clear
            must_clear = False

            global current_week
            current_week = datetime.datetime.now().strftime("%U %Y")

            data = {
                "must_clear": must_clear,
                "current_week": current_week
            }

            threading.Thread(target=write_must_clear_to_file, args=(data,)).start()

            global readytostart
            readytostart = True

            app.weekly_daily_tabs.daily_tab.start_end_button.configure(state="normal")

class ProgrammingFrame(CTk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)

        left_right_padding = 0
        if (platform.system() == "Linux"):
            left_right_padding = 10
        else:
            left_right_padding = 12
        
        # Title Label
        self.title = CTk.CTkLabel(self, text="Weekly Work Statistics", fg_color="gray30")
        self.title.grid(row=0, column=0, columnspan=4, sticky="ew")
        
        # Category Labels
        self.time_programming_label = CTk.CTkLabel(self, text="Time Working")
        self.time_programming_label.grid(row=1, column=1)
        
        self.time_punches_label = CTk.CTkLabel(self, text="Time Punches")
        self.time_punches_label.grid(row=1, column=2)

        self.description_label = CTk.CTkLabel(self, text="Description of Weekly Work Completed")
        self.description_label.grid(row=1, column=3)
        
        # Weekday Labels
        self.thursday_label = CTk.CTkLabel(self, text="Thursday")
        self.thursday_label.grid(row=6, column=0, padx=(left_right_padding, 5), sticky="w")

        self.friday_label = CTk.CTkLabel(self, text="Friday")
        self.friday_label.grid(row=7, column=0, padx=(left_right_padding, 5), sticky="w")

        self.saturday_label = CTk.CTkLabel(self, text="Saturday")
        self.saturday_label.grid(row=8, column=0, padx=(left_right_padding, 5), sticky="w")

        self.sunday_label = CTk.CTkLabel(self, text="Sunday")
        self.sunday_label.grid(row=2, column=0, padx=(left_right_padding, 5), sticky="w")

        self.monday_label = CTk.CTkLabel(self, text="Monday")
        self.monday_label.grid(row=3, column=0, padx=(left_right_padding, 5), sticky="w")

        self.tuesday_label = CTk.CTkLabel(self, text="Tuesday")
        self.tuesday_label.grid(row=4, column=0, padx=(left_right_padding, 5), sticky="w")

        self.wednesday_label = CTk.CTkLabel(self, text="Wednesday")
        self.wednesday_label.grid(row=5, column=0, padx=(left_right_padding, 5), sticky="w")
        
        # Weekday Hour Entries
        global thursday_programming_time
        global friday_programming_time
        global saturday_programming_time
        global sunday_programming_time
        global monday_programming_time
        global tuesday_programming_time
        global wednesday_programming_time

        self.thursday_hour_entry = CTk.CTkEntry(self, placeholder_text="00:00:00", justify="center")
        self.thursday_hour_entry.configure(state="disabled")
        self.thursday_hour_entry.grid(row=6, column=1, padx=(5, 5))

        if (thursday_programming_time != 0):
                hours = thursday_programming_time // 3600
                minutes = (thursday_programming_time % 3600) // 60
                seconds = thursday_programming_time % 60
                programming_time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
                self.thursday_hour_entry.configure(state="normal")
                self.thursday_hour_entry.insert(0, programming_time_string)
                self.thursday_hour_entry.configure(state="disabled")

        self.friday_hour_entry = CTk.CTkEntry(self, placeholder_text="00:00:00", justify="center")
        self.friday_hour_entry.configure(state="disabled")
        self.friday_hour_entry.grid(row=7, column=1, padx=(5, 5))

        if (friday_programming_time != 0):
            hours = friday_programming_time // 3600
            minutes = (friday_programming_time % 3600) // 60
            seconds = friday_programming_time % 60
            programming_time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            self.friday_hour_entry.configure(state="normal")
            self.friday_hour_entry.insert(0, programming_time_string)
            self.friday_hour_entry.configure(state="disabled")

        self.saturday_hour_entry = CTk.CTkEntry(self, placeholder_text="00:00:00", justify="center")
        self.saturday_hour_entry.configure(state="disabled")
        self.saturday_hour_entry.grid(row=8, column=1, padx=(5, 5))

        if (saturday_programming_time != 0):
            hours = saturday_programming_time // 3600
            minutes = (saturday_programming_time % 3600) // 60
            seconds = saturday_programming_time % 60
            programming_time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            self.saturday_hour_entry.configure(state="normal")
            self.saturday_hour_entry.insert(0, programming_time_string)
            self.saturday_hour_entry.configure(state="disabled")

        self.sunday_hour_entry = CTk.CTkEntry(self, placeholder_text="00:00:00", justify="center")
        self.sunday_hour_entry.configure(state="disabled")
        self.sunday_hour_entry.grid(row=2, column=1, padx=(5, 5))

        if (sunday_programming_time != 0):
            hours = sunday_programming_time // 3600
            minutes = (sunday_programming_time % 3600) // 60
            seconds = sunday_programming_time % 60
            programming_time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            self.sunday_hour_entry.configure(state="normal")
            self.sunday_hour_entry.insert(0, programming_time_string)
            self.sunday_hour_entry.configure(state="disabled")

        self.monday_hour_entry = CTk.CTkEntry(self, placeholder_text="00:00:00", justify="center")
        self.monday_hour_entry.configure(state="disabled")
        self.monday_hour_entry.grid(row=3, column=1, padx=(5, 5))

        if (monday_programming_time != 0):
            hours = monday_programming_time // 3600
            minutes = (monday_programming_time % 3600) // 60
            seconds = monday_programming_time % 60
            programming_time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            self.monday_hour_entry.configure(state="normal")
            self.monday_hour_entry.insert(0, programming_time_string)
            self.monday_hour_entry.configure(state="disabled")

        self.tuesday_hour_entry = CTk.CTkEntry(self, placeholder_text="00:00:00", justify="center")
        self.tuesday_hour_entry.configure(state="disabled")
        self.tuesday_hour_entry.grid(row=4, column=1, padx=(5, 5))

        if (tuesday_programming_time != 0):
            hours = tuesday_programming_time // 3600
            minutes = (tuesday_programming_time % 3600) // 60
            seconds = tuesday_programming_time % 60
            programming_time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            self.tuesday_hour_entry.configure(state="normal")
            self.tuesday_hour_entry.insert(0, programming_time_string)
            self.tuesday_hour_entry.configure(state="disabled")

        self.wednesday_hour_entry = CTk.CTkEntry(self, placeholder_text="00:00:00", justify="center")
        self.wednesday_hour_entry.configure(state="disabled")
        self.wednesday_hour_entry.grid(row=5, column=1, padx=(5, 5))

        if (wednesday_programming_time != 0):
            hours = wednesday_programming_time // 3600
            minutes = (wednesday_programming_time % 3600) // 60
            seconds = wednesday_programming_time % 60
            programming_time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            self.wednesday_hour_entry.configure(state="normal")
            self.wednesday_hour_entry.insert(0, programming_time_string)
            self.wednesday_hour_entry.configure(state="disabled")

        global thursday_punches
        global friday_punches
        global saturday_punches
        global sunday_punches
        global monday_punches
        global tuesday_punches
        global wednesday_punches

        if (len(thursday_punches) == 0):
            thursday_punches = ["None"]
        if (len(friday_punches) == 0):
            friday_punches = ["None"]
        if (len(saturday_punches) == 0):
            saturday_punches = ["None"]
        if (len(sunday_punches) == 0):
            sunday_punches = ["None"]
        if (len(monday_punches) == 0):
            monday_punches = ["None"]
        if (len(tuesday_punches) == 0):
            tuesday_punches = ["None"]
        if (len(wednesday_punches) == 0):
            wednesday_punches = ["None"]

        # Weekday Punches Option Menus
        self.thursday_punches_entry = CTk.CTkOptionMenu(self, values=thursday_punches, command=self.reset_thursday_option)
        self.thursday_punches_entry.set("Punches")
        self.thursday_punches_entry.grid(row=6, column=2, padx=(5, 5), pady=(5,5))

        self.friday_punches_entry = CTk.CTkOptionMenu(self, values=friday_punches, command=self.reset_friday_option)
        self.friday_punches_entry.set("Punches")
        self.friday_punches_entry.grid(row=7, column=2, padx=(5, 5), pady=(5,5))

        self.saturday_punches_entry = CTk.CTkOptionMenu(self, values=saturday_punches, command=self.reset_saturday_option)
        self.saturday_punches_entry.set("Punches")
        self.saturday_punches_entry.grid(row=8, column=2, padx=(5, 5), pady=(5,5))

        self.sunday_punches_entry = CTk.CTkOptionMenu(self, values=sunday_punches, command=self.reset_sunday_option)
        self.sunday_punches_entry.set("Punches")
        self.sunday_punches_entry.grid(row=2, column=2, padx=(5, 5), pady=(5,5))

        self.monday_punches_entry = CTk.CTkOptionMenu(self, values=monday_punches, command=self.reset_monday_option)
        self.monday_punches_entry.set("Punches")
        self.monday_punches_entry.grid(row=3, column=2, padx=(5, 5), pady=(5,5))

        self.tuesday_punches_entry = CTk.CTkOptionMenu(self, values=tuesday_punches, command=self.reset_tuesday_option)
        self.tuesday_punches_entry.set("Punches")
        self.tuesday_punches_entry.grid(row=4, column=2, padx=(5, 5), pady=(5,5))

        self.wednesday_punches_entry = CTk.CTkOptionMenu(self, values=wednesday_punches, command=self.reset_wednesday_option)
        self.wednesday_punches_entry.set("Punches")
        self.wednesday_punches_entry.grid(row=5, column=2, padx=(5, 5), pady=(5,5))

        # Text Box
        self.description_textbox = CTk.CTkTextbox(self, width=440, height=258, wrap="word")
        self.description_textbox.grid(row=2, column=3, rowspan=7, padx=(5, left_right_padding))
        self.description_textbox.bind("<KeyRelease>", save_description)

        global description
        placeholder_string = "INSTRUCTIONS:\n\n- Paste the webhook that's been provided to you into the top entry box and click lock. This ensures that when your data will paste into the correct Discord channel.\n\n- Use the Start Button in the Daily Tracker Tab to clock in.\n\n- Once you clock in, you'll have the option to pause or resume your session.\n\n- End your session by clicking the End Button\n\n- When you aren't in a session, you'll have the ability to Send Weekly Data and Clear Weekly Data.\n\n- Sending weekly data sends your data to the discord by using a webhook. Your data will be automatically formatted to be readable and will show what dates the week covered.\n\n- Clearing Weekly Data will erase everything and set it all back to default. This will mostly be used when you want to start a new week. Be sure to send your data before doing this.\n\n- The Pomodoro switch is an option that you can add to your session. This activates a Pomodoro timer that pauses and gives a notification everytime the timer runs out. The timers go as follows: 25, 5, 25, 5, 25, 5, 25, 15\n\n- You'll only be able to type in this text box when you're not in a session. Erasing these instructions and typing a new message will save your new message."
        if (description != ""):
            self.description_textbox.insert(1.0, description)
        else:
            self.description_textbox.insert(0.0, placeholder_string)

    def reset_thursday_option(self, var):
        app.weekly_daily_tabs.weekly_tab.programming_frame.thursday_punches_entry.set("Punches")
    def reset_friday_option(self, var):
        app.weekly_daily_tabs.weekly_tab.programming_frame.friday_punches_entry.set("Punches")
    def reset_saturday_option(self, var):
        app.weekly_daily_tabs.weekly_tab.programming_frame.saturday_punches_entry.set("Punches")
    def reset_sunday_option(self, var):
        app.weekly_daily_tabs.weekly_tab.programming_frame.sunday_punches_entry.set("Punches")
    def reset_monday_option(self, var):
        app.weekly_daily_tabs.weekly_tab.programming_frame.monday_punches_entry.set("Punches")
    def reset_tuesday_option(self, var):
        app.weekly_daily_tabs.weekly_tab.programming_frame.tuesday_punches_entry.set("Punches")
    def reset_wednesday_option(self, var):
        app.weekly_daily_tabs.weekly_tab.programming_frame.wednesday_punches_entry.set("Punches")

class ExerciseFrame(CTk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        
        # Title Label
        self.title = CTk.CTkLabel(self, text="Exercising", fg_color="gray30")
        self.title.grid(row=0, column=0, columnspan=6, sticky="ew")
        
        # Category Labels
        self.weight_label = CTk.CTkLabel(self, text="Weight")
        self.weight_label.grid(row=1, column=1)
        
        self.time_walked_label = CTk.CTkLabel(self, text="Time Walked")
        self.time_walked_label.grid(row=1, column=2)

        self.distance_label = CTk.CTkLabel(self, text="Distance")
        self.distance_label.grid(row=1, column=3)

        self.steps_label = CTk.CTkLabel(self, text="Steps")
        self.steps_label.grid(row=1, column=4)

        self.calories_burned_label = CTk.CTkLabel(self, text="Calories Burned")
        self.calories_burned_label.grid(row=1, column=5)
        
        # Weekday Labels
        self.thursday_label = CTk.CTkLabel(self, text="Thursday")
        self.thursday_label.grid(row=6, column=0, padx=(10, 5), sticky="w")

        self.friday_label = CTk.CTkLabel(self, text="Friday")
        self.friday_label.grid(row=7, column=0, padx=(10, 5), sticky="w")

        self.saturday_label = CTk.CTkLabel(self, text="Saturday")
        self.saturday_label.grid(row=8, column=0, padx=(10, 5), sticky="w")

        self.sunday_label = CTk.CTkLabel(self, text="Sunday")
        self.sunday_label.grid(row=2, column=0, padx=(10, 5), sticky="w")

        self.monday_label = CTk.CTkLabel(self, text="Monday")
        self.monday_label.grid(row=3, column=0, padx=(10, 5), sticky="w")

        self.tuesday_label = CTk.CTkLabel(self, text="Tuesday")
        self.tuesday_label.grid(row=4, column=0, padx=(10, 5), sticky="w")

        self.wednesday_label = CTk.CTkLabel(self, text="Wednesday")
        self.wednesday_label.grid(row=5, column=0, padx=(10, 5), sticky="w")
        
        # Weight Entries
        self.thursday_weight_entry = CTk.CTkEntry(self, placeholder_text="Enter Weight", justify="center")
        self.thursday_weight_entry.grid(row=6, column=1, padx=(5, 5), pady=(5,5))
        self.thursday_weight_entry.bind("<KeyRelease>", validate_thursday_weight_float)

        if (thursday_weight != 0):
            weight_string = str(thursday_weight)
            self.thursday_weight_entry.insert(0, weight_string)

        self.friday_weight_entry = CTk.CTkEntry(self, placeholder_text="Enter Weight", justify="center")
        self.friday_weight_entry.grid(row=7, column=1, padx=(5, 5), pady=(5,5))
        self.friday_weight_entry.bind("<KeyRelease>", validate_friday_weight_float)

        if (friday_weight != 0):
            weight_string = str(friday_weight)
            self.friday_weight_entry.insert(0, weight_string)

        self.saturday_weight_entry = CTk.CTkEntry(self, placeholder_text="Enter Weight", justify="center")
        self.saturday_weight_entry.grid(row=8, column=1, padx=(5, 5), pady=(5,5))
        self.saturday_weight_entry.bind("<KeyRelease>", validate_saturday_weight_float)

        if (saturday_weight != 0):
            weight_string = str(saturday_weight)
            self.saturday_weight_entry.insert(0, weight_string)

        self.sunday_weight_entry = CTk.CTkEntry(self, placeholder_text="Enter Weight", justify="center")
        self.sunday_weight_entry.grid(row=2, column=1, padx=(5, 5), pady=(5,5))
        self.sunday_weight_entry.bind("<KeyRelease>", validate_sunday_weight_float)

        if (sunday_weight != 0):
            weight_string = str(sunday_weight)
            self.sunday_weight_entry.insert(0, weight_string)

        self.monday_weight_entry = CTk.CTkEntry(self, placeholder_text="Enter Weight", justify="center")
        self.monday_weight_entry.grid(row=3, column=1, padx=(5, 5), pady=(5,5))
        self.monday_weight_entry.bind("<KeyRelease>", validate_monday_weight_float)

        if (monday_weight != 0):
            weight_string = str(monday_weight)
            self.monday_weight_entry.insert(0, weight_string)

        self.tuesday_weight_entry = CTk.CTkEntry(self, placeholder_text="Enter Weight", justify="center")
        self.tuesday_weight_entry.grid(row=4, column=1, padx=(5, 5), pady=(5,5))
        self.tuesday_weight_entry.bind("<KeyRelease>", validate_tuesday_weight_float)

        if (tuesday_weight != 0):
            weight_string = str(tuesday_weight)
            self.tuesday_weight_entry.insert(0, weight_string)

        self.wednesday_weight_entry = CTk.CTkEntry(self, placeholder_text="Enter Weight", justify="center")
        self.wednesday_weight_entry.grid(row=5, column=1, padx=(5, 5), pady=(5,5))
        self.wednesday_weight_entry.bind("<KeyRelease>", validate_wednesday_weight_float)

        if (wednesday_weight != 0):
            weight_string = str(wednesday_weight)
            self.wednesday_weight_entry.insert(0, weight_string)

        day = datetime.datetime.now().strftime("%A")
        if (day == "Thursday"):
            self.friday_weight_entry.configure(placeholder_text="NONE")
            self.saturday_weight_entry.configure(placeholder_text="NONE")
            self.sunday_weight_entry.configure(placeholder_text="NONE")
            self.monday_weight_entry.configure(placeholder_text="NONE")
            self.tuesday_weight_entry.configure(placeholder_text="NONE")
            self.wednesday_weight_entry.configure(placeholder_text="NONE")

            self.thursday_weight_entry.configure(state="normal")
            self.friday_weight_entry.configure(state="disabled")
            self.saturday_weight_entry.configure(state="disabled")
            self.sunday_weight_entry.configure(state="disabled")
            self.monday_weight_entry.configure(state="disabled")
            self.tuesday_weight_entry.configure(state="disabled")
            self.wednesday_weight_entry.configure(state="disabled")
        elif (day == "Friday"):
            self.thursday_weight_entry.configure(placeholder_text="NONE")
            self.saturday_weight_entry.configure(placeholder_text="NONE")
            self.sunday_weight_entry.configure(placeholder_text="NONE")
            self.monday_weight_entry.configure(placeholder_text="NONE")
            self.tuesday_weight_entry.configure(placeholder_text="NONE")
            self.wednesday_weight_entry.configure(placeholder_text="NONE")

            self.thursday_weight_entry.configure(state="disabled")
            self.friday_weight_entry.configure(state="normal")
            self.saturday_weight_entry.configure(state="disabled")
            self.sunday_weight_entry.configure(state="disabled")
            self.monday_weight_entry.configure(state="disabled")
            self.tuesday_weight_entry.configure(state="disabled")
            self.wednesday_weight_entry.configure(state="disabled")
        elif (day == "Saturday"):
            self.thursday_weight_entry.configure(placeholder_text="NONE")
            self.friday_weight_entry.configure(placeholder_text="NONE")
            self.sunday_weight_entry.configure(placeholder_text="NONE")
            self.monday_weight_entry.configure(placeholder_text="NONE")
            self.tuesday_weight_entry.configure(placeholder_text="NONE")
            self.wednesday_weight_entry.configure(placeholder_text="NONE")

            self.thursday_weight_entry.configure(state="disabled")
            self.friday_weight_entry.configure(state="disabled")
            self.saturday_weight_entry.configure(state="normal")
            self.sunday_weight_entry.configure(state="disabled")
            self.monday_weight_entry.configure(state="disabled")
            self.tuesday_weight_entry.configure(state="disabled")
            self.wednesday_weight_entry.configure(state="disabled")
        elif (day == "Sunday"):
            self.thursday_weight_entry.configure(placeholder_text="NONE")
            self.friday_weight_entry.configure(placeholder_text="NONE")
            self.saturday_weight_entry.configure(placeholder_text="NONE")
            self.monday_weight_entry.configure(placeholder_text="NONE")
            self.tuesday_weight_entry.configure(placeholder_text="NONE")
            self.wednesday_weight_entry.configure(placeholder_text="NONE")

            self.thursday_weight_entry.configure(state="disabled")
            self.friday_weight_entry.configure(state="disabled")
            self.saturday_weight_entry.configure(state="disabled")
            self.sunday_weight_entry.configure(state="normal")
            self.monday_weight_entry.configure(state="disabled")
            self.tuesday_weight_entry.configure(state="disabled")
            self.wednesday_weight_entry.configure(state="disabled")
        elif (day == "Monday"):
            self.thursday_weight_entry.configure(placeholder_text="NONE")
            self.friday_weight_entry.configure(placeholder_text="NONE")
            self.saturday_weight_entry.configure(placeholder_text="NONE")
            self.sunday_weight_entry.configure(placeholder_text="NONE")
            self.tuesday_weight_entry.configure(placeholder_text="NONE")
            self.wednesday_weight_entry.configure(placeholder_text="NONE")

            self.thursday_weight_entry.configure(state="disabled")
            self.friday_weight_entry.configure(state="disabled")
            self.saturday_weight_entry.configure(state="disabled")
            self.sunday_weight_entry.configure(state="disabled")
            self.monday_weight_entry.configure(state="normal")
            self.tuesday_weight_entry.configure(state="disabled")
            self.wednesday_weight_entry.configure(state="disabled")
        elif (day == "Tuesday"):
            self.thursday_weight_entry.configure(placeholder_text="NONE")
            self.friday_weight_entry.configure(placeholder_text="NONE")
            self.saturday_weight_entry.configure(placeholder_text="NONE")
            self.sunday_weight_entry.configure(placeholder_text="NONE")
            self.monday_weight_entry.configure(placeholder_text="NONE")
            self.wednesday_weight_entry.configure(placeholder_text="NONE")

            self.thursday_weight_entry.configure(state="disabled")
            self.friday_weight_entry.configure(state="disabled")
            self.saturday_weight_entry.configure(state="disabled")
            self.sunday_weight_entry.configure(state="disabled")
            self.monday_weight_entry.configure(state="disabled")
            self.tuesday_weight_entry.configure(state="normal")
            self.wednesday_weight_entry.configure(state="disabled")
        else:
            self.thursday_weight_entry.configure(placeholder_text="NONE")
            self.friday_weight_entry.configure(placeholder_text="NONE")
            self.saturday_weight_entry.configure(placeholder_text="NONE")
            self.sunday_weight_entry.configure(placeholder_text="NONE")
            self.monday_weight_entry.configure(placeholder_text="NONE")
            self.tuesday_weight_entry.configure(placeholder_text="NONE")

            self.thursday_weight_entry.configure(state="disabled")
            self.friday_weight_entry.configure(state="disabled")
            self.saturday_weight_entry.configure(state="disabled")
            self.sunday_weight_entry.configure(state="disabled")
            self.monday_weight_entry.configure(state="disabled")
            self.tuesday_weight_entry.configure(state="disabled")
            self.wednesday_weight_entry.configure(state="normal")

        # Time Walked Entries
        self.thursday_time_walked_entry = CTk.CTkEntry(self, placeholder_text="00:00:00", justify="center")
        self.thursday_time_walked_entry.configure(state="disabled")
        self.thursday_time_walked_entry.grid(row=6, column=2, padx=(5, 5))

        if (thursday_walking_time != 0):
            hours = thursday_walking_time // 3600
            minutes = (thursday_walking_time % 3600) // 60
            seconds = thursday_walking_time % 60
            walking_time_string = f"{hours:02.0f}:{minutes:02.0f}:{seconds:02.0f}"
            self.thursday_time_walked_entry.configure(state="normal")
            self.thursday_time_walked_entry.insert(0, walking_time_string)
            self.thursday_time_walked_entry.configure(state="disabled")

        self.friday_time_walked_entry = CTk.CTkEntry(self, placeholder_text="00:00:00", justify="center")
        self.friday_time_walked_entry.configure(state="disabled")
        self.friday_time_walked_entry.grid(row=7, column=2, padx=(5, 5))

        if (friday_walking_time != 0):
            hours = friday_walking_time // 3600
            minutes = (friday_walking_time % 3600) // 60
            seconds = friday_walking_time % 60
            walking_time_string = f"{hours:02.0f}:{minutes:02.0f}:{seconds:02.0f}"
            self.friday_time_walked_entry.configure(state="normal")
            self.friday_time_walked_entry.insert(0, walking_time_string)
            self.friday_time_walked_entry.configure(state="disabled")

        self.saturday_time_walked_entry = CTk.CTkEntry(self, placeholder_text="00:00:00", justify="center")
        self.saturday_time_walked_entry.configure(state="disabled")
        self.saturday_time_walked_entry.grid(row=8, column=2, padx=(5, 5))

        if (saturday_walking_time != 0):
            hours = saturday_walking_time // 3600
            minutes = (saturday_walking_time % 3600) // 60
            seconds = saturday_walking_time % 60
            walking_time_string = f"{hours:02.0f}:{minutes:02.0f}:{seconds:02.0f}"
            self.saturday_time_walked_entry.configure(state="normal")
            self.saturday_time_walked_entry.insert(0, walking_time_string)
            self.saturday_time_walked_entry.configure(state="disabled")

        self.sunday_time_walked_entry = CTk.CTkEntry(self, placeholder_text="00:00:00", justify="center")
        self.sunday_time_walked_entry.configure(state="disabled")
        self.sunday_time_walked_entry.grid(row=2, column=2, padx=(5, 5))

        if (sunday_walking_time != 0):
            hours = sunday_walking_time // 3600
            minutes = (sunday_walking_time % 3600) // 60
            seconds = sunday_walking_time % 60
            walking_time_string = f"{hours:02.0f}:{minutes:02.0f}:{seconds:02.0f}"
            self.sunday_time_walked_entry.configure(state="normal")
            self.sunday_time_walked_entry.insert(0, walking_time_string)
            self.sunday_time_walked_entry.configure(state="disabled")

        self.monday_time_walked_entry = CTk.CTkEntry(self, placeholder_text="00:00:00", justify="center")
        self.monday_time_walked_entry.configure(state="disabled")
        self.monday_time_walked_entry.grid(row=3, column=2, padx=(5, 5))

        if (monday_walking_time != 0):
            hours = monday_walking_time // 3600
            minutes = (monday_walking_time % 3600) // 60
            seconds = monday_walking_time % 60
            walking_time_string = f"{hours:02.0f}:{minutes:02.0f}:{seconds:02.0f}"
            self.monday_time_walked_entry.configure(state="normal")
            self.monday_time_walked_entry.insert(0, walking_time_string)
            self.monday_time_walked_entry.configure(state="disabled")

        self.tuesday_time_walked_entry = CTk.CTkEntry(self, placeholder_text="00:00:00", justify="center")
        self.tuesday_time_walked_entry.configure(state="disabled")
        self.tuesday_time_walked_entry.grid(row=4, column=2, padx=(5, 5))

        if (tuesday_walking_time != 0):
            hours = tuesday_walking_time // 3600
            minutes = (tuesday_walking_time % 3600) // 60
            seconds = tuesday_walking_time % 60
            walking_time_string = f"{hours:02.0f}:{minutes:02.0f}:{seconds:02.0f}"
            self.tuesday_time_walked_entry.configure(state="normal")
            self.tuesday_time_walked_entry.insert(0, walking_time_string)
            self.tuesday_time_walked_entry.configure(state="disabled")

        self.wednesday_time_walked_entry = CTk.CTkEntry(self, placeholder_text="00:00:00", justify="center")
        self.wednesday_time_walked_entry.configure(state="disabled")
        self.wednesday_time_walked_entry.grid(row=5, column=2, padx=(5, 5))

        if (wednesday_walking_time != 0):
            hours = wednesday_walking_time // 3600
            minutes = (wednesday_walking_time % 3600) // 60
            seconds = wednesday_walking_time % 60
            walking_time_string = f"{hours:02.0f}:{minutes:02.0f}:{seconds:02.0f}"
            self.wednesday_time_walked_entry.configure(state="normal")
            self.wednesday_time_walked_entry.insert(0, walking_time_string)
            self.wednesday_time_walked_entry.configure(state="disabled")

        # Distance Entries
        self.thursday_distance_entry = CTk.CTkEntry(self, placeholder_text="0", justify="center")
        self.thursday_distance_entry.configure(state="disabled")
        self.thursday_distance_entry.grid(row=6, column=3, padx=(5, 5))

        if (thursday_walking_distance != 0):
            walking_distance_string = str(thursday_walking_distance)
            self.thursday_distance_entry.configure(state="normal")
            self.thursday_distance_entry.insert(0, walking_distance_string)
            self.thursday_distance_entry.configure(state="disabled")

        self.friday_distance_entry = CTk.CTkEntry(self, placeholder_text="0", justify="center")
        self.friday_distance_entry.configure(state="disabled")
        self.friday_distance_entry.grid(row=7, column=3, padx=(5, 5))

        if (friday_walking_distance != 0):
            walking_distance_string = str(friday_walking_distance)
            self.friday_distance_entry.configure(state="normal")
            self.friday_distance_entry.insert(0, walking_distance_string)
            self.friday_distance_entry.configure(state="disabled")

        self.saturday_distance_entry = CTk.CTkEntry(self, placeholder_text="0", justify="center")
        self.saturday_distance_entry.configure(state="disabled")
        self.saturday_distance_entry.grid(row=8, column=3, padx=(5, 5))

        if (saturday_walking_distance != 0):
            walking_distance_string = str(saturday_walking_distance)
            self.saturday_distance_entry.configure(state="normal")
            self.saturday_distance_entry.insert(0, walking_distance_string)
            self.saturday_distance_entry.configure(state="disabled")

        self.sunday_distance_entry = CTk.CTkEntry(self, placeholder_text="0", justify="center")
        self.sunday_distance_entry.configure(state="disabled")
        self.sunday_distance_entry.grid(row=2, column=3, padx=(5, 5))

        if (sunday_walking_distance != 0):
            walking_distance_string = str(sunday_walking_distance)
            self.sunday_distance_entry.configure(state="normal")
            self.sunday_distance_entry.insert(0, walking_distance_string)
            self.sunday_distance_entry.configure(state="disabled")

        self.monday_distance_entry = CTk.CTkEntry(self, placeholder_text="0", justify="center")
        self.monday_distance_entry.configure(state="disabled")
        self.monday_distance_entry.grid(row=3, column=3, padx=(5, 5))

        if (monday_walking_distance != 0):
            walking_distance_string = str(monday_walking_distance)
            self.monday_distance_entry.configure(state="normal")
            self.monday_distance_entry.insert(0, walking_distance_string)
            self.monday_distance_entry.configure(state="disabled")

        self.tuesday_distance_entry = CTk.CTkEntry(self, placeholder_text="0", justify="center")
        self.tuesday_distance_entry.configure(state="disabled")
        self.tuesday_distance_entry.grid(row=4, column=3, padx=(5, 5))

        if (tuesday_walking_distance != 0):
            walking_distance_string = str(tuesday_walking_distance)
            self.tuesday_distance_entry.configure(state="normal")
            self.tuesday_distance_entry.insert(0, walking_distance_string)
            self.tuesday_distance_entry.configure(state="disabled")

        self.wednesday_distance_entry = CTk.CTkEntry(self, placeholder_text="0", justify="center")
        self.wednesday_distance_entry.configure(state="disabled")
        self.wednesday_distance_entry.grid(row=5, column=3, padx=(5, 5))

        if (wednesday_walking_distance != 0):
            walking_distance_string = str(wednesday_walking_distance)
            self.wednesday_distance_entry.configure(state="normal")
            self.wednesday_distance_entry.insert(0, walking_distance_string)
            self.wednesday_distance_entry.configure(state="disabled")

        #Steps Entries
        self.thursday_steps_entry = CTk.CTkEntry(self, placeholder_text="0", justify="center")
        self.thursday_steps_entry.configure(state="disabled")
        self.thursday_steps_entry.grid(row=6, column=4, padx=(5, 5))

        if (thursday_walking_steps != 0):
            walking_steps_string = str(thursday_walking_steps)
            self.thursday_steps_entry.configure(state="normal")
            self.thursday_steps_entry.insert(0, walking_steps_string)
            self.thursday_steps_entry.configure(state="disabled")

        self.friday_steps_entry = CTk.CTkEntry(self, placeholder_text="0", justify="center")
        self.friday_steps_entry.configure(state="disabled")
        self.friday_steps_entry.grid(row=7, column=4, padx=(5, 5))

        if (friday_walking_steps != 0):
            walking_steps_string = str(friday_walking_steps)
            self.friday_steps_entry.configure(state="normal")
            self.friday_steps_entry.insert(0, walking_steps_string)
            self.friday_steps_entry.configure(state="disabled")

        self.saturday_steps_entry = CTk.CTkEntry(self, placeholder_text="0", justify="center")
        self.saturday_steps_entry.configure(state="disabled")
        self.saturday_steps_entry.grid(row=8, column=4, padx=(5, 5))

        if (saturday_walking_steps != 0):
            walking_steps_string = str(saturday_walking_steps)
            self.saturday_steps_entry.configure(state="normal")
            self.saturday_steps_entry.insert(0, walking_steps_string)
            self.saturday_steps_entry.configure(state="disabled")

        self.sunday_steps_entry = CTk.CTkEntry(self, placeholder_text="0", justify="center")
        self.sunday_steps_entry.configure(state="disabled")
        self.sunday_steps_entry.grid(row=2, column=4, padx=(5, 5))

        if (sunday_walking_steps != 0):
            walking_steps_string = str(sunday_walking_steps)
            self.sunday_steps_entry.configure(state="normal")
            self.sunday_steps_entry.insert(0, walking_steps_string)
            self.sunday_steps_entry.configure(state="disabled")

        self.monday_steps_entry = CTk.CTkEntry(self, placeholder_text="0", justify="center")
        self.monday_steps_entry.configure(state="disabled")
        self.monday_steps_entry.grid(row=3, column=4, padx=(5, 5))

        if (monday_walking_steps != 0):
            walking_steps_string = str(monday_walking_steps)
            self.monday_steps_entry.configure(state="normal")
            self.monday_steps_entry.insert(0, walking_steps_string)
            self.monday_steps_entry.configure(state="disabled")

        self.tuesday_steps_entry = CTk.CTkEntry(self, placeholder_text="0", justify="center")
        self.tuesday_steps_entry.configure(state="disabled")
        self.tuesday_steps_entry.grid(row=4, column=4, padx=(5, 5))

        if (tuesday_walking_steps != 0):
            walking_steps_string = str(tuesday_walking_steps)
            self.tuesday_steps_entry.configure(state="normal")
            self.tuesday_steps_entry.insert(0, walking_steps_string)
            self.tuesday_steps_entry.configure(state="disabled")

        self.wednesday_steps_entry = CTk.CTkEntry(self, placeholder_text="0", justify="center")
        self.wednesday_steps_entry.configure(state="disabled")
        self.wednesday_steps_entry.grid(row=5, column=4, padx=(5, 5))

        if (wednesday_walking_steps != 0):
            walking_steps_string = str(wednesday_walking_steps)
            self.wednesday_steps_entry.configure(state="normal")
            self.wednesday_steps_entry.insert(0, walking_steps_string)
            self.wednesday_steps_entry.configure(state="disabled")

        #Colories Entries
        self.thursday_calories_entry = CTk.CTkEntry(self, placeholder_text="0", justify="center")
        self.thursday_calories_entry.configure(state="disabled")
        self.thursday_calories_entry.grid(row=6, column=5, padx=(5, 10))

        if (thursday_calories != 0):
            walking_calories_string = str(thursday_calories)
            self.thursday_calories_entry.configure(state="normal")
            self.thursday_calories_entry.insert(0, walking_calories_string)
            self.thursday_calories_entry.configure(state="disabled")

        self.friday_calories_entry = CTk.CTkEntry(self, placeholder_text="0", justify="center")
        self.friday_calories_entry.configure(state="disabled")
        self.friday_calories_entry.grid(row=7, column=5, padx=(5, 10))

        if (friday_calories != 0):
            walking_calories_string = str(friday_calories)
            self.friday_calories_entry.configure(state="normal")
            self.friday_calories_entry.insert(0, walking_calories_string)
            self.friday_calories_entry.configure(state="disabled")

        self.saturday_calories_entry = CTk.CTkEntry(self, placeholder_text="0", justify="center")
        self.saturday_calories_entry.configure(state="disabled")
        self.saturday_calories_entry.grid(row=8, column=5, padx=(5, 10))

        if (saturday_calories != 0):
            walking_calories_string = str(saturday_calories)
            self.saturday_calories_entry.configure(state="normal")
            self.saturday_calories_entry.insert(0, walking_calories_string)
            self.saturday_calories_entry.configure(state="disabled")

        self.sunday_calories_entry = CTk.CTkEntry(self, placeholder_text="0", justify="center")
        self.sunday_calories_entry.configure(state="disabled")
        self.sunday_calories_entry.grid(row=2, column=5, padx=(5, 10))

        if (sunday_calories != 0):
            walking_calories_string = str(sunday_calories)
            self.sunday_calories_entry.configure(state="normal")
            self.sunday_calories_entry.insert(0, walking_calories_string)
            self.sunday_calories_entry.configure(state="disabled")

        self.monday_calories_entry = CTk.CTkEntry(self, placeholder_text="0", justify="center")
        self.monday_calories_entry.configure(state="disabled")
        self.monday_calories_entry.grid(row=3, column=5, padx=(5, 10))

        if (monday_calories != 0):
            walking_calories_string = str(monday_calories)
            self.monday_calories_entry.configure(state="normal")
            self.monday_calories_entry.insert(0, walking_calories_string)
            self.monday_calories_entry.configure(state="disabled")

        self.tuesday_calories_entry = CTk.CTkEntry(self, placeholder_text="0", justify="center")
        self.tuesday_calories_entry.configure(state="disabled")
        self.tuesday_calories_entry.grid(row=4, column=5, padx=(5, 10))

        if (tuesday_calories != 0):
            walking_calories_string = str(tuesday_calories)
            self.tuesday_calories_entry.configure(state="normal")
            self.tuesday_calories_entry.insert(0, walking_calories_string)
            self.tuesday_calories_entry.configure(state="disabled")

        self.wednesday_calories_entry = CTk.CTkEntry(self, placeholder_text="0", justify="center")
        self.wednesday_calories_entry.configure(state="disabled")
        self.wednesday_calories_entry.grid(row=5, column=5, padx=(5, 10))

        if (wednesday_calories != 0):
            walking_calories_string = str(wednesday_calories)
            self.wednesday_calories_entry.configure(state="normal")
            self.wednesday_calories_entry.insert(0, walking_calories_string)
            self.wednesday_calories_entry.configure(state="disabled")

class TotalsFrame(CTk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        
        # Title Label
        self.title = CTk.CTkLabel(self, text="Total", fg_color="gray30")
        self.title.grid(row=0, column=0, columnspan=6, sticky="ew")
        
        # Category Labels
        self.time_programming_label = CTk.CTkLabel(self, text="Time Worked")
        self.time_programming_label.grid(row=1, column=1, padx=(380, 380))

        # self.weight_lost_label = CTk.CTkLabel(self, text="Weight Lost")
        # self.weight_lost_label.grid(row=1, column=2, padx=(50, 50))
        
        # self.time_walked_label = CTk.CTkLabel(self, text="Time Walked")
        # self.time_walked_label.grid(row=1, column=3, padx=(50, 108))

        # self.distance_label = CTk.CTkLabel(self, text="Distance")
        # self.distance_label.grid(row=3, column=1, padx=(108, 50))

        # self.steps_label = CTk.CTkLabel(self, text="Steps")
        # self.steps_label.grid(row=3, column=2, padx=(50, 50))

        # self.calories_burned_label = CTk.CTkLabel(self, text="Calories Burned")
        # self.calories_burned_label.grid(row=3, column=3, padx=(50, 108))
        
        # Total Time Programming Entry
        global total_programming_time
        self.time_programming_entry = CTk.CTkEntry(self, placeholder_text="00:00:00", justify="center")
        self.time_programming_entry.configure(state="disabled")
        self.time_programming_entry.grid(row=2, column=1, padx=(108, 108), pady=(5,5))

        if (total_programming_time != 0):
            hours = total_programming_time // 3600
            minutes = (total_programming_time % 3600) // 60
            seconds = total_programming_time % 60
            programming_time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            self.time_programming_entry.configure(state="normal")
            self.time_programming_entry.insert(0, programming_time_string)
            self.time_programming_entry.configure(state="disabled")

        # # Total Weight Lost
        # self.total_weight_lost_entry = CTk.CTkEntry(self, placeholder_text="0", justify="center")
        # self.total_weight_lost_entry.configure(state="disabled")
        # self.total_weight_lost_entry.grid(row=2, column=2, padx=(50, 50), pady=(5,5))

        # if (total_weight_lost != 0):
        #     weight_lost_string = str(total_weight_lost)
        #     self.total_weight_lost_entry.configure(state="normal")
        #     self.total_weight_lost_entry.insert(0, weight_lost_string)
        #     self.total_weight_lost_entry.configure(state="disabled")

        # # Total Time Walked Entry
        # global total_walking_time
        # self.time_walked_entry = CTk.CTkEntry(self, placeholder_text="00:00:00", justify="center")
        # self.time_walked_entry.configure(state="disabled")
        # self.time_walked_entry.grid(row=2, column=3, padx=(50, 108), pady=(5,5))

        # if (total_walking_time != 0):
        #     hours = total_walking_time // 3600
        #     minutes = (total_walking_time % 3600) // 60
        #     seconds = total_walking_time % 60
        #     walking_time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        #     self.time_walked_entry.configure(state="normal")
        #     self.time_walked_entry.insert(0, walking_time_string)
        #     self.time_walked_entry.configure(state="disabled")

        # # Total Distance Entry
        # self.distance_entry = CTk.CTkEntry(self, placeholder_text="0", justify="center")
        # self.distance_entry.configure(state="disabled")
        # self.distance_entry.grid(row=4, column=1, padx=(108, 50), pady=(5,5))

        # if (total_walking_distance != 0):
        #     walking_distance_string = str(total_walking_distance)
        #     self.distance_entry.configure(state="normal")
        #     self.distance_entry.insert(0, walking_distance_string)
        #     self.distance_entry.configure(state="disabled")

        # # Total Steps Entry
        # self.steps_entry = CTk.CTkEntry(self, placeholder_text="0", justify="center")
        # self.steps_entry.configure(state="disabled")
        # self.steps_entry.grid(row=4, column=2, padx=(50, 50), pady=(5,5))

        # if (total_walking_steps != 0):
        #     walking_distance_string = str(total_walking_steps)
        #     self.steps_entry.configure(state="normal")
        #     self.steps_entry.insert(0, walking_distance_string)
        #     self.steps_entry.configure(state="disabled")

        # # Total Calories Burned Entry
        # self.calories_burned_entry = CTk.CTkEntry(self, placeholder_text="0", justify="center")
        # self.calories_burned_entry.configure(state="disabled")
        # self.calories_burned_entry.grid(row=4, column=3, padx=(50, 108), pady=(5,5))

        # if (total_calories != 0):
        #     walking_distance_string = str(total_calories)
        #     self.calories_burned_entry.configure(state="normal")
        #     self.calories_burned_entry.insert(0, walking_distance_string)
        #     self.calories_burned_entry.configure(state="disabled")

class WeeklyLogTabs(CTk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # create tabs
        self.add("Programming")
        #self.add("Exercising")

        # Add Frames to tabs
        self.programming_frame = ProgrammingFrame(self.tab("Programming"))
        self.programming_frame.grid(row=0, column=0, pady=(10, 0))
        
        #self.exercise_frame = ExerciseFrame(self.tab("Exercising"))
        #self.exercise_frame.grid(row=1, column=0, pady=(10, 0))

class WeeklyDailyTabs(CTk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # create tabs
        self.add("Weekly Log")
        self.add("Daily Tracker")

        # Add Frames to tabs
        # self.weekly_tab = WeeklyLogTabs(self.tab("Weekly Log"), fg_color="transparent")
        self.weekly_tab = ProgrammingFrame(self.tab("Weekly Log"))
        self.weekly_tab.grid(row=0, column=0)

        self.daily_tab = DailyFrame(self.tab("Daily Tracker"))
        self.daily_tab.grid(row=0, column=0)

class DailyFrame(CTk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)

        timer_font_size = 0
        if (platform.system() == "Linux"):
            timer_font_size = 58
        else:
            timer_font_size = 75

        top_padding = 0
        if (platform.system() == "Linux"):
            top_padding = 54
        else:
            top_padding = 55

        bottom_padding = 0
        if (platform.system() == "Linux"):
            bottom_padding = 64
        else:
            bottom_padding = 47
        
        # Title Label
        self.title = CTk.CTkLabel(self, text="Time Trackers", fg_color="gray30")
        self.title.grid(row=0, column=0, columnspan=4, sticky="ew")

        # Header Labels
        self.session_time_worked_today_header_label = CTk.CTkLabel(self, text="Session Time Worked")
        self.session_time_worked_today_header_label.grid(row=1, column=0, padx=(50,0), pady=(top_padding,0))

        self.pomodoro_header_label = CTk.CTkLabel(self, text="Pomodoro Timer")
        self.pomodoro_header_label.grid(row=1, column=2, padx=(0,50), pady=(top_padding,0))

        # Labels for tracking total daily and pomodoro time
        self.total_time_label = CTk.CTkLabel(self, text="00:00:00", font=("", timer_font_size, "bold"))
        self.total_time_label.grid(row=2, column=0, padx=(50,0))

        self.pomodoro_time_label = CTk.CTkLabel(self, text="00:25:00", font=("", timer_font_size, "bold"))
        self.pomodoro_time_label.grid(row=2, column=2, padx=(0,50))

        # Labels for tracking pomodoro status
        self.pomodoro_focus_label = CTk.CTkLabel(self, text="Focus")
        self.pomodoro_focus_label.grid(row=3, column=2, padx=(0,50))

        self.pomodoro_count_label = CTk.CTkLabel(self, text="#1")
        self.pomodoro_count_label.grid(row=4, column=2, padx=(0,50), pady=(0, 55))

        # # Options for walking and pomodoro
        # self.walking_switch = CTk.CTkSwitch(self, text="Walking")
        # self.walking_switch.grid(row=3, column=0, padx=(50,0))

        self.pomodoro_switch = CTk.CTkSwitch(self, text="Pomodoro")
        self.pomodoro_switch.grid(row=3, column=0, rowspan=2, padx=(50,0), pady=(0,55))

        # Buttons for start/end and resume/pause
        self.start_end_button = CTk.CTkButton(self, text="Start", command=start_end)
        self.start_end_button.grid(row=3, column=1, pady=(10,0))

        if (must_clear):
            self.start_end_button.configure(state="disabled")

        self.pause_resume_button = CTk.CTkButton(self, text="Pause", state="disabled", command=pause_resume)
        self.pause_resume_button.grid(row=4, column=1, pady=(10,bottom_padding))

class ButtonsFrame(CTk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="transparent")
        self.grid_columnconfigure(0, weight=1)

        # Add Send Weekly Data Button
        self.send_weekly_data_button = CTk.CTkButton(self, text="Send Weekly Data", command=send_data_modal)
        self.send_weekly_data_button.grid(row=0, column=0, padx=(0,30), pady=(10,0))

        # Add Clear Weekly Data Button
        self.clear_weekly_data_button = CTk.CTkButton(self, text="Clear Weekly Data", command=clear_data_modal)
        self.clear_weekly_data_button.grid(row=0, column=1, padx=(30,0), pady=(10,0))

class ToplevelWindow(CTk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")

        self.label = CTk.CTkLabel(self, text="ToplevelWindow")
        self.label.pack(padx=20, pady=20)

class App(CTk.CTk):
    def __init__(self):
        super().__init__()

        # Define Window Settings
        self.title("Productivity Tracker")
        # Load and set the icon
        #self.iconbitmap("icon4.ico")  # For .ico files
        # or
        #self.iconphoto(True, ctk.CTkImage(Image.open("path/to/your/icon.png"), size=(32, 32)))  # For other image formats

        if (platform.system() == "Linux"):
            self.iconphoto(False, PhotoImage(file='icon4-2.png'))
        else:
            self.iconbitmap("icon4.ico")  # For .ico files

        self.geometry("920x635")
        center_window(self, 920, 635)
        self.grid_columnconfigure(0, weight=1)

        self.webhook_frame = CTk.CTkFrame(self, fg_color="transparent")
        self.webhook_frame.grid(row=0, column=0)

        # Add place to put webhook
        self.webhook_entry = CTk.CTkEntry(self.webhook_frame, placeholder_text="Paste Webhook Here",  width=685)
        self.webhook_entry.grid(row=0, column=0, padx=(0,10), pady=(20, 40))

        self.webhook_entry_lock_button = CTk.CTkButton(self.webhook_frame, text="Lock", command=lock_webhook)
        self.webhook_entry_lock_button.grid(row=0, column=1, pady=(30, 50))

        global webhook_locked
        load_dotenv(".env")
        discord_webhook = os.environ.get("Discord_Webhook")

        if (discord_webhook != "None"):
            self.webhook_entry.insert(0, discord_webhook)
            self.webhook_entry.configure(state="disabled")
            self.webhook_entry_lock_button.configure(text="Unlock")
            webhook_locked = True

        # Add Content for weekly and daily tabs
        self.weekly_daily_tabs = WeeklyDailyTabs(self, fg_color="transparent")
        self.weekly_daily_tabs.grid(row=1, column=0)

        # Add Content for weekly totals
        self.totals_frame = TotalsFrame(self)
        self.totals_frame.grid(row=2, column=0, padx=10)

        #Add Buttons
        self.buttons_frame = ButtonsFrame(self)
        self.buttons_frame.grid(row=3, column=0)
        
#Run app in dark mode
CTk.set_appearance_mode("dark")
color = ""
if (platform.system() == "Linux"):
    color = "green"
else:
    color = "dark-blue"
CTk.set_default_color_theme(color)
app = App()

#Function to run before closing window
def on_close():
    global thursday_punches
    global friday_punches
    global saturday_punches
    global sunday_punches
    global monday_punches
    global tuesday_punches
    global wednesday_punches

    try:
        app.after_cancel(timer_id)
    except:
        pass

    # Adds new punchout if close window before punching out
    if (not readytostart):
        day = datetime.datetime.now().strftime("%A")
        if (day == "Thursday"):
            thursday_punches.append("End: " + str(datetime.datetime.now().strftime("%I:%M:%S %p")))
        elif (day == "Friday"):
            friday_punches.append("End: " + str(datetime.datetime.now().strftime("%I:%M:%S %p")))
        elif (day == "Saturday"):
            saturday_punches.append("End: " + str(datetime.datetime.now().strftime("%I:%M:%S %p")))
        elif (day == "Sunday"):
            sunday_punches.append("End: " + str(datetime.datetime.now().strftime("%I:%M:%S %p")))
        elif (day == "Monday"):
            monday_punches.append("End: " + str(datetime.datetime.now().strftime("%I:%M:%S %p")))
        elif (day == "Tuesday"):
            tuesday_punches.append("End: " + str(datetime.datetime.now().strftime("%I:%M:%S %p")))
        else:
            wednesday_punches.append("End: " + str(datetime.datetime.now().strftime("%I:%M:%S %p")))

        data = {
            "thursday_punches": thursday_punches,
            "friday_punches": friday_punches,
            "saturday_punches": saturday_punches,
            "sunday_punches": sunday_punches,
            "monday_punches": monday_punches,
            "tuesday_punches": tuesday_punches,
            "wednesday_punches": wednesday_punches,
        }

        threading.Thread(target=write_punches_to_file, args=(data,)).start()

    app.quit()

app.protocol("WM_DELETE_WINDOW", on_close)

app.mainloop()