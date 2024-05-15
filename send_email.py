import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "farukh.mushtaq@gmail.com"
    password = "hpsvehsyfnqbisia"
    context = ssl.create_default_context()
    receiver = "farukh.mushtaq@gmail.com"

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


if __name__ == '__main__':
    raw_message = " i want to meet you"
    receiver_email = "pakipcs@yahoo.com"
    message = f"""Subject: Email Portfolio App\n

   Sent Following Message: {raw_message}
   From: {receiver_email}
       """
    print("Sending Email...")
    send_email(message)
    print("Email Sent...")


