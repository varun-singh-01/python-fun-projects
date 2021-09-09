
#  @author Varun Singh
#  @email admin@talkhash.com
#  @create date 2021-09-09 16:02:29
#  @modify date 2021-09-09 16:02:29
#  @desc Sends an email

import smtplib, ssl, getpass

class Email(object):
    def __init__(self):
        self.port = 465  # SSL port
        self.smtp_server = "smtp.gmail.com" # smtp server address
        creds = self.login_credentials()    # Sender credentials
        self.sender_email = creds["email"]  # Senders email
        self.password = creds["pass"]       # Senders password
        # Create a secure SSL context
        self.context = ssl.create_default_context()
    

    def login_credentials(self):
        """ The senders login credentials - password is hidden. """
        sender_email = str(input(r"Enter your email here: "))
        password = getpass.getpass("Enter your password here: ")
        return {"email":sender_email, "pass":password}

    def message(self):
        """ Subject and message content """
        subject = str(input(r"Subject: "))
        message = str(input(r"Message: "))
        return str(f"Subject: {subject}\n"
                   f"{message}")

    def send_mail(self):
        """ Email control and forwarding """
        receiver_email = str(input(r"Enter receivers email here: ")) # Receivers email
        message = self.message()
        try:
            with smtplib.SMTP_SSL(self.smtp_server, self.port, context=self.context) as server:
                server.login(self.sender_email, self.password)
                server.sendmail(self.sender_email, receiver_email, message)
                print("\nEmail successfully sent!")
        except Exception as e:
            print("\nError occurred while trying to send the email.. Please try again. {}".format(e))


if __name__ == "__main__":
    Email().send_mail()