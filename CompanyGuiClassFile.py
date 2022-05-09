import tkinter
import tkinter.messagebox
import FunctionsToGui

class CompanyGui:

    def __init__(self,company_):
        self.company = company_
        self.root = tkinter.Tk()

    def start(self):
        self.root.mainloop()

    def create_menu(self):
        menubar = tkinter.Menu(self.root)
        filemenu = tkinter.Menu(menubar, tearoff=0)
        filemenu.add_command(label="open", command = lambda : FunctionsToGui.open_func(self.root, self.company))

        filemenu.add_command(label = "Save as", command = lambda: FunctionsToGui.save_as_func(self.root,self.company))
        filemenu.add_command(label= "Save", command = lambda: FunctionsToGui.save_now(self.root,self.company))
        menubar.add_cascade(label="file", menu=filemenu)
        self.root.config(menu=menubar)

    def create_pic(self):
        my_image = tkinter.PhotoImage(file = "employee.png")
        label_with_image = tkinter.Label(self.root, image = my_image)
        label_with_image.image = my_image
        label_with_image.pack()




    def create_buttons(self):

        button_to_add_employee = tkinter.Button(self.root, text = "click to add a Employee", command = lambda : FunctionsToGui.create_func(self.root, self.company))
        button_to_remove_employee = tkinter.Button(self.root , text = "click to remove a Employee", command = lambda : FunctionsToGui.remove_func(self.root, self.company))
        button_to_show_employees = tkinter.Button ( self.root, text = "Show Employees", command = lambda : FunctionsToGui.func_to_show(self.root, self.company))
        #button_to_open = tkinter.Button(self.root, text = "Open", command = lambda : FunctionsToGui.open_func(self.root, self.company))
        button_to_increase_salary = tkinter.Button(self.root, text = "Increase Salary", command = lambda :FunctionsToGui.increase_salary_func(self.root,self.company))
        button_to_decrease_salary = tkinter.Button(self.root, text = "Decrease salary", command = lambda : FunctionsToGui.decrease_salary_func(self.root,self.company))
        button_to_close = tkinter.Button (self.root, text = "Close", command = lambda: FunctionsToGui.close_func(self.root))
        button_to_decrease_by_procentage = tkinter.Button(self.root, text ="decrease salary by procentage", command = lambda: FunctionsToGui.decrease_salary_by_precentage_func(self.root,self.company))
        button_to_increase_by_procentage = tkinter.Button(self.root, text= "increase salary by procentage", command = lambda: FunctionsToGui.increase_salary_func_by_percentage_func(self.root, self.company))
      #  button_to_show_least_salary = tkinter.Button(self.root, text = "Shwo least salary", command = lambda: FunctionsToGui.show_least_salary_employee(self.root,self.company))
     #   button_to_show_highst_salary = tkinter.Button(self.root, text = "show highst salary", command = lambda: FunctionsToGui.show_highst_salary_employee(self.root, self.company))


        button_to_add_employee.pack()
        button_to_remove_employee.pack()

        button_to_decrease_by_procentage.pack()
        button_to_increase_by_procentage.pack()
        button_to_show_employees.pack()
        #button_to_open.pack()
        button_to_increase_salary.pack()
        button_to_decrease_salary.pack()
     #   button_to_show_least_salary.pack()
    #    button_to_show_highst_salary.pack()
        button_to_close.pack()