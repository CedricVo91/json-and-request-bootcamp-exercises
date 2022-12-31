# Load .json from URL. Try translating the following instruction into code:
# use requests library and get function of this library to send a HTTPS request to the URL.
# print the content attribute of the object that is returned from the get request.
# Then, deserialize the content attribute
# explore the obtained dictionary


import json
import requests
import numpy as np
from pandas import json_normalize

# import numpy as np

url = "https://jsonplaceholder.typicode.com/posts"
r = requests.get(url)

print(type(r.content))  # content is in bytes
#json_data  = json_normalize(r.content) not really helpful


dict_from_string = json.loads(r.content)[0] # so I can enter the dictionary stored as list I need to add the [0]
#print(json_normalize(dict_from_string)) #json normalize gives me a pandas data frame table
print(type(dict_from_string)) #gives me a a dict 

print(dict_from_string.items())

#I dump the dictionary into a new json file.
with open("new_json_file.json", "w") as f:
    json.dump(dict_from_string,f, indent =2)