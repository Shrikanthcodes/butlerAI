class Table:
    """
    A class representing a database table.

    Attributes:
        name (str): The name of the table.
        columns (list): A list of column names in the table.
    """

    def __init__(self, name, columns):
        """
        Initialize a Table instance.

        Args:
            name (str): The name of the table.
            columns (list): A list of column names in the table.
        """
        self.name = name
        self.columns = columns


# A dictionary of Table instances representing the tables in the database.
Tables = {
    "users": Table("users", ["user_id", "name"]),
    "items": Table("items", ["item_id", "name", "category", "calories"]),
    "recipes": Table("recipes", ["recipe_id", "name", "ingredients", "instructions"]),
    "conversations": Table("conversations", ["conversation_id", "user_id", "chat_history"])
}

AuthTable = {
    "usersauth": Table("usersauth", ["id", "username", "password"])
}


class Schemas:
    """
    A class containing the schema definitions for the database tables.

    Each schema is a string defining the SQL CREATE TABLE statement for the corresponding table.

    conversations table columns: conversation_id, user_id, chat_history.
    users table columns: user_id, name.
    items table columns: item_id, name, category, calories.
    recipes table columns: recipe_id, name, ingredients, instructions.
    """

    conversations = """
    conversation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    chat_history TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
    """

    users = """
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
    """

    items = """
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    category TEXT,
    calories INTEGER
    """

    recipes = """
    recipe_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    ingredients TEXT,
    instructions TEXT
    """

    usersauth = """
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
    """
