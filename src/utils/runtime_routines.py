from services.database_service import DatabaseService
from services.chat_service import ChatService
from utils.formatting import ChatFormatter as fmt
import sqlite3
import bcrypt
import os

class Routines:
    """A service class for defining run_time routines/operations."""

    def __init__(self, db_name, auth_db_name):
        self.db_name = db_name
        self.auth_db_name = auth_db_name
        self.ds = DatabaseService(self.db_name)
        self.cs = ChatService()
        self.initialize_auth_db()

    def initialize_auth_db(self):
        if not os.path.exists(self.auth_db_name):
            auth_conn = sqlite3.connect(self.auth_db_name)
            cursor = auth_conn.cursor()
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
            ''')
            auth_conn.commit()
            auth_conn.close()

    def register_user(self, username, password):
        auth_conn = sqlite3.connect(self.auth_db_name)
        cursor = auth_conn.cursor()
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        try:
            cursor.execute('''
            INSERT INTO users (username, password) VALUES (?, ?)
            ''', (username, password_hash))
            auth_conn.commit()
            print("User registered successfully!")
        except sqlite3.IntegrityError:
            print("Username already exists.")
        finally:
            auth_conn.close()

    def authenticate_user(self, username, password):
        auth_conn = sqlite3.connect(self.auth_db_name)
        cursor = auth_conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()
        auth_conn.close()
        if user and bcrypt.checkpw(password.encode('utf-8'), user[2]):
            print("Login successful!")
            return user[0]  # Return user ID
        else:
            print("Invalid username or password.")
            return None

    def new_user_new_chat(self, user_name):
        self.ds.create_tables()
        user_id = self.ds.add_user(user_name)
        conversation_id = self.ds.add_conversation(user_id)
        self.cs.complete_chat(self.ds, conversation_id)
        return user_id, conversation_id

    def get_chat_and_print(self, conversation_id):
        print("\nChat Transcript: for conversation_id: " + str(conversation_id) + "\n")
        chat_history = fmt.convert_chat_store_to_string_print(
            self.ds.get_conversation_chat_history_by_id(conversation_id))
        print(chat_history)

    def create_tables_initial(self):
        self.ds.create_tables()



# from services.database_service import DatabaseService
# from services.chat_service import ChatService
# from utils.formatting import ChatFormatter as fmt


# class Routines:
#     """
#     A service class for defining run_time routines/operations.

#     Attributes:
#         db (SQLService): The database service instance.
#     """

#     def __init__(self, db_name):
#         """Initialize a Routines instance.
#         """
#         self.db_name = db_name
#         self.ds = DatabaseService(self.db_name)
#         self.cs = ChatService()

#     def new_user_new_chat(self, user_name):
#         """
#         Create a new user and a new chat conversation.

#         Args:
#             user_name (str): The name of the user.

#         Returns:
#             None: dumps the conversation into the conversations table.
#         """
#         self.ds.create_tables()
#         user_id = self.ds.add_user(user_name)
#         conversation_id = self.ds.add_conversation(user_id)
#         self.cs.complete_chat(self.ds, conversation_id)
#         return user_id, conversation_id

#     def get_chat_and_print(self, conversation_id):
#         """
#         Get the chat conversation by ID and print it.

#         Args:
#             conversation_id (int): The ID of the conversation.
#         """
#         print("\nChat Transcript: for conversation_id: "+str(conversation_id)+"\n")
#         chat_history = fmt.convert_chat_store_to_string_print(
#             self.ds.get_conversation_chat_history_by_id(conversation_id))
#         print(chat_history)

#     def create_tables_initial(self):
#         """Create the initial tables in the database."""
#         self.ds.create_tables()
