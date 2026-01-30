import fileDBReader as db

DB_FILE = "movies_db.txt"
OPTIONS = ["Find a Movie", "Rent a Movie", "See Rented Movies", "See Available Movies", "Return a Movie", "Exit"]
OPTIONS_MAP = [0, 1, 2, 3, 4, 5]


print("Welcome to Movie Rental System")

running = True

def main_menu():
    user_menu_selection = input("Your selection: ")
    selection = int(user_menu_selection)
    return selection

def check_menu_selection(options: list, selection: int) -> bool:
    return True if selection in options else False

def find_a_movie() -> str:
    movie_name = input("Enter movie name: ").lower()
    db_files = db.readAllLines(DB_FILE)
    for file in db_files:
        lf = file.split("|")[0].lower()
        if movie_name == lf:
            return file
    return "No movie found."

def rent_a_movie() -> str:
    user_input = input("Enter movie name: ").lower()
    db_files = db.readAllLines(DB_FILE)
    for i, file in enumerate(db_files):
        elements = file.split("|")
        movie_name = elements[0].lower()
        rent_status = elements[4].lower().strip()
        if user_input == movie_name:
            if rent_status == "notrented":
                elements[4] = "Rented"
                restored_line = "|".join(elements)
                restored_line = restored_line + "\n"
                db_files[i] = restored_line
                db.updateDatabase(DB_FILE, db_files)
                print("You have successfully rented a movie! Bring it back soon :)")
            else: 
                print("Movie not available for renting.")
            
    return "No movie found."

def return_a_movie() -> str:
    user_input = input("Enter movie name: ").lower()
    db_files = db.readAllLines(DB_FILE)
    for i, file in enumerate(db_files):
        elements = file.split("|")
        movie_name = elements[0].lower()
        rent_status = elements[4].lower().strip()
        if user_input == movie_name:
            if rent_status == "rented":
                elements[4] = "NotRented"
                restored_line = "|".join(elements)
                restored_line = restored_line + "\n"
                db_files[i] = restored_line
                db.updateDatabase(DB_FILE, db_files)
                print("You have successfully returned a movie! Need another one?")
            else: 
                print("Movie already returned.")
            
    return "No movie found."

def see_rented_or_available(rented: bool):
    if rented:
        db_files = db.readAllLines(DB_FILE)
        for i, file in enumerate(db_files):
            elements = file.split("|")
            rent_status = elements[4].lower().strip()
            if rent_status == "rented":
                print(file)
    else:
        db_files = db.readAllLines(DB_FILE)
        for i, file in enumerate(db_files):
            elements = file.split("|")
            rent_status = elements[4].lower().strip()
            if rent_status == "notrented":
                print(file)
            

while running:
    print("Select one of the options")
    for i, o in enumerate(OPTIONS):
        print(f"{i} - {o}")

    main_menu_selection = main_menu()
    is_selection_ok = check_menu_selection(OPTIONS_MAP, main_menu_selection)

    if not is_selection_ok:
        print("Your selection is not valid")
    else:

        if main_menu_selection == 5:
            print("Goodbye!")
            running = False

        if main_menu_selection == 0:
            print(find_a_movie())
        
        if main_menu_selection == 1:
            rent_a_movie()

        if main_menu_selection == 2:
            see_rented_or_available(True)

        if main_menu_selection == 3:
            see_rented_or_available(False)

        if main_menu_selection == 4:
            return_a_movie()

