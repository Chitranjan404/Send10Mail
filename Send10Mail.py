import smtplib
senderMail='justin.fuller15537@gmail.com'
recieverMail='chitranjan15537@gmail.com'
body='Hello world!'

server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(senderMail,'storm_thunder')
server.ehlo()
server.sendmail('bill@microsoft.com',recieverMail,body)
server.quit()