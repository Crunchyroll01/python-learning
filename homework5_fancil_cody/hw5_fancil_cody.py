import re
# Cody Fancil, Homework 3. CS 1350 Day AB


def format_receipt():
    # Create a formatted receipt using string methods.
    items = ["Coffee", "Sandwich", "Cookie"]
    prices = [3.50, 8.99, 2.00]
    quantities = [2, 1, 3]
    lines = []
    separator = "=" * 40
    # Header
    lines.append(separator)
    lines.append(f"{'Item':<20}{'Qty':^5}{'Price':>8}")
    lines.append(separator)
    
    total = 0
    for item, price, qty in zip(items, prices, quantities):
        item_total = price * qty
        total += item_total
        lines.append(f"{item:<20}{qty:^5}{'$'+format(item_total, '6.2f'):>8}")
    
    lines.append(separator)
    lines.append(f"{'TOTAL':<25}{'$'+format(total, '.2f'):>10}")
    lines.append(separator)
    
    return "\n".join(lines)


def process_user_data():
    
    while True:
        name = input("Enter your name: ")
        if name == "":
            print("Name cannot be empty. Please try again.")
            continue
        email = input("Enter your email: ")
        if email == "" or "@" not in email or "." not in email:
            print("Invalid email. Please ensure your email isnt empty and contains '@' and '.'")
            continue
        phone = input("Enter your phone number: ")
        if phone == "":
            print("Invalid phone number. Please ensure your phone number isnt empty.")
            continue
        address = input("Enter your address: ")
        if address == "":
            print("Invalid address. Please ensure your address isnt empty.")
            continue
        break
    
    raw_data = {
        'name' : name,
        'email' : email,
        'phone' : phone,
        'address' : address
    }
    
    print(f"This is the raw data you entered: {raw_data}")
    print("\nCleaning up data...")
    for key, value in raw_data.items():
        if key == 'name':
            cleaned_name = value.strip().title().replace("   "," ")
            username = cleaned_name.lower().replace(" ", "_")
        elif key == 'email':
            cleaned_email = value.strip().lower().replace(" ", "")
        elif key == 'phone':
            if value.isdigit() is not True:
                cleaned_phone = value.replace("-", "").replace("(", "").replace(")", "").replace(" ", "")
            else: 
                cleaned_phone = value
        elif key == 'address':
            cleaned_address = value.strip().title().replace("   "," ").replace("  "," ")
    cleaned_data = {
        'name' : cleaned_name,
        'email' : cleaned_email,
        'phone' : cleaned_phone,
        'address' : cleaned_address,
        'username' : username
        }
    print(f"This is the cleaned data: {cleaned_data}")


def analyze_text():
    # Perform comprehnsive text analysis using string methods.
    text = '''Hello world! How are you?
    ... This is a test. Another line here! How'''
    total_chars = len(text)
    total_lines = len(text.splitlines())
    most_common_word = ""
    most_common_count = 0
    longest_line = 0
    words_per_line = 0
    capitalized_sentences = 0
    questions = 0
    exclamations = 0
    
    pattern_1 = r"\w+"
    matches_1 = re.findall(pattern_1, text)
    total_words = len(matches_1)
    if total_words > 0:
        total_letters = 0
        for word in matches_1:
            total_letters += len(word)
        avg_word_length = total_letters / total_words
    else:
        avg_word_length = 0
        
    for word in matches_1:
        word_count = matches_1.count(word)
        if word_count > most_common_count:
            most_common_word = word
            most_common_count = word_count
    lines = text.splitlines()
    if lines:
        longest_line = max(len(line) for line in lines)
        words_per_line = total_words / len(lines)
    sentence_pattern = r'[^.!?]+[.!?]'
    sentences = [s.strip() for s in re.findall(sentence_pattern, text)]
    for sentence in sentences:
        if sentence and sentence[0].isupper():
            capitalized_sentences += 1
        if sentence.endswith('?'):
            questions += 1
        if sentence.endswith('!'):
            exclamations += 1
    analyzed_text = {
        'total_chars': total_chars,
        'total_words': total_words,
        'total_lines': total_lines,
        'avg_word_length': avg_word_length,
        'most_common_word': most_common_word,
        'longest_line': longest_line,
        'words_per_line': words_per_line,
        'capitalized_sentences': capitalized_sentences,
        'questions': questions,
        'exclamations': exclamations
    }
    print(analyzed_text)

def find_patterns():
    # Find basic patterns in text using regex.
    text = "I have 25 apples and 3.14 Pies pies. HELLO W0RLD!"
    integers = []
    decimals = []
    words_with_digits = []
    capitalized_words = []
    all_caps_words = []
    repeated_chars = []
    
    for word in text.split():
        if word.isdigit():
            integers.append(word)
        if re.match(r'^\d+\.\d+$', word):
            decimals.append(word)
        if re.search(r'\d', word) and re.search(r'[A-Za-z]', word):
            words_with_digits.append(word)
        if word.istitle():
            capitalized_words.append(word)
        if word.isupper() and word.isalpha():
            all_caps_words.append(word)
    repeated_chars = re.findall(r'\b\w*(\w)\w*\1\w*\b', text)
    
    pattern_dict = {
        'integers' : integers,
        'decimals' : decimals,
        'words_with_digits' : words_with_digits,
        'capitalized_words' : capitalized_words,
        'all_caps_words' : all_caps_words,
        'repeated_chars' : repeated_chars
    }
    print(pattern_dict)
