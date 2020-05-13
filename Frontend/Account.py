import tkinter as tk 
import json
import sys
sys.path.append('../Backend')
login_credentials = r'..\Backend\Credentials.json'
user_data = r'..\Backend\User_Info.json'

class Account_Window(tk.Frame):
    def __init__(self, user_name, data, master = "None"):
        tk.Frame.__init__(self, master)
        self.master = master
        self.user_name = user_name
        self.User_Data = data
        self.init_Window()
    
    def init_Window(self):
        self.master.title("Account Info")

        name_var = tk.StringVar()
        name_var.set("Name")
        name_label = tk.Label(self.master, textvariable = name_var, padx= 20, pady = 5)
        name_label.grid(row = 1, column = 0)
        name_text = tk.Text(self.master, height = 1, width = 20)
        name_text.insert(tk.END, self.User_Data["name"])
        name_text.grid(row = 1, column = 1)
        
        age_var = tk.IntVar()
        age_var.set("Age")
        age_label = tk.Label(self.master, textvariable = age_var, padx= 20)
        age_label.grid(row = 2, column = 0)
        age_text = tk.Text(self.master, height = 1, width = 20)
        age_text.insert(tk.END, self.User_Data["age"])
        age_text.grid(row = 2, column = 1)

        team_var = tk.StringVar()
        team_var.set("Team")
        team_label = tk.Label(self.master, textvariable = team_var, pady = 5)
        team_label.grid(row = 3, column = 0)
        team_text = tk.Text(self.master, height = 1, width = 20)
        team_text.insert(tk.END, self.User_Data["team"])
        team_text.grid(row = 3, column = 1)


        username_var = tk.IntVar()
        username_var.set("Username")
        username_label = tk.Label(self.master, textvariable = username_var)
        username_label.grid(row = 0, column = 0)
        username_text = tk.Text(self.master, height = 1, width = 20)
        username_text.insert(tk.END, self.user_name)
        username_text.grid(row = 0, column = 1)

        Back_Button = tk.Button(self.master, text = "Home", command = self.Back_Home)
        Back_Button.grid(row = 4, column = 1, sticky = tk.E)
        Edit_Button = tk.Button(self.master, text = "Edit Info")
        Edit_Button.grid(row = 4, column = 2)

        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        from tkinter import messagebox
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.master.quit()

    def Back_Home(self):
        self.master.withdraw()
        self.HomeWin = tk.Toplevel(self.master)
        import Main
        Main.Home(self.user_name, self.HomeWin)
