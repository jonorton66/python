path = 'WODList.txt'

print('Hello')
print('What Activity Do you want to do?')
interest = raw_input()

wod_file = open(path, 'r')
wod = wod_file.read()
answer = wod.find(interest)
print(answer)

wod_file.close()
