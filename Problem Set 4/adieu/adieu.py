import inflect
p = inflect.engine()
names = []
while True:
    try:
        x = input("Name: ")
        names.append(x)
    except(EOFError):
        break
if names:
    f= p.join(names)
    print(f"Adieu, adieu, to {f}")

