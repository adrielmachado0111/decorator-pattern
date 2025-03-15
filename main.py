from abc import ABC, abstractmethod

class IEmail(ABC):
    @abstractmethod
    def send():
        pass

class Email:
    def __init__(self, IEmail):
        self._email = IEmail
    def send():
        print("send email")
        return

class EmailDecorador:
    def __init__(self, IEmail):
        self._email = IEmail
    def send():
        print("email sended")
        return

class SmsDecorador(EmailDecorador):
    def send():
        print("hacer envio por sms")
        return super().send()

class TelegramDecorator(EmailDecorador):
    def send(self):
        print("hacer envio por telegram")
        return super().send()



