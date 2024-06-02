from tkinter import *
from tkinter.ttk import Progressbar

class Gui:
    def __init__(self, window: Tk):

        self.window = window

# Initialize counters, checks, and modifiers
        self.give_counter, self.pet_counter, self.walk_counter = 0, 0, 0
        self.give_check, self.pet_check, self.walk_check = False, False, False
        self.give_modifier, self.pet_modifier, self.walk_modifier = 0, 0, 0
        self.state = 1
        self.Hunger_text = StringVar()
        self.Social_text = StringVar()
        self.Phys_text = StringVar()
# Set up Gui elements
        self.frame_one = Frame(self.window)
        self.frame_two = Frame(self.window)
        self.frame_three = Frame(self.window)
        self.give_progress = Progressbar(self.frame_one, orient='horizontal', length=100, mode='determinate', value=100)
        self.give_progress.pack(side = 'left', padx = 20, pady=5)
        self.Button1 = Button(self.frame_three, text="Increase", command=self.press_Button1)
        self.Button1.pack(side = 'left', padx = (0,60), pady=5)

        self.pet_progress = Progressbar(self.frame_one, orient='horizontal', length=100, mode='determinate', value=100)
        self.pet_progress.pack(side = 'left', pady=10)
        self.Button2 = Button(self.frame_three, text="Increase", command=self.press_Button2)
        self.Button2.pack(side = 'left', pady=5)

        self.walk_progress = Progressbar(self.frame_one, orient='horizontal', length=100, mode='determinate', value=100)
        self.walk_progress.pack(side = 'left', padx = 20, pady=5)
        self.Button3 = Button(self.frame_three, text="Increase", command=self.press_Button3)
        self.Button3.pack(side = 'left', padx = (60,0), pady=5)

        Hunger_health = Label(self.frame_two, textvariable=self.Hunger_text)
        Social_health = Label(self.frame_two, textvariable=self.Social_text)
        Phys_health = Label(self.frame_two, textvariable=self.Phys_text)
        Hunger_health.pack(side='left')
        Social_health.pack(side='left')
        Phys_health.pack(side='left')

        self.dog_progress = Progressbar(self.window, orient='horizontal', length=100, mode='determinate', value=100)
        self.dog_progress.pack(pady=5)
        self.frame_one.pack()
        self.frame_two.pack()
        self.frame_three.pack()

    def start(self):
        self.decrease_give_progress()
        self.decrease_pet_progress()
        self.decrease_walk_progress()
        self.modify_dog_progress()
    def decrease_give_progress(self):

        # Check if button has been pressed
        if self.give_check:
            # Increment counter
            self.give_counter += 1

            # Check if counter has reached a certain value
            if self.give_counter == 10:
                self.give_check = False
                self.increase_give_progress(self.give_progress)
                self.give_counter = 0  # Reset counter

        if self.give_progress['value'] > 0:

            self.give_progress['value'] -= 1
            self.Hunger_text.set(str(self.give_progress['value'])+'/100 hunger')
            if self.give_progress['value'] > 50:
                self.give_modifier = 1
            elif self.give_progress['value'] > 0:
                self.give_modifier = 0
            else:
                self.give_modifier = -10
            print(self.give_progress['value'])
        self.window.after(100, self.decrease_give_progress)  # Call this function again after 100ms

    def decrease_pet_progress(self):

        # Check if button has been pressed
        if self.pet_check:
            # Increment counter
            self.pet_counter += 1

            # Check if counter has reached a certain value
            if self.pet_counter == 1:
                self.pet_check = False
                self.increase_pet_progress(self.pet_progress)
                self.pet_counter = 0  # Reset counter

        if self.pet_progress['value'] > 0:

            self.pet_progress['value'] -= 1
            self.Social_text.set(str(self.pet_progress['value']) + '/100 social health')
            if self.pet_progress['value'] > 50:
                self.pet_modifier = 1
            elif self.pet_progress['value'] > 0:
                self.pet_modifier = 0
            else:
                self.pet_modifier = -10
            print(self.pet_progress['value'])
        self.window.after(100, self.decrease_pet_progress)  # Call this function again after 100ms

    def decrease_walk_progress(self):

        # Check if button has been pressed
        if self.walk_check:
            # Increment counter
            self.walk_counter += 1

            # Check if counter has reached a certain value
            if self.walk_counter == 15:
                self.walk_check = False
                self.increase_walk_progress(self.walk_progress)
                self.walk_counter = 0  # Reset counter

        if self.walk_progress['value'] > 0:

            self.walk_progress['value'] -= 1
            self.Phys_text.set(str(self.walk_progress['value']) + '/100 physical health')
            if self.walk_progress['value'] > 50:
                self.walk_modifier = 1
            elif self.walk_progress['value'] > 0:
                self.walk_modifier = 0
            else:
                self.walk_modifier = -10
            print(self.walk_progress['value'])
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
        else:
            pass
    # net gain is the value added to the progress value in the if statement of increase_progress - counter needed to execute if statement
    def increase_give_progress(self, give_progress):
        if give_progress['value'] + 19 <= 100:
            give_progress['value'] += 20
        else:
            give_progress['value'] = 101
    def increase_pet_progress(self, pet_progress):
        if pet_progress['value'] + 5 <= 100:
            pet_progress['value'] += 6
        else:
            pet_progress['value'] = 101
    def increase_walk_progress(self, walk_progress):
        if walk_progress['value'] + 29 <= 100:
            walk_progress['value'] += 30
        else:
            walk_progress['value'] = 101

    def press_Button1(self):
        self.give_check = True
        print('pressed give')

    def press_Button2(self):
        if self.state == 1:
            self.start()
            self.state = 2
        elif self.state == 2:
            self.pet_check = True
            print('pressed pet')

    def press_Button3(self):
        self.walk_check = True
        print('pressed walk')





