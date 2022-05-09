import tkinter
import tkinter.messagebox
import tkinter.filedialog
import tkinter.font

##########################################################
def func_to_show(root,company):
    child = tkinter.Toplevel(root)
    my_label = tkinter.Label(child, text = company.toString())
    my_label.pack()


##########################################################
def increase_salary_func(root,company):
    child = tkinter.Toplevel(root)
    lab1 = tkinter.Label(child,text="set id")
    lab2 = tkinter.Label(child,text="set increament")

    ent1 = tkinter.Entry(child)
    ent2 = tkinter.Entry(child)

    def sub_func():
        id_= ent1.get()
        increament = ent2.get()

        company.increase_salary(int(increament),id_)

        child.destroy()

    but = tkinter.Button(child, text="rise salary", command=sub_func)

    lab1.grid(row=0,column = 0)
    ent1.grid(row=0,column = 1)

    lab2.grid(row=1,column = 0)
    ent2.grid(row=1,column = 1)
    but.grid(row=2,column = 1)

##########################################################
def increase_salary_func_by_percentage_func(root,company):
    child = tkinter.Toplevel(root)
    lab1 = tkinter.Label(child, text = "Set Id")
    lab2 = tkinter.Label(child, text = "Set Increament")

    ent1 = tkinter.Entry(child)
    ent2 = tkinter.Entry(child)

    def sub_func():
        id_ = ent1.get()
        increament = ent2.get()

        company.increase_salary_by_procentage(int(increament), id_)

        child.destroy()

    but = tkinter.Button(child, text = "öka salary", command = sub_func)

    lab1.grid(row= 0, column = 0)
    ent1.grid(row = 0, column = 1)

    lab2.grid(row = 1, column =0 )
    ent2.grid (row= 1, column = 1)

    but.grid(row = 2, column = 1)


##########################################################
def decrease_salary_func(root,company):
    child = tkinter.Toplevel(root)
    lab1 = tkinter.Label(child, text="set id")
    lab2 = tkinter.Label(child, text="set reduction")

    ent1 = tkinter.Entry(child)
    ent2 = tkinter.Entry(child)

    def sub_func():
        id_ = ent1.get()
        reduction = ent2.get()

        company.decrease_salary(int(reduction), id_)

        child.destroy()

    but = tkinter.Button(child, text="minska salary", command = sub_func)

    lab1.grid(row=0, column=0)
    ent1.grid(row=0, column=1)

    lab2.grid(row=1, column=0)
    ent2.grid(row=1, column=1)
    but.grid(row=2, column=1)


##########################################################
def decrease_salary_by_precentage_func(root, company):
    child = tkinter.Toplevel(root)
    lab1 = tkinter.Label(child,text = "Set ID" )
    lab2 = tkinter.Label(child,text = "set percent reduction")

    ent1 = tkinter.Entry(child)
    ent2 = tkinter.Entry(child)

    def sub_func():
        id_ = ent1.get()
        reduction = ent2.get()

        company.decrease_salary_by_precentage(int(reduction),id_ )
        child.destroy()


    but = tkinter.Button(child, text = "reducate salary", command = sub_func)

    lab1.grid(row = 0 , column = 0)
    ent1.grid (row = 0, column = 1)

    lab2.grid(row = 1, column = 0)
    ent2.grid(row = 1, column = 1)
    but.grid(row = 2, column = 1)


##########################################################
def show_least_salary_employee(root, company):
    child = tkinter.Toplevel(root)
    child.grab_set()

    my_label = tkinter.Label(child, text=company.get_str_of_least_salary_employee())

    my_label.pack()

##########################################################
def show_highst_salary_employee(root, company):
    child = tkinter.Toplevel(root)
    child.grab_set()

    ##########################################################
def close_func(root):

    answer = tkinter.messagebox.askyesno(message= "Close?")
    if answer == True:
        root.destroy()




##########################################################
def open_func(root,company):
    child = tkinter.Toplevel(root)
    lab = tkinter.Label(child, text = company.openFile)

    lab.pack()
    def sub_func():
        filename = ent.get()
        company.openFile(filename)
        child.destroy()

    ent = tkinter.Entry(child)
    but = tkinter.Button(child, text = "Give file name to open", command = sub_func)
    ent.pack()
    but.pack()


#########################################################

