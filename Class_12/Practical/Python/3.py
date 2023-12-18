# Remove All The Lines That Contain The Character 'a' In A File And Write It To Another File.
def remove_character():
    s=" "
    Read=[]
    lst1=[]
    lst2=[]
    with open(r".\Class_12\Practical\Python\poemold.txt", "r",)as file: # For Record I Am Use Different File.
        Read=file.readlines()           # For This Program You Use Same File In Place Of poemold and poemnew 
    for i in Read:
        a=list(i)
        if 'a' in a:
            lst1.append(i)
        else:
            lst2.append(i)
    return lst1,lst2
old,new=remove_character()
with open(r".\Class_12\Practical\Python\poem_with_a.txt", "w+",)as myfile:
    myfile.writelines(old)
with open(r".\Class_12\Practical\Python\poemnew.txt", "w+",)as Myfile:
    Myfile.writelines(new)