from sys import argv

script, user_name = argv
prompt = '> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like {user_name}?")
likes = input(prompt)

print("Where do you live {user_name}?")
lives = input(prompt)

print(f"How old are you {user_name}?")
age = input(prompt)

print(f"What kind of computer do you have?")
computer = input(prompt)

print(F"""
Alright, so you said {likes} about liking me.
And you live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")