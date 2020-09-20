import pandas as pd
import numpy as np

# name of students you want to search
students = ['abc', 'def', 'ghi', 'jlk', 'mno']
print(students)

excel_file = pd.ExcelFile('students.xlsx') # It loads xl file
no_of_sheets = len(excel_file.sheet_names)
print('No. of sheets:', no_of_sheets)

record = [['a']]*no_of_sheets

# It take the data from sheet1 and pass it as it is to variable 'df'
n = 0
for sheet in excel_file.sheet_names:
    df = excel_file.parse(sheet)

    rec = pd.DataFrame() # making record dataframe
    
    rec = df['names']
    record[n] = np.array(rec) # converting records to array
    record[n] = list(record[n]) # converting it to a list
    n += 1

print('Student\'s names in record:', record)

print('\nStudents exist in record:')
i = 1

for rec in record:
    print('=== sheet #', i, '===')
    i += 1
    j = 1
    
    for student in students:
        if student in rec:
            print(student,j)
            j += 1
            
            
            
