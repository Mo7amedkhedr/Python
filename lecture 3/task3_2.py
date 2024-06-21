import requests


ip= requests.get("https://api.ipify.org/?format=json")


print(ip)

print(ip.content)

location=input("enter your ip: ")
print(location)

z=requests.get("https://ipinfo.io/"+str(location)+"/geo")

print(z)
print(z.content)