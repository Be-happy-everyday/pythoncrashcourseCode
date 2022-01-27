import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename, encoding='utf-8') as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it
def greet_user():
    """Greet the user by name."""

    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        #print(f"Welcome back, {username}!")
        filename = 'username.json'
        username = input("What's your name?")

        with open(filename,'w') as f:
            json.dump(username,f)
            print(f"We'll remember you when you come back, {username}.")

greet_user()