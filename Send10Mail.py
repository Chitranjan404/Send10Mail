import smtplib
senderMail='***SENDERS MAIL*****'
recieverMail='*****RECIEVERS MAIL******'
body='Hello world!'

server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(senderMail,'*****SENDERS MAIL PASSWORD*******')
server.ehlo()
server.sendmail('bill@microsoft.com',recieverMail,body)
server.quit()
