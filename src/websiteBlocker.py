import time
from datetime import datetime as dt

hostsPath = 'C:/Windows/System32/drivers/etc/hosts' #r"H:/Python_Programming/websiteBlocker/src/websiteBlocker.py"  #
redirect = "127.0.0.1"

websites = ["www.youtube.com", "youtube.com", "www.google.com", "google.com"]
while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 1) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,
                                                                          18):
        print("path:", hostsPath)
        with open(hostsPath, 'r+') as file:
            print("file:", file)
            content = file.read()
            for site in websites:
                if site in content:
                    pass
                else:
                    file.write(redirect + " " + site + "\n")
        print("path:", hostsPath)
        print("All the listed website are blocked")
        break
    else:
        with open(hostsPath, '+r') as file:
            content = file.readline()
            file.seek(0)
            for line in content:
                if not any(site in line for site in websites):
                    file.write(line)
                file.truncate()
        print("path:", hostsPath)
        print("Allowed access!")
        time.sleep(5)
        break
