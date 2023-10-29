from observer import ChatRoom, User
from factory import PhoneDisplay, TVDisplay

if __name__ == "__main__":
    chat_room = ChatRoom("General Chat")

    user1 = User("Alma")
    user2 = User("Beksultan")

    phone_display = PhoneDisplay()
    tv_display = TVDisplay()

    chat_room.register_observer(user1)
    chat_room.register_observer(user2)

    chat_room.send_message("Hello, everyone!")

    phone_display.show("Welcome to the chat!")
    tv_display.show("New message received")
