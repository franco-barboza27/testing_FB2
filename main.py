from creater import charCreator

print("test")

def main():
    startquestion = input("You may create a character (1) or see characters (2)")

    if startquestion == "1":
        charCreator()
    else:
        print("OK")

main()