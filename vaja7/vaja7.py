import re

pattern1 = r"^Hello"
print(bool(re.search(pattern1, "Hello World")))

pattern2 = r"bye$"
print(bool(re.search(pattern2, "Goodbye")))

pattern3 = r"dog"
print(bool(re.search(pattern3, "Dog", re.I)))
print(bool(re.search(pattern3, "DOG", re.I)))
print(bool(re.search(pattern3, "dOg", re.I)))
print(bool(re.search(pattern3, "dog", re.I)))

pattern4 = r"[a-z]"
print(re.findall(pattern4, "abcdefg"))

pattern5 = r"\d"
print(re.findall(pattern5, "1234567890"))

pattern6 = r"[A-Z]"
print(re.findall(pattern6, "ABCDEFG"))

pattern7 = r"[a-zA-Z0-9]"
print(re.findall(pattern7, "aB3Xz9"))

pattern8 = r"\w"
print(re.findall(pattern8, "hello_world123"))

pattern9 = r"\d+"
print(re.findall(pattern9, "42"))
print(re.findall(pattern9, "1234"))
print(re.findall(pattern9, "9"))

pattern10 = r"^[A-Za-z0-9_]+@[A-Za-z0-9_]+\.[A-Za-z]{2,}$"
print(bool(re.search(pattern10, "user_123@gmail.com")))

pattern11 = r"^[Aa].*[Zz]$"
print(bool(re.search(pattern11, "Arizona")))
print(bool(re.search(pattern11, "amz")))
print(bool(re.search(pattern11, "AtoZ")))

pattern12 = r"^[A-Z][a-z]+$"
print(bool(re.search(pattern12, "Hello")))
print(bool(re.search(pattern12, "World")))
print(bool(re.search(pattern12, "Javascript")))

pattern13 = r"^\d{3}$"
print(bool(re.search(pattern13, "123")))
print(bool(re.search(pattern13, "456")))
print(bool(re.search(pattern13, "789")))

pattern14 = r"[A-Z]{2,}"
print(bool(re.search(pattern14, "HEllo")))
print(bool(re.search(pattern14, "JAVAscript")))
print(bool(re.search(pattern14, "GO")))
print(bool(re.search(pattern14, "ABC")))
print(bool(re.search(pattern14, "code")))

pattern15 = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$"
print(bool(re.search(pattern15, "Pass1234")))
print(bool(re.search(pattern15, "Secure1")))
print(bool(re.search(pattern15, "helloWORLD2")))
