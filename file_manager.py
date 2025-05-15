import os

def merge_elements_in_lst(lst , index):
    str = ""
    
    
    for i in range(index,len(lst)):
        if(i!= index or i!=len(lst)-1):
            str = str + lst[i] + " "
            
        else:
            if(i==index):
                str = str + lst[i][1:] + " "
                
            else:
                str = str + lst[i][:-1] + " "
                
    return str

def elements_in_dir():
    str = ""
    lst = os.listdir()
    
    for i in lst:
        if os.path.isfile(i):
            str = str + i + " "
        else:
            str = str + f"/{i}" + " "   
        
    return str



def create_file(df):
    file = open(df,'w')
    file.close()

def write_files(df , content = ""):
    file = open(df,'w')
    file.write(content)
    file.close()

def open_file(df):
    try:
        file = open(df,'r')
        content = file.read()
        file.close()
        return content
    except:
        print("File does not exist")


def remove_content(df):
    os.remove(df)

def changing_directory(inp):
    
    os.chdir(f"{os.getcwd()}//{inp}")  
    

def get_prev_dir(txt):
    reversed_txt = txt[::-1]
    index_of_slash = reversed_txt.index("\\")
    new_dir = txt[:-index_of_slash-1]
    return new_dir

def go_back_in_directory(txt):
    os.chdir(get_prev_dir(txt))

# os.remove("sample.txt")

print('Running my own CLI')
while (1==1):
    txt = os.getcwd()
    user_command = input(f"(python cmd) {txt}> ")

    user_command_list = user_command.split()

    if(user_command_list[0] == "touch"):

        if (len(user_command_list) == 2):

            create_file(user_command_list[1][1:-1])

        else:
            create_file(user_command_list[1][1:-1])
            str = merge_elements_in_lst(user_command_list,2)
            write_files(user_command_list[1][1:-1] , str)


    if(user_command_list[0] == "ls"):
        print(elements_in_dir())

    if(user_command_list[0] == "cd"):
        try:
            changing_directory(user_command_list[1])
        except:
            print("Directory does not exist")

    if(user_command_list[0] == "cd.."):
        go_back_in_directory(txt)
        txt = get_prev_dir(txt)

    if(user_command_list[0] == "end"):
        print("Ending the cmd")
        break

