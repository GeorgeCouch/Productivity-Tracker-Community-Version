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

operating_system = ""

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

daily_programming_times = []
daily_punches = []

for i in range(7):
    daily_programming_times.append(0)
    daily_punches.append(["None"])

total_programming_time = 0

description = ""

must_clear = False
current_week = -1

curr_week_str = ""

# Functions for writing to JSON Files
def write_variables_to_file(data):
    try:
        with open("variables.json", "w") as file:
            json.dump(data, file)
    except Exception as e:
        write_variables_to_file(data)

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

def write_current_vars_to_variables_json():
    data = {
        "thursday_programming_time": daily_programming_times[0],
        "friday_programming_time": daily_programming_times[1],
        "saturday_programming_time": daily_programming_times[2],
        "sunday_programming_time": daily_programming_times[3],
        "monday_programming_time": daily_programming_times[4],
        "tuesday_programming_time": daily_programming_times[5],
        "wednesday_programming_time": daily_programming_times[6],
        "total_programming_time": total_programming_time,
    }

    threading.Thread(target=write_variables_to_file, args=(data,)).start()

def write_current_vars_to_description_json():
    data = {
        "description": description
    }

    threading.Thread(target=write_description_to_file, args=(data,)).start()

def write_current_vars_to_punches_json():
    data = {
        "sunday_punches": daily_punches[0],
        "monday_punches": daily_punches[1],
        "tuesday_punches": daily_punches[2],
        "wednesday_punches": daily_punches[3],
        "thursday_punches": daily_punches[4],
        "friday_punches": daily_punches[5],
        "saturday_punches": daily_punches[6]
    }

    threading.Thread(target=write_punches_to_file, args=(data,)).start()

def write_current_vars_to_must_clear_json():
    data = {
        "must_clear": must_clear,
        "current_week": current_week
    }

    threading.Thread(target=write_must_clear_to_file, args=(data,)).start()

def write_current_vars_to_current_week_json():
    data = {
        "curr_week_str": curr_week_str
    }

    threading.Thread(target=write_current_week_to_file, args=(data,)).start()

# Create Json Files if they don't already exist
json_files = ["variables.json", "punches.json", "description.json", "must_clear.json", "current_week.json"]
write_functions = [write_current_vars_to_variables_json, write_current_vars_to_punches_json, write_current_vars_to_description_json, write_current_vars_to_must_clear_json, write_current_vars_to_current_week_json]
for i in range(len(json_files)):
    file_path = json_files[i]
    if not os.path.isfile(file_path):
        write_functions[i]()

file_path = ".env"
if not os.path.isfile(file_path):
    with open(".env", "w", newline='') as file:
        file.write("Discord_Webhook='None'")

# Assign Vars from JSON Files
with open("variables.json", "r") as file:
    data = json.load(file)

# Vars for Programming
i = 0
for key, value in data.items():
    if ("total" not in key):
        daily_programming_times[i] = value
        i += 1

total_programming_time = data["total_programming_time"]

# Vars for Punches
with open("punches.json", "r") as file:
    data = json.load(file)

i = 0
for key, value in data.items():
    daily_punches[i] = value
    i += 1

with open("description.json", "r") as file:
    data = json.load(file)

description = data["description"]

with open("must_clear.json", "r") as file:
    data = json.load(file)

must_clear = data["must_clear"]
current_week = data["current_week"]

with open("current_week.json", "r") as file:
    data = json.load(file)

curr_week_str = data["curr_week_str"]

can_clear = True
webhook_locked = False

def format_time_as_string_from_num(time):
    hours = time // 3600
    minutes = (time % 3600) // 60
    seconds = time % 60
    time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    return time_string

def delete_and_insert_data_into_entry(entry, data):
    entry.configure(state="normal")
    entry.delete(0, "end")
    entry.insert(0, str(data))
    entry.configure(state="disabled")

def reset_entry(entry, placeholder_text):
    entry.configure(state="normal")
    entry.delete(0, "end")
    entry.configure(placeholder_text=placeholder_text)
    entry.configure(state="disabled")

