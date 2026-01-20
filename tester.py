print("test")

chars = []
def main():
    startquestion = input("You may create a character (1) or see characters (2)")
    if startquestion == "1":
        chars.append(charCreator())
    else:
        pass

main()