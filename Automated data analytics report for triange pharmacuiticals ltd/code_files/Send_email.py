import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

project_dir = os.path.abspath('..')

# ------------ Group email ----------------------------------------
msgRoot = MIMEMultipart('related')
me = 'healthcare.testmail@gmail.com'
password = r"yqle citn waue zopc"

to = ['mdfazlerabbyrabby@gmail.com', '']
cc = ['md.fazle.rabby34@gmail.com', '']
bcc = ['', '']

recipient = to + cc + bcc

subject = "Test Purpose: Triangle Pharmaceuticals limited monthly report"

email_server_host = 'smtp.gmail.com'
port =  465

msgRoot['From'] = me

msgRoot['To'] = ', '.join(to)
msgRoot['Cc'] = ', '.join(cc)
msgRoot['Bcc'] = ', '.join(bcc)
msgRoot['Subject'] = subject

msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

msgText = MIMEText('This is the alternative plain text message.')
msgAlternative.attach(msgText)

msgText = MIMEText("""
                       <img src="cid:report" height='1200', width='1250'><br>

                       """, 'html')

msgAlternative.attach(msgText)

# ---------  final pi added here  -----------------------
fp = open(project_dir+'/photos/merged_pic.png', 'rb')
report = MIMEImage(fp.read())
fp.close()

report.add_header('Content-ID', '<report>')
msgRoot.attach(report)

# # ----------- Finally send mail and close server connection ---
print('-----------------------------------------------')
print('sending mail')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
    # Login to the SMTP server using the sender's credentials.
    smtp_server.login(me, password)
    # Send the email. The sendmail function requires the sender's email, the list of recipients, and the email message as a string.
    smtp_server.sendmail(me, recipient, msgRoot.as_string())
print('mail sent')
print('-----------------------------------------------')