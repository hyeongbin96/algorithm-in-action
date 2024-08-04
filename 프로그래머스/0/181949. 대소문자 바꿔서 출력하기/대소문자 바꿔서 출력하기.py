str = input()
print("".join(i.lower() if i.isupper() == True else i.upper() for i in str))
