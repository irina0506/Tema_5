import datetime  # pt afisarea datei
import os
import time
from typing import TextIO


path = '/home/irina/IRINA-CURS-PYTHON/TEMA_5(TODOLIST)/'
l = os.listdir(path)
print(l)


def Category() -> str:
	with open("category.txt", "r") as f:
		f_contents = f.read()
		print(f_contents)

time.sleep(0.5)

def Option() -> int:
    print('''
        1-Add a category
        2-Add a task
        3-Delete a task
        4-Sort task''')
    lista=[]
    x=input("Choose an option:")
    while True:
        x=int(x)
        if x==1:
            categories_function()
        elif x==2:
            save_task()
        elif x==3:
            lista.delete_and_sort()
            print(lista)
        elif x==4:
            lista.delete_and_sort()
            print(lista)
        else:
            print("Error,the choosen option does not exist!")

def save_new_category(text: str) -> TextIO:
    with open("category.txt", "r+") as file1:
        lista = []
        for x in file1.read():  
            lista.append(x)
        if text in lista:
            print(f"\nCategory <{text.upper()}> is already saved on file!\n")
            pass
        else:
            file1.write(f"{text}\n")
    return file1

def save_person(task:str, person:str , category:str , date=(datetime)) -> dict:
    x={"task":task, "date":date, "person":person , "category":category}
    with open("person.txt","r") as file2:
        file2.write(task+","+person+","+category+","+int(date))
    return x

def save_task() -> (int,str,str):
    while True:
        with open("person.txt","w") as file3:
            task_date = datetime.datetime(int(input("An: ")),
                                          int(input("Luna: ")),
                                          int(input("Zi: ")),
                                          int(input("Ora: ")),
                                          int(input("Minut: ")))
        person_responsible=input("Person responsible:")
        print("Choose a task:")
        Category()
        task_category=input("\n ****** \n")
        task_category=save_new_category(task_category)
        save_person(person_responsible.upper(),task_category,task_date)
        return task_date,task_category,person_responsible

x_list=[]

def categories_function() -> str:
    while True:
        x=input("Add a new category:") 
        if x.title().strip() in x_list: #metoda strip sterge spatiul dintre linii si le uneste
            print(f'\n\tCategory <{x.upper()}> already exists.')
        elif x.strip() == "":
            print("Please type a category or press Q to exit.")
        else:
            x_list.append(x.title().strip())
            save_new_category(x)
            print(x_list)
    return x


def delete_and_sort() -> str:
    x=""
    lista=[]
    #str(input("Enter what you want to do: 'D' for delete , 'S' for sort"))
    while x!='Q':
        if x=='D':
            del_no=input('Please enter the index number you want to delete: ')
            del_no=input(del_no)
            to_do.drop([del_no], inplace=True)
        elif x=='S':
            sorted=input('''Please enter how do you want the list sorted:
                            1-sortare ascendenta task
                            2-sortare descendenta task
                            3-sortare ascendenta data
                            4-sortare descendenta data
                            5-sortare ascendenta persoana responsabila
                            6-sortare descendenta persoana responsabila
                            7-sortare ascendenta categorie
                            8-sortare descendenta categorie
                            ''').upper()

            if sorted==1:
                to_do=to_do.sort_values('task',ascending=True)
                print (lista)
            elif sorted==2:
                to_do=to_do.sort_values('task',ascending=False)
                print (lista)
            elif sorted==3:
                to_do=to_do.sort_values('data', ascending=True)
                print (lista)
            elif sorted==4:
                to_do=to_do.sort_values('data', ascending=False)
                print (lista)
            elif sorted==5:
                to_do=to_do.sort_values('persoana', ascending=True)
                print (lista)
            elif sorted==6:
                to_do=to_do.sort_values('persoana',ascending=False)
                print (lista)
            elif sorted==7:
                to_do=to_do.sort_values('categorie', ascending=True)
                print (lista)
            elif sorted==8:
                to_do=to_do.sort_values('categorie', ascending=False)
                print (lista)
            quit=input("Apasa S pentru iesire si orice tasta pentru a repeta operatiile:")
            if quit.upper()=="S":
                break
            else:
                pass


while True:
        Category()
        Option()
        save_task()
        categories_function()
        quit = input(
        "Apasa S pentru iesire si orice tasta pentru a repeta operatiile:")
    if quit.upper() == "S":
        break
    else:
        pass


	

