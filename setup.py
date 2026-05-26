import os
import urllib.request

foldername = input("Enter base folder name (on Desktop or current directory): ")

BASE = os.path.join(foldername, "starting", "projects", "Void")

INCOMING = os.path.join(BASE, "incoming")
SURVIVORS = os.path.join(BASE, "survivors")
CONSUMED = os.path.join(BASE, "consumed")

os.makedirs(INCOMING, exist_ok=True)
os.makedirs(SURVIVORS, exist_ok=True)
os.makedirs(CONSUMED, exist_ok=True)

with open(os.path.join(INCOMING, "xp.txt"), "w") as f:
    f.write("A Black Hole?")

url = "https://media1.tenor.com/m/-sm2tV23fK8AAAAC/cat-brainrot.gif"
urllib.request.urlretrieve(url, os.path.join(INCOMING, "um.gif"))

files = os.listdir(INCOMING)

for file in files:
    print(file)

with open(os.path.join(INCOMING, "test.txt"), "w") as f:
    f.write("hello world")

with open(os.path.join(INCOMING, "test2.txt"), "w") as f:
    f.write("what is void?")
