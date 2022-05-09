from EmployeeClassFile import Employee



class Company:

    def __init__(self,name_,city_):
        self.companyName = name_
        self.city = city_

        self.list_of_employees = []
        self.list_of_employees = []
        self.openFile("company")


        #save_file = ""




    def add_new_Employee(self,name,birthdate,salary,ID, languages):
        my_employee = Employee(name,birthdate,salary,ID,languages)
        self.list_of_employees.append(my_employee)
        self.saveFile("company")
        self.saveFile("company")

    def kick_employee(self,id_to_remove):
        employee_do_exist = False

        for i in range (0, len(self.list_of_employees)):
            if self.list_of_employees[i].id ==  id_to_remove:
                self.list_of_employees.pop(i)
                employee_do_exist = True
            break
        return employee_do_exist


    def toString(self):
        return_string = ""
        for i  in range (0, len(self.list_of_employees)):
            return_string = return_string + self.list_of_employees[i].toString() + "\n"
        return return_string

    def openFile(self, filename):
        self.save_file = filename
        tmp_list = self.list_of_employees
        self.list_of_employees = []
        try:
            file = open(filename+".txt", "r")
            while True:
                name = file.readline().rstrip()
                if name =="":
                    file.close()
                    return True


                birthdate = file.readline().rstrip()
                if  birthdate == "":
                    self.list_of_employees = tmp_list
                    file.close()
                    return False


                str_salary = file.readline().rstrip()
                if str_salary == "":
                    self.list_of_employees = tmp_list
                    file.close()
                    return False
                salary = int(str_salary)


                ID = file.readline().rstrip()
                if ID == "":
                    self.list_of_employees = tmp_list
                    file.close()
                    return False


                Langages = file.readline().strip()
                if Langages == "":
                    self.list_of_employees = tmp_list
                    file.close()
                    return False
                languages = Langages.split(" ")


                employee = Employee(name, birthdate, salary, ID, languages)
                self.list_of_employees.append(employee)
                file.close()
                return True
        except:
            self.list_of_employees = tmp_list
            return False

   #current_filename = ""

    def saveAsFile(self,filename):
        try:
            #global current_filename
            file = open(filename+".txt", "w")

            for i in range (0,len(self.list_of_employees)):
                file.write(self.list_of_employees[i].name + "\n")
                file.write(self.list_of_employees[i].birthdate + "\n")
                file.write(str(self.list_of_employees[i].salary) + "\n")
                file.write(self.list_of_employees[i].id + "\n")
                for languages in self.list_of_employees[i].languages :
                    file.write(languages + " ")
                file.write("\n")
                file.write("\n")

            file.close()
            return True
        except:
            return False

    #############################################

    def saveFile(self, filename):
        try:
            self.save_file = filename
            file = open(filename + ".txt", "w")
            file2 = open(filename + "antal.txt", "w")

            for i in range(0, len(self.list_of_employees)):
                print(self.list_of_employees[i].id)
                file.write(self.list_of_employees[i].name + "\n")
                file.write(self.list_of_employees[i].birthdate + "\n")
                file.write(str(self.list_of_employees[i].salary) + "\n")
                file.write(str(self.list_of_employees[i].id) + "\n")
                for languages in self.list_of_employees[i].languages:
                    file.write(languages + "")
                file.write("\n")
                file.write("\n")
            file2.write(str(Employee.employees))

            file.close()
            file2.close()
            return True
        except:
            return False






    ######################################################################

    def get_employee_str_by_id(self,id_of_wanted_employee):
         for employee in self.list_of_employees:
             if employee.id == id_of_wanted_employee:
                 return employee.toString()
         return "non"

    def increase_salary(self, increment, id_):

         for i in range(0, len(self.list_of_employees)):

             #print(id_ + "..." + self.list_of_employees[i].id)
             #print(type(self.list_of_employees[i].salary))

             if self.list_of_employees[i].id == id_:
                 self.list_of_employees[i].salary = self.list_of_employees[i].salary + increment
                 break

    def increase_salary_by_procentage(self,percent_increment, id_):
        for i in range(0,len(self.list_of_employees)):
            if self.list_of_employees[i].id == id_:
                self.list_of_employees[i].salary = self.list_of_employees[i].salary * (1 + percent_increment/100)
                break




    def decrease_salary(self, reduction, id_):
         for i in range(0, len(self.list_of_employees)):
            if reduction > self.list_of_employees[i].salary:
                 return False
            if self.list_of_employees[i].id == id_:
                self.list_of_employees[i].salary = self.list_of_employees[i].salary - reduction
            break




    def decrease_salary_by_precentage(self, percent_reduction, id_):
        for i in range(0,len(self.list_of_employees)):
            if self.list_of_employees[i].id == id_:
                self.list_of_employees[i].salary = self.list_of_employees[i].salary * (1 - percent_reduction/100)
                break

    def get_str_of_least_salary_employee(self):
        array_possition = 0
        min_var = self.list_of_employees[0].salary

        for i in range (0,len(self.list_of_employees)):
            if self.list_of_employees[i].salary <= min_var :
                min_var = self.list_of_employees[i].salary

                array_possition = i
        return self.list_of_employees[array_possition].toString()


    def get_str_of_highst_salary_employee(self):
        max_var = 0
        array_possition = 0

        for i in range(0, len(self.list_of_employees)):
            if self.list_of_employees[i].salary >= max_var:
                max_var = self.list_of_employees[i].salary

                array_possition = i
        return self.list_of_employees[array_possition].toString()

    #def Save_as(self):
    #    global file
    #    file = open(filename + ".txt", "w")
    #    file = tkinter.filedialog.asksaveasfile(mode='w', defaultextension=".txt",filetypes=(("filename", ".txt"))
    #        if file is None:
    #            return True
    #        else:
    #            print(file)
#
    #    textoutput = self.textbox.get(0.0, END)
    #    file.write(textoutput.rstrip())
    #    file.write("\n")
