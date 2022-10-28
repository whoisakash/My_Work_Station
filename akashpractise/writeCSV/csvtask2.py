import csv
file_name=str(input("Enter File Name(.csv):- "))
print("w =write, r =read, x = create file, a =add detail, 0 =Exit")
fieldNames = ["Fullname", "Email", "Number"]
while True:
    _mode = str(input("Enter work:- "))
    if _mode=="w":
        with open(file_name, mode="w") as csvFile:

            writer = csv.DictWriter(csvFile, fieldnames=fieldNames)

            writer.writeheader()
            _name = str(input("Enter Name:- "))
            _email = str(input("Enter Email(@gamil.com):- "))
            phone_no = str(input("Enter Phone no.:- "))
            data_list = ({'Fullname': _name, 'Email': _email, 'Number': phone_no})
            writer.writerow(data_list)
            print(data_list)
        print("Data written successfully")
    elif _mode == "r":
        with open(file_name, mode="r") as csvFile:
            csv_reader = csv.DictReader(csvFile, fieldnames=fieldNames)
            for row in csv_reader:
                print(row)
    elif _mode == "x":
        with open(file_name, mode="x") as csvFile:
            print("Your file was created")
    elif _mode == "a":
        with open(file_name, mode="a") as csvFile:

            writer = csv.DictWriter(csvFile, fieldnames=fieldNames)

            _name = str(input("Enter Name:- "))
            _email = str(input("Enter Email(@gamil.com):- "))
            phone_no = str(input("Enter Phone no.:- "))
            data_list = ({'Fullname': _name, 'Email': _email, 'Number': phone_no})
            writer.writerow(data_list)
        print("Data written successfully")
    elif _mode == "0":
        break
    else:
        print("Invalid code")



