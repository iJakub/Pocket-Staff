#iJ

import os
import random
import time
import pyfiglet
from colorama import just_fix_windows_console
just_fix_windows_console()


trebleclef = ("""

 ___|)_______________________________________\033[49m\033[39m
|___/________________________________________\033[49m\033[39m
|__/|________________________________________\033[49m\033[39m
|_/(|,\______________________________________\033[49m\033[39m
|_\_|_/______________________________________\033[49m\033[39m
    |
  (_|""")

bassclef = ("""

 ____________________________________________\033[49m\033[39m
|__/___\_.___________________________________\033[49m\033[39m
|__\___|_.___________________________________\033[49m\033[39m
|_____/______________________________________\033[49m\033[39m
|____/_______________________________________\033[49m\033[39m
     """)

altoclef = ("""

 _,-.________________________________________\033[49m\033[39m
||___)_______________________________________\033[49m\033[39m
||'==;_______________________________________\033[49m\033[39m
||___)_______________________________________\033[49m\033[39m
|_`-'________________________________________\033[49m\033[39m
     """)


previous_note = ""
def treble():
    global trebleclef, previous_note

    notes = {"C4":("".join((trebleclef[:287], f"{' '*6}\033[31m{'_'*34}\033[39m", trebleclef[287:]))),
            "D4":("".join((trebleclef[:287], f"{' '*6}\033[41m{' '*34}\033[49m", trebleclef[287:]))),
            "E4":("".join((trebleclef[:237], "\033[31m", trebleclef[237:]))),
            "F4":("".join((trebleclef[:237], "\033[41m", trebleclef[237:]))),
            "G4":("".join((trebleclef[:181], "\033[31m", trebleclef[181:]))),
            "A4":("".join((trebleclef[:181], "\033[41m", trebleclef[181:]))),
            "B4":("".join((trebleclef[:125], "\033[31m", trebleclef[125:]))),
            "C5":("".join((trebleclef[:125], "\033[41m", trebleclef[125:]))),
            "D5":("".join((trebleclef[:69], "\033[31m", trebleclef[69:]))),
            "E5":("".join((trebleclef[:69], "\033[41m", trebleclef[69:]))),
            "F5":("".join((trebleclef[:13], "\033[31m", trebleclef[13:]))),
            "G5":("".join((trebleclef[:13], "\033[41m", trebleclef[13:]))),
            "A5":("".join((trebleclef[:1], f"{' '*11}\033[31m{'_'*34}\033[39m", trebleclef[1:])))}

    try:
        while True:
            while True:
                note = random.choice(list(notes.keys()))
                
                if len(notes) == 1:
                    break
                if note != previous_note:
                    break

            previous_note = note
            os.system('cls||clear')

            print(pyfiglet.figlet_format(' Treble\n clef\n') + "NOTES: \nC4, D4, E4, F4, G4, A4, B4,\nC5, D5, E5, F5, G5, A5" + notes[note])

            anwser = input("\n This note is: ")

            if anwser.strip().upper() != note:

                if (anwser.strip().upper()[0]) == (note[0]):
                    print(f"\n \033[33mCORRECT, but in the wrong octave\033[39m\n The correct anwser is: {note}")
                else:
                    print(f"\n \033[31mWRONG\033[39m\n The correct anwser is: {note}")

            else:
                print(f"\n \033[92mCORRECT\033[39m")
                del notes[note]
                
            input("\nPress enter to continue...")
    except:
        start()


