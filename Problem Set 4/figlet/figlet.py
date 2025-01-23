import sys
from pyfiglet import Figlet

def main():
    # Initialize Figlet object
    figlet = Figlet()

    # Check for command-line arguments
    if len(sys.argv) == 1:
        # No font specified, proceed with default font
        font = figlet.getFonts()[0]  # Default font
    elif len(sys.argv) == 3 and sys.argv[1] == '-f':
        # If -f is provided, use the specified font
        if sys.argv[2] in figlet.getFonts():
            font = sys.argv[2]
        else:
            print("Invalid font.")
            sys.exit(1)
    else:
        print("Usage: figlet.py [-f font]")
        sys.exit(1)

    # Set the font
    figlet.setFont(font=font)

    # Get user input and render the text
    text = input("Input: ")
    print(figlet.renderText(text))

if __name__ == "__main__":
    main()
