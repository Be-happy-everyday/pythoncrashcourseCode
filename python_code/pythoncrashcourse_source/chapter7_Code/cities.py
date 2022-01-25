prompt = "\nPlease enter the name of a city you have visted: "
prompt += "\n(Enter 'quit' when ypu are finished.)"

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")