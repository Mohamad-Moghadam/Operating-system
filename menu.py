from operating_system import Tree, Commands


def menu():
    while True:
        command = input("What do you want to do?\n1. mkdir\n2. cd\n3. rm\n4. ls")
        if command == 1:
            name= input(f"folder name: ")
            Commands.mkdir(name)
        elif command == 2:
            dir= input(f"desired dir: ")
            Commands.cd(dir)