user_input = input("Enter a number representing day of the week (1-Monday ... 7-Sunday)")

day_num = int(user_input)

if day_num < 0 or day_num > 6:
    print("Incorrect value")
    raise SystemExit


days = ["Monday", "Tuseday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

print("First day of the week is " + days[0])

i = 0
output = ""
for day in days:
    output += day
    if day_num - 1 == i:
        break
    else:
        output += ", "
        i += 1
    
print(output)