def configure_clock_out_ui():
    app.weekly_daily_tabs.daily_tab.start_end_button.configure(text="Start")
    app.weekly_daily_tabs.daily_tab.pause_resume_button.configure(state="disabled")
    app.weekly_daily_tabs.daily_tab.total_time_label.configure(text="00:00:00")
    app.weekly_daily_tabs.daily_tab.pomodoro_time_label.configure(text="00:25:00")
    app.weekly_daily_tabs.daily_tab.pause_resume_button.configure(text="Pause")
    app.weekly_daily_tabs.daily_tab.pomodoro_count_label.configure(text="#1")
    app.weekly_daily_tabs.daily_tab.pomodoro_focus_label.configure(text="Focus")

def pause_resume():
    global paused
    global tracking
    global timer_id

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
        app.after_cancel(timer_id)
        update_time(True)

def create_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name="Productivity Tracker",
        app_icon="icon4.ico",
        timeout=10
    )
    app.attributes("-topmost", True)
    app.attributes("-topmost", False)

def pomodoro():
    global pomodoro_break
    global p_focus_time
    global p_long_break_time
    global p_break_time
    global p_cycle_count
    global focus_time
    global break_time
    global long_break_time

    # Determine pomodoro state. Subtract time depending on state
    if (not pomodoro_break):
        # 25 min
        p_focus_time = p_focus_time - 1
        time_string = format_time_as_string_from_num(p_focus_time)
        app.weekly_daily_tabs.daily_tab.pomodoro_time_label.configure(text=time_string)
    elif (pomodoro_break and p_cycle_count % 4 == 0):
        # 15 min
        p_long_break_time = p_long_break_time - 1
        time_string = format_time_as_string_from_num(p_long_break_time)
        app.weekly_daily_tabs.daily_tab.pomodoro_time_label.configure(text=time_string)
    else:
        # 5 min
        p_break_time = p_break_time - 1
        time_string = format_time_as_string_from_num(p_break_time)
        app.weekly_daily_tabs.daily_tab.pomodoro_time_label.configure(text=time_string)
        
    # Handle pomodoro state end (time reaches 00:00:00)
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
        p_break_time = break_time
        p_focus_time = focus_time
        p_long_break_time = long_break_time

        # Pause and reset label
        pause_resume()

        # Determine pomodoro state and create notification
        if (app.weekly_daily_tabs.daily_tab.pomodoro_switch.get() == 1):
            if (not pomodoro_break):
                # 25 min
                create_notification("Focus", "Focus for 25 minutes.")
                time_string = format_time_as_string_from_num(p_focus_time)
                app.weekly_daily_tabs.daily_tab.pomodoro_time_label.configure(text=time_string)
            elif (pomodoro_break and p_cycle_count % 4 == 0):
                # 15 min
                create_notification("Long Break", "Break for 15 minutes.")
                time_string = format_time_as_string_from_num(p_long_break_time)
                app.weekly_daily_tabs.daily_tab.pomodoro_time_label.configure(text=time_string)
            else:
                # 5 min
                create_notification("Short Break", "Break for 5 minutes.")
                time_string = format_time_as_string_from_num(p_break_time)
                app.weekly_daily_tabs.daily_tab.pomodoro_time_label.configure(text=time_string)

