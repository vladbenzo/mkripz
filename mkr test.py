from datetime import datetime
import base64

# Основний клас для мого повідомлення
class Message:
    def __init__(self, text):
        self.text = text

    def get_text(self):
        return self.text


# Декор, що збільшує можливості початкового (основного) повідомлення
class MyDekoMassage:
    def __init__(self, message):
        self._message = message

    def get_text(self):
        return self._message.get_text()


# Декоратори для всього разом
class MessEncryp(MyDekoMassage):
    def get_text(self):
        # Шифрую текст
        return base64.b64encode(self._message.get_text().encode()).decode()


class MessCompres(MyDekoMassage):
    def get_text(self):
        # Позбуваюсь пробілів та малих літер
        return ''.join(char for char in self._message.get_text() if char.isupper())


class DateTimeMessage(MyDekoMassage):
    def get_text(self):
        # Додаємо дату та час
        return f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} --> {self._message.get_text()}"


class AuthorNotification(MyDekoMassage):
    def get_text(self):
        # my ПІБ 
        return f"{self._message.get_text()} --> Цвєтков В.О"



if __name__ == "__main__":
    # Будь-який текст
    message = Message("my massage hola hola com estas")

    # Поетапне додавання декораторів
    message = MessEncryp(message)
    print("Encrypted message:", message.get_text())

    message = MessCompres(message)
    print("Compressed message:", message.get_text())

    message = DateTimeMessage(message)
    print("Compressed message + data:", message.get_text())

    message = AuthorNotification(message)
    print("Message + data + author:", message.get_text())
