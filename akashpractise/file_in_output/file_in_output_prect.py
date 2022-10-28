print_yourfile= open("yourfile.txt", "w")

print_yourfile.write("Yourfile name is ready for try")
print_yourfile.close()

print_yourfile= open("yourfile.txt","r")
read_yourfile = print_yourfile.read()
print_yourfile.close()
print(read_yourfile)
