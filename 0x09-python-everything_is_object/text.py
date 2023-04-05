#!/usr/bin/python3
user_inputs = ()

while True:
    user_input = input("Enter some text: ")
    if not user_input:
        break
    user_inputs += (user_input,)  # add the user input to the tuple

print("User inputs:", user_inputs)
