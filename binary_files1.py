"""
 @author Balkrishna Srivastava
 Copyright © CodeWithBK 2023. All rights reserved.

 Python program to create a binary file with roll number, name and marks
 Input a roll number and update the marks.
"""

import pickle

bk = {"name":"bk", "roll number":1, "marks":64}

student_records = []
student_records.append(bk)
student_records.append({"name":"ammo", "roll number":4, "marks":92})
student_records.append({"name":"akath", "roll number":18, "marks":98})
student_records.append({"name":"chirag", "roll number":3, "marks":88})
student_records.append({"name":"su", "roll number":31, "marks":93})

def write_data(filename):
    fout = open(filename, "wb")
    for student_record in student_records:
        pickle.dump(student_record, fout)
    fout.close()

def read_data(filename):
    fin = open(filename, "rb")
    student_record = {}
    while True:
        try:
            student_record = pickle.load(fin)
            print(student_record)
        except:
            break
    fin.close()

def update_data(filename, updated_filename):
    fin = open(filename, "rb")
    fout = open(updated_filename, "wb")
    student_record = {}
    roll_number = int(input("Enter roll number to update marks: "))
    found = False
    while True:
        try:
            student_record = pickle.load(fin)
            # print(student_record)
            if( student_record["roll number"]==roll_number ):
                new_marks = int(input("Enter updated marks: "))
                student_record["marks"] = new_marks
                pickle.dump(student_record, fout)
                found = True
            else:
                pickle.dump(student_record, fout)
        except:
            break
    if( found ):
        print(f"Marks of student with roll number {roll_number} is updated!")
    else:
        print(f"No student with roll number {roll_number} found!")
    fin.close()
    fout.close()

# write_data("records.dat")
read_data("records.dat")
# update_data("records.dat", "updated_records.dat")



