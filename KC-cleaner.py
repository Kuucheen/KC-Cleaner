import os, sys
import time
import ctypes
from random import randrange

try:
    from sty import fg
except ImportError:
    os.system('python -m pip install sty')
    from sty import fg

if sys.platform == "win32":
    os.system('color')

def title():
    os.system("cls")
    print(f"""{fg(15)}
     __  __     ______       {fg(99)} ______     __         ______     ______     __   __     ______     ______    {fg(15)}
    /\ \/ /    /\  ___\      {fg(99)}/\  ___\   /\ \       /\  ___\   /\  __ \   /\ "-.\ \   /\  ___\   /\  == \   {fg(15)}
    \ \  _"-.  \ \ \____     {fg(99)}\ \ \____  \ \ \____  \ \  __\   \ \  __ \  \ \ \-.  \  \ \  __\   \ \  __<   {fg(15)}
     \ \_\ \_\  \ \_____\    {fg(99)} \ \_____\  \ \_____\  \ \_____\  \ \_\ \_\  \ \_\\\\"\_\  \ \_____\  \ \_\ \_\ {fg(15)}
      \/_/\/_/   \/_____/    {fg(99)}  \/_____/   \/_____/   \/_____/   \/_/\/_/   \/_/ \/_/   \/_____/   \/_/ /_/ {fg(250)}

    \nby {fg(99)}Kuchen#2472\n""")


def selection():
    print(f"""
    {fg(250)}[{fg(99)}1{fg(250)}] {fg(99)}Autocleaner
    \t->  {fg(250)}Automatically cleans your combo list

    {fg(250)}[{fg(99)}2{fg(250)}] {fg(99)}Costum Cleaner
    \t->  {fg(250)}Removes everything after a certain symbol

    {fg(250)}[{fg(99)}3{fg(250)}] {fg(99)}Exit\n
    """)


    sel = input(f"{fg(15)}>> {fg(99)}")

    if sel == "1" or sel == "2":

        title()
        global file
        file = input(f"\n\n{fg(15)}File {fg(99)} >>  {fg(15)}")

        if checkfile(file):
            if sel == "1":
                autocleaner(file)
            else:
                customcleaner(file, input(f"{fg(15)}Symbol {fg(99)}>> {fg(15)}"))

        else:
            time.sleep(3)
            title()
            selection()

    else:
        if sel == "3":
            exit()

        else:
            title()
            notification("Please use a correct number")
            selection()


def autocleaner(file: str):

    title()
    temp = file.split("\\")
    notification(f"{fg(15)}Cleaning{fg(99)} {temp[-1]}", "*")
    with open(file, encoding="utf-8") as inp:
        with open("[CLEAN]-"+file.split("\\")[-1], "w", encoding="utf-8") as output:

            for line in inp:
                if line.count(":") > 0 and line.count("@") > 0 and line.count(".") > 0 and line.index(":") > line.index(".") > line.index("@") and len(line.split(":")[1]) > 0 and len(line.split("@")[0]) > 0 and len(line[line.index("@"):line.index(".")]):

                    try:
                        output.write(line[:line.index(" ")])
                    except ValueError:
                        output.write(line.replace("\n", ""))

                    output.write("\n")
    
    title()
    notification("Done!", "*")
    time.sleep(0.3)
    showcase(file)
            


def customcleaner(file: str, symbol: str):

    temp = file.split("\\")
    notification(f"{fg(15)}Cleaning{fg(99)} {temp[-1]}", "*")

    with open(file) as inp:
        with open("[CLEAN]-"+file.split("\\")[-1], "w") as output:

            for i in inp:
                try:
                    output.write(i[:i.index(symbol)])
                except ValueError:
                    output.write(i.replace("\n",""))

                output.write("\n")

    title()
    notification("Done!", "*")
    time.sleep(0.3)
    showcase(file)


def showcase(file:str = None, hits:list = None):
    title()
    notification("Showing three random hits", "*")
    time.sleep(2)
    if type(file) == str and hits == None:

        with open("[CLEAN]-"+file.split("\\")[-1], encoding="utf-8") as inp:
            hits = inp.readlines()

        for count in range(1,4):

            if type(hits) == list and len(hits) > 0:
                random = randrange(len(hits))
                notification(f"{fg(99)}-> {fg(15)}" + hits[random][:-2], count)
                hits.remove(hits[random])
            else:
                notification("Showed every hit in the cleaned file", "*")

    else:
        for count in range(1,4):

            if type(hits) == list and len(hits) > 0:
                random = randrange(len(hits))
                notification(f"{fg(99)}-> {fg(15)}" + hits[random][:-2], count)
                hits.remove(hits[random])

            else:
                notification("Showed every hit in the cleaned file", "*")

    print(f"""
    {fg(250)}[{fg(99)}1{fg(250)}] {fg(99)}Refresh
    \t->  {fg(250)}Show other three hits

    {fg(250)}[{fg(99)}2{fg(250)}] {fg(99)}Costum Cleaner
    \t->  {fg(250)}still seeing something? Try Costum Cleaner

    {fg(250)}[{fg(99)}3{fg(250)}] {fg(99)}Menu
    """)

    sel = input(f"{fg(15)}>> {fg(99)}")
    
    if sel == "1" or sel == "2" or sel == "3":

        if sel == "1":
            showcase(None, hits)

        elif sel == "2":
            customcleaner(file, input(f"{fg(15)}Symbol {fg(99)}>> {fg(15)}"))

        elif sel == "3":
            title()
            selection()

    else:
        notification("Please use a correct number")
        time.sleep(2)
        title()
        selection()
    




def checkfile(file:str) -> bool:
    try:
        with open(file):
            pass

    except FileNotFoundError:
        notification("File was not found!")
        return False

    except OSError:
        notification("Make sure your file is in a directory without a space in its name!")
        return False

    else:
        return True


def notification(string:str, symb:str = "!"):
    print(f"\n{fg(15)}[{fg(99)}{symb}{fg(15)}] {string}\n")

    
ctypes.windll.kernel32.SetConsoleTitleW("KC Cleaner | By Kuchen#2472")


title()
selection()     