def handle_being_clocked_in_past_saturday_midnight():
    global current_week
    global can_clear
    global readytostart
    global paused
    global p_focus_time
    global p_break_time
    global p_long_break_time
    global focus_time
    global break_time
    global long_break_time
    global p_cycle_count
    global tracking
    global must_clear
    global daily_punches

    # Test to see if current week is equal to the week we get now, if not then user must delete data
    week_num = datetime.datetime.now().strftime("%U %Y")
    if (current_week != week_num):
        can_clear = True
        
        # Reset UI and disable clock in
        configure_clock_out_ui()
        app.buttons_frame.send_weekly_data_button.configure(state="normal")
        app.buttons_frame.clear_weekly_data_button.configure(state="normal")
        app.weekly_daily_tabs.weekly_tab.description_textbox.configure(state="normal")
        app.weekly_daily_tabs.daily_tab.start_end_button.configure(state="disabled")
        
        # Reset Vars
        readytostart = True
        paused = False
        p_focus_time = focus_time
        p_break_time = break_time
        p_long_break_time = long_break_time
        p_cycle_count = 1

        # Spoof Punchout on Saturday 11:59:59 PM 
        daily_punches[6].append("End: 11:59:59 PM")
        if (daily_punches[6][0] == "None"):
            daily_punches[6].pop(0)
        app.weekly_daily_tabs.weekly_tab.daily_punches_option_menus[6].configure(values=daily_punches[6])

        write_current_vars_to_punches_json()

        create_notification("You've been clocked out!", "You've been clocked out due to being clocked in during a new week without clearing first.")

        new_week_modal()

        # Save must_clear as true so the user will have to clear before they clock in again
        must_clear = True

        write_current_vars_to_must_clear_json()

        # Break out of time tracker
        tracking = False
        app.after_cancel(timer_id)

def update_time(firstpass):
    global current_week
    global tracking
    global total_programming_time
    global timer_id
    global daily_programming_times

    # Save current_week if it hasn't been set yet, else see if user is clocked in past saturday at midnight
    if (current_week == -1):
        current_week = datetime.datetime.now().strftime("%U %Y")
        write_current_vars_to_must_clear_json()
    else:
        handle_being_clocked_in_past_saturday_midnight()

    if (tracking):
        # Allows for 1 second buffer
        if (firstpass):
            firstpass = False
        else:
            # Add time to total time
            label_text = app.weekly_daily_tabs.daily_tab.total_time_label._text
            hours, minutes, seconds = map(int, label_text.split(":"))
            label_value = hours * 3600 + minutes * 60 + seconds
            label_value = label_value + 1
            time_string = format_time_as_string_from_num(label_value)
            app.weekly_daily_tabs.daily_tab.total_time_label.configure(text=time_string)
            
            # Use local day_as_number in case of day change while program running
            day_as_number = (datetime.datetime.now().weekday() + 1) % 7

            # Call functions that handle selected options
            if (app.weekly_daily_tabs.daily_tab.pomodoro_switch.get() == 1):
                pomodoro()
            
            programming_time_entries = app.weekly_daily_tabs.weekly_tab.programming_time_entries
            for i in range(7):
                # Add time to current day
                if (day_as_number == i):
                    daily_programming_times[i] = daily_programming_times[i] + 1
                    time_as_str = format_time_as_string_from_num(daily_programming_times[i])
                    delete_and_insert_data_into_entry(programming_time_entries[i], time_as_str)
                    
            # Calculate total programming time
            total_programming_time = 0
            for i in range(7):
                total_programming_time = total_programming_time + daily_programming_times[i]
            
            time_as_str = format_time_as_string_from_num(total_programming_time)
            delete_and_insert_data_into_entry(app.totals_frame.time_programming_entry, time_as_str)

            write_current_vars_to_variables_json()

        # Recursively call update_time every second. Save timer in timer_id
        timer_id = app.after(1000, update_time, False)

def get_date_range_for_current_week():
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
    if (3 < day < 21) or (23 < day < 31):
        suffix = "th"
    else:
        suffixes = ["th", "st", "nd", "rd"]
        suffix = suffixes[day % 10]
    return suffix

def append_pop_configure_punches(punches, day_as_number, start_end_str):
    # Append start punch
    start_str = start_end_str + str(datetime.datetime.now().strftime("%I:%M:%S %p"))
    punches.append(start_str)
    
    # Pop None punch if it exists
    if (punches[0] == "None"):
        punches.pop(0)
    
    # Display on UI
    punch_option_menus = app.weekly_daily_tabs.weekly_tab.daily_punches_option_menus
    punch_option_menus[day_as_number].configure(values=punches)

def append_and_save_start_end_punch(start_end_str):
    # Use local day_as_number in case of day change while program running
    day_as_number = (datetime.datetime.now().weekday() + 1) % 7

    for i in range(7):
        if (day_as_number == i):
            append_pop_configure_punches(daily_punches[i], day_as_number, start_end_str)

    write_current_vars_to_punches_json()

