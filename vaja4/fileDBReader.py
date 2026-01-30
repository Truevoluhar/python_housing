import os

def readDatabase(filename: str):
    try:
        return open(filename, "r")
    except Exception as e:
        print(f"Napaka: {e}")
        return False

def readAllLines(filename: str):
    try:
        with open(filename, "r") as f:
            return f.readlines()
    except Exception as e:
        print(f"Napaka: {e}")
        return []


def updateDatabase(filename: str, data):
    try:
        with open(filename, "w") as f:
            f.write("")
    except Exception as e:
        print(f"Napaka pri brisanju podatkov iz baze: {e}")
    try:
        with open(filename, "a") as f:
            for line in data:
                f.write(line)
    except Exception as e:
        print(f"Napaka pri posodabljanju podatkov: {e}")


def writeToFile(filename, data):
    with open(filename, "a") as f:
        f.write(str(data) + "\n")

def writeLinesToFile(filename, data_list, append=True):
    mode = "a" if append else "x"
    with open(filename, mode) as f:
        for i in data_list:
            f.write(str(i) + "\n")

def deleteDatabase(filename):
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print("Datoteka ne obstaja.")

def createDatabase(filename, demoContent=False):
    with open(filename, "w") as f:
        pass
    if demoContent:
        lines = [
            "Die Hard|1988|Action|Bruce Willis|NotRented",
            "RoboCop|1987|Action|Peter Weller|Rented",
            "Predator|1987|Action|Arnold Schwarzenegger|NotRented",
            "Lethal Weapon|1987|Action|Mel Gibson|Rented",
            "Commando|1985|Action|Arnold Schwarzenegger|NotRented",
            "First Blood|1982|Action|Sylvester Stallone|Rented",
            "The Terminator|1984|Action|Arnold Schwarzenegger|NotRented",
            "Mad Max 2|1981|Action|Mel Gibson|Rented",
            "Beverly Hills Cop|1984|Action|Eddie Murphy|NotRented",
            "Escape from New York|1981|Action|Kurt Russell|Rented"
        ]
    with open(filename, "a") as f:
        for line in lines:
            f.write(line + "\n")