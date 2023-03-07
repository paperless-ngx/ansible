from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
import glob
import subprocess

colorama_init()

passes=0
fails=0
fail_messages=[]

checks = glob.glob('./**/check*.py', recursive=True)
for check in checks:
    print("\n")
    print('-' * (len(check) + 15))
    print(f"{Fore.BLUE}{Style.BRIGHT}Running check {check}{Style.RESET_ALL}")
    print('-' * (len(check) + 15))
    cmd = "python3 " + check
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    out, err = p.communicate() 
    result = out.decode().split('\n')
    for lin in result:
        if "[ERROR]" in lin:
            print(f"{Style.DIM}{Fore.RED}{lin}{Style.RESET_ALL}")
            fails+=1
            fail_messages.append(lin)
        elif "[PASS]" in lin:
            print(f"{Style.DIM}{Fore.GREEN}{lin}{Style.RESET_ALL}")
            passes+=1
        else:
            print(f"{Style.DIM}{lin}{Style.RESET_ALL}")

print("\n")
print('-' * (30))
print(f"{Style.BRIGHT}Number of passes:   {Fore.GREEN}{passes}{Style.RESET_ALL}")
print(f"{Style.BRIGHT}Number of failed:   {Fore.RED}{fails}{Style.RESET_ALL}")
print('-' * (30))
print("\n")
if len(fail_messages) > 0:
    print(f"{Fore.RED}Errors detected:{Style.RESET_ALL}")
    print(*fail_messages, sep = "\n")
    print(f"\n\n\n{Style.BRIGHT}{Fore.RED}| RESULT: FAILED |{Style.RESET_ALL}")
    exit(42)
else:
    print(f"\n\n\n{Style.BRIGHT}{Fore.GREEN}| RESULT: SUCCESS |{Style.RESET_ALL}")
