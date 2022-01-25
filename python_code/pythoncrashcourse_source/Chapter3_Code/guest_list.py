my_guests = ['ZengSiNa', 'LiZhiHan', 'LiYuZhen']

print(f"\nI am sorry to here that you can't come, {my_guests.pop()}!")

my_guests.append("ZouYin")

for i in range(3):
    print(f"\nThere is a party, would you come, {my_guests[i]}?")
print(my_guests)