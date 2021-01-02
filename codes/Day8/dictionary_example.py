#empty dictionary
dictionary_example={}
print(type(dictionary_example))

#add item
#dictionary_example[key_name]=value
#dictionary_example.update({key_name:value})
dictionary_example={}
dictionary_example["first_name"]="Anand"
dictionary_example["last_name"]="Kumar"
dictionary_example.update({"phone_no":1234567890})
print(dictionary_example)

#get value
print(dictionary_example["first_name"])

#update value
dictionary_example.update({"phone_no":999999999})
dictionary_example["phone_no"]=1111111111
print(dictionary_example)

#get all the keys
print(dictionary_example.keys())
#get all the values
print(dictionary_example.values())

#get all the items
print(dictionary_example.items())
