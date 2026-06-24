#write json file:

#import json
import json

#json file
user ={
    "name": "Ray",
    "age": 18,
    "city": "New York",
    "gender": "male"
}

#write json file
with open(r"C:\Users\User\OneDrive\Documents\HelloPython\AI\AItest\user.json","w",encoding="utf-8") as f: #w: write
    #ensure_ascii=False: write chinese, otherwise(True) only accept english
    #indent=4: add space
    json.dump(user,f,indent=4)

#read json file
with open(r"C:\Users\User\OneDrive\Documents\HelloPython\AI\AItest\user.json","r",encoding="utf-8") as f: #r: read
    user = json.load(f)
    print(user)