import tkinter as tk
import time
import pygame

class Countdown:
    def __init__(self, master, seconds, title):
        self.master = master
        self.seconds = seconds
        self.title = title
        self.label = tk.Label(self.master, text="", font=("Helvetica", 20))
        self.label.pack()
        self.remaining = 0
        self.paused = False
        self.countdown()

    def countdown(self):
        if self.seconds <= 0:
            pygame.mixer.music.stop()
            self.label.configure(text=self.title + " Time's up!")
        elif self.paused:
            self.remaining = self.master.after(1000, self.countdown)
        else:
            self.label.configure(text=self.title + " - %d seconds remaining" % self.seconds)
            self.seconds -= 1
            self.remaining = self.master.after(1000, self.countdown)

    def stop(self):
        pygame.mixer.music.stop()
        self.master.after_cancel(self.remaining)
        self.label.configure(text=self.title + " Countdown stopped")
        button.config(text="Resume", command=self.resume)
        self.paused = True

    def resume(self):
        button.config(text="Stop", command=self.stop)
        self.paused = False
        self.countdown()
        pygame.mixer.music.play()

def start_countdown():
    try:
        seconds = int(seconds_entry.get())
        title = title_entry.get()
        countdown = Countdown(root, seconds, title)
        button.config(text="Stop", command=countdown.stop)

        pygame.mixer.init()
        pygame.mixer.music.load("relaxing_music.mp3")
        pygame.mixer.music.play(-1)
    except ValueError:
        tk.messagebox.showerror("Error", "Please enter a valid number of seconds.")

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Countdown Timer")

    title_label = tk.Label(root, text="Title: ")
    title_label.pack(side="left")

    title_entry = tk.Entry(root, width=20)
    title_entry.pack(side="left")

    seconds_label = tk.Label(root, text="Seconds: ")
    seconds_label.pack(side="left")

    seconds_entry = tk.Entry(root, width=10)
    seconds_entry.pack(side="left")

    button = tk.Button(root, text="Start", command=start_countdown)
    button.pack()

    root.mainloop()
