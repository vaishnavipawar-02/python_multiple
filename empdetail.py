# Import Parent Classes
from personaldetail import person
from companydetail import company

# Child Class (Multiple Inheritance)
class employee(person, company):

    # Constructor
    def __init__(self, name, city, age, dept, role, cname, salary):

        # Call person class constructor
        person.__init__(self, name, city, age)

        # Call company class constructor
        company.__init__(self, dept, role, cname)

        # Instance Variable
        self.salary = salary

    # Instance Method
    def display_emp_info(self):

        print("<===== All Information Of Employee =====>")

        print()

        # Call person class method
        self.display_personal_details()

        print()

        # Call company class method
        self.display_company()

        print()

        # Display Employee Salary
        print(f"Salary : {self.salary}")