def create_func(root,company):
    child = tkinter.Toplevel(root)

    lab1 = tkinter.Label(child, text = "name")
    lab2 = tkinter.Label(child, text = "Birthdate")
    lab3 = tkinter.Label (child, text = "Salary")
    lab4 = tkinter.Label(child, text = "ID")

    ent1 = tkinter.Entry(child)
    ent2 = tkinter.Entry(child)
    ent3 = tkinter.Entry(child)
    ent4 = tkinter.Entry(child)

    checklab1 = tkinter.Label(child, text = "Svenska")
    valueOfCheckB1 = tkinter.IntVar()
    checkb1 = tkinter.Checkbutton(child, variable = valueOfCheckB1)

    checklab2 = tkinter.Label(child, text = "Engelska")
    valueOfCheckB2= tkinter.IntVar()
    checkb2 = tkinter.Checkbutton(child, variable = valueOfCheckB2)


    checklab3 = tkinter.Label(child, text = "Norska")
    valueOfCheckB3 = tkinter.IntVar()
    checkB3 = tkinter.Checkbutton(child, variable = valueOfCheckB3)


    checklab4 = tkinter.Label(child, text = "Arabiska")
    valueOfCheckB4 = tkinter.IntVar()
    checkB4 = tkinter.Checkbutton(child, variable = valueOfCheckB4)
    print("Hej")

    def sub_func():
        try:

            Name = ent1.get()
            Birthdate = ent2.get()
            Salary =int(ent3.get())
            ID = ent4.get()
            Languages = []




            if valueOfCheckB1.get() ==1:
                Languages.append("Svenska")
            if valueOfCheckB2.get()== 1:
                Languages.append("Engelska")
            if valueOfCheckB3.get()== 1:
                Languages.append("Norska")
            if valueOfCheckB4.get()== 1:
                Languages.append("Arabiska")

            company.add_new_Employee(Name, Birthdate, Salary, ID, Languages)
        except ValueError:
            tkinter.messagebox.showinfo("Error", "Salary Should be a number")


        ent1.delete(0, tkinter.END)
        ent2.delete(0,tkinter.END)
        ent3.delete(0,tkinter.END)
        ent4.delete(0,tkinter.END)

        child.destroy()



    but1 = tkinter.Button(child, text = "create Employee", command = sub_func)

    #print("bbb")
    lab1.grid(row = 0 , column = 0)
    ent1.grid(row= 0, column = 1)
    lab2.grid( row = 1, column = 0)
    ent2.grid( row= 1, column = 1)
    lab3.grid(row= 2, column = 0)
    ent3.grid(row=2, column = 1)
    lab4.grid(row = 3, column = 0)
    ent4.grid(row = 3, column = 1)


    checklab1.grid(row = 4, column = 0)
    checkb1.grid(row = 4, column = 1)
    checklab2.grid(row= 5, column = 0 )
    checkb2.grid(row= 5, column = 1)
    checklab3.grid(row= 6, column = 0)
    checkB3.grid(row= 6, column = 1)
    checklab4.grid(row= 7, column = 0)
    checkB4.grid(row= 7, column = 1)

    but1.grid(row= 8, column = 1)

##########################################################
def remove_func(root,company):
     child = tkinter.Toplevel(root)

     lab1= tkinter.Label(child, text = "ID")
     ent1 = tkinter.Entry(child)

     def sub_funk():
         id_of_employee = ent1.get()
         company.kick_employee(id_of_employee)
         ent1.delete(0, tkinter.END)
         child.destroy()
     but1 = tkinter.Button(child, text = "remove", command = sub_funk)

     lab1.grid(row= 0, column = 0)
     ent1.grid(row = 0, column= 1)
     but1.grid(row = 1 , column = 1)


def save_as_func(root,company):
    child = tkinter.Toplevel(root)

    def sub_func():
        filename = ent.get()
        company.saveAsFile(filename)
        child.destroy()

    ent = tkinter.Entry(child)
    but = tkinter.Button(child, text="save", command=sub_func)
    ent.pack()
    but.pack()
##################################################

current_filename = ""
##def save_func(root,company):
#
 #
 #    if str(current_filename)== "":
 #        Company.saveAsFile(current_filename)
 #    else:
 #        save_func(current_filename)
#


#def save_as_func(root, company):
#    child = tkinter.Toplevel(root)
#    lab = tkinter.Label(child, text = company.save_as)
#    lab.pack()
#
#    def sub_func():
#        filename = ent.get()
#        company.save_as(filename)
#        child.destroy()
#
#    ent = tkinter.Entry(child)
#    but = tkinter.Button(child , text = "Save as", command = sub_func)
#    file = tkinter.filedialog.asksaveasfile(child,mode='w', defaultextension=".txt",filetypes=(("filename", ".txt")))
#
#    ent.pack()
#    but.pack()
#    file.pack()
    # tkinter.Button(child, text = "Save as", command = sub_func)

def save_now(root,company):

   if company.save_file == "":
       save_as_func(root,company)

   else:
       company.saveFile(company.save_file)
