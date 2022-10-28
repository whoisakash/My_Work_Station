import json

# JSON - Javascript Object Notation
# Use - Interchange data from web to app
# Js Datatype - Number, String, Boolean, Null, Object , Array
# Structure - key:value pair

# Serializing Json - Convert python object to json. For conversion - dump() and dumps()
# Deserializing Json - Convert Json to python object. For conversion - loads and load


employee = {
    "Name": "Akash",
    "Position": "CEO",
    "Experience": 5
}


# with open("employee.json", "w") as writeData:
#     json.dump(employee, writeData)

with open("employee.json", "r") as readData:
    showData = json.load(readData)
print(showData)


