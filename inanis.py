#Central inanis program

#######################
#   Import Modules    #
#######################

import os
#
import sys
#
import platform
#
import subprocess
#
import nmap3
#
import time
#
import psutil
#
####################################
#    Color and Variable Setup      #
####################################

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# print(f"{bcolors.HEADER} sample text {bcolors.ENDC}")

option_simple = False
option_complex = False
option_verycomplex = False
option_logmore = False
option_silent = False

#######################
# Program Definitions #
#######################

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_intro():
    print(f'''{bcolors.OKGREEN}
{bcolors.OKGREEN} __________________________________________
{bcolors.OKGREEN}/_____/_____/_____/_____/_____/_____/_____/
{bcolors.OKGREEN}|     _                   _     
{bcolors.OKGREEN}|    (_)___  ____ _____  (_)____
{bcolors.OKGREEN}|   / / __ \/ __ `/ __ \/ / ___/ {bcolors.OKCYAN}mx#0001{bcolors.OKGREEN}
{bcolors.OKGREEN}|  / / / / / /_/ / / / / (__  ) {bcolors.OKBLUE}github.com/{bcolors.OKGREEN}
{bcolors.OKGREEN}| /_/_/ /_/\__,_/_/ /_/_/____/ {bcolors.OKBLUE}clemensdotson{bcolors.OKGREEN}
{bcolors.OKGREEN}|________{bcolors.FAIL}v.0.1{bcolors.OKGREEN}_____________________________
{bcolors.OKGREEN}/_____/_____/_____/_____/_____/_____/_____/

{bcolors.ENDC}''')


def printOptions():
    clear()
    print(f'''{bcolors.OKGREEN}
{bcolors.OKGREEN}  ____  ____  / /_(_)___  ____  _____
{bcolors.OKGREEN} / __ \/ __ \/ __/ / __ \/ __ \/ ___/
{bcolors.OKGREEN}/ /_/ / /_/ / /_/ / /_/ / / / (__  ) 
{bcolors.OKGREEN}\____/ .___/\__/_/\____/_/ /_/____/  
{bcolors.OKGREEN}    /_/                              
{bcolors.OKGREEN}________{bcolors.FAIL}search parameters{bcolors.OKGREEN}___________
{bcolors.ENDC}''')
    print(f"{bcolors.WARNING} =- Pick ONE of these options -= \n{bcolors.ENDC}")
    print(f"{bcolors.BOLD} [-s] {bcolors.OKGREEN} [Simple] {bcolors.ENDC}{bcolors.ENDC}{bcolors.OKBLUE} Basic system information and common ports{bcolors.ENDC}")
    print(f"{bcolors.BOLD} [-c] {bcolors.OKGREEN} [Complex] {bcolors.ENDC}{bcolors.ENDC}{bcolors.OKBLUE} In-depth system information and all ports{bcolors.ENDC}")
    print(f"{bcolors.BOLD} [-v] {bcolors.OKGREEN} [Very Complex]{bcolors.ENDC}{bcolors.ENDC}{bcolors.OKBLUE} In-depth system information and advanced port information{bcolors.ENDC}")
    print(f"{bcolors.WARNING}\n =- Pick ONE of these verbose modifiers -= \n{bcolors.ENDC}")
    print(f"{bcolors.HEADER}*   {bcolors.ENDC} {bcolors.BOLD}inasis outputs important information by default")
    print(f"{bcolors.BOLD} [-l] {bcolors.OKGREEN} [Log more Information] {bcolors.ENDC}{bcolors.ENDC}{bcolors.OKBLUE} Prints more information on top of the default{bcolors.ENDC}")
    print(f"{bcolors.BOLD} [-silent] {bcolors.OKGREEN} [Silent Mode] {bcolors.ENDC}{bcolors.ENDC}{bcolors.OKBLUE} Inansis will print no information except for the standard output.{bcolors.ENDC}")


def ensure_valid_verbose():
    if (option_silent and option_logmore == True):
        print(f'[{bcolors.FAIL}X{bcolors.ENDC}]{bcolors.WARNING}   Inanis recieved both the log more and silent options. What?!{bcolors.ENDC}')
        sys.exit()

def ensure_valid_options():
    if ((option_simple and option_complex == True) or (option_simple and option_verycomplex == True) or (option_complex and option_simple == True) or (option_complex and option_verycomplex == True) or (option_verycomplex and option_simple == True) or (option_verycomplex and option_complex == True)):
        print(f'[{bcolors.FAIL}X{bcolors.ENDC}]{bcolors.WARNING}   Inanis was provided multiple complexity modes. Only select one!{bcolors.ENDC}')

def simple_system_information():
    simple_system_information = ('test')

#########################
# Ensuring Installation #
#########################

