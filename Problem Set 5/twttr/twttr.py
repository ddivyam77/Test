def main():
    u = input("Input: ")w
    s = remove_vowels(u)
    print("Output:",s)
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return ''.join([char for char in text if char not in vowels])

main()
