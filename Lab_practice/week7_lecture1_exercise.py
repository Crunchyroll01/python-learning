import sys
from datetime import datetime

def practice_1_beginner():
    """
    Beginner: Understanding why we need files
    """
    print("\n" + "="*50)
    print("EXERCISE 1.1: Save Your Name")
    print("="*50)
    # TODO 1: Get user's name
    name = input("Enter your name: ")
    # TODO 2: Open a file called "myname.txt" for writing
    # Hint: Use open("myname.txt", "w")
    file = open("myname.txt", "w") # Replace None with open() function
    # TODO 3: Write the name to the file
    # Hint: Use file.write(name)
    file.write(name)
    # TODO 4: Close the file
    # Hint: Use file.close()
    print(f"Name '{name}' saved to myname.txt!")
    file.close()
    # TODO 5: Read it back
    # Open the file for reading with "r" mode
    file = open("myname.txt", "r") # Replace with open() for reading
    # Read the content
    saved_name = file.read() # Replace with file.read()
    # Close the file
    print(f"Read back: '{saved_name}'")
# Run the exercise

#practice_1_beginner()

#Exercise Set 2: Intermediate - Save and Load Settings
def practice_1_intermediate():
    """
    Intermediate: Create a settings saver
    """
    print("\n" + "="*50)
    print("EXERCISE 1.2: Settings Manager")
    print("="*50)
    # Game settings to save
    username = input("Enter username: ")
    difficulty = input("Enter difficulty (easy/medium/hard): ")
    sound = input("Sound on? (yes/no): ")
    # TODO 1: Save all settings to "settings.txt"
    # Open file for writing
    file = open("settings.txt","w") # Replace with open("settings.txt", "w")
    # TODO 2: Write each setting on a new line
    # Write username, then newline, then difficulty, etc.
    # Hint: file.write(username + "\n")
    file.write(username + "\n" + difficulty + "\n" + sound)
    # TODO 3: Close the file
    print("Settings saved!")
    # TODO 4: Load settings back
    print("\nLoading settings...")
# Run the exercise

#practice_1_intermediate()

def practice_2_beginner():
    """
    Beginner: Work with file objects
    """
    print("\n" + "="*50)
    print("EXERCISE 2.1: File Object Basics")
    print("="*50)
    # TODO 1: Create a text file with 3 lines
    number_text = open("numbers.txt", "w")
    # Write three numbers, each on a new line
    number_text.write("10\n")
    number_text.write("20\n")
    number_text.write("30\n")
    number_text.close()
    # TODO 2: Open the file and check its properties
    number_text = open("numbers.txt", "r")
    number_text.read()
    # Print file name
    print(f"File name: {number_text.name}")
    # TODO: Print file mode
    # Hint: Use file.mode
    print(f"File mode: {number_text.mode}")
    # TODO: Check if file is closed
    # Hint: Use file.closed
    print(f"File closed: {number_text.closed}")
    # TODO 3: Read one line at a time until EOF
    while True:
        line = number_text.readline()
        if line == "": # Check for EOF
            print("Reached end!")
        break
    print(f"Read: {line.strip()}")
    number_text.close()
    # Run the exercise
practice_2_beginner()

#Exercise Set 2: Intermediate - File Position

