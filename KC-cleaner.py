#by Kuchen#2472
import os, sys, time, ctypes, re
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
    terminal()
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
        if file.count("\"") > 1:
            file = file[1:len(file)-1]

        if checkfile(file):
            if sel == "1":
                autocleaner(file)
            else:
                customcleaner(file)

        else:
            time.sleep(3)
            title()
            selection()

    else:
        if sel == "3":
            print(fg("white"), end="")
            exit()

        else:
            title()
            notification("Please use a correct number")
            selection()


def autocleaner(file: str):
    timer = time.time()
    title()
    temp = file.split("\\")
    notification(f"{fg(15)}Cleaning{fg(99)} {temp[-1]}", "*")
    with open(file, encoding="utf-8") as inp:
        with open("[CLEAN] "+file.split("\\")[-1], "w", encoding="utf-8") as output:

            for line in inp:
                if line.count("@") > 0:
                    line = line.replace("\n", "")
                    line = re.split(' |:', line)
                    count = 0

                    for i in line:
                        if i.count("@") == 1:
                            line = f"{line[count]}:{line[count+1]}"
                            continue
                        else:
                            count += 1

                    if line.count(":") > 0 and line.count("@") > 0 and line.count(".") > 0 and line.index(":") > line.index(".") > line.index("@") and len(line.split(":")[1]) > 0 and len(line.split("@")[0]) > 0 and len(line[line.index("@"):line.index(".")]):
                        output.write(f"{line}\n")
    
    with open("[CLEAN] "+file.split("\\")[-1],encoding="utf-8") as inp:
        lines = inp.readlines()

        with open("[CLEAN] "+file.split("\\")[-1], "w", encoding="utf-8") as output:

            duplicates = []

            for i in lines:
                if i not in duplicates:
                    output.write(i)
                    duplicates.append(i)
    
    timer = (time.time() - timer)*10

    with open("[CLEAN] "+file.split("\\")[-1],encoding="utf-8") as inp: 
        lines = inp.readlines()

    terminal(f"| Remaining hits: {len(lines)} | Finished in {timer:.2f}ms")
    title()
    notification("Done!", "*")
    time.sleep(0.3)
    showcase(file)
            


def customcleaner(file: str):

    timer = time.time()
    title()
    print(f"\n\t{fg(250)}Clean everything\n\n{fg(250)}[{fg(99)}1{fg(250)}] {fg(99)}Before\t\t{fg(250)}[{fg(99)}2{fg(250)}] {fg(99)}After\n")
    mode = input(f"{fg(15)}Mode {fg(99)}>> {fg(15)}")




    with open(file) as inp:
        with open("[CLEAN] "+file.split("\\")[-1], "w") as output:

            if mode == "1" or mode == "2":
                title()
                symbol = input(f"\n{fg(15)}Symbol {fg(99)}>> {fg(15)}")
                temp = file.split("\\")
                notification(f"{fg(15)}Cleaning{fg(99)} {temp[-1]}", "*")
                if mode == "1":
                    for i in inp:
                        try:
                            output.write(i[i.index(symbol)+len(symbol):])
                        except ValueError:
                            output.write(i.replace("\n",""))

                elif mode == "2":
                    for i in inp:
                        try:
                            output.write(i[:i.index(symbol)])
                        except ValueError:
                            output.write(i.replace("\n",""))

                        output.write("\n")

            else:
                notification("No mode selected")
                time.sleep(2)
                title()
                selection()


    
    terminal(f"| Finished in {(time.time() - timer)*10:.2f}ms")
    title()
    notification("Done!", "*")
    time.sleep(0.3)
    showcase(file)


def showcase(file:str = None, hits:list = None):
    title()
    notification("Showing three random hits", "*")
    time.sleep(2)
    if type(file) == str and hits == None:

        with open("[CLEAN] "+file.split("\\")[-1], encoding="utf-8") as inp:
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

    print(f"\n{fg(250)}[{fg(99)}1{fg(250)}] {fg(99)}Refresh\t{fg(250)}[{fg(99)}2{fg(250)}] {fg(99)}Costum Cleaner\t{fg(250)}[{fg(99)}3{fg(250)}] {fg(99)}Menu\n")

    sel = input(f"{fg(15)}>> {fg(99)}")
    
    if sel == "1" or sel == "2" or sel == "3":

        if sel == "1":
            showcase(None, hits)

        elif sel == "2":
            customcleaner(file)

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

    else:
        return True


def notification(string:str, symb:str = "!"):
    print(f"\n{fg(15)}[{fg(99)}{symb}{fg(15)}] {string}\n")

def terminal(string:str = ""):
    ctypes.windll.kernel32.SetConsoleTitleW("KC Cleaner | By Kuchen#2472 " + string)

title()
selection()     