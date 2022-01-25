alien_0 = {'color' : 'green', 'speed' : 'slow'}

#point_value = alien_0.get('points')
#print(point_value)

for key,value in alien_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

for key in alien_0.keys():
    print(key.title())