
def garden_operations(operation_number):
    if operation_number == 0:
        number = int("abc")
        print(number)
    elif operation_number == 1:
        a = 5
        b = 0
        c = a/b
        print(c)
    elif operation_number == 2:
        f = open("newfile.txt")
    elif operation_number == 3:
        a = 123
        b = "abc"
        c = b + a
        print(c)
    else:
        print(operation_number)
        return operation_number

def test_error_types(operation_number):
    try:
        garden_operations(operation_number)
    except ValueError as error:
        print(f"Caught ValueError: {error}")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    except FileNotFoundError:
        print("Caught FileNotFoundError: [Errno 2] No such file or directory: 'newfile.txt'")
    except TypeError:
        print(f"Caught TypeError: can only concatenate str (not \"int\") to str")

def main():
    print("=== Garden Error Types Demo ===")

    print("Testing operation 0...")
    test_error_types(0)

    print("Testing operation 1...")
    test_error_types(1)

    print("Testing operation 2...")
    test_error_types(2)

    print("Testing operation 3...")
    test_error_types(3)

    print("Testing operation 4...")
    test_error_types(4)

    print("All error types tested successfully!")

if __name__ == "__main__":
    main()
