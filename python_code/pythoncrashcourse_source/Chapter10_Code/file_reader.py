
with open('pythoncrashcourse_source\Chapter10_Code\pi_digits.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

print(lines)
    #for line in file_object:
        #print(line.rstrip())
    #contents = file_object.read()
    #print(contents.rstrip())
#print(contents)