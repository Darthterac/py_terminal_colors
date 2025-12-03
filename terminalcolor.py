#!/usr/bin/env python3
import os
import sys

def clear(): os.system('cls' if os.name == 'nt' else 'clear')

def print_palette(selected=-1):
    clear()
    print("  256-COLOR PALETTE PICKER  (q to quit)\n")
    
    # Standard 6x6x6 cube (16–231)
    print("   Standard colors (16–231):")
    for i in range(16, 232):
        code = i
        mark = "← YOU" if code == selected else "   "
        print(f"\033[38;5;{code}m▓▓▓\033[0m {code:3d} {mark}", end=" ")
        if code % 36 == 15 + 16:  # 16 + (6*6 -1)
            print()
    
    # Grayscale (232–255)
    print("\n\n   Grayscale (232–255):")
    for i in range(232, 256):
        code = i
        mark = "← YOU" if code == selected else "   "
        print(f"\033[38;5;{code}m▓▓▓\033[0m {code:3d} {mark}", end=" ")
        if (i - 231) % 12 == 0 and i != 255:
            print()
    print("\n")

def main():
    selected = None
    while True:
        print_palette(selected)
        
        if selected is not None:
            print(f"  Selected color: \033[38;5;{selected}m▓▓▓▓▓▓▓▓▓▓\033[0m  code = {selected}")
            print(f"  → Example Usage in Python:\n\n" + f"example = \"\"\"\n\\033[38;5;{selected}mTEXT\\033[0m\n\"\"\"\n" + f"print(example)\n\n")
            print(f"Output in terminal:\n" + f"\033[38;5;{selected}mTEXT\033[0m")
            
        print("Enter color number (0–255) or 'q' to quit: ", end="")
        choice = input().strip()
        
        if choice.lower() == 'q':
            print("Bye!")
            break
        
        if choice.isdigit() and 0 <= int(choice) <= 255:
            selected = int(choice)
        else:
            input("\nInvalid color! Press Enter to continue...")
            selected = None

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nBye!")