### this program for overwritting file .allready file present but open ,read and write another file by using pat
## read another file by using path
filename=open("c:/Users/Admin/Desktop/file handling/madhuri/sonali/palindrome.py",'r')
print(filename.read())
filename.close()

##create file and write
filename1=open("demo_write.txt",'w')
filename1.write("I am create new and write-Hello everyone--")
filename1.close()

## write multilines ny using writelines() assecc mode.
person_data={"Name:Madhuri\n","Last_Name:Burande\n","Address:Narhe,Pune\n","Job_Profile:Python Deveolper"}
file_w=open("demo_multilines.txt",'w')
print("mulitiple data or line")
file_w.writelines(person_data)
file_w.close()

## another exmple.
course={"Class:Python\n","Fees:2,40000\n","Duration:8'th months"}
file_w=open("demo_multilines.txt",'w')
file_w.writelines(course)
file_w.close


## open file in read mode:
file_w=open("demo_multilines.txt",'r')
file_w.read()
file_w.close()

## by using with acess mode
name="Writting using vontext manager"
with open("demo_multilines.txt",'w') as f:
    f.write(name)

##Appending New Content to an Existing File
name="Name:Madhuri\n"
address=['Address:Narhe\n','City:Pune\n','Class:Python']
with open("demo_multilines.txt",'a') as f:
    f.write(name)
    f.writelines(address)
    print()

## Append (a+) and read the file.
name2="Name:Anant\n"
address2=["Address:Pune\n","Job:Gov\n","Age:30"]
with open("demo_multilines.txt",'a+') as F:
    F.write(name2)
    F.writelines(address2)
    F.seek(0)
    print(F.read())
    print()

name3="Name:Madhuri"
address3=["Address:Baner\n","Job:Python Developer\n"]
with open("demo_multilines.txt",'a+') as File:
    File.write(name3)
    File.writelines(address3)
    File.seek(0)
    print(File.read())

## write and read file both at time using w+
fp=open("write_read_file.txt",'w+')
fp.write("I am Madhuri\n")
fp.write("I am Python deveolper\n")
fp.write("I am living in pune\n")
fp.seek(0)
print(fp.read())

##Writing to a Binary File i.e write and read image.
pic=open("pic_file.jpg", "rb") 
my_pic=open("newpic.jpg",'wb')
for i in pic:
    my_pic.write(i)

## another example
photo=open("my_pic.jpg",'rb') 
my_new=open("mynew.jpg",'wb')
for line in photo:
    my_new.write(line)

