import requests
from colorama import Fore

print(Fore.RED+"""
                     ▄█     ▄███████▄       ▄█  ███▄▄▄▄      ▄████████  ▄██████▄  
                    ███    ███    ███      ███  ███▀▀▀██▄   ███    ███ ███    ███ 
                    ███▌   ███    ███      ███▌ ███   ███   ███    █▀  ███    ███ 
                    ███▌   ███    ███      ███▌ ███   ███  ▄███▄▄▄     ███    ███ 
                    ███▌ ▀█████████▀       ███▌ ███   ███ ▀▀███▀▀▀     ███    ███ 
                    ███    ███             ███  ███   ███   ███        ███    ███ 
                    ███    ███             ███  ███   ███   ███        ███    ███ 
                    █▀    ▄████▀           █▀    ▀█   █▀    ███         ▀██████▀   

""")
## single ip rewquest
# response = request.get("http://ip-api.com/json/24.48.0.1").json()
#
# print(response['lat'])
# print(response['lon'])

# batch ip request
ip = input(f"{Fore.RED}[+]{Fore.LIGHTCYAN_EX}Enter the ip : ")
print("")
response = requests.post("http://ip-api.com/batch", json=[

    {"query": (ip)},

]).json()

for ip_info in response:
    for k,v in ip_info.items():
        print(k,v)
    print("\n")
