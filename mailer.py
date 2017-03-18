import smtplib, os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email import Encoders
from email.mime.text import MIMEText

emaillist=['abhijit.bangera@hotmail.com']
msg = MIMEMultipart('mixed')
msg['Subject'] = 'Arrest Warrent'
msg['From'] = 'xyz@gmail.com'
msg['To'] = ', '.join(emaillist)

part = MIMEBase('application', "octet-stream")

part.set_payload(open('C:'+os.sep+'Users'+os.sep+'abangerx'+os.sep+'Desktop'+os.sep+'WarrentDetails.txt', "rb").read())
Encoders.encode_base64(part)

part.add_header('Content-Disposition', 'attachment; filename="WarrentDetails.txt"')

msg.attach(part)
msg.add_header('To', msg['From'])
text = "Dear Sir, \n\n An arrest warrent has been generated due to XYZ reason by ZZZ complain.\n YOU MUST APPEAR IN PERSON TO RESOLVE THIS MATTER. \n\n Regards,\n FBI :)"
part1 = MIMEText(text, 'plain')
msg.attach(part1)

server = smtplib.SMTP_SSL("smtp.gmail.com",465)
# server.ehlo()
# server.starttls()

server.login("girishprasana@gmail.com", "blackhat89")
 
server.sendmail(msg['From'], emaillist , msg.as_string())
