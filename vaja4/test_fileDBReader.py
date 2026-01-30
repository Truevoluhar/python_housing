import fileDBReader as db

filename = "movies_db.txt"

db.deleteDatabase(filename)

db.createDatabase(filename, demoContent=True)

lines = db.readAllLines(filename)
print("ReadAllLines length:", len(lines))
print("First line:", lines[0].strip() if lines else "")

db.writeToFile(filename, "Test Movie|2024|Action|Test Actor|NotRented")

lines_after = db.readAllLines(filename)
print("After writeToFile count:", len(lines_after))
print("Last line:", lines_after[-1].strip() if lines_after else "")

extra_lines = [
    "Movie A|2001|Action|Actor A|Rented",
    "Movie B|2002|Action|Actor B|NotRented"
]
db.writeLinesToFile(filename, extra_lines, append=True)

lines_after_append = db.readAllLines(filename)
print("After writeLinesToFile append count:", len(lines_after_append))
print("Last two lines:", [lines_after_append[-2].strip(), lines_after_append[-1].strip()])

handler = db.readDatabase(filename)
if handler:
    content = handler.read()
    handler.close()
    print("ReadDatabase worked, chars:", len(content))
else:
    print("ReadDatabase failed")

new_file = "new_db.txt"
#db.deleteDatabase(new_file)
db.writeLinesToFile(new_file, ["Line 1", "Line 2"], append=False)
print("Exclusive file created lines:", [l.strip() for l in db.readAllLines(new_file)])

#db.deleteDatabase(filename)
#db.deleteDatabase(new_file)