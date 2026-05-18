#!/usr/bin/env python3
def main():
    while True:
        try:
            s = input("Height: ")
            height = int(s)
        except (ValueError, TypeError):
            # non-integer or blank input — re-prompt
            continue
        if 1 <= height <= 8:
            break

    for i in range(1, height + 1):
        left_spaces = " " * (height - i)
        left_hashes = "#" * i
        right_hashes = "#" * i
        print(f"{left_spaces}{left_hashes}  {right_hashes}")

if __name__ == "__main__":
    main()