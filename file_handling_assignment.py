
# Task: File Creation, Reading, Appending, and Error Handling in Python

def create_and_write_file():
    try:
        # Creating a new text file 'my_file.txt' in write mode
        with open("my_file.txt", 'w') as file:
            file.write("Line 1: This is the first line.\n")
            file.write("Line 2: The number is 1234.\n")
            file.write("Line 3: Here's a mix of text and number 5678.\n")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error while writing to file: {e}")
    finally:
        print("File writing operation completed.")

def read_file():
    try:
        # Reading and displaying the contents of 'my_file.txt'
        with open("my_file.txt", 'r') as file:
            content = file.read()
            print("File content after reading:")
            print(content)
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error while reading the file: {e}")
    finally:
        print("File reading operation completed.")

def append_to_file():
    try:
        # Opening the file in append mode to add more lines
        with open("my_file.txt", 'a') as file:
            file.write("Line 4: This is an appended line.\n")
            file.write("Line 5: Another appended line with number 4321.\n")
            file.write("Line 6: Final line, more text with number 8765.\n")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error while appending to the file: {e}")
    finally:
        print("File appending operation completed.")

# Running the tasks
create_and_write_file()
read_file()
append_to_file()
read_file()  # Reading again after appending
