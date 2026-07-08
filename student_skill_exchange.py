# Student Skill Exchange Platform

students = {}

while True:
    print("\n===== Student Skill Exchange Platform =====")
    print("1. Register Student")
    print("2. View All Students")
    print("3. Search by Skill")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        skill = input("Enter your skill: ")
        learn = input("Enter the skill you want to learn: ")

        students[name] = {
            "Skill": skill,
            "Wants to Learn": learn
        }

        print("✅ Student registered successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No students registered.")
        else:
            print("\nRegistered Students:")
            for name, details in students.items():
                print("----------------------------")
                print("Name:", name)
                print("Skill:", details["Skill"])
                print("Wants to Learn:", details["Wants to Learn"])

    elif choice == "3":
        search = input("Enter skill to search: ")

        found = False
        for name, details in students.items():
            if details["Skill"].lower() == search.lower():
                print("----------------------------")
                print("Name:", name)
                print("Skill:", details["Skill"])
                print("Wants to Learn:", details["Wants to Learn"])
                found = True

        if not found:
            print("No student found with that skill.")

    elif choice == "4":
        print("Thank you for using Student Skill Exchange Platform!")
        break

    else:
        print("Invalid choice! Please try again.")