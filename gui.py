from tkinter import *
from tkinter.ttk import Progressbar
from time import sleep
from logic import *
class Gui:
    def __init__(self, window: Tk):

        self.window = window

# Initialize counters, checks, and modifiers
        self.feed_counter, self.pet_counter, self.walk_counter = 0, 0, 0
        self.feed_check, self.pet_check, self.walk_check = False, False, False
        self.feed_modifier, self.pet_modifier, self.walk_modifier = 0, 0, 0
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

        self.feed_progress = Progressbar(self.frame_one, orient='horizontal', length=100, mode='determinate', value=100)
        self.feed_progress.pack(side = 'left', padx = 20, pady=5)
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
        self.feed_progress['value'] = 100
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
        self.decrease_feed_progress()
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
        self.feed_progress['value'] = 0
        self.pet_progress['value'] = 0
        self.walk_progress['value'] = 0
        self.dog_progress['value'] = 0
        self.Entry.config(state='disabled')
        self.window.update()
        sleep(3)
        self.Entry.config(state='normal')
        self.Button2.config(state='normal')
    def startstate4(self):
        self.state = 4
        self.Happy_text.set('')
        self.Entry.delete(0,'end')
        self.Name.pack_forget()
        self.Entry.pack_forget()
        self.displayframe.pack_forget()
        self.lineframe2.pack_forget()
        self.displayframe.pack(fill='both')
        self.Image_label.pack(side='top')
        self.lineframe2.pack(fill='x')
        self.Title.config(text='Management Over')
        self.image.config(file='dog_end.png')
        self.frame_three.pack_forget()
        self.frame_three.pack(pady=10)
        self.Button1.config(text='Stats', state='normal')
        self.Button2.config(state='disabled')
        self.Button3.config(text='Home', state='normal')
    def decrease_feed_progress(self):
        if self.state == 2:


            # Check if button has been pressed
            if self.feed_check:
                # Increment counter
                self.feed_counter += 1

                # Check if counter has reached a certain value
                if self.feed_counter == 10:
                    self.Button2.config(state='normal')
                    self.Button3.config(state='normal')
                    self.feed_check = False
                    self.increase_feed_progress(self.feed_progress)
                    self.feed_counter = 0  # Reset counter

            if self.feed_progress['value'] > 0:

                self.feed_progress['value'] -= 1
                self.Hunger_text.set(str(self.feed_progress['value'])+'/100 hunger')
                self.feed_modifier = determine_feed(self.feed_progress['value'])
            self.window.after(250, self.decrease_feed_progress)  # Call this function again after 100ms

    def decrease_pet_progress(self):
        if self.state == 2:


            # Check if button has been pressed
            if self.pet_check:
                # Increment counter
                self.pet_counter += 1

                # Check if counter has reached a certain value
                if self.pet_counter == 2:
                    self.Button1.config(state='normal')
                    self.Button3.config(state='normal')
                    self.pet_check = False
                    self.increase_pet_progress(self.pet_progress)
                    self.pet_counter = 0  # Reset counter

            if self.pet_progress['value'] > 0:

                self.pet_progress['value'] -= 1
                self.Social_text.set(str(self.pet_progress['value']) + '/100 social health')
                self.pet_modifier = determine_pet(self.pet_progress['value'])

            self.window.after(250, self.decrease_pet_progress)  # Call this function again after 100ms

    def decrease_walk_progress(self):
        if self.state == 2:


            # Check if button has been pressed
            if self.walk_check:
                # Increment counter
                self.walk_counter += 1

                # Check if counter has reached a certain value
                if self.walk_counter == 12:
                    self.Button1.config(state='normal')
                    self.Button2.config(state='normal')
                    self.walk_check = False
                    self.increase_walk_progress(self.walk_progress)
                    self.walk_counter = 0  # Reset counter

            if self.walk_progress['value'] > 0:

                self.walk_progress['value'] -= 1
                self.Phys_text.set(str(self.walk_progress['value']) + '/100 physical health')
                self.walk_modifier = determine_walk(self.walk_progress['value'])

            self.window.after(250, self.decrease_walk_progress)  # Call this function again after 100ms

    def modify_dog_progress(self):
        if self.dog_progress['value'] > 0:
            if self.dog_progress['value'] + self.feed_modifier + self.pet_modifier + self.walk_modifier <= 100: #Check to make sure progress is not raised above 100
                self.dog_progress['value'] += self.feed_modifier + self.pet_modifier + self.walk_modifier
            else:
                self.dog_progress['value'] = 100
            self.Happy_text.set(str(self.dog_progress['value']) + '/100 happiness')
            self.time += 0.25
            self.window.after(250, self.modify_dog_progress)  # Call this function again after 100ms
        else:
            self.startstate3()

    def increase_feed_progress(self, feed_progress):
        feed_progress['value'] = increase_feed(feed_progress['value'])

    def increase_pet_progress(self, pet_progress):
        pet_progress['value'] = increase_pet(pet_progress['value'])
    def increase_walk_progress(self, walk_progress):
        walk_progress['value'] = increase_walk(walk_progress['value'])

    def press_Button1(self):
        if self.state == 1 or self.state == 4:
            self.openstats()
        if self.state == 2:
            self.Button2.config(state='disabled')
            self.Button3.config(state='disabled')
            self.feed_check = True

    def press_Button2(self):
        if self.state == 1:
            self.startstate2()
        elif self.state == 2:
            self.pet_check = True
            self.Button1.config(state='disabled')
            self.Button3.config(state='disabled')
        elif self.state == 3:
            bool = self.submit()
            if bool:
                self.startstate4()


    def press_Button3(self):
        if self.state == 1:
            self.openinfo()
        elif self.state == 2:
            self.Button1.config(state='disabled')
            self.Button2.config(state='disabled')
            self.walk_check = True
        elif self.state == 4:
            self.startstate1()


    def openstats(self):
        stat_window = Toplevel()
        stat_window.title('Stats')
        stat_window.geometry('150x200')
        stat_window.resizable(False, False)

        Csv_title = Label(stat_window, text='Leaderboard', font=('Playfair Display', 10))
        Csv_title.pack()
        Csv_subtitle = Label(stat_window, text='  Name                  Seconds', font=('Playfair Display', 8))
        Csv_subtitle.pack()
        Csv_label = Label(stat_window, text="")
        Csv_label.pack()

        Csv_label.config(text=stats())


    def submit(self):
        try:
            write(self.Entry.get(), self.time)
            return True
        except NameError:
            self.Happy_text.set("Choose a name that isn't on the leaderboard")
        except ValueError:
            self.Happy_text.set("Name should be alphanumeric and <= 20 characters")
    def openinfo(self):
        text_window = Toplevel()
        text_window.title('Info')
        text_window.geometry('300x450')
        text_window.resizable(False, False)

        txt = ("Welcome to Dog Manager. In this game, you need to keep Sarah happy!\n\n"
               "Sarah's happiness is controlled by three health bars: Hunger health, Social health, and Physical health."
               " Every fourth of a second each health bar loses one point out of 100. Depending on how many points of health you currently have"
               " in a health bar, happiness will increase or decrease by a different amount. The range of points that cause a certain effect"
               " are listed below\n\nHunger: (100-86): 5 (85-41): 2 (40-31): -2 (30-21): -4 (20-0): -5\n\n"
               "Social: (100-76): 3 (75-66): 1 (65-51): 0 (50-31): -1 (30-21): -2 (20-0): -4\n\n"
               "Physical: (100-81): 5 (81-46): 2 (45-26): 1 (25-0): -3\n\n"
               "If any health bar reaches zero, happiness will drop by 10 every fourth second. If the feed, pet, or walk button is pressed"
               " the corresponding health bar will increase by 10 after 2.5 seconds, 5 after 0.5 seconds, and 15 after 3 seconds.\n\nGood Luck.")

        Text_title = Label(text_window, text='Instructions', font=('Playfair Display', 15, 'bold'))
        Text_title.pack()
        Text_label = Label(text_window, text=txt, wraplength=280, justify='left')
        Text_label.pack(anchor='w',padx=(5,0), pady=10)






