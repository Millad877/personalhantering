class Employee:

    def __init__(self, name_, birthdate_, salary_, id_,languages_):
        self.name = name_
        self.birthdate = birthdate_
        self.salary = salary_
        self.id = id_
        self.languages = languages_

    def toString(self):
        return_string = " - Name: "+ str(self.name) + \
                        " - Birthdate: "+str(self.birthdate)+ " - Salary: "+ str (self.salary)+ \
                        " - Id: " + str(self.id)+ " - Languages: " + str(self.languages)
        return return_string


