c = input("camelCase: ").strip()
snake_case = ""
for x in c:
    if x.isupper():
        snake_case += '_' + x.lower()
    else:
        snake_case += x
print('snake_case:', snake_case)
