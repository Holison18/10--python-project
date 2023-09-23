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
staff_mail = ['kobinaholison2002@gmail.com']

# define a function to save the excel sheet
def savefile():
    book.save(r'data.xlsx')
    print("Saved!")

# create a function to take user password
def get_email_password():
    password = input("Enter email password: ")
    return password

# create a function to mail student
def mailStudent(listofmails,msg):
    from_id = "kobinaakofiholison@gmail.com"
    password = get_email_password() # get password from user

    # use smtplib to login to the staff email
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(from_id,password)

    # for each student to warn send an email
    for email in range(0,len(listofmails)):
        to_id = listofmails[email] 
        message = MIMEMultipart()
        message['Subject'] = 'Attendance Report'
        message.attach(MIMEText(msg,'plain'))
        content = message.as_string()
        s.sendmail(from_id,to_id,content)
        s.quit()
    print("Message sent successfully!")

# create a function to send staff a message
def staffMail(mail_id,msg):
    from_id = 'kobinaakofiholison@gmail.com'
    password = get_email_password()

    # use smtplib to login into email
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.starttls() # start ttls
    s.login(from_id,password) # login to the email of the sender

    # send message to staff
    message = MIMEMultipart()
    message['Subject'] = 'Lack of attendance report' # write mail subject
    message.attach(MIMEText(msg,'plain')) # add message attachment
    content = message.as_string()

    # to id
    to_id = mail_id
    s.sendmail(from_id,to_id,content) # send message from sender to the staff
    s.quit() # quit smtp

# create a function to track attendance
def track(no_of_days,row_num,b):

    global staff_mail
    global list2
    global listofLack

    # loop through the list students row_num
    for student in range(0,len(row_num)):
        # if total of number of leaves == warning threshol
        if no_of_days[student] == 2:
            pass
        elif no_of_days[student] > 2:
            pass
