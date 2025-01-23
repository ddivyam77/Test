while True:
    try:
        x = input("Fraction: ").split('/')
        first_no,second_no = x
        first_no = int(first_no)
        second_no = int(second_no)
        if first_no > second_no:
            continue
        z = (first_no / second_no) *100
        if z <= 1:
            print("E")
        elif 90 <= z <= 100 :
            print("F")
        else:
            print(f"{round(z)}%")
        break
    except (ValueError, ZeroDivisionError):
        pass




