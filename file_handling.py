# f=open("/exact_path/file.txt")
# print(f.read())    we can pass number of character 
# f.close()           close file can not be open
# print(f,readline())   read full line     give lines one by one


# f=open("txt_file",'a')     #'a' stands for append
# f.write("hello")
# f.close()
# f=open("txt_file",'r')        #'r' stands for read
# print(f.read())

# f=open("txt_file",'w')     #'w' stands for write and overwrite the value and vanishes old value
# f.write("hello")
# f.close()
# f=open("txt_file",'r')        #'r' stands for read
# print(f.read())


# f=open("txt_file",'x')     #'x' stands for creating a file 
# f.write("hello")
# f.close()
# f=open("txt_file",'r')        #'r' stands for read
# print(f.read())





# f=open("file.txt",'x')    #creation mode
f=open("file.txt",'w')      #write mode
f.write("hello")


f=open("file.txt",'w')
f.write("this file is all about file handling. ")
f=open("file.txt",'a')      #append mode
f.write("this file is append command.")   
f.close()

f=open("file.txt",'r')
print(f.read())             #read mode
