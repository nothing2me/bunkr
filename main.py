from tkinter import *
from encryptbunkr import encrypt_message, check_master_key_exists, return_user, return_pass
import time


# Centers the window being passed
def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))


# Counts the number of lines in the database to display in the main menu
def update_login_count(line_count_text):
    counter = 0
    try:
        with open("database.txt", "r") as database_file:
            for line in database_file:
                counter += 1
    except FileNotFoundError:
        counter = 0
    line_count_text.set(str(counter))


def window_login_menu():
    # Retrieves credentials
    def get_login_credentials():
        username = get_username.get()
        password = get_password.get()

        encryption_key = check_master_key_exists()

        encrypted_user = encrypt_message(username, encryption_key)
        encrypted_password = encrypt_message(password, encryption_key)

        try:
            decrypted_user = return_user(encryption_key)
            decrypted_pass = return_pass(encryption_key)
        except Exception as e:
            decrypted_user, decrypted_pass = None, None

        if decrypted_user is None or decrypted_pass is None:
            with open("master.txt", "wb") as f:
                f.write(encrypted_user + b'\n')
                f.write(encrypted_password + b'\n')
            print("Credentials saved.")
            notification_label = Label(settings_frame, text="Credentials Saved", font=("Jacquard 12", 15, "bold"),
                                       fg="#ebebeb",
                                       bg="#3d3c3c")
            notification_label.pack(anchor=CENTER, pady=2, padx=13)
            time.sleep(4)  # Display credentials saved text before transitioning to new window
            return 1

        elif decrypted_user == username and decrypted_pass == password:
            print("Logged in successfully")
            print("Username:", decrypted_user)
            print("Password:", decrypted_pass)
            return 1
        else:
            warning_label = Label(settings_frame, text="Incorrect username or password.",
                                  font=("Jacquard 12", 15, "bold"), fg="#ebebeb", bg="#3d3c3c")
            warning_label.pack(anchor=CENTER, pady=2, padx=13)
            print("Incorrect username or password.")

    # Exit the login menu and pass on to the main menu if
    # the login was successful
    def login_successful():
        status = get_login_credentials()
        if status == 1:
            # Destroy the login and show the main menu
            login_menu.destroy()
            window_main_menu()

    # Create the Tkinter window
    login_menu = Tk()
    login_menu.geometry("500x350")
    login_menu.title("Bunkr")
    login_menu.iconbitmap("assets/bunkrlogo.ico")
    login_menu.configure(background='#3d3c3c')

    # Center the window
    center_window(login_menu)

    # Create a frame to act as padding with a different color
    padding_frame = Frame(login_menu, bg="#4d4c4c")
    padding_frame.pack(fill=BOTH, padx=20, pady=20, expand=True)

    # Create the settings frame inside the padding frame
    settings_frame = Frame(padding_frame, bg="#3d3c3c")
    settings_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

    # Header
    label = Label(settings_frame, text="Bunkr Login:", font=("Jacquard 12", 30, "bold"), fg="#ebebeb", bg="#3d3c3c",
                  anchor=CENTER)
    label.pack(side=TOP, pady=(10, 0))

    # Username Entry
    label = Label(settings_frame, text="Enter Username:", font=("Jersey 15", 18), fg="#ebebeb", bg="#3d3c3c")
    label.pack(anchor=CENTER, pady=(0, 10))
    get_username = Entry(settings_frame, width=30)
    get_username.pack(anchor=CENTER)

    # Password Entry
    label = Label(settings_frame, text="Enter Password:", font=("Jersey 15", 18), fg="#ebebeb", bg="#3d3c3c")
    label.pack(anchor=CENTER, pady=(10, 10))
    get_password = Entry(settings_frame, width=30)
    get_password.pack(anchor=CENTER)

    # Create the button
    button = Button(settings_frame, text="Enter", font=("Jersey 15", 15), width=10, command=login_successful,
                    bg='#8360a8', fg='#dedede')
    # Place the button below the feedback label
    button.pack(anchor=CENTER, pady=(20, 10))

    # Call to loop
    login_menu.mainloop()

    # Close the root window
    login_menu.destroy()


