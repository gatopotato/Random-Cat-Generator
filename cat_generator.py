import requests
import json 
from PIL import Image
from io import BytesIO

def jprint(obj):
    text=json.dumps(obj,sort_keys =  True, indent=4)
    print(text)

def url():
    base_url = "https://cataas.com/cat"
    print("Random Cat Generator")
    print("1.Will return a random cat")
    print("2.Will return a random cat with a :tag")
    print("3.Will return a random gif cat")
    print("4.Will return a random cat saying :text")
    print("5.Will return a random cat with a :tag and saying :text")
    print("6.Will return a random cat saying :text with text's :size and text's :color")
    choice = int(input("Please enter your choice: "))

    match choice:
        case 1:
            ext = ""
        case 2:
            tag = input("Input tag: ")
            ext="/"+tag
        case 3:
            ext= "/gif"
        case 4:
            text = input("Enter text: ")
            ext = "/says/" + text
        case 5:
            tag = input("Input tag: ")
            text = input("Enter text: ")
            ext = "/"+tag+"/says/"+text
        case _:
            print("Invalid Choice. Try Again")
            url()
    return base_url+ext

final_url = url()
response = requests.get(final_url)
if response.status_code == 200:
    print("Displaying Content")
    img = Image.open(BytesIO(response.content))
    img.show()
else:
    print("Error ", end = " ")
    print(response.status_code)