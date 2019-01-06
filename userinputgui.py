import tkinter as tk

'''
This function is used to build the GUI used to enter information
about the user being added to the LDAP.
'''


def gui(window):

    window.title("Add a user to the LDAP")

    ############################
    #      LEFT COLUMN         #
    ############################

    # First Name
    first_name = tk.Label(window, text="First Name")
    first_name.grid(column=0, row=0, padx=(20, 0), pady=(20, 0))
    first_name_entry = tk.Entry(window)
    first_name_entry.grid(column=0, row=1, padx=(20, 0), pady=(20, 0))

    # Last Name
    last_name = tk.Label(window, text="Last Name")
    last_name.grid(column=0, row=2, padx=(20, 0), pady=(20, 0))
    last_name_entry = tk.Entry(window)
    last_name_entry.grid(column=0, row=3, padx=(20, 0), pady=(20, 0))

    # User Name
    user_name = tk.Label(window, text="User Name")
    user_name.grid(column=0, row=4, padx=(20, 0), pady=(20, 0))
    user_name_entry = tk.Entry(window)
    user_name_entry.grid(column=0, row=5, padx=(20, 0), pady=(20, 0))

    ############################
    #      RIGHT COLUMN        #
    ############################

    # Enter Password
    enter_password = tk.Label(window, text="Enter Password")
    enter_password.grid(column=3, row=0, padx=(0, 20), pady=(20, 0))
    enter_password_entry = tk.Entry(window, show="*")
    enter_password_entry.grid(column=3, row=1, padx=(0, 20), pady=(20, 0))

    # Verify Password
    verify_password = tk.Label(window, text="Verify Password")
    verify_password.grid(column=3, row=2, padx=(0, 20), pady=(20, 0))
    verify_password_entry = tk.Entry(window, show="*")
    verify_password_entry.grid(column=3, row=3, padx=(0, 20), pady=(20, 0))

    # Admin Password
    admin_password = tk.Label(window, text="LDAP Admin Password")
    admin_password.grid(column=3, row=4, padx=(0, 20), pady=(20, 0))
    admin_password_entry = tk.Entry(window, show="*")
    admin_password_entry.grid(column=3, row=5, padx=(0, 20), pady=(20, 0))

    ############################
    #     ADD USER BUTTON      #
    ############################

    # Add user button - We need the lambda function because we are passing in parameters
    btn = tk.Button(window, text="Add User", command=lambda: add_user_button_pressed(first_name_entry,
                                                                                     last_name_entry,
                                                                                     user_name_entry,
                                                                                     enter_password_entry,
                                                                                     verify_password_entry,
                                                                                     admin_password_entry))
    btn.grid(column=2, row=6, padx=(20, 20), pady=(20, 20))

    return window


'''
This function is called when a user hits the "Add User" button
in the GUI. It will verify the passwords match. If so, it will
add the user. Otherwise, it will prompt the user of the issue
and return them to the gui.
'''


def add_user_button_pressed(fn, ln, un, pw, vp, ap):

    # If the passwords don't match, let the user know!
    if pw.get() != vp.get():
        popup_window = tk.Tk()
        popup_window.wm_title("Password Error")
        popup_label = tk.Label(popup_window, text="Passwords Don't Match. Try again!")
        popup_label.grid(column=0, row=0, padx=(20, 20), pady=(20, 20))
        popup_button = tk.Button(popup_window, text="Okay", command=popup_window.destroy)
        popup_button.grid(column=0, row=1, padx=(20, 20), pady=(20, 20))

    # TODO add the check to see if all fields are full
        


'''
Main driver that builds and launches the gui
'''


if __name__ == "__main__":
    inputWindow = tk.Tk()
    inputWindow = gui(inputWindow)
    inputWindow.mainloop()

