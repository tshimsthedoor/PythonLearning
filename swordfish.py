from _ast import Continue

print('Who are you?')
name = input()
if name != 'Joe':
   Continue
print('Hello, Joe. what is the password? (It is a fish.)')
password = input()
if password == 'swordfish':
    breakpoint

print('Access granted.')