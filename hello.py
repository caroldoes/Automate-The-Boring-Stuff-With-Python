#This program says hello and asks my name

print('Hello, world!')
my_name = input('What is your name? ')
print('Nice to meet you, ' + my_name)
print('The length of your name is: ')
print(len(my_name), 'letters')

print('How old are you? ')
my_age = int(input())
print('You will be ' + str(int(my_age + 1)) + ' in a year.')