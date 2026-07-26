# Import Employee Class
from empdetail import employee

# Object Creation
obj=employee("ram","pune","20","IT","dev","linkcode",50000)

# Method Calling (Inherited from Person Class)
obj.display_personal_details()

# Method Calling (Inherited from Company Class)
obj.display_company()

# Method Calling (Employee Class)
obj.display_emp_info()




