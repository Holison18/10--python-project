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

# Warning messages
m1 = "warning!!! you can take only one more day leave for COE 354 class"
m2 = "warning!!! you can take only one more day leave for COE 321 class"
m3 = "warning!!! you can take only one more day leave for COE 356 class"

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
    print("Staff mail send successfully!")

# create a function to track attendance
def track(no_of_days,row_num,b):

    global staff_mail
    global list2
    global listofLack

    # loop through the list students row_num
    for student in range(0,len(row_num)):
        # if total of number of leaves == warning threshol
        if no_of_days[student] == 2:
            if b is 1:
                list_of_studentsTR.append(sheet.cell(row=row_num[student],column=2).value)
                mailStudent(list_of_studentsTR,m1)
            elif b is 2:
                list_of_studentsTR.append(sheet.cell(row=row_num[student],column=2).value)
                mailStudent(list_of_studentsTR,m2)
            else:
                list_of_studentsTR.append(sheet.cell(row=row_num[student],column=2).value)
                mailStudent(list_of_studentsTR,m3)
        elif no_of_days[student] > 2:
            if b is 1:
                # adding roll no
                list2 = list2+str(sheet.cell(row=row_num[student], column=1).value)
  
                # student mail_id appending
                listofLack.append(sheet.cell(row=row_num[student], column=2).value)
                subject = "COE 354"  # subject based on the code number
  
            elif b is 2:
                list2 = list2+str(sheet.cell(row=row_num[student], column=1).value)
                listofLack.append(sheet.cell(row=row_num[student], column=2).value)
                subject = "COE 321"
  
            else:
                list2 = list2+str(sheet.cell(row=row_num[student], column=1).value)
                listofLack.append(sheet.cell(row=row_num[student], column=2).value)
                subject = "COE 356"
        
        # if treshold is crossed modify the message
        if list2 != "" and len(listofLack) != 0:
            # message for student
            msg1 = "you have lack of attendance in " + subject + " !!!"
  
            # message for staff
            msg2 = "the following students have lack of attendance in your subject : "+list2
  
            mailStudent(listofLack, msg1)  # mail to students
            staff_id = staff_mail  
            staffMail(staff_id, msg2)  # mail to staff