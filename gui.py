from tkinter import *
from tkinter.ttk import Progressbar
from time import sleep

class Gui:
    def __init__(self, window: Tk):

        self.window = window

# Initialize counters, checks, and modifiers
        self.give_counter, self.pet_counter, self.walk_counter = 0, 0, 0
        self.give_check, self.pet_check, self.walk_check = False, False, False
        self.give_modifier, self.pet_modifier, self.walk_modifier = 0, 0, 0
        self.state = 1
        self.time = 0

        self.Hunger_text = StringVar()
        self.Social_text = StringVar()
        self.Phys_text = StringVar()
        self.Happy_text = StringVar()
# Set up Gui elements

        self.image = PhotoImage(file='dog.png')
        self.Image_label = Label(self.window, image=self.image)

        self.lineframe = Frame(self.window, relief='ridge', bd=5)
        self.displayframe = Frame(self.window)
        self.lineframe2 = Frame(self.window, relief='ridge', bd=5)
        self.frame_one = Frame(self.lineframe2)
        self.frame_two = Frame(self.lineframe2)
        self.frame_three = Frame(self.lineframe2)

        self.Title = Label(self.lineframe, text='Dog Manager', font=('Lora', 15))
        self.Name = Label(self.displayframe, text='Name:')
        self.Entry = Entry(self.displayframe, relief='sunken',bd=2)

        self.image = PhotoImage(file='dog_start.png')
        self.Image_label = Label(self.displayframe, image=self.image, relief='sunken', bd=5)

        self.give_progress = Progressbar(self.frame_one, orient='horizontal', length=100, mode='determinate', value=100)
        self.give_progress.pack(side = 'left', padx = 20, pady=5)
        self.Button1 = Button(self.frame_three, text="Stats", command=self.press_Button1, width= 6)
        self.Button1.pack(side = 'left', padx = (0,60), pady=5)

        self.pet_progress = Progressbar(self.frame_one, orient='horizontal', length=100, mode='determinate', value=100)
        self.pet_progress.pack(side = 'left', pady=10)
        self.Button2 = Button(self.frame_three, text="Start", command=self.press_Button2, width='6')
        self.Button2.pack(side = 'left', pady=5)

        self.walk_progress = Progressbar(self.frame_one, orient='horizontal', length=100, mode='determinate', value=100)
        self.walk_progress.pack(side = 'left', padx = 20, pady=5)
        self.Button3 = Button(self.frame_three, text="Info", command=self.press_Button3, width='6')
        self.Button3.pack(side = 'left', padx = (60,0), pady=5)

        self.Hunger_health = Label(self.frame_two, textvariable=self.Hunger_text)
        self.Social_health = Label(self.frame_two, textvariable=self.Social_text)
        self.Phys_health = Label(self.frame_two, textvariable=self.Phys_text)
        self.Hunger_health.pack(side='left', padx=(50,0))
        self.Social_health.pack(side='left', padx=(25,10))
        self.Phys_health.pack(side='left', padx=(0, 20))

        self.dog_progress = Progressbar(self.lineframe2, orient='horizontal', length=100, mode='determinate', value=100)
        self.Happy_health = Label(self.lineframe2, textvariable=self.Happy_text)

        self.lineframe.pack(fill='x')
        self.Title.pack(fill='x', pady=5)
        self.displayframe.pack(fill='both')
        self.Name.pack()
        self.Entry.pack()
        self.Name.pack_forget()
        self.Entry.pack_forget()
        self.Image_label.pack(side='top')
        self.lineframe2.pack(fill='x')
        self.dog_progress.pack(side='top', pady=5)
        self.Happy_health.pack()
        self.frame_one.pack()
        self.frame_two.pack()
        self.frame_three.pack(pady=10)

    def startstate1(self):
        self.state = 1
        self.give_progress['value'] = 100
        self.pet_progress['value'] = 100
        self.walk_progress['value'] = 100
        self.dog_progress['value'] = 100
        self.Title.config(text='Dog Manager')
        self.image.config(file='dog_start.png')
        self.Button2.config(text='Start', state='normal')
        self.Button3.config(text='Info')

    def startstate2(self):
        self.state = 2
        self.image.config(file='dog.png')
        self.Button1.config(text='Feed')
        self.Button2.config(text='Pet')
        self.Button3.config(text='Walk')
        self.Title.config(text='Sarah')
        self.frame_three.pack_forget()
        self.frame_three.pack()
        self.decrease_give_progress()
        self.decrease_pet_progress()
        self.decrease_walk_progress()
        self.modify_dog_progress()
    def startstate3(self):
        self.state = 3
        time_title = 'You kept Sarah happy for ' + str(self.time) + ' seconds'
        self.Happy_text.set('')
        self.Hunger_text.set('')
        self.Social_text.set('')
        self.Phys_text.set('')
        self.Title.config(text='')
        self.Image_label.pack_forget()
        self.displayframe.pack_forget()
        self.lineframe2.pack_forget()
        self.displayframe.pack(fill='both', pady=125)
        self.Name.pack()
        self.Entry.pack()
        self.lineframe2.pack(fill='x')
        self.Title.config(text=time_title)
        self.Button1.config(text='', state='disabled')
        self.Button2.config(text='Submit', state='disabled')
        self.Button3.config(text='', state='disabled')
        self.give_progress['value'] = 0
        self.pet_progress['value'] = 0
        self.walk_progress['value'] = 0
        self.dog_progress['value'] = 0
        self.window.update()
        sleep(3)
        self.Button2.config(state='normal')
    def startstate4(self):
        self.state = 4
        self.Name.pack_forget()
        self.Entry.pack_forget()
        self.displayframe.pack_forget()
        self.lineframe2.pack_forget()
        self.displayframe.pack(fill='both')
        self.Image_label.pack(side='top')
        self.lineframe2.pack(fill='x')
        self.Title.config(text='Game Over')
        self.image.config(file='dog_end.png')
        self.frame_three.pack_forget()
        self.frame_three.pack(pady=10)
        self.Button1.config(text='Stats', state='normal')
        self.Button2.config(state='disabled')
        self.Button3.config(text='Home', state='normal')
    def decrease_give_progress(self):
        if self.state == 2:


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
        if self.state == 2:


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
        if self.state == 2:


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
            self.Happy_text.set(str(self.dog_progress['value']) + '/100 happiness')
            print(self.dog_progress['value'])
            self.time += 1
            self.window.after(100, self.modify_dog_progress)  # Call this function again after 100ms
        else:
            self.startstate3()




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
        if self.state == 1 or self.state == 4:
            self.openstats()
        if self.state == 2:
            self.give_check = True
            print('pressed give')

    def press_Button2(self):
        if self.state == 1:
            self.startstate2()
        elif self.state == 2:
            self.pet_check = True
            print('pressed pet')
        elif self.state == 3:
            self.submit()
            self.startstate4()


    def press_Button3(self):
        if self.state == 1:
            self.openstats()
        elif self.state == 2:
            self.walk_check = True
            print('pressed walk')
        elif self.state == 4:
            self.startstate1()


    def openstats(self):
        pass
    def submit(self):
        pass
    def openinfo(self):
        pass





