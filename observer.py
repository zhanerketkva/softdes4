class Subject:
    def register_observer(self, observer):
        pass

    def remove_observer(self, observer):
        pass

    def notify_observers(self, message):
        pass

class ChatRoom(Subject):
    def __init__(self, name):
        self.name = name
        self.users = []

    def join(self, user):
        self.users.append(user)

    def leave(self, user):
        self.users.remove(user)

    def send_message(self, message):
        self.notify_observers(message)

    def register_observer(self, observer):
        self.users.append(observer)

    def remove_observer(self, observer):
        self.users.remove(observer)

    def notify_observers(self, message):
        for user in self.users:
            user.update(self, message)

class Observer:
    def update(self, chat_room, message):
        pass

class User(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, chat_room, message):
        print(f"{self.name} received a new message in '{chat_room.name}': {message}")
