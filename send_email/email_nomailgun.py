import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
 
fromaddr = "twitterfreeze@gmail.com"
toaddr = "ychen108@sheffield.ac.uk"
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "test"
 
body = "testing testing"
 
msg.attach(MIMEText(body, 'plain'))
 
filename = "text2.txt"
attachment = open("F:\\Sublime Text 3\\Python Practise\\send_email\\text2.txt", "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "twitfree")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()