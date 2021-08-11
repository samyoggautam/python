from tkinter import *
import tkinter.messagebox as mb


class WinAndFrame:
    def __init__(self, win):

        self.win = win  # Window passed by the user is store here.
        self.win.title('!!!!!!!!!!!! Group D: Basic Calculator !!!!!!!!!!!!!!')  # Title of the window.
        self.win.geometry('520x548+0+0')  # Size of window is set to 520x548 and start from x,y = 0,0.
        self.win.resizable(width=False, height=False)  # User cannot resize the window.
        self.operator = ''  # This variable stores operator provided by user.
        self.total = StringVar()  # We need to this variable to update the entry box.
        self.text = ''  # This variable stores everything that user enters.
        # _________________________________Frames___________________________________
        self.main_frame = Frame(self.win)  # This is the frame of tkinter window.
        self.main_frame.pack()

        self.entry_frame = Frame(self.main_frame)  # This frame is used to store entry box and belongs to main frame.
        self.entry_frame.pack()

        self.button_frame = Frame(self.main_frame)  # This frame is used for buttons and goes to main frame.
        self.button_frame.pack()


class MenuAndButton(WinAndFrame):
    def __init__(self, win):
        """This class only focuses on creating and associating menus and buttons with parent class WinAndFrame."""
        WinAndFrame.__init__(self, win)

        """Menus are created here."""
        self.menu_bar = Menu(self.main_frame)  # Menu bar is created.
        self.win.config(menu=self.menu_bar)  # Insert menu bar to the tkinter window.

        self.about_menu = Menu(self.menu_bar)  # About menu is created.
        self.menu_bar.add_cascade(label='About', menu=self.about_menu)  # Given label as About.
        self.about_menu.add_command(label='Credits', command=MenuAndButton.creation_credits)  # Inside About label
        # Credits is created and given command of static method creation_credits.

        self.exit_menu = Menu(self.menu_bar)  # Exit menu is created.
        self.menu_bar.add_cascade(label='Exit', menu=self.exit_menu)  # Given label as Exit.
        self.exit_menu.add_command(label='Exit', command=self.exit_me)  # Inside Exit label Exit is created and
        # given command of instance method exit_me.

        """Entry box is designed here."""
        self.entry_box = Entry(self.entry_frame, textvariable=self.total, font='arial 22 bold',
                               width=40, bd=16, justify=RIGHT)  # Create entry box having text variable self.total.
        self.entry_box.pack()
        self.entry_box.insert(0, '0')  # Insert 0 to entry box on the startup.

        """Buttons are designed here."""
        btn_pads = f'C{chr(8730)}e+789-456*123{chr(247)}.0d='  # Store string value of all buttons that will be created.
        i = 0  # This is variable is use to access element in variable btn_pads.
        self.btn_list = []  # Stores buttons we have created using for loop in the following lines.
        for j in range(0, 5):
            for k in range(4):
                self.btn_list.append(Button(self.button_frame, text=btn_pads[i], font='arial 18 bold', width=7,
                                            height=2, bd=10))  # Appends buttons to the empty list self.btn_list.
                self.btn_list[i].grid(row=j, column=k)  # This line arrange buttons on button_frame which are created.

                if btn_pads[i] in f'1 2 3 4 5 6 7 8 9 0 .'.split(' '):
                    self.btn_list[i]['command'] = lambda x=btn_pads[i]: self.number_press(x)  # Add commands to buttons.

                if btn_pads[i] in f'+ - * {chr(247)} e'.split(' '):
                    self.btn_list[i]['command'] = lambda x=btn_pads[i]: self.add_operator(x)

                if btn_pads[i] == f'{chr(8730)}':
                    self.btn_list[i]['command'] = lambda x=btn_pads[i]: self.square_root()

                if btn_pads[i] == 'C':
                    self.btn_list[i]['command'] = lambda: self.all_clear()

                if btn_pads[i] == 'd':
                    self.btn_list[i]['command'] = lambda: self.deletion()

                if btn_pads[i] == '=':
                    self.btn_list[i]['command'] = lambda: self.equal()

                i += 1

    @staticmethod
    def creation_credits():

        mb.showinfo('Credits', 'Credits goes to \nsamyog Gautam')

    def display(self, value):

        self.total.set(value)

    def add_operator(self, value):


        self.text = self.entry_box.get()
        self.equal()

        if self.text == '0':
            self.text = ''

        try:
            if self.text[-1] in f'+ - * {chr(247)} e'.split(' '):
                self.text = self.text[:-1] + value
                self.operator = value
                self.display(self.text)

            else:
                self.text += value
                self.operator = value
                self.display(self.text)

        except IndexError:
            mb.showinfo("Logic Problem", "Cannot use operator with Zero. It will be meaningless.")

    def number_press(self, value):
        """This method allows user to add number to the entry box."""
        if self.text == '0':
            self.text = ''

        if value == '.' and self.text.count('.') == 1:
            value = ''
        self.text += value
        self.display(self.text)

    def square_root(self):
        """Helps to calculate square root and update it to the entry box."""
        try:
            self.text = str(float(self.text) ** (1 / 2))
            self.display(self.text)

        except ValueError:
            mb.showinfo('Operator error!!', 'Remove operator to use square root function.')

    def deletion(self):
        """Helps to delete value at the last index of the entry box."""
        self.entry_box.delete(len(self.entry_box.get()) - 1)
        self.text = self.entry_box.get()

    def all_clear(self):
        """Helps to clear and insert 0 in the entry box."""
        self.text = '0'
        self.entry_box.delete(0, 'end')
        self.entry_box.insert(0, self.text)

    def equal(self):
        """Helps to evaluate data in the entry box based on the operator present in it."""
        try:
            if self.operator == "+":
                calculate = self.text.split('+')
                self.text = str(float(calculate[0]) + float(calculate[1]))

            if self.operator == "-":
                calculate = self.text.split('-')
                self.text = str(float(calculate[0]) - float(calculate[1]))

            if self.operator == "*":
                calculate = self.text.split('*')
                self.text = str(float(calculate[0]) * float(calculate[1]))

            if self.operator == f"{chr(247)}":
                calculate = self.text.split(f'{chr(247)}')
                self.text = str(float(calculate[0]) / float(calculate[1]))

            if self.operator == "e":
                calculate = self.text.split('e')
                self.text = str(float(calculate[0]) ** float(calculate[1]))

            self.display(self.text)

        except OverflowError:
            mb.showinfo('Over Flow Error', 'Result is too large to show. \nTry something smaller.')

        except ZeroDivisionError:
            mb.showinfo('Zero Division Error', 'Cannot divide by zero.')

        except IndexError:
            pass

        except ValueError:
            pass

        except AttributeError:
            pass

    def exit_me(self):
        """Helps to end/close the program."""
        answer = mb.askquestion("!!! Confirm Exit !!!", 'Are you sure you want to exit?')
        if answer == 'yes':
            self.win.destroy()


w = Tk()

c = MenuAndButton(w)

w.mainloop()