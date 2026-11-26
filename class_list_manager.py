# Class List Manager - Group _4_
# MIS 211 Bonus Assignment (GitHub Teamwork)
names = [" maha", "Latifah", "Raneem ", "Fatima", "Jumanah"]
# ===== Each student adds her function BELOW this line =====
# Written by: Fatima (Task 1)
def count_names(names):
    return len(names)

# Written by: Latifah (task 2)
def search_name(names, name="Latifah"):
    target = name.strip().lower()
    for n in names:
        if n.strip().lower() == target:
            return True
    return False

    
# Written by: Raneem (task3) 
def sort_names(names):
    return sorted(names) 
# Written by: [maha] (Task 5)
def names_starting_with(names, letter):
    result = []
    for name in names:
        if name.strip().lower().startswith(letter.lower()):
            result.append(name.strip())
    return result
    # Written by: Jumanah (Task 6)
def to_upper(names):
    result = []
    for name in names:
        result.append(name.upper())
    return result
    
def main():
print("Welcome to the Class List Manager!")
print("Class list:", names)
# Each student calls her function here, for example:
print("Number of names:", count_names(names))
print("Is Latifah found?:", search_name(names, "Latifah"))
print("Sorted names:", sort_names(names)) 
print("Names starting with M:", names_starting_with(names, "M"))
print("Uppercase names:", to_upper(names))

main()
