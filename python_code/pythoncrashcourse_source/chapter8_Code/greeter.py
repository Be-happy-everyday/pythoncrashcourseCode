def greet_user(names):
    """Display a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

#usernames = ['hannah', 'ty', 'margot']
usernames = list('usernames')
print(usernames)
#greet_user(usernames)