# Class List Manager - Group _4_
# MIS 211 Bonus Assignment (GitHub Teamwork)
names = [" maha", "Latifah", "Raneem ", "Fatima", "Jumanah"]
# ===== Each student adds her function BELOW this line =====
# Written by: Fatima (Task 1)
def count_names(names):
    return len(names)

# Written by: Latifah (task 2)
def search_name(names, name="Latifah"):
    for n in names:
        if n.strip().lower() == name.lower():
            return "Name is found"
    return "Name is not found"
# Written by: Raneem (task3) 
def sort_names(names):
    return sorted(name) 
# Written by: [maha] (task 4)
def longest_name(names):
    longest = names[0]
    for name in names:
        if len(name.strip()) > len(longest.strip()):
            longest = name.strip()
    return longest

    
def main():
print("Welcome to the Class List Manager!")
print("Class list:", names)
# Each student calls her function here, for example:
print("Number of names:", count_names(names))
print("Sorted names:", sort_names(names)) 
print("Longest name:", longest_name(names))

main()
