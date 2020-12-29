#!/usr/bin/env/python3
# This Python file uses the following encoding: utf-8

from __future__ import print_function
try:
    from googlesearch import search

except ImportError:
    print("")

import sys
import time


# Dorks Eye v1.0


if sys.version[0] in "2":
    print ("\n[x] Parler Search Is Not Supported For python 2.x Use Python 3.x\n")
    exit()


class colors:
    CRED2 = "\33[91m"
    CBLUE2 = "\33[94m"
    ENDC = "\033[0m"


banner = ("\nParler Search Tool V.1\n")


for col in banner:
    print(colors.CRED2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.0025)

x = ("""
Author:  Vincent Cook | CYB3R INTELLIGENCE
Github:  https://github.com/cyb3r-intelligence/
Website: https://cyb3rintelligence.com \n """)

for col in x:
    print(colors.CBLUE2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.0040)

y = "\nPlease follow the steps below\n"
for col in y:
    print(colors.CRED2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.0040)

z = "\n"
for col in z:
    print(colors.ENDC + col, end="")
    sys.stdout.flush()
    time.sleep(0.4)


try:
    data = input("\n[+] Do You Like To Save The Output In A File? (Y/N) ").strip()
    l0g = ("")

except KeyboardInterrupt:
        print ("\n")
        print ("\033[1;91m[!] Cenceled..!\033[0")
        time.sleep(0.5)
        print ("\033[1;91m[!] Please run the script again for another search \033[0m\n\n")
        time.sleep(0.5)
        sys.exit(1)


def logger(data):
    file = open((l0g) + ".txt", "a")
    file.write(str(data))
    file.write("\n")
    file.close()


if data.startswith("y" or "Y"):
    l0g = input("[~] Give The File a Name: ")
    print ("\n" + "  " + "»" * 78 + "\n")
    logger(data)
else:
    print ("[!] Saving is Skipped...")
    print ("\n" + "  " + "»" * 78 + "\n")

def menu():
        print("")
        print("[1] Exact Profile Search")
        print("[2] Profile to Profile")
        print("[3] Search Posts")
        print("[4] Search Comments")
        print("[5] General Search")
        
        selection = input("\n[~] Please Select an Option: ")
        if selection =='1':
            exact_profile_search()
        elif selection == '2': 
            profile_to_profile()
        elif selection == '3':
            posts()
        elif selection == '4': 
            comments()
        elif selection == '5': 
            gernal_search()            
        else:
            print("Unknown Option Selected!")


def gernal_search():
    try:
        general_search = ("site:parler.com/ ")
        time.sleep(0.5)
        print ("\033[1;91m[!] Please use quotes for a more effcient search \033[0m\n")
        time.sleep(0.5)
        keyword_input = input("\n[+] Keyword: ")
        dork = general_search + keyword_input
        print ("\n ")      

        for results in search(dork, lang="en",):
            print ("[+] ", results)
            if dork in results:
                break

            data = (results)

            logger(data)
            time.sleep(0.1)
            
    except KeyboardInterrupt:
            print ("\n")
            print ("\033[1;91m[!] Canceled..!\033[0")
            time.sleep(0.5)
            print ("\033[1;91m[!] Please run the script again for another search \033[0m\n\n")
            time.sleep(0.5)
            sys.exit(1)


def comments():
    try:
        comment = ("site:parler.com/comment/ ")
        time.sleep(0.5)
        print ("\033[1;91m[!] Please use quotes for a more effcient search \033[0m\n")
        time.sleep(0.5)        
        keyword_input = input("\n[+] Keyword: ")
        dork = comment + keyword_input
        print ("\n ")      

        for results in search(dork, lang="en",):
            print ("[+] ", results)
            if dork in results:
                break

            data = (results)

            logger(data)
            time.sleep(0.1)
            
    except KeyboardInterrupt:
            print ("\n")
            print ("\033[1;91m[!] Canceled..!\033[0")
            time.sleep(0.5)
            print ("\033[1;91m[!] Please run the script again for another search \033[0m\n\n")
            time.sleep(0.5)
            sys.exit(1)

def posts():
    try:
        post = ("site:parler.com/post/ ")
        time.sleep(0.5)
        print ("\033[1;91m[!] Please use quotes for a more effcient search \033[0m\n")
        time.sleep(0.5)
        keyword_input = input("\n[+] Keyword: ")
        dork = post + keyword_input
        print ("\n ")      

        for results in search(dork, lang="en",):
            print ("[+] ", results)
            if dork in results:
                break

            data = (results)

            logger(data)
            time.sleep(0.1)
            
    except KeyboardInterrupt:
            print ("\n")
            print ("\033[1;91m[!] Canceled..!\033[0")
            time.sleep(0.5)
            print ("\033[1;91m[!] Please run the script again for another search \033[0m\n\n")
            time.sleep(0.5)
            sys.exit(1)

def profile_to_profile():
    try:
        username = ("site:parler.com/profile/ ")
        time.sleep(0.5)
        print ("\033[1;91m[!] Please use quotes for a more effcient search \033[0m\n")
        time.sleep(0.5)
        username_input = input("\n[+] Username: ")
        dork = username + username_input
        print ("\n ")      

        for results in search(dork, lang="en",):
            print ("[+] ", results)
            if dork in results:
                break

            data = (results)

            logger(data)
            time.sleep(0.1)
            
    except KeyboardInterrupt:
            print ("\n")
            print ("\033[1;91m[!] Canceled..!\033[0")
            time.sleep(0.5)
            print ("\033[1;91m[!] Please run the script again for another search \033[0m\n\n")
            time.sleep(0.5)
            sys.exit(1)

    print ("[•] Done... Exiting...")
    sys.exit()
    
        
def exact_profile_search():
    try:
        username = ("site:parler.com/profile/")
        time.sleep(0.5)
        print ("\033[1;91m[!] Please use quotes for a more effcient search \033[0m\n")
        time.sleep(0.5)
        username_input = input("\n[+] Username: ")
        dork = username + username_input
        print ("\n ")      

        for results in search(dork, lang="en",):
            print ("[+] ", results)
            if dork in results:
                break

            data = (results)

            logger(data)
            time.sleep(0.1)
            
    except KeyboardInterrupt:
            print ("\n")
            print ("\033[1;91m[!] Canceled..!\033[0")
            time.sleep(0.5)
            print ("\033[1;91m[!] Please run the script again for another search \033[0m\n\n")
            time.sleep(0.5)
            sys.exit(1)

    print ("[•] Done... Exiting...")
    sys.exit()


# =====# Main #===== #
if __name__ == "__main__":
    menu()