def practice_2_intermediate():
    """
    Intermediate: Track file position
    """
    print("\n" + "="*50)
    print("EXERCISE 2.2: File Position Tracking")
    print("="*50)
    # Create a file with alphabet
    alphabet_file = open("alphabet.txt", "w")
    alphabet_file.write("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    alphabet_file.close()
    # TODO 1: Open and read specific positions
    alphabet_file = open("alphabet.txt", "r")
    # Read first 5 characters
    chunk1 = alphabet_file.read(5)
    print(f"First 5: {chunk1}")
    # TODO 2: Check current position
    position = alphabet_file.tell()
    print(f"Current position: {position}")
    # TODO 3: Read next 5 characters
    chunk2 = alphabet_file.read(5)
    print(f"Next 5: {chunk2}")
    # TODO 4: Check position again
    position = alphabet_file.tell()
    print(f"Current position: {position}")
    # TODO 5: Read until EOF
    remaining = alphabet_file.read()
    print(f"Remaining: {remaining}")
    alphabet_file.close()
    # Run the exercise
practice_2_intermediate()

def practice_2_advanced():
    """
    Advanced: Work with multiple files
    """
    print("\n" + "="*50)
    print("EXERCISE 2.3: Multi-File Log System")
    print("="*50)
    # TODO 1: Create three different log files
    info_log = open("info.log", "w")
    error_log = open("error.log", "w")
    debug_log = open("debug.log", "w")
    # TODO 2: Write appropriate messages to each
    # Info log: Normal operations
    info_log.write("System started\n")
    # TODO: Add more info messages
    # Error log: Problems
    # TODO: Write error messages
    # Debug log: Detailed information
    # TODO: Write debug information
    # TODO 3: Close all files
    # Your code here
    # TODO 4: Create a master log reader
    print("\n📊 Log Summary:")
    # Read and count lines in each log
    for log_name in ["info.log", "error.log", "debug.log"]:
        log_file = open(log_name, "r")
        lines = log_file.readlines()
        log_file.close()
        print(f"{log_name}: {len(lines)} entries")
    # TODO 5: Show first line of each log
    if lines:
        print(f" First entry: {lines[0].strip()}")
    # Run the exercise
#practice_2_advanced()

def practice_2_beginner():
    """
    Beginner: Work with file objects
    """
    print("\n" + "="*50)
    print("EXERCISE 2.1: File Object Basics")
    print("="*50)
    # TODO 1: Create a text file with 3 lines
    number_text = open("numbers.txt", "w")
    # Write three numbers, each on a new line
    number_text.write("10\n")
    # TODO: Write 20 and 30
    number_text.close()
    # TODO 2: Open the file and check its properties
    number_text = open("numbers.txt", "r")
    # Print file name
    print(f"File name: {number_text.name}")
    # TODO: Print file mode
    # Hint: Use file.mode
    # TODO: Check if file is closed
    # Hint: Use file.closed
    # TODO 3: Read one line at a time until EOF
    while True:
        line = number_text.readline()
        if line == "": # Check for EOF
            print("Reached end!")
        break
        print(f"Read: {line.strip()}")

    number_text.close()
# Run the exercise
practice_2_beginner()
#Exercise Set 2: Intermediate - File Position
def practice_2_intermediate():
    """
    Intermediate: Track file position
    """
    print("\n" + "="*50)
    print("EXERCISE 2.2: File Position Tracking")
    print("="*50)
    # Create a file with alphabet
    alphabet_file = open("alphabet.txt", "w")
    alphabet_file.write("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    alphabet_file.close()
    # TODO 1: Open and read specific positions
    alphabet_file = open("alphabet.txt", "r")
    # Read first 5 characters
    chunk1 = alphabet_file.read(5)
    print(f"First 5: {chunk1}")
    # TODO 2: Check current position
    position = None # Replace with file.tell()
    print(f"Current position: {position}")
    # TODO 3: Read next 5 characters
    chunk2 = None # Replace with file.read(5)
    print(f"Next 5: {chunk2}")
    # TODO 4: Check position again
    # Your code here
    # TODO 5: Read until EOF
    remaining = None # Read the rest
    print(f"Remaining: {remaining}")
    alphabet_file.close()
# Run the exercise
practice_2_intermediate()

def practice_2_advanced():
    """
    Advanced: Work with multiple files
    """
    print("\n" + "="*50)
    print("EXERCISE 2.3: Multi-File Log System")
    print("="*50)
    import sys
    from datetime import datetime
    # TODO 1: Create three different log files
    info_log = open("info.log", "w")
    error_log = open("error.log", "w")
    debug_log = open("debug.log", "w")
    # TODO 2: Write appropriate messages to each
    # Info log: Normal operations
    info_log.write("System started\n")
    # TODO: Add more info messages
    # Error log: Problems
    # TODO: Write error messages
    # Debug log: Detailed information
    # TODO: Write debug information
    # TODO 3: Close all files
    # Your code here
    # TODO 4: Create a master log reader
    print("\n📊 Log Summary:")
    # Read and count lines in each log
    for log_name in ["info.log", "error.log", "debug.log"]:
        log_file = open(log_name, "r")
        lines = log_file.readlines()
        log_file.close()
    print(f"{log_name}: {len(lines)} entries")
    # TODO 5: Show first line of each log
    if lines:
        print(f" First entry: {lines[0].strip()}")
# Run the exercise
practice_2_advanced()