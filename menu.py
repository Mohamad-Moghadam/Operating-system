from operating_system import Tree, Commands


def menu():
    cmd = Commands(None, "root", None)

    while True:
        command = input("What do you want to do?\n1. mkdir\n2. cd\n3. rm\n4. ls")
        if command == "1":
            name= input(f"folder name: ")
            cmd.mkdir(name)

        elif command == "2":
            dir= input(f"desired dir: ")
            cmd.cd(dir)

        elif command == "3":
            des= input(f"which dir: ")
            cmd.rm(des)

        elif command == "4":
            cmd.ls()

menu()

