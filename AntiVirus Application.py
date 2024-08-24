from time import sleep 
from alive_progress import alive_bar 
import os
import random


os.system("cls")

for i in range(50):
    
    print("A-DATA")


    for my_list in [
        "1: update", 
        "2: Quick scan", 
        "3: full scan"
        ]:
        print(my_list)
        
        
    viruses = [
            "Ransomware", 
            "Trojan", 
            "Rootkit", 
            "Keylogger", 
            "Malware", 
            "CryptoLocker", 
            "NO threat detected"
            ]

    detected = random.choice(viruses)
        
    print()
        
    user = input("Select an action by choosing a number: ")


    if user == "1":
        print("Processing...")
        sleep(1)
        print()
        
        with alive_bar(100) as bar:
            for i in range(100):
                sleep(0.0070)
                bar()
                
        print("Update completed")
                    
    elif user == "2":
        print("Please wait...")
        sleep(1)
        print("Quick Scan in progress...")
        print()
        
        with alive_bar(100) as bar:
            for i in range(100):
                sleep(0.25)
                bar()
                
        print(f"Scanning result: {detected}")


    elif user == "3":
        print("Please wait...")
        sleep(1)
        print("Full scan in progress...")
        print()  
        
        with alive_bar(100) as bar:
            for i in range(100):
                sleep(2.120)
                bar()
                
        print(f"Scanning result: {detected}")
    
    
    
