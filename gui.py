import tkinter as tk
from tkinter import messagebox
from main import WebAutomation

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Web Automation GUI")

        self.login = tk.Frame(self.root)
        self.login.pack(padx=10, pady=10)

        tk.Label(self.login, text='Username').grid(row=0, column=0, sticky="w")
        self.username = tk.Entry(self.login)
        self.username.grid(row=0, column=1, sticky='ew')

        tk.Label(self.login, text='Password').grid(row=1, column=0, sticky="w")
        self.password = tk.Entry(self.login, show="*")
        self.password.grid(row=1, column=1, sticky='ew')

        self.fill = tk.Frame(self.root)
        self.fill.pack(padx=10, pady=10)

        tk.Label(self.fill, text='Full Name').grid(row=0, column=0, sticky="w")
        self.Full_name = tk.Entry(self.fill)
        self.Full_name.grid(row=0, column=1, sticky='ew')

        tk.Label(self.fill, text='Email').grid(row=1, column=0, sticky="w")
        self.email = tk.Entry(self.fill)
        self.email.grid(row=1, column=1, sticky='ew')

        tk.Label(self.fill, text='Current Address').grid(row=2, column=0, sticky="w")
        self.Current_Address = tk.Entry(self.fill)
        self.Current_Address.grid(row=2, column=1, sticky='ew')

        tk.Label(self.fill, text='Permanent Address').grid(row=3, column=0, sticky="w")
        self.Permanent_Address = tk.Entry(self.fill)
        self.Permanent_Address.grid(row=3, column=1, sticky='ew')

        self.button = tk.Frame(self.root)
        self.button.pack(padx=10, pady=10)

        tk.Button(self.button, text="Submit", command=self.submit_data).grid(row=0, column=0, padx=5)
        tk.Button(self.button, text='Close Browser', command=self.close_browser).grid(row=0, column=1, padx=5)


    def submit_data(self):
        username = self.username.get()
        password = self.password.get()

        Full_name = self.Full_name.get()
        Email = self.email.get()
        Current_Address = self.Current_Address.get()
        Permanent_Address = self.Permanent_Address.get()

        self.web_automation = WebAutomation()
        self.web_automation.login(username, password)
        self.web_automation.fill_form(Full_name, Email, Current_Address, Permanent_Address)

    def close_browser(self):
        self.web_automation.close()
        messagebox.showinfo("Browse clone", "Submitted Successfully!")

root = tk.Tk()
app = App(root)
root.mainloop()

