from datetime import datetime
import os

# Welcome message
print("Hello and welcome to Daftarche Khatere software.")

# Creates the data directory if it doesn't exist
os.makedirs("data", exist_ok=True)
file_path = os.path.join("data", "Khaterat.txt")  # New relative path

running = True

def line_count(file):
    with open(file, "r") as f:
        return len(f.readlines())

def add():
    khatere = input("Enter your memory: ").strip()
    with open(file_path, "a") as f: 
        f.write(f"{line_count(file_path) + 1}. {khatere}\n")

def show(file): 
    with open(file, 'r') as f: 
        print(f.read())
        
def remove(file): 
    new_lines = []
    remove_ID = input("Enter the ID to delete: ").strip()
    with open(file, "r") as f: 
        lines = f.readlines()
    
    for line in lines: 
        if not line.startswith(f"{remove_ID}."): 
            new_lines.append(line)
    
    with open(file, "w") as f:
        for idx, line in enumerate(new_lines):
            if ". " in line:
                content = line.split(". ", 1)[1]
            else:
                content = line
            f.write(f"{idx + 1}. {content}")

def isday():
    current_hour = datetime.now().hour
    if 6 <= current_hour < 18: 
        return "day"
    else: 
        return "night"

while running: 
    input_message = input("What would you like to do? (help/add/remove/show/quit): ").strip().lower()

    if input_message == "help": 
        print("""
Available commands:
add    - Add new memory
remove - Delete a memory by ID
show   - View all memories
quit   - Exit the program
        """)
    elif input_message == "add": 
        add()
    elif input_message == "remove": 
        remove(file_path)
    elif input_message == "show": 
        show(file_path)
    elif input_message in ("quit", "exit"): 
        running = False
        if isday() == "day": 
            print("Have a great day.")
        else: 
            print("Have a great night.")
        print("Your memories are saved.")
    else:
        print("Invalid command. Type 'help' for options.")
