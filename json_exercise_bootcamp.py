# Load .json from URL. Try translating the following instruction into code:
# use requests library and get function of this library to send a HTTPS request to the URL.
# print the content attribute of the object that is returned from the get request.
# Then, deserialize the content attribute
# explore the obtained dictionary


import json
import requests
import numpy as np
from pandas import json_normalize

## theory block

url = "https://jsonplaceholder.typicode.com/posts"
r = requests.get(url)

print(type(r.content))  # content is in bytes
#json_data  = json_normalize(r.content) not really helpful


dict_from_string = json.loads(r.content)[0] # so I can enter the dictionary stored as list I need to add the [0]
#print(json_normalize(dict_from_string)) #json normalize gives me a pandas data frame table
#these steps above are called deserialization
#print(type(dict_from_string)) #gives me a a dict 

#print(dict_from_string.items())

#I dump the dictionary into a new json file. -> serialization
with open("new_json_file.json", "w") as f:
    json.dump(dict_from_string,f, indent =2)



##exercise block - nobel prize

#1.How many Nobel prizes were given per category?
#2.Flatten the Data Structure.
#3.How many Nobel prizes were given to people called ‘Michael’?
#4.What is the smallest relative share of a Nobel prize ever given?
#5.Which laureates were awarded multiple prizes?
#6.Which laureates were awarded prizes in multiple categories?

url2 = "http://api.nobelprize.org/v1/prize.json" #always use a string for the url when entering it into a request function

r = requests.get(url2)

#print(r.headers)
#print(r.status_code)
#print(type(r.content)) #bytes
#print(type(r.text)) #serialized Json content

nobel_prize = r.json() #deserialization using request library
#print(type(nobel_prize)) #python dic

#open a json file to read it more easily
with open("nobel_prize.json", "w") as f2:
    json.dump(nobel_prize, f2, indent = 2) 

#inspecting the file without looking at the json file
#get the keys
nobel_prize.keys() #I get one key called "prizes"
#nobel_prize["prizes"].keys() # error as for nobel_prize["prizes"] we get a list
#print(nobel_prize["prizes"][0].keys()) #dict keys ['year', 'category', 'laureates']



#1.How many Nobel prizes were given per category?
#hypothesis: {"category_key_unique": "laureates"}


q1_dic_year_categories = []

for list_entry_as_dic in nobel_prize["prizes"]:
    q1_dic_year_categories.append(list_entry_as_dic["category"])
    

q1_dic_categories_unique_keys_dic = dict.fromkeys(q1_dic_year_categories)
#adding an empty table to as values to the key, so I can add entries for each category later
for key in q1_dic_categories_unique_keys_dic:
    q1_dic_categories_unique_keys_dic[key] = 0

#print(q1_dic_categories_unique_keys_dic) #works

#adding an empty table to as values to the key, so I can add entries for each category later
no_nobel_price_awarded = dict.fromkeys(q1_dic_year_categories)
for key in no_nobel_price_awarded:
    no_nobel_price_awarded[key] = 0

#should give me the amount of prices per category & amount of times per category where no prize has been awared -> test after break with data frame
for list_entry_as_dic in nobel_prize["prizes"]:
    #print(len(list_entry_as_dic["laureates"])) #for every entry in the json dic we have the list 
    try: 
        q1_dic_categories_unique_keys_dic[list_entry_as_dic["category"]] += len(list_entry_as_dic["laureates"])
    except KeyError:
        #print(list_entry_as_dic) #we have a keyerror in our json because there are entries where no nobel laureate was awarded, thus we do not have a laureates key
        no_nobel_price_awarded[list_entry_as_dic["category"]] += 1 #add on feature: list of times per category no prize has been awared
        pass
        
print(q1_dic_categories_unique_keys_dic)
print(f"amount of times per category where no nobel prize was awared: {no_nobel_price_awarded}")
    

#2.Flatten the Data Structure.

# use from pandas import json_normalize to make inspection of data files easier

import pandas as pd
request_dic = requests.get(url2).json()["prizes"]
df = json_normalize(request_dic)
#print(df.head())
df = df.explode("laureates").reset_index(drop = True) #explode merges the
#print(df.head())
df2 = json_normalize(df["laureates"]) # I can apply json_normalize on any deserialize json python dic object
#print(df2.head())
df_final = pd.concat([df,df2], axis = 1).drop(["laureates","overallMotivation"], axis = 1)
print(df_final.head())


