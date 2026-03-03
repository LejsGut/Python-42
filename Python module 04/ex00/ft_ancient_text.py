import os
def main() -> None:
    if not os.path.exists("ancient_fragment.txt"):
        print("ERROR: Storage vault not found. Run data generator first.")

    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print("Accessing Storage Vault: ancient_fragment.txt")

    file = open("ancient_fragment.txt", "r")
    print("Connection established...")
    print("RECOVERED DATA:")

    content = file.read()
    print(content)

    file.close()
    print("Data recovery complete. Storage unit disconnected.")

if __name__== "__main__":
    main()