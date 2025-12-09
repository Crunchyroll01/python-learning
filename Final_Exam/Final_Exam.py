#Final Exam - Cody Fancil
#Problem 1, File Statistics
#Complete the function that analyzes a text file and returns basic statistics.
def get_file_stats(filename):
    """
    Get statistics about a text file.

    Parameters:
        filename (str): Name of the file to analyze

    Returns:
        dict: Dictionary with 'lines', 'words', and 'characters' counts
        Returns None if file doesn't exist

    Example:
        If file contains:
        "Hello world
        Python is great"

        get_file_stats("file.txt") returns:
        {'lines': 2, 'words': 5, 'characters': 26}
    """

    # YOUR CODE HERE
    # Hint: Use try-except for file handling
    # Hint: Use readlines() to get all lines
    # Hint: Use split() to count words
    # Hint: Use len() for character count

    try:
        with open(filename, 'r') as file:
        # Read all lines
            lines = file.readlines()
        # Count lines
            line_count = len(lines)
        # Count words (split each line and count)
            word_count = sum(len(line.split()) for line in lines)

        # Count characters (total length of all lines)
            char_count = sum(len(line) for line in lines)

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    return {
        'lines': line_count, # Replace with actual count
        'words': word_count, # Replace with actual count
        'characters': char_count # Replace with actual count
    }

#Test your function:
'''
stats = get_file_stats("test.txt")
if stats:
    print(f"Lines: {stats['lines']}")
    print(f"Words: {stats['words']}")
    print(f"Characters: {stats['characters']}")
'''
#-------------------------------------------------------------------

#Problem 3: Safe List Access
#Write a function that safely accesses list elements with error handling.
def safe_get_element(my_list, index, default_value=None):
    """
    Safely get an element from a list at the given index.

    Parameters:
        my_list: List to access (might not be a list!)
        index: Index to access (might not be valid!)
        default_value: Value to return if access fails

    Returns:
        Element at index if successful
        default_value if any error occurs
    Examples:
        safe_get_element([1, 2, 3], 1, -1) returns 2
        safe_get_element([1, 2, 3], 10, -1) returns -1
        safe_get_element("not a list", 0, -1) returns -1
        safe_get_element([1, 2, 3], "bad", -1) returns -1
    """
    
    # YOUR CODE HERE
    # Use try-except to handle:
    # - IndexError (index out of range)
    # - TypeError (not a list or bad index type)
    # - Any other unexpected errors
    
    try:
        # Try to access the element
        return my_list[index]
    except IndexError:
        #Handle index out of range
        print(f"\nIndexError occured, default value returned\n")
        return default_value
    except TypeError:
        #Handle wrong types
        print("\nTypeError occurred, default value returned\n")
        return default_value
    except Exception:
        # Handle any other error
        print("\nException error occurred, default value returned\n")
        return default_value

#Test your functions:
print("Test 1")
print(safe_get_element([1, 2, 3], 1)) # 2
print(f"\nTest 2")
print(safe_get_element([1, 2, 3], 10, -1)) # -1
print("Test 3")
print(safe_get_element("not list", 0, -1)) # -1