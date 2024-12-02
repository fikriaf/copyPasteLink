import requests, random, time, os, sys
from bs4 import BeautifulSoup
from requests import post, get

url1= "https://klipit.in"
url2= "https://klipit.in/ajax_save_data.php"

user_a = random.choice(open("uaua.txt", "r").read().splitlines())

cookiet = get(url1, headers={'user-agent': user_a}).cookies
halo = '; '.join([f"{cookie.name}={cookie.value}" for cookie in cookiet])
cek = [cookie.value for cookie in cookiet]
php = get(url1, headers={'user-agent': user_a}).headers
print(php)
get_key = BeautifulSoup(get(f"https://klipit.in/{cek[0]}").text, "html.parser").find_all("script")
keyny=None
for key in get_key:
    if key.string and "const key" in key.string:
        lines = key.string.split(";")
        for line in lines:
            if "const key" in line:
                keyny= line.split("=")[1].strip().strip('"').strip("'")
                break
        if keyny:
            break

print(keyny)
textny=input("Masukkan textnya: ")
data = {
    "i": "copypaste",
    "k": keyny,
    "d": textny
}
head={
    'user-agent': user_a,
    "cookie": halo
}
exe = post(url2, headers={}, files=data).text
print(exe)




