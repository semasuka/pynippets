import platform
import time
from datetime import datetime as dt

the_os = platform.system()

#getting the host file
if the_os == "Darwin" or the_os == "Linux":
    hosts_path = "/etc/hosts"
else:
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
# hosts_path = "hosts"

redirect = "127.0.0.1"

website_list = ["www.facebook.com","facebook.com","https://mail.google.com","www.gmail.com","https:www.google.com/gmail","https://www.udemy.com"]


while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,18) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,20):
        print("Working hours")
        with open(hosts_path,"r+") as host_file:
            content = host_file.read()
            for website in website_list:
                if website not in content:
                    host_file.write(redirect+" "+website+"\n")
    else:
        print("Fun hours")
        with open(hosts_path,"r+") as host_file:
            content_list = host_file.readlines()
            #starting back to the beginning of the file
            host_file.seek(0)
            for line in content_list:
                if not any(website in line for website in website_list):
                    host_file.write(line)
            #deleting all the remaining text in the file
            host_file.truncate()
    time.sleep(5)