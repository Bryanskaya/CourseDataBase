from load_config_file import *
import smtplib
from email.mime.text import MIMEText
from random import randint

class MailManager():
    smtp_ssl_host = None
    smtp_ssl_port = None
    username = None
    password = None
    sender = None
    server = None
    codes = {}

    def __init__(self, obj: EmailConfig):
        self.smtp_ssl_host = obj.smtp_ssl_host
        self.smtp_ssl_port = obj.smtp_ssl_port
        self.username = obj.username
        self.password = obj.password
        self.sender = obj.sender

        # self.server = smtplib.SMTP_SSL(self.smtp_ssl_host, self.smtp_ssl_port)
        # self.server.login(self.username, self.password)

    def generate_mail(self, target):
        self.server = smtplib.SMTP_SSL(self.smtp_ssl_host, self.smtp_ssl_port)
        self.server.login(self.username, self.password)

        code = self.registry_code(target)
        msg = MIMEText("Здравсвуйте, Ваш код для восстановления пароля к аккаунту в "
                       "Сообществе Охоников: " + code)
        msg['Subject'] = 'Восстановление пароля'
        msg['From'] = self.sender
        msg['To'] = ', '.join([target])

        self.server.sendmail(self.sender, [target], msg.as_string())

        self.server.quit()

    def __del__(self):
        pass
        # self.server.quit()

    def get_code(self, email):
        if email in self.codes.keys():
            code = self.codes[email]
            del self.codes[email]
            return code
        return None

    def generate_code(self):
        return '{:0>4d}'.format(randint(0, 9999))

    def registry_code(self, email):
        self.codes[email] = self.generate_code()
        return self.codes[email]

