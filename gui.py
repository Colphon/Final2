from tkinter import *
from tkinter.ttk import Progressbar

class Gui:
    def __init__(self, window: Tk):

        self.window = window

# Initialize counters, checks, and modifiers
        self.give_counter, self.pet_counter, self.walk_counter = 0, 0, 0
        self.give_check, self.pet_check, self.walk_check = False, False, False
        self.give_modifier, self.pet_modifier, self.walk_modifier = 0, 0, 0

        self.give_progress = Progressbar(self.window, orient='horizontal', length=100, mode='determinate', value=100)
        self.give_progress.pack(pady=10)
        self.decrease_button = Button(self.window, text="Start Decreasing", command=self.start)
        self.decrease_button.pack(pady=10)
        self.Button1 = Button(self.window, text="Increase", command=self.press_Button1)
        self.Button1.pack(pady=10)

        self.pet_progress = Progressbar(self.window, orient='horizontal', length=100, mode='determinate', value=100)
        self.pet_progress.pack(pady=10)
        self.Button2 = Button(self.window, text="Increase", command=self.press_Button2)
        self.Button2.pack(pady=10)

        self.walk_progress = Progressbar(self.window, orient='horizontal', length=100, mode='determinate', value=100)
        self.walk_progress.pack(pady=10)
        self.Button3 = Button(self.window, text="Increase", command=self.press_Button3)
        self.Button3.pack(pady=10)

        self.dog_progress = Progressbar(self.window, orient='horizontal', length=100, mode='determinate', value=100)
        self.dog_progress.pack(pady=10)

    def start(self):
        self.decrease_give_progress()
        self.decrease_pet_progress()
        self.decrease_walk_progress()
        self.modify_dog_progress()
    def decrease_give_progress(self):
        if self.give_progress['value'] > 0:
            # Check if button has been pressed
            if self.give_check:
                # Increment counter
                self.give_counter += 1

                # Check if counter has reached a certain value
                if self.give_counter == 10:
                    self.give_check = False
                    self.increase_progress(self.give_progress)
                    self.give_counter = 0  # Reset counter

            self.give_progress['value'] -= 1
            if self.give_progress['value'] > 50:
                self.give_modifier = 1
            else:
                self.give_modifier = -1
            self.window.after(100, self.decrease_give_progress)  # Call this function again after 100ms

    def decrease_pet_progress(self):
        if self.pet_progress['value'] > 0:
            # Check if button has been pressed
            if self.pet_check:
                # Increment counter
                self.pet_counter += 1

                # Check if counter has reached a certain value
                if self.pet_counter == 10:
                    self.pet_check = False
                    self.increase_progress(self.pet_progress)
                    self.pet_counter = 0  # Reset counter

            self.pet_progress['value'] -= 1
            if self.pet_progress['value'] > 50:
                self.pet_modifier = 1
            else:
                self.pet_modifier = -1
            self.window.after(100, self.decrease_pet_progress)  # Call this function again after 100ms

    def decrease_walk_progress(self):
        if self.walk_progress['value'] > 0:
            # Check if button has been pressed
            if self.walk_check:
                # Increment counter
                self.walk_counter += 1

                # Check if counter has reached a certain value
                if self.walk_counter == 10:
                    self.walk_check = False
                    self.increase_progress(self.walk_progress)
                    self.walk_counter = 0  # Reset counter

            self.walk_progress['value'] -= 1
            if self.walk_progress['value'] > 50:
                self.walk_modifier = 1
            else:
                self.walk_modifier = -1
            self.window.after(100, self.decrease_walk_progress)  # Call this function again after 100ms

    def modify_dog_progress(self):
        if self.dog_progress['value'] > 0:
            print(self.give_modifier, self.pet_modifier, self.walk_modifier)
            if self.dog_progress['value'] + self.give_modifier + self.pet_modifier + self.walk_modifier <= 100: #Check to make sure progress is not raised above 100
                self.dog_progress['value'] += self.give_modifier + self.pet_modifier + self.walk_modifier
            else:
                self.dog_progress['value'] = 100
            print(self.dog_progress['value'])
            self.window.after(100, self.modify_dog_progress)  # Call this function again after 100ms
    def increase_progress(self, progress):
        if progress['value'] < 100:
            progress['value'] += 10

    def press_Button1(self):
        self.give_check = True

    def press_Button2(self):
        self.pet_check = True

    def press_Button3(self):
        self.walk_check = True





