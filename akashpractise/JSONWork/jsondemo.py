import json

BOD = {
    "Name":"Akash",
    "Role":"CEO",
    "Share":75
}

with open ("BOD.json","w") as writeData:
    json.dump(BOD, writeData)

with open ("BOD.json","r")as readData:
     showdata = json.load(readData)
     for i in showdata:
         print(i,showdata[i],sep=":",end=" <> ")
print()
# print(showdata)