# The main menu
def window_main_menu():
    # Menu pages
    def view_logins():
        def exit_logins():
            show_logins.destroy()
            window_main_menu()

        main_menu.destroy()
        show_logins = Tk()
        show_logins.geometry("700x350")
        show_logins.title("Bunkr")
        show_logins.configure(background='#3d3c3c')
        show_logins.iconbitmap("assets/bunkrlogo.ico")

        # Center the window
        center_window(show_logins)

        # Create a frame to act as padding with a different color
        back_padding_frame = Frame(show_logins, bg="#4d4c4c", width=400, height=400)
        back_padding_frame.pack(padx=20, pady=20)

        back_button = Button(back_padding_frame, text="Back", font=("Jersey 15", 13), bg="#7e68a8", command=exit_logins)
        back_button.pack(side=LEFT, padx=10, pady=10)  # Controls vertical pad for whole bar

    def add_logins():
        def exit_logins():
            add_logins.destroy()
            window_main_menu()

        main_menu.destroy()
        add_logins = Tk()
        add_logins.geometry("700x350")
        add_logins.title("Bunkr")
        add_logins.configure(background='#3d3c3c')
        add_logins.iconbitmap("assets/bunkrlogo.ico")

        # Center the window
        center_window(add_logins)

        # Create a frame to act as padding with a different color
        back_padding_frame = Frame(add_logins, bg="#4d4c4c", width=400, height=400)
        back_padding_frame.pack(padx=20, pady=20)

        back_button = Button(back_padding_frame, text="Back", font=("Jersey 15", 13), bg="#7e68a8", command=exit_logins)
        back_button.pack(side=LEFT, padx=10, pady=10)  # Controls vertical pad for whole bar

    def view_logs():
        def exit_logs():
            view_logs.destroy()
            window_main_menu()

        main_menu.destroy()
        view_logs = Tk()
        view_logs.geometry("700x350")
        view_logs.title("Bunkr")
        view_logs.configure(background='#3d3c3c')
        view_logs.iconbitmap("assets/bunkrlogo.ico")
        # Center the window
        center_window(view_logs)

        # Create a frame to act as padding with a different color
        back_padding_frame = Frame(view_logs, bg="#4d4c4c", width=400, height=400)
        back_padding_frame.pack(padx=20, pady=20)

        back_button = Button(back_padding_frame, text="Back", font=("Jersey 15", 13), bg="#7e68a8", command=exit_logs)
        back_button.pack(side=LEFT, padx=10, pady=10)  # Controls vertical pad for whole bar

    # Help Window
    def view_help():
        def exit_help():
            view_help.destroy()

        view_help = Toplevel()  # Create a new top-level window
        view_help.geometry("300x450")
        view_help.title("Bunkr Help Menu")
        view_help.configure(background='#3d3c3c')
        view_help.iconbitmap("assets/bunkrlogo.ico")

        # Create a frame to act as padding with a different color
        back_padding_frame = Frame(view_help, bg="#4d4c4c", width=400, height=400)
        back_padding_frame.pack(padx=20, pady=20)

        back_button = Button(back_padding_frame, text="Back", font=("Jersey 15", 13), bg="#7e68a8", command=exit_help)
        back_button.pack(side=LEFT, padx=10, pady=10)  # Controls vertical pad for whole bar

        # Create a frame to act as padding with a different color
        paragraph_padding_frame = Frame(view_help, bg="#4d4c4c")
        paragraph_padding_frame.pack(fill=BOTH, padx=5, pady=5, expand=True)

        # Create the settings frame inside the padding frame
        settings_frame = Frame(paragraph_padding_frame, bg="#3d3c3c")
        settings_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # Define your paragraph text
        paragraph = """
        Home - \nShows usage statistics\n
        View Logins - \nDisplays all stored logins\n
        Add Logins - \nAdd a new login \nto the database\n
        Export Data - \nExport a backup of database
        """

        # Create the label with left anchor and set the text
        label = Label(paragraph_padding_frame, text=paragraph, font=("Jersey 15", 15), bg="#3d3c3c", fg="white",
                      padx=.1, pady=.1)
        label.place(relx=0.125, rely=0.5, anchor='w')

        # Main loop
        view_help.mainloop()

    # Export Data Window
    def export_data():
        def exit_export_data():
            export_data.destroy()
            window_main_menu()

        main_menu.destroy()
        export_data = Tk()
        export_data.geometry("700x350")
        export_data.title("Bunkr")
        export_data.configure(background='#3d3c3c')
        export_data.iconbitmap("assets/bunkrlogo.ico")

        # Center the window
        center_window(export_data)

        # Create a frame to act as padding with a different color
        back_padding_frame = Frame(export_data, bg="#4d4c4c", width=400, height=400)
        back_padding_frame.pack(padx=20, pady=20)

        back_button = Button(back_padding_frame, text="Back", font=("Jersey 15", 13), bg="#7e68a8",
                             command=exit_export_data)
        back_button.pack(side=LEFT, padx=10, pady=10)  # Controls vertical pad for whole bar

    def destroy_all_windows():
        for window in main_menu.winfo_children():
            window.destroy()
        main_menu.destroy()
        window_login_menu()

    # Create the main window
    main_menu = Tk()
    main_menu.iconbitmap("assets/bunkrlogo.ico")
    main_menu.geometry("700x350")
    main_menu.title("Bunkr")
    main_menu.configure(background='#3d3c3c')

    # Center the window
    center_window(main_menu)

    # Create a frame to act as padding with a different color
    padding_frame = Frame(main_menu, bg="#4d4c4c", width=400, height=400)
    padding_frame.pack(padx=20, pady=20)

    # Create buttons for the menu bar
    home_button = Button(padding_frame, text="Home", font=("Montserrat Light", 10), bg="#7e68a8")
    home_button.pack(side=LEFT, padx=10, pady=10)  # Controls vertical pad for whole bar

    view_passwords_button = Button(padding_frame, text="View Logins", font=("Montserrat Light", 10),
                                   command=view_logins)
    view_passwords_button.pack(side=LEFT, padx=10)

    add_login_button = Button(padding_frame, text="Add Logins", font=("Montserrat Light", 10), command=add_logins)
    add_login_button.pack(side=LEFT, padx=10)

    remove_login_button = Button(padding_frame, text="View Logs", font=("Montserrat Light", 10), command=view_logs)
    remove_login_button.pack(side=LEFT, padx=10)

    export_data_button = Button(padding_frame, text="Export Data", font=("Montserrat Light", 10), command=export_data)
    export_data_button.pack(side=LEFT, padx=10)

    help_button = Button(padding_frame, text="Help", font=("Montserrat Light", 10), command=view_help)
    help_button.pack(side=LEFT, padx=10)

    logins_stored_frame = Frame(main_menu, bg="#4d4c4c", width=275, height=80)
    logins_stored_frame.pack(padx=20, pady=20)
    logins_stored_frame.place(relx=0.03, rely=0.25)

    # Create a label for the main content area
    logins_stored_content_label = Label(logins_stored_frame, text="Logins Stored:", font=("Montserrat Light", 16),
                                        fg="white",
                                        bg="#4d4c4c", justify="left")
    logins_stored_content_label.place(relx=0.05, rely=0.03)

    # Create a frame for the file selection elements
    linecount_frame = Frame(main_menu, bg="#3d3c3c", height=10)
    linecount_frame.place(relx=0.285, rely=0.276)

    # Text variable to store the line count string
    line_count_text = StringVar()
    line_count_text.set("0")

    # Label to display the line count
    line_count_label = Label(linecount_frame, textvariable=line_count_text, font=("Montserrat Light", 30), bg="#3d3c3c",
                             fg="white", )
    line_count_label.pack()

    # Button to trigger line count with command set to call line_count_text function
    count_button = Button(logins_stored_frame, text="Update Login Count", font=("Montserrat Light", 10),
                          command=lambda: update_login_count(line_count_text))
    count_button.place(relx=0.069, rely=0.45)

    # Footer text
    version_label = Label(main_menu, text="Bunkr-Password-Manager Pre-Alpha 0.0.1", font=("Montserrat Light", 10),
                          bg="#3d3c3c", fg="white", )
    version_label.place(relx=0.01, rely=0.91)

    # Initial call to update the login count
    update_login_count(line_count_text)

    # Force relog after 90 seconds
    main_menu.after(90000, destroy_all_windows)

    # Run the main event loop
    main_menu.mainloop()


def main():
    # Login menu transitions to main menu
    window_login_menu()


if __name__ == '__main__':
    main()
