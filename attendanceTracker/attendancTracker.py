import openpyxl
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# loading the excel book
book = openpyxl.load_workbook('data.xlsx')

# choose the sheet
sheet = book['sheet1']

# counting number of rows/students
row = sheet.max_row

# variable for looping for inputs
response = 1

# counting the number of columns for subjects
columns  = sheet.max_column

# create a list of students to remind
list_of_studentsTR = []

# to concatenate list of roll numbers with lack of attendance
list2 = []

# list of roll numbers with lack of attendance
listofLack = []

# staff mail id
staff_mail = ['akofiholisonkobina@gmail.com']

# define a function to save the excel sheet
def savefile():
    book.save(r'data.xlsx')
    print("Saved!")

# create a function to track attendance