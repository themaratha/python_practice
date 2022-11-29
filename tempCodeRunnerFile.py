f=open("file.txt",'w')
f.write("this file is all about file handling. ")
f=open("file.txt",'a')      #append mode
f.write("this file is append command.")   
f.close()