def start_end():
    global current_week
    global readytostart
    global curr_week_str
    global can_clear
    global start_time
    global tracking
    global timer_id
    global paused
    global p_focus_time
    global p_break_time
    global p_long_break_time
    global p_cycle_count

    # Check if data exists in the previous week. If so then don't allow user to clock in and display message/notification
    if (current_week != datetime.datetime.now().strftime("%U %Y") and current_week != -1):
        app.weekly_daily_tabs.daily_tab.start_end_button.configure(state="disabled")
        
        create_notification("You've been clocked out!", "You've been clocked out due to being clocked in during a new week without clearing first.")
        
        new_week_modal()
    else:
        can_clear = False
        app.buttons_frame.send_weekly_data_button.configure(state="disabled")
        app.buttons_frame.clear_weekly_data_button.configure(state="disabled")
        app.weekly_daily_tabs.weekly_tab.description_textbox.configure(state="disabled")

        if (readytostart):
            # Clock In
            readytostart = False
            start_time = time.time()
            tracking = True
            app.weekly_daily_tabs.daily_tab.start_end_button.configure(text="End")
            app.weekly_daily_tabs.daily_tab.pause_resume_button.configure(state="normal")
            
            append_and_save_start_end_punch("Start: ")

            # Save current week to curr_week_str if one isn't already set
            if (curr_week_str == ""):
                curr_week_str = get_date_range_for_current_week()
                write_current_vars_to_current_week_json()

            # Do the same as above but for must clear file
            if (current_week == -1):
                current_week = datetime.datetime.now().strftime("%U %Y")
                write_current_vars_to_must_clear_json()
            
            # Flush out timer if one is set and start clock
            if (timer_id != ""):
                app.after_cancel(timer_id)

            # Begin Timer
            update_time(True)
        else:
            # Clock Out
            can_clear = True
            
            app.buttons_frame.send_weekly_data_button.configure(state="normal")
            app.buttons_frame.clear_weekly_data_button.configure(state="normal")
            app.weekly_daily_tabs.weekly_tab.description_textbox.configure(state="normal")

            configure_clock_out_ui()

            # Reset Vars
            readytostart = True
            paused = False
            p_focus_time = focus_time
            p_break_time = break_time
            p_long_break_time = long_break_time
            p_cycle_count = 1

            append_and_save_start_end_punch("End: ")

            # Flush out timer
            app.after_cancel(timer_id)

def get_operating_system():
    global operating_system
    # Determine operating system being used
    if (platform.system() == "Linux"):
        operating_system = "Linux"
    else:
        operating_system = "Windows"

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
    window.geometry(f"+{x}+{y}")