def alto():
    global altoclef, previous_note

    notes = {"D3":("".join((altoclef[:287], f"{' '*6}\033[31m{'_'*34}\033[39m", altoclef[287:]))),
            "E3":("".join((altoclef[:287], f"{' '*6}\033[41m{' '*34}\033[49m", altoclef[287:]))),
            "F3":("".join((altoclef[:237], "\033[31m", altoclef[237:]))),
            "G3":("".join((altoclef[:237], "\033[41m", altoclef[237:]))),
            "A3":("".join((altoclef[:181], "\033[31m", altoclef[181:]))),
            "B3":("".join((altoclef[:181], "\033[41m", altoclef[181:]))),
            "C4":("".join((altoclef[:125], "\033[31m", altoclef[125:]))),
            "D4":("".join((altoclef[:125], "\033[41m", altoclef[125:]))),
            "E4":("".join((altoclef[:69], "\033[31m", altoclef[69:]))),
            "F4":("".join((altoclef[:69], "\033[41m", altoclef[69:]))),
            "G4":("".join((altoclef[:13], "\033[31m", altoclef[13:]))),
            "A4":("".join((altoclef[:13], "\033[41m", altoclef[13:]))),
            "B4":("".join((altoclef[:1], f"{' '*11}\033[31m{'_'*34}\033[39m", altoclef[1:])))}

    try:
        while True:
            while True:
                note = random.choice(list(notes.keys()))
                
                if len(notes) == 1:
                    break
                if note != previous_note:
                    break

            previous_note = note
            os.system('cls||clear')

            print(pyfiglet.figlet_format(' Alto\n clef\n') + "NOTES: \nD3, E3, F3, G3, A3, B3, C4,\nD4, E4, F4, G4, A4, B4" + notes[note])

            anwser = input("\n This note is: ")

            if anwser.strip().upper() != note:

                if (anwser.strip().upper()[0]) == (note[0]):
                    print(f"\n \033[33mCORRECT, but in the wrong octave\033[39m\n The correct anwser is: {note}")
                else:
                    print(f"\n \033[31mWRONG\033[39m\n The correct anwser is: {note}")

            else:
                print(f"\n \033[92mCORRECT\033[39m")
                del notes[note]
                
            input("\nPress enter to continue...")
    except:
        start()


def bass():
    global bassclef, previous_note

    notes = {"E2":("".join((bassclef[:287], f"{' '*6}\033[31m{'_'*34}\033[39m", bassclef[287:]))),
            "F2":("".join((bassclef[:287], f"{' '*6}\033[41m{' '*34}\033[49m", bassclef[287:]))),
            "G2":("".join((bassclef[:237], "\033[31m", bassclef[237:]))),
            "A2":("".join((bassclef[:237], "\033[41m", bassclef[237:]))),
            "B2":("".join((bassclef[:181], "\033[31m", bassclef[181:]))),
            "C3":("".join((bassclef[:181], "\033[41m", bassclef[181:]))),
            "D3":("".join((bassclef[:125], "\033[31m", bassclef[125:]))),
            "E3":("".join((bassclef[:125], "\033[41m", bassclef[125:]))),
            "F3":("".join((bassclef[:69], "\033[31m", bassclef[69:]))),
            "G3":("".join((bassclef[:69], "\033[41m", bassclef[69:]))),
            "A3":("".join((bassclef[:13], "\033[31m", bassclef[13:]))),
            "B3":("".join((bassclef[:13], "\033[41m", bassclef[13:]))),
            "C4":("".join((bassclef[:1], f"{' '*11}\033[31m{'_'*34}\033[39m", bassclef[1:])))}

    try:
        while True:
            while True:
                note = random.choice(list(notes.keys()))
                
                if len(notes) == 1:
                    break
                if note != previous_note:
                    break

            previous_note = note
            os.system('cls||clear')

            print(pyfiglet.figlet_format(' Bass\n clef\n') + "NOTES: \nE2, F2, G2, A2, B2, C3, D3,\nE3, F3, G3, A3, B3, C4" + notes[note])

            anwser = input("\n This note is: ")

            if anwser.strip().upper() != note:

                if (anwser.strip().upper()[0]) == (note[0]):
                    print(f"\n \033[33mCORRECT, but in the wrong octave\033[39m\n The correct anwser is: {note}")
                else:
                    print(f"\n \033[31mWRONG\033[39m\n The correct anwser is: {note}")

            else:
                print(f"\n \033[92mCORRECT\033[39m")
                del notes[note]
                
            input("\nPress enter to continue...")
    except:
        start()


def start():
    os.system('cls||clear')

    clef = input(pyfiglet.figlet_format(" Pocket\n Staff") + """
     All ascii arts by ejm

     (1) Treble clef
     (2) Alto clef
     (3) Bass clef

     Select a clef: """)

    if clef == "1":
        treble()

    elif clef == "2":
        alto()

    elif clef == "3":
        bass()


start()
