import csv

with open("demo.csv", mode='w') as csvFile:
    fieldNames = ['fullname', 'email', 'number']

    writer = csv.DictWriter(csvFile, fieldnames=fieldNames)

    writer.writeheader()

    writer.writerow({'fullname': 'aakash', 'email': 'aakash@test.com', 'number': 987456541230})
    writer.writerow({'fullname': 'abhishek', 'email': 'abhishek@test.com', 'number': 987456541230})
    writer.writerow({'fullname': 'gautam', 'email': 'gautam@test.com', 'number': 987456541230})
    writer.writerow({'fullname': 'deep', 'email': 'deep@test.com', 'number': 987456541230})

print("Data inserted Successfully")