find_patterns()

def validate_format(input_string, format_type):
    
    patterns = {
        'email': r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
        'phone': r'^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$',
        'date': r'^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/\d{4}$',
        'url': r'^(https?://)?(www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/[\w.-]*)*/?$'
    }
    pattern = patterns.get(format_type)
    if not pattern:
        return False
    return bool(re.match(pattern, input_string))

def extract_information():
    
    text = 'The price is $19.99 (20% off). "Great deal!" she said/'
    
    prices = re.findall(r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?", text)

    percentages = re.findall(r"\b\d+(?:\.\d)?%", text)

    years = re.findall(r"\b(?:19|20)\d{2}\b", text)

    sentence_pattern = r'[^.!?]+[.!?]'
    
    sentences = [s.strip() for s in re.findall(sentence_pattern, text)]

    questions = [s for s in sentences if s.endswith('?')]

    quoted_text = re.findall(r'"(.*?)"', text)

    extracted_info ={
        'prices': prices,
        'percentages': percentages,
        'years': years,
        'sentences': sentences,
        'questions': questions,
        'quoted_text': quoted_text
    }
    print(extracted_info)
extract_information()

def clean_text_pipeline():
    original_text = " Hello WORLD! Visit https://example.com and email me@site.com  "
    text = original_text
    operations = ['trim', 'lowercase', 'remove_urls', 'remove_emails', 'remove_extra_spaces']

    for op in operations:
        if op == 'trim':
            text = text.strip()
        elif op == 'lowercase':
            text = text.lower()
        elif op == 'remove_punctuation':
            text = re.sub(r'[^\w\s]', '', text)
        elif op == 'remove_digits':
            text = re.sub(r'\d+', '', text)
        elif op == 'remove_extra_spaces':
            text = re.sub(r'\s+', ' ', text).strip()
        elif op == 'remove_urls':
            text = re.sub(r'http\S+|www\.\S+', '', text)
        elif op == 'remove_emails':
            text = re.sub(r'\S+@\S+\.\S+', '', text)
        elif op == 'capitalize_sentences':
            parts = re.split(r'([.!?]\s*)', text)
            text = ''.join(p.capitalize() for p in parts)

    print("Original:", original_text)
    print("Cleaned:", text)
clean_text_pipeline()


def smart_replace():
    text = "Call me at 555-123-4567. I'm busy ,don't email me@site.com! I have 2 cats."
    contractions = {
        "don't": "do not",
        "won't": "will not",
        "can't": "cannot",
        "I'm": "I am",
        "you're": "you are",
        "it's": "it is",
        "he's": "he is",
        "she's": "she is",
        "we're": "we are",
        "they're": "they are",
        "I've": "I have",
        "you've": "you have",
        "we've": "we have",
        "they've": "they have"
    }
    number_words = {
        "0": "zero",
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine"
    }
    text = re.sub(r"\b\d{3}-\d{3}-\d{4}\b", "XXX-XXX-XXXX", text)

    text = re.sub(r"\b[\w\.-]+@[\w\.-]+\.\w+\b", "[EMAIL]", text)

    text = re.sub(r"\s+([.,!?])", r"\1", text)
    text = re.sub(r"([.,!?])([^\s])", r"\1 \2", text)

    for short, full in contractions.items():
        text = re.sub(r"\b" + re.escape(short) + r"\b", full, text)
        
    for digit, word in number_words.items():
        text = re.sub(r"\b" + digit + r"\b", word, text)

    return text


print(smart_replace())


def analyze_log_file():
    # Regex pattern to capture: date, time, level, message
    
    log_text = """[2024-01-15 10:30:45] ERROR: Connection failed
    [2024-01-15 10:31:00] INFO: Retry attempt 1
    [2024-01-15 11:00:00] WARNING: High memory usage"""
    
    pattern = r"\[(\d{4}-\d{2}-\d{2}) (\d{2}):(\d{2}):(\d{2})\] (\w+): (.+)"
    matches = re.findall(pattern, log_text)

    total_entries = len(matches)
    error_count = 0
    warning_count = 0
    info_count = 0

    dates = []
    error_messages = []
    times = []
    hours = []

    for date, hour, minute, second, level, message in matches:
        # Collect unique dates
        if date not in dates:
            dates.append(date)

        # Collect times
        full_time = f"{hour}:{minute}:{second}"
        times.append(full_time)

        # Count levels
        if level == "ERROR":
            error_count += 1
            error_messages.append(message)
        elif level == "WARNING":
            warning_count += 1
        elif level == "INFO":
            info_count += 1

        # Collect hours
        hours.append(int(hour))

    # Time
    earliest_time = min(times) if times else None
    latest_time = max(times) if times else None

    # Most active hour
    most_active_hour = None
    if hours:
        max_count = 0
        for h in hours:
            count = hours.count(h)
            if count > max_count:
                max_count = count
                most_active_hour = h

    return {
        "total_entries": total_entries,
        "error_count": error_count,
        "warning_count": warning_count,
        "info_count": info_count,
        "dates": dates,
        "error_messages": error_messages,
        "time_range": (earliest_time, latest_time),
        "most_active_hour": most_active_hour
    }
analyze_log_file()