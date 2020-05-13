import tkinter as tk 
import json
import sys
import time
sys.path.append('../Backend')
login_credentials = r'..\Backend\Credentials.json'
user_data = r'..\Backend\User_Info.json'
class Home(tk.Frame):
    def __init__(self, user_name, master = "None"):
        tk.Frame.__init__(self, master)
        self.master = master
        self.user_name = user_name
        self.Data_Load()
        self.init_Window()
    
    def init_Window(self):
        # self.user_name = user_name
        self.master.title("Home")
        welcome_var = tk.StringVar()
        welcome_var.set("Welcome " + self.User_Data["name"] + "!")
        welcome_label = tk.Label(self.master, textvariable = welcome_var, padx= 20, pady = 5)
        welcome_label.grid(row = 0, column = 0)

        time_var = tk.StringVar()
        time_var.set("Time:")
        time_label = tk.Label(self.master, textvariable = time_var, padx= 20, pady = 5)
        time_label.grid(row = 1, column = 0, sticky = tk.W)

        self.realtime_var = tk.StringVar()
        real_time = tk.Label(self.master, textvariable = self.realtime_var, padx= 20, pady = 5)
        real_time.grid(row = 1, column = 1, sticky = tk.W)

        Acc_Button = tk.Button(self.master, text = "View Account", command = self.View_Account)
        Acc_Button.grid(row = 2, column = 1)
        Data_Button = tk.Button(self.master, text = "View Database", command = self.View_Database)
        Data_Button.grid(row = 2, column = 2)
        Logout_Button = tk.Button(self.master, text = "Log Out", command = self.Log_Out)
        Logout_Button.grid(row = 2, column = 3)
        

        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.update_clock()
        # username_text.insert(tk.END, Data_Gen()['now_cost'])
    def Data_Load(self):
        path2 = r"..\Backend\User_Info.json"
        file = open(path2, encoding='utf-8')
        data = json.load(file)
        file.close()
        for item in data:
            if item["username"] == self.user_name:
                self.User_Data = item
       
    
    def View_Account(self):
        import Account
        self.master.withdraw()
        self.AccountWin = tk.Toplevel(self.master)
        Account.Account_Window(self.user_name ,self.User_Data, self.AccountWin)

    def View_Database(self):
        import Database
        self.master.withdraw()
        self.DatabaseWin = tk.Toplevel(self.master)
        Database.Database_Window(self.user_name, self.User_Data, self.DatabaseWin) 

    def on_closing(self):
        from tkinter import messagebox
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.master.quit()
    
    def Log_Out(self):
        self.user_name = "None"
        self.LogWin = tk.Toplevel(self.master)
        self.master.withdraw()
        from tkinter import messagebox
        import Login
        Login.Login(self.LogWin)
        messagebox.showinfo("Success", "You Have Been Logged Out")

    def update_clock(self):
        current_time = time.strftime("%H:%M:%S")
        self.realtime_var.set(current_time)
        self.master.after(500, self.update_clock)
        
        
        


# master = tk.Tk()
# app = Home('user1', master)
# master.mainloop()