def clear_data():
    # Check if files exist
    variables_path = "variables.json"
    punches_path = "punches.json"
    description_path = "description.json"
    must_clear_path = "must_clear.json"
    current_week_path = "current_week.json"
    # Check if the file exists
    if (os.path.isfile(variables_path) and os.path.isfile(punches_path) and os.path.isfile(description_path) and os.path.isfile(must_clear_path) and os.path.isfile(current_week_path)):
        # Check that not tracking (this needs to be fixed, currently it only works on boot)
        global can_clear
        if (can_clear):
            # Reset all UI fields

            # Time Programming Fields
            programming_time_entries = app.weekly_daily_tabs.weekly_tab.programming_time_entries
            daily_punches_option_menus = app.weekly_daily_tabs.weekly_tab.daily_punches_option_menus
            for i in range(7):
                # Reset weekly entry arrays
                reset_entry(programming_time_entries[i], "00:00:00")
                daily_punches_option_menus[i].configure(values=["None"])

                # Reset weekly var arrays
                daily_programming_times[i] = 0
                daily_punches[i] = ["None"]

            # Description Field
            app.weekly_daily_tabs.weekly_tab.description_textbox.delete("1.0", "end-1c")
            placeholder_string = "INSTRUCTIONS:\n\n- Edit the .env file in the dist folder to include any discord webhooks that you want to send data to.\n\n- Use the Start Button in the Daily Tracker Tab to clock in.\n\n- Once you clock in, you'll have the option to pause or resume your session.\n\n- End your session by clicking the End Button\n\n- When you aren't in a session, you'll have the ability to Send Weekly Data and Clear Weekly Data.\n\n- Sending weekly data sends your data to the discord by using webhooks. Your data will be automatically formatted to be readable and will show what dates the week covered.\n\n- Clearing Weekly Data will erase everything and set it all back to default. This will mostly be used when you want to start a new week. Be sure to send your data before doing this.\n\n- The Walking and Pomodoro switches are options that you can add to your session.\n\n- Walking assumes you are walking on a treadmill at 2mph and tracks your distance, steps, and calories burned. Calories burned are determined by the weight that you enter in the Weekly Log Exercising Tab. \n\n- Pomodoro pauses and gives a notification everytime the timer runs out. The timers go as follows: 25, 5, 25, 5, 25, 5, 25, 15\n\n- You'll only be able to type in this text box when you're not in a session. Erasing these instructions and typing a new message will save your new message."        
            app.weekly_daily_tabs.weekly_tab.description_textbox.insert(0.0, placeholder_string)

            # Totals Fields
            reset_entry(app.totals_frame.time_programming_entry, "00:00:00")

            global total_programming_time
            global description
            global must_clear
            global current_week
            global curr_week_str

            total_programming_time = 0

            description = ""

            must_clear = False
            current_week = -1

            curr_week_str = ""
            
            # Reinitialze vars in json files like on first boot
            write_current_vars_to_variables_json()
            write_current_vars_to_punches_json()
            write_current_vars_to_description_json()
            write_current_vars_to_must_clear_json()
            write_current_vars_to_current_week_json()

            # Reset Variables in Memory in case user doesn't reboot program
            # Settings Vars
            global tracking
            global pomodoro_break
            global readytostart
            global paused
            global p_string_store
            global focus_time
            global break_time
            global long_break_time
            global p_focus_time
            global p_break_time
            global p_long_break_time
            global p_cycle_count
            global start_time
            global time_passed
            global timer_id

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
            curr_week_str = ""

            can_clear = True

            app.weekly_daily_tabs.daily_tab.start_end_button.configure(state="normal")

def send_data(webhook_arr, filename, text):
    if (webhook_arr == "None"):
        pass
    else:
        webhook_arr = webhook_arr.split(",")
        for i in webhook_arr:
            webhook_str = i

            webhook = discord.SyncWebhook.from_url('https://discord.com/api/webhooks/https://discord.com/api/webhooks/' + webhook_str)

            with open(file=filename, mode='rb') as f:
                my_file = discord.File(f)

            webhook.send(text, file=my_file)

def modal_setup(modal, width, height):
    if (operating_system == "Linux"):
        modal.wait_visibility()
    else:
        pass
    modal.grab_set()
    modal.geometry(f"{width}x{height}")
    modal.title("Send Data")
    if (operating_system == "Linux"):
        pass
    else:
        modal.after(250, lambda: modal.iconbitmap("icon4.ico"))
    center_window(modal, width, height)
    modal.grid_columnconfigure(0, weight=1)

