# Company Class
class company:

    # Constructor
    def __init__(self, dept, role, cname):

        # Instance Variables
        self.dept = dept
        self.role = role
        self.cname = cname

    # Instance Method
    def display_company(self):

        print("====== Company Details ======")

        # Display Company Details
        print(f"Company Name: {self.cname}  Role: {self.role}  Department: {self.dept}")