from helpers.redis import redis_connection
from helpers.user import sign_up
from helpers.message import create_message

from threading import Thread
from faker import Faker
from random import randint
import atexit

class Emulation(Thread):
    def __init__(self, name, users):
        Thread.__init__(self)
        self.name = name
        self.users = users
        self.user_id = sign_up(name)

    def run(self):
        for i in range(5):
            text = fake.sentence(nb_words=5, variable_nb_words=True, ext_word_list=None)
            recipient = users[randint(0, quantity_of_users - 1)]
            create_message(self.user_id, text, recipient)

def on_emulation_off():
    online = redis_connection.smembers("online")
    for i in online:
        redis_connection.srem("online", i)
        print(f"{i} exits app. Have a good day!")

if __name__ == '__main__':
    atexit.register(on_emulation_off)
    quantity_of_users = 3
    fake = Faker()
    users = [fake.profile(fields=["name"], sex=None)["name"] for user in range(quantity_of_users)]
    threads = []

    for i in range(quantity_of_users):
        print(f"User: {users[i]}")
        threads.append(Emulation(users[i], users))

    for t in threads:
        t.start()