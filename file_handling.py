# allows program to manage files - open(filename,mode)
# with open("file.txt","r") as f:
#     print("Read with r mode \n",f.read())

# write mode removes all previous data in the file
# with open("file.txt","w") as f:
#     f.write("Written with write mode \n")

# use append function to add to file 
# with open("file.txt","a") as f:
#     f.write("Written with append mode \n")


# with open("file.txt","r+") as f: #if written with this then file data is erased
#     # f.seek(6) #from where you fant to read the file
#     pos = f.tell()
#     content = f.read()
#     print("Currently pointer is at :",pos,end="\n")
#     print(content)

with open("file.txt","r") as f:
    content = f.read()
    print(content)