

my_dict = {"a": 1, "b": 2, "c": 3}

# Convert to a list to access by index
keys = list(my_dict.keys())
values = list(my_dict.values())

print(keys[0])  # Output: "a"
print(values[0])  # Output: 1



random_key = random.choice(list(deck.keys()))
random_value = deck[random_key]












# Demo of dict, short for dictionary
# In Python a dictionary is collection of key value pairs.

# create dictionary
dictionary = {"key 1": "value 1", "key 2": "value 2"}
print(dictionary)
# print output is shown below each print statement
# {'key 1': 'value 1', 'key 2': 'value 2'}

# read value at specified key
value = dictionary["key 1"]
print(value)
# value 1

# read value at specified key
value = dictionary.get("key 2")
print(value)
# value 2

# change value at given key
dictionary["key 1"] = "new value 1"
print(dictionary)
# {'key 1': 'new value 1', 'key 2': 'value 2'}

# add another key value pair
dictionary["key 3"] = "value 3"
print(dictionary)
# {'key 1': 'new value 1', 'key 2': 'value 2', 'key 3': 'value 3'}

# collection of keys
keys = dictionary.keys()
print(keys)
# dict_keys(['key 1', 'key 2', 'key 3'])

# collection of values
values = dictionary.values()
print(values)
# dict_values(['new value 1', 'value 2', 'value 3'])

# remove a key value pair
value = dictionary.pop("key 1")
print(value)
# new value 1

print(dictionary)
# {'key 2': 'value 2', 'key 3': 'value 3'}

# remove everything
dictionary.clear()
print(dictionary)
# {}