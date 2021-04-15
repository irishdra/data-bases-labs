from helpers.redis import redis_connection

def admin_menu() -> int:
    print("\nADMIN MENU", 15 * "-", ">")
    print("0. Exit.")
    print("1. Most active senders.")
    print("2. Most active spammers.")
    print("3. Users online.\n")
    return int(input("Enter the number of action: "))

def admin():
    while True:
        action = admin_menu()

        if action == 0:
            print("Goodbye, have a good day :)")
            break

        elif action == 1:
            quantity = 5
            active_senders = redis_connection.zrange("sent", 0, quantity, desc=True, withscores=True)

            if len(active_senders) == 0:
                print("No senders at all :(")
            else:
                print("5 most active senders: ")
                for index, sender in enumerate(active_senders):
                    print(index + 1, ". ", sender[0], "(", int(sender[1]), ")")

        elif action == 2:
            quantity = 5
            active_spamers = redis_connection.zrange("spam", 0, quantity, desc=True, withscores=True)

            if len(active_spamers) == 0:
                print("No spamers at all :(")
            else:
                print("5 most active spamers: ")
                for index, sender in enumerate(active_spamers):
                    print(index + 1, ". ", sender[0], "(", int(sender[1]), ")")

        elif action == 3:
            online_users = redis_connection.smembers("online")
            if len(online_users) == 0:
                print("There no users online :(")
            else:
                print("Users online:")
                for user in online_users:
                    print(user)

        else:
            print("Choose only available [0-3] actions :)")

if __name__ == '__main__':
    admin()