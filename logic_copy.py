from tkinter import *
from tkinter.ttk import Progressbar

class Gui:
    def __init__(self, window: Tk):

        self.window = window

# Initialize counters, checks, and modifiers
        self.give_counter, self.pet_counter, self.walk_counter = 0, 0, 0
        self.give_check, self.pet_check, self.walk_check = False, False, False
        self.give_modifier, self.pet_modifier, self.walk_modifier = 0, 0, 0

        def start():
            decrease_give_progress()
            decrease_pet_progress()
            decrease_walk_progress()
            modify_dog_progress()
        def decrease_give_progress():
            if give_progress['value'] > 0:
                # Check if button has been pressed
                if self.give_check:
                    # Increment counter
                    self.give_counter += 1

                    # Check if counter has reached a certain value
                    if self.give_counter == 10:
                        self.give_check = False
                        increase_progress(give_progress)
                        self.give_counter = 0  # Reset counter

                give_progress['value'] -= 1
                if give_progress['value'] > 50:
                    self.give_modifier = 1
                else:
                    self.give_modifier = -1
                window.after(100, decrease_give_progress)  # Call this function again after 100ms

        def decrease_pet_progress():
            if pet_progress['value'] > 0:
                # Check if button has been pressed
                if self.pet_check:
                    # Increment counter
                    self.pet_counter += 1

                    # Check if counter has reached a certain value
                    if self.pet_counter == 10:
                        self.pet_check = False
                        increase_progress(pet_progress)
                        self.pet_counter = 0  # Reset counter

                pet_progress['value'] -= 1
                if pet_progress['value'] > 50:
                    self.pet_modifier = 1
                else:
                    self.pet_modifier = -1
                window.after(100, decrease_pet_progress)  # Call this function again after 100ms

        def decrease_walk_progress():
            if walk_progress['value'] > 0:
                # Check if button has been pressed
                if self.walk_check:
                    # Increment counter
                    self.walk_counter += 1

                    # Check if counter has reached a certain value
                    if self.walk_counter == 10:
                        self.walk_check = False
                        increase_progress(walk_progress)
                        self.walk_counter = 0  # Reset counter

                walk_progress['value'] -= 1
                if walk_progress['value'] > 50:
                    self.walk_modifier = 1
                else:
                    self.walk_modifier = -1
                window.after(100, decrease_walk_progress)  # Call this function again after 100ms

        def modify_dog_progress():
            if dog_progress['value'] > 0:
                print(self.give_modifier, self.pet_modifier, self.walk_modifier)
                if dog_progress['value'] + self.give_modifier + self.pet_modifier + self.walk_modifier <= 100: #Check to make sure progress is not raised above 100
                    dog_progress['value'] += self.give_modifier + self.pet_modifier + self.walk_modifier
                else:
                    dog_progress['value'] = 100
                print(dog_progress['value'])
                window.after(100, modify_dog_progress)  # Call this function again after 100ms
        def increase_progress(progress):
            if progress['value'] < 100:
                progress['value'] += 10

        def press_Button1():
            global give_check
            self.give_check = True

        def press_Button2():
            global pet_check
            self.pet_check = True

        def press_Button3():
            global walk_check
            self.walk_check = True

        window = Tk()
        window.title("Progressbar Example")

        give_progress = Progressbar(window, orient='horizontal', length=100, mode='determinate', value=100)
        give_progress.pack(pady=10)
        decrease_button = Button(window, text="Start Decreasing", command=start)
        decrease_button.pack(pady=10)
        Button1 = Button(window, text="Increase", command=press_Button1)
        Button1.pack(pady=10)

        pet_progress = Progressbar(window, orient='horizontal', length=100, mode='determinate', value=100)
        pet_progress.pack(pady=10)
        Button2 = Button(window, text="Increase", command=press_Button2)
        Button2.pack(pady=10)

        walk_progress = Progressbar(window, orient='horizontal', length=100, mode='determinate', value=100)
        walk_progress.pack(pady=10)
        Button3 = Button(window, text="Increase", command=press_Button3)
        Button3.pack(pady=10)

        dog_progress = Progressbar(window, orient='horizontal', length=100, mode='determinate', value=100)
        dog_progress.pack(pady=10)