def send_data_modal():
    modal_dialog = CTk.CTkToplevel(app)
    modal_setup(modal_dialog, 800, 490)

    # Display message as labels
    label = CTk.CTkLabel(modal_dialog, text="Preview of data to be sent:")
    label.grid(row=0, column=0, pady=(10,0))

    tab_view = CTk.CTkTabview(modal_dialog, fg_color="transparent")
    tab_view.add("Programming Data")
    tab_view.add("Exercise Data")
    tab_view.grid(row=1, column=0, columnspan=4, sticky="we")

    # Make correct week display if data is from previous week
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

    days_as_strings = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    # Write Programming Times
    programming_time_entries = app.weekly_daily_tabs.weekly_tab.programming_time_entries
    daily_punches_option_menus = app.weekly_daily_tabs.weekly_tab.daily_punches_option_menus
    programming_times_strings = []
    punches_times_strings = []
    for i in range(7):
        text_to_send += "\n" + days_as_strings[i] + " - Time Worked: "
        if (programming_time_entries[i].get() != ""):
            text_to_send += programming_time_entries[i].get()
            programming_times_strings.append(programming_time_entries[i].get())
        else:
            text_to_send += "00:00:00"
            programming_times_strings.append("00:00:00")
        text_to_send += ", Punches: "
        count = 0
        punches_str = ""
        for j in daily_punches_option_menus[i]._values:
            count += 1
            text_to_send += j
            punches_str += j
            if (count != len(daily_punches_option_menus[i]._values)):
                text_to_send += ", "
                punches_str += ", "
        punches_times_strings.append(punches_str)

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
    text_to_send += "\n\nDESCRIPTION:\n"
    description_str = ""
    if (description != ""):
        text_to_send += description
        description_str = description
    else:
        text_to_send += "No description given..."
        description_str = "No description given..."

    #Textbox to preview programming data that will be sent
    textbox = CTk.CTkTextbox(tab_view.tab("Programming Data"), wrap="word", height=350, width=750)
    textbox.pack()
    textbox.insert(1.0, text_to_send)
    textbox.configure(state="disabled")

    button_frame = CTk.CTkFrame(modal_dialog, fg_color="transparent")
    button_frame.grid(row=12, column=0, pady=(10,10))

    def send_code_data_and_close():
        with open('work.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            # Dates
            writer.writerow(["Dates"])
            writer.writerow([current_week_range])
            writer.writerow([""])
            # Time Worked Each Day
            writer.writerow(["Day of the Week", "Time Worked Each Day", "Punches for Each Day"])
            for i in range(7):
                writer.writerow([days_as_strings[i], programming_times_strings[i], punches_times_strings[i]])
            writer.writerow([""])
            # Total Time Worked
            writer.writerow(["Total Time Worked"])
            writer.writerow([total_str_time_worked])
            writer.writerow([""])
            # Description
            writer.writerow(["Description"])
            writer.writerow([description_str])

        load_dotenv(".env", override=True)
        webhook_arr = os.environ.get("Programming_Webhooks")
        send_data(webhook_arr, "work.csv", text_to_send)

        modal_dialog.destroy()

    button = CTk.CTkButton(button_frame, text="Send Work Data", command=send_code_data_and_close)
    button.grid(row=0, column=0, padx=(0,5))

    button = CTk.CTkButton(button_frame, text="Cancel", command=modal_dialog.destroy)
    button.grid(row=0, column=2, padx=(5,0))

    app.wait_window(modal_dialog)

def clear_data_modal():
    modal_dialog = CTk.CTkToplevel(app)
    modal_setup(modal_dialog, 400, 150)

    # Display message as labels
    first_label = CTk.CTkLabel(modal_dialog, text="Make sure that all data is sent beforehand.")
    first_label.grid(row=0, column=0)
    
    second_label = CTk.CTkLabel(modal_dialog, text="All data not sent will be permanently lost!")
    second_label.grid(row=1, column=0)

    third_label = CTk.CTkLabel(modal_dialog, text="Are you sure you want to clear your data?")
    third_label.grid(row=2, column=0)

    def clear_data_and_close():
        clear_data()
        modal_dialog.destroy()

    # Frame to display buttons side by side
    button_frame = CTk.CTkFrame(modal_dialog, fg_color="transparent")
    button_frame.grid(row=3, column=0, pady=(15,0))

    button = CTk.CTkButton(button_frame, text="Clear Data", command=clear_data_and_close)
    button.grid(row=0, column=0, padx=(0,5))

    button = CTk.CTkButton(button_frame, text="Cancel", command=modal_dialog.destroy)
    button.grid(row=0, column=1, padx=(5,0))

    app.wait_window(modal_dialog)

def new_week_modal():
    # Create modal differently based on operating system
    modal_dialog = CTk.CTkToplevel(app)
    modal_setup(modal_dialog, 750, 200)

    # Display message as labels
    first_label = CTk.CTkLabel(modal_dialog, text="You have been clocked out due to being clocked in during a new week without clearing first.")
    first_label.grid(row=0, column=0, pady=(15,0))

    second_label = CTk.CTkLabel(modal_dialog, text="Your program has been locked except for the description box, send weekly data button and clear weekly data button.")
    second_label.grid(row=1, column=0)

    third_label = CTk.CTkLabel(modal_dialog, text="Please send your data and then clear your data to unlock your program.")
    third_label.grid(row=2, column=0)
    
    fourth_label = CTk.CTkLabel(modal_dialog, text="All data not sent will be permanently lost!")
    fourth_label.grid(row=3, column=0)

    button = CTk.CTkButton(modal_dialog, text="Close", command=modal_dialog.destroy)
    button.grid(row=4, column=0, pady=(15,0))

    app.wait_window(modal_dialog)

class ProgrammingFrame(CTk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)

        global daily_programming_times
        global daily_punches

        # Title Label
        self.title = CTk.CTkLabel(self, text="Programming", fg_color="gray30")
        self.title.grid(row=0, column=0, columnspan=4, sticky="ew")
        
        # Category Labels
        category_labels = ["Time Programming", "Time Punches", "Description of Weekly Work Completed"]
        for i in range(3):
            label = CTk.CTkLabel(self, text=category_labels[i])
            label.grid(row=1, column=(i + 1))
        
        # Weekday Labels
        left_right_padding = 0
        if (operating_system == "Linux"):
            left_right_padding = 10
        else:
            left_right_padding = 12

        days_of_the_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        for i in range(7):
            label = CTk.CTkLabel(self, text=days_of_the_week[i])
            label.grid(row=(i + 2), column=0, padx=(left_right_padding, 5), sticky="w")
        
        # Weekday Hour Entries
        self.programming_time_entries = []
        for i in range(7):
            entry = CTk.CTkEntry(self, placeholder_text="00:00:00", justify="center")
            entry.configure(state="disabled")
            entry.grid(row=(i + 2), column=1, padx=(5, 5))

            if (daily_programming_times[i] != 0):
                programming_time_string = format_time_as_string_from_num(daily_programming_times[i])
                delete_and_insert_data_into_entry(entry, programming_time_string)

            self.programming_time_entries.append(entry)
        
        # Weekday Punches Option Menus
        self.daily_punches_option_menus = []
        for i in range(7):
            option_menu = CTk.CTkOptionMenu(self, values=daily_punches[i])
            option_menu.set("Punches")
            option_menu.grid(row=(i + 2), column=2, padx=(5, 5), pady=(5,5))
            # Taking out selected_option causes this to break. It may be a bug with customtkinter
            option_menu.configure(command=lambda selected_option="Punches", option_menu=option_menu: self.reset_option_menu(option_menu, selected_option))
            self.daily_punches_option_menus.append(option_menu)

        # Description Text Box
        self.description_textbox = CTk.CTkTextbox(self, width=440, height=258, wrap="word")
        self.description_textbox.grid(row=2, column=3, rowspan=7, padx=(5, left_right_padding))
        # Calls function to save description to json on each key press.
        self.description_textbox.bind("<KeyRelease>", self.save_description)

        # If description hasn't been edited, display instructions, else display edited text.
        placeholder_string = "INSTRUCTIONS:\n\n- Edit the .env file in the dist folder to include any discord webhooks that you want to send data to.\n\n- Use the Start Button in the Daily Tracker Tab to clock in.\n\n- Once you clock in, you'll have the option to pause or resume your session.\n\n- End your session by clicking the End Button\n\n- When you aren't in a session, you'll have the ability to Send Weekly Data and Clear Weekly Data.\n\n- Sending weekly data sends your data to the discord by using webhooks. Your data will be automatically formatted to be readable and will show what dates the week covered.\n\n- Clearing Weekly Data will erase everything and set it all back to default. This will mostly be used when you want to start a new week. Be sure to send your data before doing this.\n\n- The Walking and Pomodoro switches are options that you can add to your session.\n\n- Walking assumes you are walking on a treadmill at 2mph and tracks your distance, steps, and calories burned. Calories burned are determined by the weight that you enter in the Weekly Log Exercising Tab. \n\n- Pomodoro pauses and gives a notification everytime the timer runs out. The timers go as follows: 25, 5, 25, 5, 25, 5, 25, 15\n\n- You'll only be able to type in this text box when you're not in a session. Erasing these instructions and typing a new message will save your new message."        
        if (description != ""):
            self.description_textbox.insert(1.0, description)
        else:
            self.description_textbox.insert(0.0, placeholder_string)

    # Sets Option Menus back to "Punches" after they've been changed. Taking out selected option causes this to break. It may be a bug with customtkinter.
    def reset_option_menu(self, option_menu, selected_option):
        option_menu.set("Punches")

    def save_description(self, event):
        global description
        description = app.weekly_daily_tabs.weekly_tab.description_textbox.get("1.0", "end-1c")
        write_current_vars_to_description_json()

class DailyFrame(CTk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)

        # Adjust UI based on operating system
        timer_font_size = 0
        top_padding = 0
        bottom_padding = 0
        
        if (operating_system == "Linux"):
            timer_font_size = 58
            top_padding = 54
            bottom_padding = 64
        else:
            timer_font_size = 75
            top_padding = 55
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

        self.pomodoro_switch = CTk.CTkSwitch(self, text="Pomodoro")
        self.pomodoro_switch.grid(row=3, column=0, rowspan=2, padx=(50,0), pady=(0, 55))

        # Buttons for start/end and resume/pause
        self.start_end_button = CTk.CTkButton(self, text="Start", command=start_end)
        self.start_end_button.grid(row=3, column=1, pady=(10, 0))

        if (must_clear):
            self.start_end_button.configure(state="disabled")

        self.pause_resume_button = CTk.CTkButton(self, text="Pause", state="disabled", command=pause_resume)
        self.pause_resume_button.grid(row=4, column=1, pady=(10,bottom_padding))

class WeeklyDailyTabs(CTk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # create tabs
        self.add("Weekly Log")
        self.add("Daily Tracker")

        # Add Frames to tabs
        self.weekly_tab = ProgrammingFrame(self.tab("Weekly Log"))
        self.weekly_tab.grid(row=0, column=0)

        self.daily_tab = DailyFrame(self.tab("Daily Tracker"))
        self.daily_tab.grid(row=0, column=0)

class TotalsFrame(CTk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)

        global total_programming_time
        
        # Title Label
        self.title = CTk.CTkLabel(self, text="Total", fg_color="gray30")
        self.title.grid(row=0, column=0, columnspan=6, sticky="ew")
        
        # Category Labels
        self.time_programming_label = CTk.CTkLabel(self, text="Time Worked")
        self.time_programming_label.grid(row=1, column=1, padx=(380, 380))
        
        # Total Time Programming Entry
        self.time_programming_entry = CTk.CTkEntry(self, placeholder_text="00:00:00", justify="center")
        self.time_programming_entry.configure(state="disabled")
        self.time_programming_entry.grid(row=2, column=1, padx=(108, 108), pady=(5,5))

        if (total_programming_time != 0):
            programming_time_string = format_time_as_string_from_num(total_programming_time)
            delete_and_insert_data_into_entry(self.time_programming_entry, programming_time_string)

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

class App(CTk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Productivity Tracker")

        # Use different method to set icon based on operating system
        if (operating_system == "Linux"):
            self.iconphoto(False, PhotoImage(file='icon4-2.png'))
        else:
            self.iconbitmap("icon4.ico")
        
        # Define Window Size and Behavior
        window_width = 920
        window_height = 635
        self.geometry(f"{window_width}x{window_height}")
        center_window(self, window_width, window_height)
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

        # # Add Content for weekly totals
        self.totals_frame = TotalsFrame(self)
        self.totals_frame.grid(row=2, column=0, padx=10)

        # #Add Buttons
        self.buttons_frame = ButtonsFrame(self)
        self.buttons_frame.grid(row=3, column=0)

#Run app in dark mode
get_operating_system()
CTk.set_appearance_mode("dark")
color = ""
if (operating_system == "Linux"):
    color = "green"
else:
    color = "dark-blue"
CTk.set_default_color_theme(color)

# Run App
app = App()
app.mainloop()