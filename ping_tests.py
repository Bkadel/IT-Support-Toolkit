import os

def ping_host(host):
    response = os.system(f"ping -n 2 {host}")
    if response == 0:
        print(f"{host} is reachable")
    else:
        print(f"{host} is NOT reachable")

hosts = ["8.8.8.8", "www.google.com"]
for h in hosts:
    ping_host(h)