jahr = int(input("Enter year:"))
if jahr % 400 == 0:
    print("Schaltjahr")
elif jahr % 100 == 0:
    print("Kein Schaltjahr")
elif jahr % 4 == 0:
    print("Schaltjahr")
else:
    print("Kein Schaltjahr")
