# TODO: Implement number_of_people = x and make x and negative so for whatever x is it'd take x off venue capacity.
# When venue capcity reaches <= 0 deny that or further requests (if at 0 already)
#MARKERS READ:
#TODO: pip3 install <<Module>> for function to work

# Where tkinter is transferred over
from tkinter import *
import tkinter as tk
from tkcalendar import DateEntry
# import os for test cases (massive help from my dad)
import os
# import regex for email validation (learned this from dad)
import re
# import tkinter as ttk
# from ttk import *
# CONSTANTS = integer for basic boundries.
VENUE_DATA = {
  "Coastlands Theatre": 331,
  "Blackbox Theatre": 200,
  "Music Room": 50
}

# Destroys the main window closing everything down as a result excluding the shell, just the body gets shut off
def quit():
    main_window.destroy()

# print_names
def print_names():
    global events_list
    table_header = 10
    table_body = 11
    Label(main_window, font='bold', text="Row").grid(             column=0, row=table_header)
    Label(main_window, font='bold', text="Name").grid(            column=1, row=table_header)
    Label(main_window, font='bold', text="Number of People").grid(column=2, row=table_header)
    Label(main_window, font='bold', text="Email").grid(           column=4, row=table_header)
    Label(main_window, font='bold', text="Venue").grid(           column=6, row=table_header)
    Label(main_window, font='bold', text="Date").grid(            column=8, row=table_header)

    print ("events list", events_list)
    # The Output
    for entry_index, entry in enumerate(events_list):
        print ("entry", entry)
        # RowNum - Done
        Label(main_window, text=entry_index).grid(column=0, row=table_body+entry_index)
        # Name - Done
        Label(main_window, text=entry['name']).grid(
            column=1, row=table_body+entry_index)
        # no of people
        Label(main_window, text=entry['peeps']).grid(
            column=2, row=table_body+entry_index)
        # Email - Done
        Label(main_window, text=entry['email']).grid(
            column=4, row=table_body+entry_index)
        # Venue
        Label(main_window, text=entry['venue']).grid(
            column=6, row=table_body+entry_index)
        #FIXME: Date - wip | opt | y?: ver if it's in present or near future
        # SOLVED: Just update it manually to solve the probelm. As this project isn't requesting an advanced solution to fix the problem, this includes the where the errors lie, as the method used is a general error, so it'll just prevent anything going forward. You could modify it just stating 'Please re-check if you've entered the values correctly.
        Label(main_window, text=entry['date']).grid(
            column=8, row=table_body+entry_index)

# The calendar function shows the calander when clicked (acts as a widgit)
def tk_calendar(): #
    global cal
    cal = DateEntry(main_window, width=12, year=2021, month=5, day=12,
    background='darkblue', foreground='white', borderwidth=2)
    cal.grid(column = 1, row = 8)

# def allow_numbers_only(action, index, value_if_allowed,
#                     prior_value, text, validation_type, trigger_type, widget_name):

#     print("key pressed", value_if_allowed)
#     if value_if_allowed:
#         try:
#             int(value_if_allowed)
#             return True
#         except ValueError:
#             return False
#     else:
#         return False

# Function that creates a drop box for the venues
def venue_locations():
    global venue_locations
    # Create a Tkinter variable
    venue_locations = StringVar()

    # Dictionary with options on venue locations
    choices = list(VENUE_DATA.keys())
    venue_locations.set('Venue')  # set the default option

    popupMenu = OptionMenu(main_window, venue_locations, *choices)
    popupMenu.grid(row=6, column=1)

# used as blueprint till found something better.
def validation():

    global input_errors
    input_errors = []
    if (name_validation(customer.get()) == False):
        input_errors.append('Name is invalid')

    if (email_validation(entry_email.get()) == False):
        input_errors.append('Email is invalid')

    peeps = entry_people_counter.get()
    if (peeps_validation(peeps) == False):
        input_errors.append('Not a number')
    else:
        # only do capacity validation, if entry_people_counter is a number
        if (venue_capacity_validation(venue_locations.get(), peeps) == False):
            input_errors.append('Capacity mismatch')

    return (len(input_errors) == 0)

# Fancy way of validating the Email
# NOTE: Use <-- Issue lies here next to where the issue is, and highlight the box red until selected

