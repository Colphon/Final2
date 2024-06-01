import tkinter as tk
from tkinter.ttk import Progressbar

# Initialize counters and checks
counter1, counter2, counter3 = 0, 0, 0
check1, check2, check3 = False, False, False
modifier1, modifier2, modifier3 = 0, 0, 0

def dec():
    decrease_progress1()
    decrease_progress2()
    decrease_progress3()
    decrease_mainprogress()
def decrease_progress1():
    global counter1, check1, modifier1
    if progress1['value'] > 0:
        # Check if button has been pressed
        if check1:
            # Increment counter
            counter1 += 1

            # Check if counter has reached a certain value
            if counter1 == 10:
                check1 = False
                increase_progress(progress1)
                counter1 = 0  # Reset counter

        progress1['value'] -= 1
        if progress1['value'] > 50:
            modifier1 = 1
        else:
            modifier1 = -1
        root.after(100, decrease_progress1)  # Call this function again after 100ms

def decrease_progress2():
    global counter2, check2, modifier2
    if progress2['value'] > 0:
        # Check if button has been pressed
        if check2:
            # Increment counter
            counter2 += 1

            # Check if counter has reached a certain value
            if counter2 == 10:
                check2 = False
                increase_progress(progress2)
                counter2 = 0  # Reset counter

        progress2['value'] -= 1
        if progress2['value'] > 50:
            modifier2 = 1
        else:
            modifier2 = -1
        root.after(100, decrease_progress2)  # Call this function again after 100ms

def decrease_progress3():
    global counter3, check3, modifier3
    if progress3['value'] > 0:
        # Check if button has been pressed
        if check3:
            # Increment counter
            counter3 += 1

            # Check if counter has reached a certain value
            if counter3 == 10:
                check3 = False
                increase_progress(progress3)
                counter3 = 0  # Reset counter

        progress3['value'] -= 1
        if progress3['value'] > 50:
            modifier3 = 1
        else:
            modifier3 = -1
        root.after(100, decrease_progress3)  # Call this function again after 100ms

def decrease_mainprogress():
    global modifier1, modifier2, modifier3
    if mprogress['value'] > 0:
        print(modifier1, modifier2, modifier3)
        if mprogress['value'] + modifier1 + modifier2 + modifier3 <= 100:
            mprogress['value'] += modifier1 + modifier2 + modifier3
        else:
            mprogress['value'] = 100
        print(mprogress['value'])
        root.after(100, decrease_mainprogress)  # Call this function again after 100ms
def increase_progress(progress):
    if progress['value'] < 100:
        progress['value'] += 10

def press_button1():
    global check1
    check1 = True

def press_button2():
    global check2
    check2 = True

def press_button3():
    global check3
    check3 = True

root = tk.Tk()
root.title("Progressbar Example")

progress1 = Progressbar(root, orient='horizontal', length=100, mode='determinate', value=100)
progress1.pack(pady=10)
decrease_button1 = tk.Button(root, text="Start Decreasing", command=dec)
decrease_button1.pack(pady=10)
increase_button1 = tk.Button(root, text="Increase", command=press_button1)
increase_button1.pack(pady=10)

progress2 = Progressbar(root, orient='horizontal', length=100, mode='determinate', value=100)
progress2.pack(pady=10)
decrease_button2 = tk.Button(root, text="Start Decreasing", command=decrease_progress2)
decrease_button2.pack(pady=10)
increase_button2 = tk.Button(root, text="Increase", command=press_button2)
increase_button2.pack(pady=10)

progress3 = Progressbar(root, orient='horizontal', length=100, mode='determinate', value=100)
progress3.pack(pady=10)
decrease_button3 = tk.Button(root, text="Start Decreasing", command=decrease_progress3)
decrease_button3.pack(pady=10)
increase_button3 = tk.Button(root, text="Increase", command=press_button3)
increase_button3.pack(pady=10)

mprogress = Progressbar(root, orient='horizontal', length=100, mode='determinate', value=100)
mprogress.pack(pady=10)


root.mainloop()
