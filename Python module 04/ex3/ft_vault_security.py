def secure_archive(
    filename: str,
    mode: str = "r",
    content: str = ""
) -> tuple:
    try:
        if mode == "r":
            with open(filename, "r") as file:
                return (True, file.read())
        else:
            with open(filename, "w") as file:
                file.write(content)
                return (True, "Content successfully written to file")
    except OSError as e:
        return (False, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))

    print("Using 'secure_archive' to read from a regular file:")
    result = secure_archive("ancient_fragment.txt")
    print(result)

    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("output.txt", "w", result[1]))


if __name__ == "__main__":
    main()
