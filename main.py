"""
Application search for a possible buyer of the car

"""
import base64
import json

dictionary: dict = {}
try:
    with open('Code.txt', 'r', encoding='utf-8', errors='ignore') as file:
        data: object = file.read()
except FileNotFoundError:
    print("File don't found")
try:
    decode: str = base64.b64decode(data).decode('utf-8')
    dictionary = json.loads(decode)
except NameError:
    print("Name Error")
except UnicodeDecodeError:
    print("Decode Error")

try:
    for cars in dictionary["cars"]:
        for customers in dictionary["customers"]:
            if cars["price"] / 100 <= customers["balance"]:
                print(
                    f'Cars {cars["brand"]} {cars["model"]} can be offered for,'
                    f' {customers["firstname"]} {customers["lastaname"]}.')
except NameError:
    print("Incorrect name in dictionary or dictionary don't created")
except KeyError:
    print("Error key")
