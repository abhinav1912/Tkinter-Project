from tkinter import messagebox
import tkinter as tk
import sys
sys.path.append('../Backend')  #to enable custom module imports
from Back_Main import Login_Custom, Register_Custom, Username_Check
class Login(tk.Frame):
    def __init__(self, master = "None"):
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.title("Login")
        self.init_window()

    def init_window(self):
        user_var = tk.StringVar()
        user_var.set("Username: ")
        user_label = tk.Label(self.master, textvariable = user_var)
        user_label.grid(row = 0, column = 0, sticky = tk.W, padx = 10)
        self.user_name = tk.StringVar()
        user_text = tk.Entry(self.master, textvariable = self.user_name)
        user_text.grid(row = 0, column = 1, pady = 7, padx = 20, columnspan = 2)

        pass_var = tk.StringVar()
        pass_var.set("Password: ")
        pass_label = tk.Label(self.master, textvariable = pass_var)
        pass_label.grid(row = 1, column = 0, sticky = tk.W, padx = 10)
        self.pass_word = tk.StringVar()
        pass_text = tk.Entry(self.master, textvariable = self.pass_word)
        pass_text.grid(row = 1, column = 1, pady = 7, padx = 20, columnspan = 2)
        Log_Button = tk.Button(self.master, text = "Login", command = self.login)
        Log_Button.grid(row = 2, column = 1, sticky = tk.E, padx = 5)
        Reg_Button = tk.Button(self.master, text = "Sign Up", command = self.reg)
        Reg_Button.grid(row = 2, column = 2, sticky = tk.W, padx = 5)
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)

    def login(self):
        current_user = self.user_name.get()
        if Login_Custom(self.user_name.get(), self.pass_word.get()) == True:
            messagebox.showinfo("Success", "Login Successful")
            self.master.withdraw()
            self.MainWin = tk.Toplevel(self.master)
            import Main
            Main.Home(current_user, self.MainWin)
        else:
            messagebox.showerror("Error", "Invalid Username or Password")

    def reg(self):
        self.master.withdraw()
        self.newWin = tk.Toplevel(self.master)
        import Register as regis
        regis.Register(self.newWin) 
    
    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.master.quit()
    

    

# root = tk.Tk()
# root.title("Login")
# Login_app = Login(root)
# root.mainloop()