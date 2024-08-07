from config import MY_EMAIL, MY_PASSOWRD, PORT_EMAIL, HOST
import smtplib

def send_mail(name, mail, msg):
    
    with smtplib.SMTP(host=HOST, port=PORT_EMAIL) as con_mail:
        con_mail.starttls()
        con_mail.login(MY_EMAIL, MY_PASSOWRD)
        con_mail.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject:Portfolio Servicios\n\nDe: {name} - {mail}\n\n{msg}")