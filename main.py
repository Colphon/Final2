from gui import *
def main():
    window = Tk()
    window.title('Dog Manager')
    window.geometry('300x300')
    window.resizable(False, False)
    Gui(window)
    window.mainloop()

if __name__ == '__main__':
    main()