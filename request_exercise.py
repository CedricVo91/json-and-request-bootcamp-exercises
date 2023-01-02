import json
import requests
import numpy as np
from pandas import json_normalize

##theory block

#authentication to a restful api is always a post request!
resp = requests.post(
    "https://motion.propulsion-home.ch/backend/api/auth/token/",
    data={"email": "python@propulsionacademy.com", "password": "python_course2020"},
)

#print(type(resp.content)) #gives me the response in bytes
login_data = resp.json() #gives me the response as a python dictionary () i.e. the json _strong has already been deserialized



#print(type(login_data))
#print(login_data)

token = login_data["access"]
#This is the token you will have to copy and paste into the headers of your subsequent authenticated request

#Now that we have the access token let's retrieve all the posts of the logged in user. This is a GET request since we don't write any data to the API
resp = requests.get(
    "https://motion.propulsion-home.ch/backend/api/social/posts/me/",
    headers={
        "Authorization": f"Bearer {token}",
    },
)

posts = resp.json() #deserialize
#print(posts)3

#by creating a new json file I find it easier to inspect the file than in the terminal
with open("new_json_file_request_response.json", "w") as f2:
    json.dump(posts, f2, indent = 2) #here we need to always entere deserialized variable i.e python dict to reserialize in a json


#print(posts["results"][:2])
#I just have information on posts of one user i.e. one dictionary

#we create a new post now using a post request
resp2 = requests.post(
    "https://motion.propulsion-home.ch/backend/api/social/posts/me/",
    headers={
        "Authorization": f"Bearer {token}",
    },
    data = json.dumps( #here we have to serialize the deserialized python object (i.e. dictionary) into a format the http can work with i.e. a serialized json string
        {"content": "Post created with the request module by Cédric Vogt"}
    )
)

new_post = resp2.json()
print(new_post)


##exercise block