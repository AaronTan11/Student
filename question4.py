options = input(
    "Your options are: \n1. Add new student detail \n2. View all student details \n3. Search Specific student detail. \nSelect your Choice(1-3): "
)

if options == '1':
    name = input("Enter Student Name: ")
    tp_number = input("Enter John Billy's TP number: ")
    subjects = int(input("How many subjects in Semester: "))
    count = 1
    marks_list = []

    while count <= subjects:
        marks = int(input(f'Enter {count} subject Marks: '))
        marks_list.append(marks)
        count += 1

elif options == '2':
    sqlquery = "SELECT Name, TP_Number, Subjects, TotalMarks, AverageMarks, Grade FROM student_marks"
    templist = []

    mycursor.execute(sqlquery)
    myresult = mycursor.fetchall()

    for x in myresult:
        for y in x:
            templist.append(y)
    print("Name: ", templist[0])
    print("TPNumber: ", templist[1])
    print("Subjects: ", templist[2])
    print("Total: ", templist[3])
    print("Average: ", templist[4])
    print("Grade: ", templist[5])
