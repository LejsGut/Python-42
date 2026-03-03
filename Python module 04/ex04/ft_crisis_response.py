def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")


    file_missing = "lost_archive.txt"
    print(f"CRISIS ALERT: Attempting access to '{file_missing}'...")
    try:
        with open(file_missing, "r") as f:
            f.read()
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")

    file_secret = "classified_vault.txt"
    print(f"CRISIS ALERT: Attempting access to '{file_secret}'...")
    try:
        with open(file_secret, "r") as f:
            f.read()
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")

    file_standard = "standard_archive.txt"
    print(f"ROUTINE ACCESS: Attempting access to '{file_standard}'...")
    try:
        with open(file_standard, "r") as f:
            content = f.read().strip()
            print(f"SUCCESS: Archive recovered - \"{content}\"")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()