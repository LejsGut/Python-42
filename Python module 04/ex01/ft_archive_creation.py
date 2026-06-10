import sys
import typing


def read_file(filename: str) -> str:
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    file: typing.IO
    try:
        file = open(filename, "r")
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")
        return ""

    content: str = file.read()
    file.close()

    print("---")
    print(content, end="")
    print("---")
    print(f"File '{filename}' closed.")

    return content


def transform(content: str) -> str:
    lines: list = content.split("\n")
    new_lines: list = []
    for line in lines:
        if line != "":
            new_lines.append(line + "#")
    new_content: str = "\n".join(new_lines) + "\n"
    return new_content


def write_file(filename: str, content: str) -> None:
    print(f"Saving data to '{filename}'")
    try:
        file: typing.IO = open(filename, "w")
        file.write(content)
        file.close()
        print(f"Data saved in file '{filename}'.")
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    content: str = read_file(sys.argv[1])
    if content == "":
        return

    new_content: str = transform(content)

    print("\nTransform data:")
    print("---")
    print(new_content, end="")
    print("---")

    filename: str = input("Enter new file name (or empty): ")
    if filename == "":
        print("Not saving data.")
    else:
        write_file(filename, new_content)


if __name__ == "__main__":
    main()