main_intro()
print(f"{bcolors.WARNING} Ensuring proper installation, this'll just take a moment... {bcolors.ENDC}")

# Python Version Check

version = (__import__('sys').version_info[:3])
formatted_version = (str(version[0]) + '.' + str(version[1]) + '.' + str(version[2]))
# version = [2, 1, 2] // debug for incorrect version
if (int(version[0] >= 3) and int(version[1] >= 7)):
    print(f'[{bcolors.OKGREEN}✓{bcolors.ENDC}]{bcolors.OKCYAN}   Python 3.7 or greater detected. Running Python {bcolors.ENDC}' + formatted_version + f'{bcolors.OKCYAN}!{bcolors.ENDC}')
else:
    print(f'[{bcolors.FAIL}X{bcolors.ENDC}]{bcolors.WARNING}   You are using an incorrect version of Python. You are using Python {bcolors.ENDC}' + formatted_version + f'{bcolors.OKCYAN}!{bcolors.ENDC}')

# Ensure arguements where given
if (len(sys.argv) <= 1):
    print(f'[{bcolors.FAIL}X{bcolors.ENDC}]{bcolors.WARNING}   You did not provide inanis with any parameters!{bcolors.ENDC}')
    print(f'[{bcolors.FAIL}-{bcolors.ENDC}]{bcolors.WARNING}   Printing options...{bcolors.ENDC}')
    time.sleep(3)
    printOptions()
else:
    print(f'[{bcolors.OKGREEN}✓{bcolors.ENDC}]{bcolors.OKCYAN}   Inanis recieved parameters.{bcolors.ENDC}')

# Input parameter parser

for option in sys.argv:
    option.lower()
    if option == ('-l'):
        if option_logmore == True:
            print(f'[{bcolors.FAIL}X{bcolors.ENDC}]{bcolors.WARNING}   Inanis recieved the -s argument multiple times.{bcolors.ENDC}')
            sys.exit()
        else:
            option_logmore = True
            print(f'[{bcolors.OKGREEN}Verbose{bcolors.ENDC}]{bcolors.OKCYAN}   Higher verbose mode selected.{bcolors.ENDC}')

for option in sys.argv:
    option.lower()
    if option == ('-silent'):
        if option_silent == True:
            print(f'[{bcolors.FAIL}X{bcolors.ENDC}]{bcolors.WARNING}   Inanis recieved the -silent argument multiple times.{bcolors.ENDC}')
            sys.exit()
        else:
            option_silent = True

    if option == ('-s'):
        if option_simple == True:
            print(f'[{bcolors.FAIL}X{bcolors.ENDC}]{bcolors.WARNING}   Inanis recieved the -s argument multiple times.{bcolors.ENDC}')
            sys.exit()
        else:
            option_simple = True
            if option_logmore == True:
                print(f'[{bcolors.OKGREEN}Verbose{bcolors.ENDC}]{bcolors.OKCYAN}   Simple mode selected.{bcolors.ENDC}')

    if option == ('-c'):
        if option_complex == True:
            print(f'[{bcolors.FAIL}X{bcolors.ENDC}]{bcolors.WARNING}   Inanis recieved the -c argument multiple times.{bcolors.ENDC}')
            sys.exit()  
        else:
            option_complex = True
            print(f'[{bcolors.OKGREEN}Verbose{bcolors.ENDC}]{bcolors.OKCYAN}   Complex mode selected.{bcolors.ENDC}')

    if option == ('-v'):
        if option_complex == True:
            print(f'[{bcolors.FAIL}X{bcolors.ENDC}]{bcolors.WARNING}   Inanis recieved the -v argument multiple times.{bcolors.ENDC}')
            sys.exit()  
        else:
            option_complex = True
            print(f'[{bcolors.OKGREEN}Verbose{bcolors.ENDC}]{bcolors.OKCYAN}   Very complex mode selected.{bcolors.ENDC}')

# Call validity checkers

ensure_valid_verbose()
ensure_valid_options()

'''
nmap = nmap3.NmapScanTechniques()
nm.scan('127.0.0.1', '22-443')
'''

print(f"\n\n\n{bcolors.HEADER} header {bcolors.ENDC}")
print(f"{bcolors.OKBLUE} ok blue {bcolors.ENDC}")
print(f"{bcolors.OKCYAN} ok cyan {bcolors.ENDC}")
print(f"{bcolors.OKGREEN} ok green {bcolors.ENDC}")
print(f"{bcolors.WARNING} warning {bcolors.ENDC}")
print(f"{bcolors.FAIL} fail {bcolors.ENDC}")
print(f"{bcolors.BOLD} bold {bcolors.ENDC}")
print(f"{bcolors.UNDERLINE} underline {bcolors.ENDC}")

# Generate information output - VITAL - 