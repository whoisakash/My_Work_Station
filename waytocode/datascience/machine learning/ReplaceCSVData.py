# data = open("grading.csv", "r")
#
# data = ''.join([i for i in data])
#
# data = data.replace("", "0")
#
#
# myFile = open("grade_system.csv", "w")
# myFile.writelines(data)
# myFile.close()

with open("grading.csv") as myFIle:
    data = myFIle.read().replace(' ', '0')

    print(data, file=open('grading_system.csv', 'w'))