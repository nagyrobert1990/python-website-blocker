import time
from datetime import datetime as dt

hosts_temp=r"D:\block_websites\Demo\hosts"
hosts_path=["/etc/hosts", r"C:\Windows\System32\drivers\etc\hosts"]
redirect="127.0.0.1"
website_list=["www.facebook.com", "facebook.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day, 8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day, 16):
        print("Working hours...")
        try:
            with open(hosts_path[0],'r+') as file:
                content=file.read()
                for website in website_list:
                    if website in content:
                        pass
                    else:
                        file.write(redirect + " " + website + "\n")
        except :
            with open(hosts_path[1], 'r+') as file:
                content=file.read()
                for website in website_list:
                    if website in content:
                        pass
                    else:
                        file.write(redirect + " " + website + "\n")
        
    else:
        try:
            with open(hosts_path[0], 'r+') as file:
                content=file.readlines()
                file.seek(0)
                for line in content:
                    if not any(website in line for website in website_list):
                        file.write(line)
                file.truncate()
            print("Fun hours...")
        except :
            with open(hosts_path[1], 'r+') as file:
                content=file.readlines()
                file.seek(0)
                for line in content:
                    if not any(website in line for website in website_list):
                        file.write(line)
                file.truncate()
            print("Fun hours...")
        
    time.sleep(5)