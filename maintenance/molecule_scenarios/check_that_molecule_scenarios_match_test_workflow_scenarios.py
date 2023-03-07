from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
import os
from pathlib import Path
import re

colorama_init()

scenarios = [ f.name for f in os.scandir(os.path.dirname(__file__) + '/../../molecule/') if f.is_dir() ]

regex = r"molecule_scenario:.*?\[(.*?)\]"
content = Path(os.path.dirname(__file__) + '/../../.github/workflows/code_testing.yml').read_text()
scenarios_enabled_raw = re.findall(regex, content, re.MULTILINE | re.DOTALL)[0]
scenarios_enabled = scenarios_enabled_raw.replace("\n", "").replace(" ","").split(',')

scenarios.sort()
scenarios_enabled.sort()

not_enabled = [x for x in scenarios if x not in scenarios_enabled]
no_scenario = [x for x in scenarios_enabled if x not in scenarios]

if (scenarios == scenarios_enabled):
    print("\n")
    print(f"{Fore.GREEN}[PASS] All available scenarios are activated{Style.RESET_ALL}")
    print(*scenarios, sep = "\n")
else:
    if len(not_enabled) > 0:
        print("\n")
        print(f"{Fore.RED}[ERROR] Not all scenarios are activated{Style.RESET_ALL}")
        print("\n")
        print(f"{Fore.BLUE}[Available]{Style.RESET_ALL}")
        print(*scenarios, sep = "\n")
        print(f"{Fore.BLUE}[Not active]{Style.RESET_ALL}")
        print(*not_enabled, sep = "\n")
    if len(no_scenario) > 0:
        print("\n")
        print(f"{Fore.RED}[ERROR] Invalid scenario names in workflow file{Style.RESET_ALL}")
        print("\n")
        print(f"{Fore.BLUE}[Valid scenarios]{Style.RESET_ALL}")
        print(*scenarios, sep = "\n")
        print(f"{Fore.BLUE}[Invalid scnarios]{Style.RESET_ALL}")
        print(*no_scenario, sep = "\n")