# Checks if email is written like an email ie@gmail.com
def email_validation(email_address):
    # A method on seeing whether or not a email is valid and plausable or not.
    # NOTE: It DOESN'T VERIFY IF THE EMAIL IS REAL, as companies tend to send an confirmation/verfication email
    # To the Inputed email through a different function. When you click that verify through that email it'll mark that email as
    # real and verified!
    match = re.match(
        '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email_address, re.IGNORECASE)

    if match == None:
        # print('Bad Syntax')
        # raise ValueError('Bad Syntax')
        # TODO: Make it so it displays where the error(s) are located for email i.e. missing @, or fullstop.
        # You need more advanced functions for that to work
        return False
    else:
        return True

# Checks if the name is writtin in alphabet
def name_validation(customer_name):
    if (customer_name.isalpha() and (len(customer_name) > 1)):
        return True
    elif (customer_name.replace(' ', '').replace('.', '').isalpha() and (len(customer_name) > 1)):
        return True
    else:
        return False

# Appends data to events_list
def append_request():
    if (True == validation()):
        append_name()
        clear_form()
    else:
        print('Input Errors')
        print(input_errors)

    print('Events List')
    print(events_list)

def peeps_validation(no_of_people):
    try:
        int(no_of_people)
        return True
    except ValueError:
        return False

def venue_capacity_validation(venue_name,peeps):
    venue_limit = int(VENUE_DATA[venue_name])
    print('venue name', venue_name)
    print('venue limit', venue_limit)
    print('peeps', peeps)
    if (int(peeps) > venue_limit):
        return False
    else:
        return True


# Appending names to the events_list
def append_name():
    global events_list, customer, entry_people_counter, entry_email,venue_locations, cal

    event_entry = {
        'name': customer.get(),
        'peeps': entry_people_counter.get(),
        'email': entry_email.get(),
        'venue': venue_locations.get(),
        'date': cal.get()
    }
    events_list.append(event_entry)
    print(events_list)

# self explanatory
def clear_form():
    customer.delete(0, 'end')
    entry_people_counter.delete(0, 'end')
    entry_email.delete(0, 'end')
# 

# def character_limit(entry_text):
#     if len(entry_people_counter.get()) < 2:
#         entry_people_counter.set(entry_text.get()[-1])

# NOTE: I cannot clean list after deleting a row, since I'm lacking more advanced techniques like classes among others
# self explanatory 
def delete_row(row_index):
    print("row_index", row_index)
    global events_list
    del events_list[int(row_index)]
    print_names()

# where the button hub is located (where all buttons are located)

def setup_buttons():
    global events_list, customer, entry_people_counter, entry_email
    Button(main_window, text="Quit", command=quit) .grid(column=0, row=1)
    Button(main_window, text="Submit Request",
           command=append_request) .grid(column=1, row=1)
    Button(main_window, text="Print all Requests",
           command=print_names) .grid(column=2, row=1)
    Label(main_window, text="Customer") .grid(column=0, row=2)
    customer = Entry(main_window)
    customer.grid(column=1, row=2)
    Label(main_window, text="Number of People") .grid(column=0, row=3)

    # validate_cmd = (main_window.register(allow_numbers_only),
    #             '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
    # entry_people_counter = Entry(main_window, validate = 'key', validatecommand = validate_cmd)
    entry_people_counter = Entry(main_window)
    entry_people_counter.grid(column=1, row=3)

    Label(main_window, text="Email") .grid(column=0, row=4)
    entry_email = Entry(main_window)
    entry_email.grid(column=1, row=4)
    Label(main_window, text="Row#") .grid(column=0, row=9)

    delete_row_entry = Entry(main_window)
    delete_row_entry.grid(column=1, row=9)
    Button(main_window, text="Delete",
           command= lambda: delete_row(delete_row_entry.get())) .grid(column=2, row=9)



# The body where everything will be house like setup_buttons() and the main_window
def main():
    global main_window
    global events_list, customer, entry_people_counter, entry_email
    events_list = []
    main_window = Tk()
    main_window.title("Main Body")
    # Button(main_window, text="date", command=tk_calendar).grid()
    setup_buttons()
    tk_calendar()
    venue_locations()

    # Limits the size of the window so it's unable to take up the entire screen so it's  more compact
    main_window.minsize(550, 530)
    main_window.maxsize(1000, 980)
    main_window.mainloop()


if __name__ == '__main__':
    main()

# NOTE(S): Indentation error is spaces/tabs from the right either too many or too little
# NOTE: I'm well aware that re-adding globals like customer, entry_people_counter and more is rather pointless and only needed to be added once
# however I just used premade ones that I made prior to the assessments during class time so they had this, but even then it was more of a framework
# apologies to full-time coders as this may harm your brain and eyes.