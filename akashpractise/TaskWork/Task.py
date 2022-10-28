import csv

# Collect cricket players info and insert line by line in csv file and in excel also
# Name, Age, Number of matches played, Runs in {odi, T20, Ipl, Test}, No. of wickets{odi, T20, Ipl, Test}, Total Ints Run


file_name=str(input("Enter File Name(.csv):- "))
print("w =write, r =read, x = create file, a =add detail, 0 =Exit")
fieldNames = ["Fullname", "Age", "Total Match","Total Runs",
              "ODI runs","T20 runs","IPl runs","Test runs",
              "ODI wickets","T20 wickets","IPl wickets","Test wickets"]
while True:
    _mode = str(input("Enter work:- "))
    if _mode=="w":
        with open(file_name, mode="w") as csvFile:

            writer = csv.DictWriter(csvFile, fieldnames=fieldNames)

            writer.writeheader()
            _name = str(input("Enter Name:- "))
            _age = str(input("Enter Age:- "))
            match_no = str(input("Enter Total Match play:- "))
            total_runs = str(input("Enter Total Runs:- "))
            odi_runs = str(input("Enter ODI Runs:- "))
            t20_runs = str(input("Enter T20 Runs:- "))
            ipl_runs = str(input("Enter IPL Runs:- "))
            test_runs = str(input("Enter Test Runs:- "))

            odi_wck = str(input("Enter ODI Wicket:- "))
            t20_wck = str(input("Enter T20 Wicket:- "))
            ipl_wck = str(input("Enter IPL Wicket:- "))
            test_wck = str(input("Enter Test Wicket:- "))

            data_list = ({'Fullname': _name, 'Age': _age, 'Total Match': match_no,'Total Runs':total_runs,
                          'ODI runs':odi_runs,'T20 runs':t20_runs,'IPl runs':ipl_runs,'Test runs':test_runs,
                          'ODI wickets': odi_wck, 'T20 wickets': t20_wck, 'IPl wickets': ipl_wck, 'Test wickets': test_wck
                          })
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
            _age = str(input("Enter Age:- "))
            match_no = str(input("Enter Total Match play:- "))
            total_runs = str(input("Enter Total Runs:- "))
            odi_runs = str(input("Enter ODI Runs:- "))
            t20_runs = str(input("Enter T20 Runs:- "))
            ipl_runs = str(input("Enter IPL Runs:- "))
            test_runs = str(input("Enter Test Runs:- "))

            odi_wck = str(input("Enter ODI Wicket:- "))
            t20_wck = str(input("Enter T20 Wicket:- "))
            ipl_wck = str(input("Enter IPL Wicket:- "))
            test_wck = str(input("Enter Test Wicket:- "))

            data_list = ({'Fullname': _name, 'Age': _age, 'Total Match': match_no, 'Total Runs': total_runs,
                          'ODI runs': odi_runs, 'T20 runs': t20_runs, 'IPl runs': ipl_runs, 'Test runs': test_runs,
                          'ODI wickets': odi_wck, 'T20 wickets': t20_wck, 'IPl wickets': ipl_wck,
                          'Test wickets': test_wck
                          })
            writer.writerow(data_list)
        print("Data written successfully")
    elif _mode == "0":
        break
    else:
        print("Invalid code")

