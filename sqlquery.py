import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234qwer",
    database="pythonQ4"
)

mycursor = mydb.cursor()


def Display():
    mark()
    average_mark()
    grade_marks()
    return


def mark():
    global total
    total = 0
    for i in marks_list:
        total += i
    print("Total of all Subjects: ", total)
    return


def average_mark():
    global average
    average = total / subjects
    print("Average of Semester: ", average)
    return


def grade_marks():
    global grade
    if 100 >= average >= 80:
        grade = "A+"
    elif 80 > average >= 75:
        grade = "A"
    elif 75 > average >= 70:
        grade = "B+"
    elif 70 > average >= 65:
        grade = "B"
    elif 65 > average >= 60:
        grade = "C+"
    elif 60 > average >= 55:
        grade = "C"
    elif 55 > average >= 50:
        grade = "C-"
    else:
        grade = "D"

    print("Grade of Semester: ", grade)
    return


flag = True
while flag:
    lines = "=" * 50
    print(lines)
    options = input(
        "Your options are: \n1. Add new student detail \n2. View all student details \n3. Search Specific student detail. \nPress '0' to exit.\nSelect your Choice(1-3): "
    )

    if options == '1':
        print(lines)
        name = input("Enter Student Name: ")
        tp_number = input("Enter Student's TP number: ")
        subjects = int(input("How many subjects in Semester: "))
        count = 1
        marks_list = []

        while count <= subjects:
            marks = int(input(f'Enter {count} subject Marks: '))
            marks_list.append(marks)
            count += 1

        Display()
        sqlquery = "INSERT INTO student_marks (Name, TP_Number, Subjects, TotalMarks, AverageMarks, Grade) VALUES (%s, %s, %s, %s, %s, %s)"
        mycursor.execute(sqlquery, (name, tp_number,
                                    subjects, total, average, grade))

        mydb.commit()

        print(mycursor.rowcount, "record inserted.")
    elif options == '2':
        print(lines)
        sqlquery = "SELECT Name, TP_Number, Subjects, TotalMarks, AverageMarks, Grade FROM student_marks"

        mycursor.execute(sqlquery)
        myresult = mycursor.fetchall()

        for x in myresult:
            templist = []
            for y in x:
                templist.append(y)
            print("Name: ", templist[0])
            print("TPNumber: ", templist[1])
            print("Subjects: ", templist[2])
            print("Total: ", templist[3])
            print("Average: ", templist[4])
            print("Grade: ", templist[5])
    elif options == '3':
        print(lines)
        name = input("Enter Student Name: ")
        tp_number = input("Enter Student's TP number: ")
        templist = []

        sqlquery = "SELECT Name, TP_Number, Subjects, TotalMarks, AverageMarks, Grade FROM student_marks WHERE Name=%s and TP_Number=%s"
        values = (name, tp_number)

        mycursor.execute(sqlquery, values)
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
    elif options == '0':
        print(lines)
        print("Exiting...")
        print("Exited.")
        flag = False
    else:
        print(lines)
        print("Error!! Please Choose 1-3 ONLY!!!")
