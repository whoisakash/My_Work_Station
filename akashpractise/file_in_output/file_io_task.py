'''r for read only, w for write, x for only creat,a for append text in file'''

print("r for read\n w for write\n x for only creat\n a for append text in file")
while True:
    op_code=str(input("Enter Code:- "))
    if op_code == "w":
        file_io = open("tastfile.txt","w")
        w_data=str(input("write your data:-"))
        file_io.write("Task File is ready...\n"+ w_data)
        file_io.close()
    elif op_code == "r":
        # file_io = open("tastfile.txt","w")
        # file_io.write("There is no data for read")
        file_io = open("tastfile.txt","r")
        read_taskfile= file_io.read()
        print(read_taskfile)
        file_io.close()
    elif op_code == "x":
        file_name= str(input("Enter file name:-"))
        file_io = open(file_name,"x")
        file_io.write("your file is creat")
        file_io.close()
        print("your file is created")
    elif op_code == "a":
        file_io = open("tastfile.txt","a")
        a_task = str(input("enter data:- "))
        file_io.write("your file is creat")
        file_io.close()
    else:
        print("enter valid code")
