def is_valid(plate):
    # Check the length of the plate
    if not (2 <= len(plate) <= 6):
        return False

    # Check that the first two characters are letters
    if not (plate[0].isalpha() and plate[1].isalpha()):
        return False

    # Ensure the plate contains only alphanumeric characters
    if not plate.isalnum():
        return False

    # Find the first digit and ensure no numbers precede it
    for i in range(2, len(plate)):
        if plate[i].isdigit():
            # If a number is found, ensure no zeros follow directly after it
            if plate[i] == '0':
                return False
            # After the first digit, ensure all following characters are digits
            if not plate[i:].isdigit():
                return False
            break

    return True


def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
