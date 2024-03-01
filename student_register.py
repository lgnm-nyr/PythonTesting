#get number of students
num_students = int(input("How many students are registering? "))

#making file
with open("reg_form.txt", "w") as reg_form:

    #loop to input all students
    for i in range(num_students):

        #get student ID
        student_id = input(f"Enter ID number for student {i+1}: ")

        #print student ID
        reg_form.write(f"Student ID: {student_id} \n\n")

        #dotted line
        reg_form.write("Sign Here: " + "." * 50 + "\n\n")

#line showing program has completed
print("Registration form has been created as reg_form.txt")
