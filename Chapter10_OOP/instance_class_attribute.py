class Employee:
    company = "google"
    salary = 1000


harry = Employee()
rajni = Employee()


harry.salary = 500  # adding instance attribute
# instance attributes takes prefarence over class attributes during Assignments and retrivals

print(harry.salary)


print(rajni.salary)
