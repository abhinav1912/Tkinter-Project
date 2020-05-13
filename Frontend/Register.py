import tkinter as tk 
import sys
sys.path.append('../Backend')
from Back_Main import Register_Custom, Username_Check
from tkinter import messagebox
class Register(tk.Frame):
    def __init__(self, master = "None"):
        tk.Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Register")
        name_var = tk.StringVar()
        name_var.set("Name: ")
        name_label = tk.Label(self.master, textvariable = name_var)
        name_label.grid(row = 0, column = 0, sticky = tk.W, padx = 10)
        self.name = tk.StringVar()
        name_text = tk.Entry(self.master, textvariable = self.name)
        name_text.grid(row = 0, column = 1, pady = 7, padx = 20, columnspan = 2)

        age_var = tk.StringVar()
        age_var.set("Age: ")
        age_label = tk.Label(self.master, textvariable = age_var)
        age_label.grid(row = 1, column = 0, sticky = tk.W, padx = 10)
        self.age = tk.StringVar()
        age_text = tk.Entry(self.master, textvariable = self.age)
        age_text.grid(row = 1, column = 1, pady = 7, padx = 20, columnspan = 2)

        team_var = tk.StringVar()
        team_var.set("Favorite Team: ")
        team_label = tk.Label(self.master, textvariable = team_var)
        team_label.grid(row = 2, column = 0, sticky = tk.W, padx = 10)
        self.team = tk.StringVar()
        team_text = tk.Entry(self.master, textvariable = self.team)
        team_text.grid(row = 2, column = 1, pady = 7, padx = 20, columnspan = 2)

        user_var = tk.StringVar()
        user_var.set("Username: ")
        user_label = tk.Label(self.master, textvariable = user_var)
        user_label.grid(row = 3, column = 0, sticky = tk.W, padx = 10)
        self.user_name = tk.StringVar()
        user_text = tk.Entry(self.master, textvariable = self.user_name)
        user_text.grid(row = 3, column = 1, pady = 7, padx = 20, columnspan = 2)
        
        pass_var = tk.StringVar()
        pass_var.set("Password: ")
        pass_label = tk.Label(self.master, textvariable = pass_var)
        pass_label.grid(row = 4, column = 0, sticky = tk.W, padx = 10)      
        self.pass_word = tk.StringVar()
        pass_text = tk.Entry(self.master, textvariable = self.pass_word)
        pass_text.grid(row = 4, column = 1, pady = 7, padx = 20, columnspan = 2)
              
        Reg_Button = tk.Button(self.master, text = "Register", command = self.Reg_Final)
        Reg_Button.grid(row = 5, column = 2, sticky = tk.W, padx = 5, pady = 10)
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)

    
    def Reg_Final(self):
        current_user = self.user_name.get()
        if Username_Check(self.user_name.get()) == False:
            messagebox.showerror("Error", "Username Taken")
        else:
            if Register_Custom(self.user_name.get(), self.pass_word.get(), self.name.get(), self.team.get(), self.age.get()) == False:
                messagebox.showerror("Error", "Fill required fields")
            else:  
                messagebox.showinfo("Success", "Registration Successful")
                self.master.withdraw()
                self.MainWin = tk.Toplevel(self.master)
                import Main
                Main.Home(current_user, self.MainWin)
                # self.master.quit()

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.master.quit()

# root = tk.Tk()
# root.title("Register")
# Register_app = Register(root)
# root.mainloop()
