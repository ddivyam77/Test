import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    pattern = r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$"
    match = re.match(pattern, ip)
    if match:
        if all(0 <= int(octet) <= 255 for octet in match.groups()):
            return True
    return False

if __name__ == "__main__":
    main()
