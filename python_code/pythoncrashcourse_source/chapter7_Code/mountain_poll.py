from timeit import repeat
from urllib import response


responses = {}

# Set a flag to indicate that polling is active
polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWaht's your name?")
    response = input("Which mountain would you like to climb someday? ")

    # Store the response in the dictionary.
    responses[name] = response

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person repond? (yes/ no)")
    if repeat == 'no':
        polling_active = False

#Polling is complete. Show the results.
print("\n--- Poll Result ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")