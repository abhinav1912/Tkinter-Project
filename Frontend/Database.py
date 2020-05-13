import sys
import tkinter as tk
import json
import time
sys.path.append('../Backend')
# sys.path.append('../Backend/Database')
login_credentials = r'..\Backend\Credentials.json'
user_data = r'..\Backend\User_Info.json'
class Database_Window(tk.Frame):
    def __init__(self, user_name, data, master = "None"):
        tk.Frame.__init__(self, master)
        self.master = master
        self.user_name = user_name
        self.user_data = data
        self.init_Window()
    
    def init_Window(self):
        # self.user_name = user_name
        self.master.title("Stock Price")
        welcome_var = tk.StringVar()
        welcome_var.set("Welcome " + self.user_data["name"] + "!")
        welcome_label = tk.Label(self.master, textvariable = welcome_var, padx= 20, pady = 5)
        welcome_label.grid(row = 0, column = 0)

        time_var = tk.StringVar()
        time_var.set("Time:")
        time_label = tk.Label(self.master, textvariable = time_var, padx= 20, pady = 5)
        time_label.grid(row = 1, column = 0, sticky = tk.W)

        self.realtime_var = tk.StringVar()
        real_time = tk.Label(self.master, textvariable = self.realtime_var, padx= 20, pady = 5)
        real_time.grid(row = 1, column = 1, sticky = tk.W)

        Stock_Choices = {'MSAT'}
        Time_Choices = {'1', '5', '10', '30', '60'}
        self.StockVar = tk.StringVar()
        self.StockVar.set('Select')
        self.TimeVar = tk.StringVar()
        self.TimeVar.set('Select')
        Stock_Label = tk.Label(self.master, textvariable = "Select Stock:", padx= 20, pady = 5)
        Stock_Label.grid(row = 3, column = 0)
        Stock_Menu = tk.OptionMenu(self.master, self.StockVar, *Stock_Choices)
        Stock_Menu.grid(row = 4, column = 0)
        Time_Label = tk.Label(self.master, textvariable = "Select Interval Time:", padx= 20, pady = 5)
        Time_Label.grid(row = 3, column = 1)
        Time_Menu = tk.OptionMenu(self.master, self.TimeVar, *Time_Choices)
        Time_Menu.grid(row = 4, column = 1)
        Sub_Button = tk.Button(self.master, text = "View Stock", command = self.View_Stock)
        Sub_Button.grid(row = 5, column = 1)
        # Data_Button = tk.Button(self.master, text = "View Database")
        # Data_Button.grid(row = 2, column = 2)
        Logout_Button = tk.Button(self.master, text = "Log Out", command = self.Log_Out)
        Logout_Button.grid(row = 5, column = 2)
        

        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.update_clock()
        
    # def Data_Load(self):
    #     path2 = r"..\Backend\User_Info.json"
    #     file = open(path2, encoding='utf-8')
    #     data = json.load(file)
    #     file.close()
    #     for item in data:
    #         if item["username"] == self.user_name:
    #             self.User_Data = item
       
    
    def View_Stock(self):
        import Stock
        # self.master.withdraw()
        # self.AccountWin = tk.Toplevel(self.master)
        # Account.Account_Window(self.user_name ,self.User_Data, self.AccountWin)
        self.req = Stock.StockPrice(self.StockVar, self.TimeVar)
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