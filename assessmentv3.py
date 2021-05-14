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
    global events_list, total_entries, name_count
    name_count = 0
    Label(main_window, font='bold', text="Row").grid(             column=0, row=10)
    Label(main_window, font='bold', text="Name").grid(            column=1, row=10)
    Label(main_window, font='bold', text="Number of People").grid(column=2, row=10)
    Label(main_window, font='bold', text="Email").grid(           column=4, row=10)
    Label(main_window, font='bold', text="Venue").grid(           column=6, row=10)
    Label(main_window, font='bold', text="Date").grid(            column=8, row=10)
    # The Output
    while name_count < total_entries:
        # RowNum - Done
        Label(main_window, text=name_count).grid(column=0, row=name_count+8)
        # Name - Done
        Label(main_window, text=(events_list[name_count][0])).grid(
            column=1, row=name_count+11)
        #TODO: num of peps- wip | y?: ver if int < 10 , > 0
        Label(main_window, text=(events_list[name_count][1])).grid(
            column=2, row=name_count+11)
        # Email - Done
        Label(main_window, text=(events_list[name_count][2])).grid(
            column=4, row=name_count+11)
        #FIXME: Venue - wip | y?: ver if it exceeds the capcity limit ()
        Label(main_window, text=(events_list[name_count][3])).grid(
            column=6, row=name_count+11)
        #FIXME: Date - wip | opt | y?: ver if it's in present or near future
        # SOLVED: Just update it manually to solve the probelm. As this project isn't requesting an advanced solution to fix the problem, this includes the where the errors lie, as the method used is a general error, so it'll just prevent anything going forward. You could modify it just stating 'Please re-check if you've entered the values correctly.
        Label(main_window, text=(events_list[name_count][4])).grid(
            column=8, row=name_count+11)
        name_count += 1

# The calendar function shows the calander when clicked (acts as a widgit)
def tk_calendar(): #
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
# Function that creates a drop box for the veubes
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
    global events_list, customer, entry_people_counter, entry_email, total_entries,venue_locations
    events_list.append(
        [customer.get(), int(entry_people_counter.get()), entry_email.get(), venue_locations.get()])
    customer.delete(0, 'end')
    entry_people_counter.delete(0, 'end')
    entry_email.delete(0, 'end')

    total_entries += 1
    print(events_list)

# def character_limit(entry_text):
#     if len(entry_people_counter.get()) < 2:
#         entry_people_counter.set(entry_text.get()[-1])

# Deletes a row of information depending on the inputed interger.
def delete_row():
    global events_list, delete_row, total_entries
    del events_list[int(delete_row.get())]
    total_entries = total_entries = 1
    delete_row.delete(0, 'end')
    print_names()

# where the button hub is located (where all buttons are located)


def setup_buttons():
    global events_list, customer, entry_people_counter, entry_email, total_entries
    Button(main_window, text="Quit", command=quit) .grid(column=0, row=1)
    Button(main_window, text="Submit Request",
           command=append_request) .grid(column=1, row=1)
    Button(main_window, text="Print all Requests",
           command=print_names) .grid(column=2, row=1)
    Button(main_window, text="Delete",
           command=delete_row) .grid(column=2, row=9)
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
    entry_row = Entry(main_window)
    entry_row.grid(column=1, row=9)



# The body where everything will be house like setup_buttons() and the main_window
def main():
    global main_window
    global events_list, customer, entry_people_counter, entry_email, total_entries
    events_list = []
    total_entries = 0
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