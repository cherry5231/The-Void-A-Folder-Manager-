import random
import os 
import shutil
files = os.listdir("starting/projects/Void/incoming")
V_codes = {}

for file in files:
    code= f"{random.randint(1000,9999)}"
    V_codes[code] = file
    print(f"V-code {code}::{file} ")
    

while True:
    choice = input("Enter V-code: ").replace(" ","-")
    if choice in V_codes:
   
     print(V_codes[choice])
     break
    else:
      print("Invalid V-code please enter again")

fate = input("Consume or Preserve?: ").lower()
if fate == "preserve":
    
    choose =  input("Enter V code for the preserving file: ")
    selected_file = V_codes[choose]
    shutil.move (
    f"starting/projects/Void/incoming/{selected_file}",
    f"starting/projects/Void/survivors/{selected_file}"
    )

    print(f"{selected_file} has been preserved in the VOID.")
elif fate == "consume":
    choose =  input("Enter V code for the consuming file: ")
    selected_file = V_codes[choose]
    
    
    shutil.move(
    f"starting/projects/Void/incoming/{selected_file}",
    f"starting/projects/Void/consumed/{selected_file}"
    )
    print(f"{selected_file} has been consumed by the VOID.")
else:
    print("Invalid file outcome")
print("You Can restore the files later by entering passkey for the files,")
print("press any key to exit/RESTORE")
choose2 = input("")
if choose2 == "RESTORE":
    files = os.listdir("starting/projects/Void/consumed")
    V_codes = {}

    for file in files:
     code= f"{random.randint(1000,9999)}"
     V_codes[code] = file
     print(f"V-code {code}::{file} ")
    
   
    while True:
     choose =  input("Enter V code for the preserving file: ")
     if choose in V_codes:
       selected_file = V_codes[choose]
       shutil.move (
       f"starting/projects/Void/consumed/{selected_file}",
       f"starting/projects/Void/survivors/{selected_file}"
       )

       print(f"{selected_file} has been preserved in the VOID.")
       break
     else:
          print("Please enter correct V-code")
else:
    print("Thankyou for accessing the VOID")
