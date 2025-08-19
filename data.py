from generate_data import *


class CompleteData:

    generate = GenerateData()

#Тело запроса для создания пользователя
    def body_create_user(self):
        return {"email": self.generate.create_email(),
                "password": self.generate.create_password(),
                "name": self.generate.create_name()
                }

#Генерированная почта
    def email_input(self):
        return self.generate.create_email()


DRIVER_NAME = None


