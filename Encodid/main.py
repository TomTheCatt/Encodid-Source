import colorama, sys, pickle, os, time
from colorama import Fore, Back, Style, init

def decode(message):
    global key
    outtake = []
    while message != "":
        for value in key:
            try:
                if message[:len(key[value])] in key[value]:
                    outtake.append(value)
                    message = message.removeprefix(key[value])
                    if message == "":
                        break
                    else:
                        continue
            except:
                pass
    return "".join(outtake)

def encode(message):
    global key
    outtake = []
    for letter in message:
        outtake.append(key[letter])
    return "".join(outtake)

def return_message(message):
    print(f"\n{Fore.RED}[Output]{Style.RESET_ALL}\n{message}\n\n"+ "-"*64 + "\n")

def main():
    init()
    #Gets key from key.txt
    with open(f"{os.getcwd()}\\key.txt", "rb") as file:
        global key
        key = pickle.load(file)
    while True:
        print(f"{Fore.RED}[Input]{Style.RESET_ALL}")
        intake = input("")
        #If intake is "e", it will break the loop and shut down the program
        if intake == "e":
            break
        #Intake cannot be one letter
        if len(intake) == 0:
            print("\n\n{Fore.RED}[Error]{Style.RESET_ALL} Cannot be one letter")
            time.sleep(2.7)
            continue
        #If the first value can be decoded, it will attempt to do so
        #If it cannot decode the first value it will encode the rest
        stop = False
        for value in key:
            if str(intake[:len(key[value])]) in str(key[value]):
                return_message(decode(intake))
                stop = True
        if not stop:
            return_message(encode(intake))

if __name__ == "__main__":
    main()
