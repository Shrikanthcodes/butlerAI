from utils.runtime_routines import Routines

def main():
    # Create a Routines instance
    run = Routines("butler.db", "auth.db")

    # User interaction loop
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            run.register_user(username, password)
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            user_id = run.authenticate_user(username, password)
            if user_id:
                conversation_id = run.new_user_new_chat(username)
                run.get_chat_and_print(conversation_id)
        elif choice == '3':
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()


# from utils.runtime_routines import Routines

# if __name__ == "__main__":
#     # Create a Routines instance
#     run = Routines("butler.db")

#     # Create the initial tables in the database
#     run.create_tables_initial()

#     # Create a new user and chat conversation
#     user_id, conversation_id = run.new_user_new_chat("Hithesh")

#     # Get and print the chat conversation
#     run.get_chat_and_print(conversation_id)
