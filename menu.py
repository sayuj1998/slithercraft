from tkinter import *
import subprocess

def easy_mode():
    subprocess.run(["python", "easymode.py"])

def medium_mode():
    subprocess.run(["python", "medium.py"])

def nightmare_mode():
    subprocess.run(["python", "nightmare.py"])

def instructions():
    pass

def exit_game():
    pass

def center_window(window, width, height):
    """Making it launch in the middle of the screen"""
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x}+{y}")

def buttons(window):
    """Buttons for the main menu"""
    button_bg = "#3498db"
    button_fg = "#ffffff"
    button_font = ("Arial", 20, "bold")

    button_width = 15
    button_height = 2

    easy_button = Button(window, text="Easy", font=button_font, fg=button_fg, bg="#013220", width=button_width, height=button_height, command=easy_mode)
    easy_button.pack(pady=15)

    medium_button = Button(window, text="Medium", font=button_font, fg=button_fg, bg="#9b870c", width=button_width, height=button_height, command=medium_mode)
    medium_button.pack(pady=15)

    nightmare_button = Button(window, text="Nightmare", font=button_font, fg=button_fg, bg="#8b0000", width=button_width, height=button_height, command=nightmare_mode)
    nightmare_button.pack(pady=15)

    instructions_button = Button(window, text="How To Play", font=button_font, fg=button_fg, bg=button_bg, width=button_width, height=button_height, command=instructions)
    instructions_button.pack(pady=15)

    exit_button = Button(window, text="Exit", font=button_font, fg=button_fg, bg=button_bg, width=button_width, height=button_height, command=exit_game)
    exit_button.pack(pady=15)

def main():
    "Main menu frontend"
    game_window_width = 1500
    game_window_height = 900

    window = Tk()
    window.title("SlitherCraft")
    window.configure(bg="#000000")

    center_window(window, game_window_width, game_window_height)

    title_frame = Frame(window, bg="#000000", bd=1, relief="solid", highlightbackground="#66ff00", highlightthickness=1)
    title_frame.pack(pady=(80, 40))

    title_label = Label(title_frame, text="SlitherCraft", font=("Arial", 60, "bold"), fg="#66ff00", bg="#000000")
    title_label.pack(pady=(10, 40))

    buttons(title_frame)

    window.mainloop()

if __name__ == "__main__":
    main()
