from stats import bookBot
import sys

def main ():
    
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        for i in range(1,len(sys.argv)):
            bookBot(sys.argv[i])

main()