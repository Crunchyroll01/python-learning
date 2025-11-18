import re, time
# Homework 6, Cody Fancil
def problem1():
    """
    Extract information using regex groups.
    """
    # a) Extract date components from various date formats
    dates_text = """
    Important dates:
    - Project due: 2024-03-15
    - Meeting on: 12/25/2024
    - Holiday: July 4, 2025
    """
    # TODO: Write a pattern that captures dates in format YYYY-MM-DD
    pattern_iso = r"[0-9]{4}-[0-9]{2}-[0-9]{2}" # Your pattern here
    # TODO: Extract all ISO format dates (YYYY-MM-DD)
    iso_dates = re.findall(pattern_iso,dates_text)
    # b) Parse email addresses and extract username and domain
    emails_text = "Contact john.doe@example.com or alice_smith@university.edu for info"
    # TODO: Write pattern with named groups for username and domain
    pattern_email = r"(?P<username>[^@]+)@(?P<domain>[^@]+)" # Use (?P<name>...) syntax
    # TODO: Extract all emails with their components
    email_parts = re.finditer(pattern_email, emails_text)
    email_parts = [{'username': match.group('username'), 'domain': match.group('domain')} for match in email_parts]
    # c) Extract phone numbers with area codes
    phones_text = "Call (555) 123-4567 or 800-555-1234 for support"
    # TODO: Write pattern to capture area code and number separately
    pattern_phone = r"\((\d{3})\) (\d{3}-\d{4})|(\d{3}-\d{3}-\d{4})" # Capture area code in group 1, rest in group 2
    # TODO: Extract all phone numbers as tuples (area_code, number)
    phone_numbers = [(match.group(1), match.group(2)) for match in re.finditer(pattern_phone, phones_text)]
    # d) Find repeated words in text
    repeated_text = "The the quick brown fox jumped over the the lazy dog"
    # TODO: Write pattern to find consecutive repeated words
    pattern_repeated = r"\b(\w+)\s+\1\b" # Hint: Use backreference \1
    # TODO: Find all repeated words
    repeated_words = re.findall(pattern_repeated, repeated_text)
    return {
    'iso_dates': iso_dates,
    'email_parts': email_parts,
    'phone_numbers': phone_numbers,
    'repeated_words': repeated_words
    }
# Expected outputs:
# iso_dates: ['2024-03-15']
# email_parts: [{'username': 'john.doe', 'domain': 'example.com'}, ...]
# phone_numbers: [('555', '123-4567'), ('800', '555-1234')]
# repeated_words: ['the', 'the']

def problem2():
    """
    Use alternation to create flexible patterns.
    """
    # a) Match different file extensions
    files_text = """
    Documents: report.pdf, notes.txt, presentation.pptx
    Images: photo.jpg, diagram.png, icon.gif, picture.jpeg
    Code: script.py, program.java, style.css
    """
    # TODO: Pattern to match image files (jpg, jpeg, png, gif)
    pattern_images = r"photo\.jpg|diagram\.png|icon\.gif|picture\.jpeg" # Use alternation
    # TODO: Find all image filenames
    image_files = re.findall(pattern_images, files_text)
    # b) Match different date formats
    mixed_dates = "Meeting on 2024-03-15 or 03/15/2024 or March 15, 2024"
    # TODO: Pattern to match all three date formats using alternation
    pattern_dates = r"2024-03-15|03/15/2024|March 15, 2024" # Match ISO, US, and text formats
    # TODO: Find all dates regardless of format
    all_dates = re.findall(pattern_dates, mixed_dates)
    # c) Extract prices in different formats
    prices_text = "$19.99, USD 25.00, 30 dollars, €15.50, £12.99"
    # TODO: Pattern to match prices with different currency symbols
    pattern_prices = r"\$\d+\.\d{2}|USD \d+\.\d{2}|[\d,]+ dollars|€\d+\.\d{2}|£\d+\.\d{2}" # Match $, USD, dollars, €, £
    # TODO: Extract all prices with their currency indicators
    prices = re.findall(pattern_prices, prices_text)
    # d) Match programming language mentions
    code_text = """
    We use Python for data science, Java for enterprise apps,
    JavaScript or JS for web development, and C++ or CPP for systems.
    """
    # TODO: Pattern to match language names and their abbreviations
    pattern_langs = r"Python|Java|JavaScript|JS|C\+\+|CPP" # Match full names and common abbreviations
    # TODO: Find all programming language mentions
    languages = re.findall(pattern_langs, code_text)
    return {
    'image_files': image_files,
    'all_dates': all_dates,
    'prices': prices,
    'languages': languages
    }
    
def problem3():
    """
    Practice with findall() and finditer() methods.
    """
    log_text = """
    [2024-03-15 10:30:45] INFO: Server started on port 8080
    [2024-03-15 10:31:02] ERROR: Connection failed to database
    [2024-03-15 10:31:15] WARNING: High memory usage detected (85%)
    [2024-03-15 10:32:00] INFO: User admin logged in from 192.168.1.100
    [2024-03-15 10:32:30] ERROR: File not found: config.yml
    """
    # a) Use findall() to extract all timestamps
    # TODO: Pattern for timestamp [YYYY-MM-DD HH:MM:SS]
    pattern_timestamp = r"[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}" # Match timestamps
    # TODO: Extract all timestamps
    timestamps = re.findall(pattern_timestamp, log_text)
    # b) Use findall() with groups to extract log levels and messages
    # TODO: Pattern with groups for log level and message
    pattern_log = r"\[(.*?)\] (\w+): (.*)" # Capture level and message separately
    # TODO: Extract tuples of (level, message)
    log_entries = re.findall(pattern_log, log_text)
    # c) Use finditer() to get positions of all IP addresses
    # TODO: Pattern for IP addresses
    pattern_ip = r"\b(?:\d{1,3}\.){3}\d{1,3}\b" # Match IPv4 addresses
    # TODO: Find all IP addresses with their positions
    ip_addresses = [] # List of dicts with 'ip', 'start', 'end' keys
    for match in re.finditer(pattern_ip, log_text):
        ip_addresses.append({
            'ip': match.group(),
            'start': match.start(),
            'end': match.end()
        })
    # d) Use finditer() to create a highlighted version of errors
    # TODO: Replace ERROR entries with **ERROR** (highlighted)
    highlighted_log = log_text # Modified version with highlighted errors
    # TODO: Create function to highlight all ERROR entries
    def highlight_errors(text):
        """
        Surround all ERROR log entries with ** markers.
        Return modified text.
        """
        # Your implementation here
        pattern_error = r"(ERROR: .*)" # Match entire ERROR line
        return re.sub(pattern_error, r"**\1**", text)
    highlighted_log = highlight_errors(log_text)
    return {
        'timestamps': timestamps,
        'log_entries': log_entries,
        'ip_addresses': ip_addresses,
        'highlighted_log': highlighted_log
        }
def problem4():
    """
    Practice text transformation using re.sub().
    """
    # a) Clean and format phone numbers
    messy_phones = """
    Contact list:
    - John: 555.123.4567
    - Jane: (555) 234-5678
    - Bob: 555 345 6789
    - Alice: 5554567890
    """
    # TODO: Standardize all phone numbers to format: (555) 123-4567
    # b) Redact sensitive information
    sensitive_text = """
    Customer: John Doe
    SSN: 123-45-6789
    Credit Card: 4532-1234-5678-9012
    Email: john.doe@email.com
    Phone: (555) 123-4567
    """

    def standardize_phones(text):
        """
        Convert all phone number formats to (XXX) XXX-XXXX.
        """
        # Your pattern and substitution here
        pattern = r"(\d{3}-\d{3}-\d{4}) |(\d{3})[.\s](\d{3})[.\s](\d{4})|(\d{10})"
        replacement = r"(\1) \2"
        cleaned_phones = re.sub(pattern, replacement, text)
        return cleaned_phones
    cleaned_phones = standardize_phones(messy_phones)
    # TODO: Redact SSN and Credit Card numbers
    def redact_sensitive(text):
        """
        Replace SSN with XXX-XX-XXXX and
        Credit Card with XXXX-XXXX-XXXX-XXXX.
        """
        # Your implementation here
        redacted_text = re.sub(r"\b\d{3}-\d{2}-\d{4}\b", "XXX-XX-XXXX", text)
        redacted_text = re.sub(r"\b(?:\d{4}[- ]?){3}\d{4}\b", "XXXX-XXXX-XXXX-XXXX", redacted_text)
        return redacted_text
    redacted_text = redact_sensitive(sensitive_text)
    # c) Convert markdown links to HTML
    markdown_text = """
    Check out [Google](https://google.com) for search.
    Visit [GitHub](https://github.com) for code.
    Read documentation at [Python Docs](https://docs.python.org).
    """
    # TODO: Convert [text](url) to <a href="url">text</a>
    def markdown_to_html(text):
        """
        Convert markdown links to HTML anchor tags.
        """
        # Your pattern and substitution here
        return text # Modified text
    html_text = markdown_to_html(markdown_text)
        # d) Implement a simple template system
    template = """
    Dear {name},
    Your order #{order_id} for {product} has been shipped.
    Tracking number: {tracking}
    """
    values = {
    'name': 'John Smith',
        'order_id': '12345',
    'product': 'Python Book',
    'tracking': 'TRK789XYZ'
    }
    # TODO: Replace {key} with corresponding values
    def fill_template(template, values):
        """
        Replace all {key} placeholders with values from dictionary.
        """
        for key, value in values.items():
            template = template.replace(f"{{{key}}}", value)
    filled_template = fill_template(template, values)
    return template, {
        'cleaned_phones': cleaned_phones,
        'redacted_text': redacted_text,
        'html_text': html_text,
        'filled_template': filled_template
        }

def problem5():
    """
    Use compiled patterns for efficiency and clarity.
    """
    # Create a class to hold compiled patterns
    class PatternLibrary:
        """
        Library of compiled regex patterns for common use cases.
        """
        # TODO: Compile these patterns
        # Use re.IGNORECASE, re.MULTILINE, re.VERBOSE as appropriate
        # a) Email validation pattern (case insensitive)
        EMAIL = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", re.IGNORECASE)
        # b) URL pattern (with optional protocol)
        URL = re.compile(r"https?://[^\s]+", re.IGNORECASE)
        # c) US ZIP code (5 digits or 5+4 format)
        ZIP_CODE = re.compile(r"\b\d{5}(-\d{4})?\b")
        # d) Strong password (verbose pattern with comments)
        # Requirements: 8+ chars, uppercase, lowercase, digit, special char
        PASSWORD = re.compile(r""" ^ (?=.*[A-Z]) (?=.*[a-z]) (?=.*\d) (?=.*[@$!%*?&]) .{8,} $ """, re.VERBOSE)
        # e) Credit card number (with spaces or dashes optional)
        CREDIT_CARD = re.compile(r"\b(?:\d{4}[- ]?){3}\d{4}\b")
    # Test your patterns
    test_data = {
    'emails': ['valid@email.com', 'invalid.email', 'user@domain.co.uk'],
    'urls': ['https://example.com', 'www.test.org', 'invalid://url'],
    'zips': ['12345', '12345-6789', '1234', '123456'],
    'passwords': ['Weak', 'Strong1!Pass', 'nouppercas3!', 'NoDigits!'],
    'cards': ['1234 5678 9012 3456', '1234-5678-9012-3456',
    '1234567890123456']
    }
    # TODO: Validate each item using your compiled patterns
    validation_results = {
    'emails': [PatternLibrary.EMAIL.fullmatch(email) is not None for email in test_data['emails']],
    'urls': [PatternLibrary.URL.search(url) is not None for url in test_data['urls']],
    'zips': [PatternLibrary.ZIP_CODE.fullmatch(zip_code) is not None for zip_code in test_data['zips']],
    'passwords': [PatternLibrary.PASSWORD.fullmatch(password) is not None for password in test_data['passwords']],
    'cards': [PatternLibrary.CREDIT_CARD.fullmatch(card) is not None for card in test_data['cards']]
    }
    # TODO: Implement validation logic
    # For each category, check if pattern matches
    return validation_results
def problem6():
    """
    Create a log file analyzer using regex.
    """
    # Sample web server log (Apache/Nginx format)
    log_data = """
    192.168.1.1 - - [15/Mar/2024:10:30:45 +0000] "GET /index.html HTTP/1.1" 200
    5234
    192.168.1.2 - - [15/Mar/2024:10:30:46 +0000] "POST /api/login HTTP/1.1" 401
    234
    192.168.1.1 - - [15/Mar/2024:10:30:47 +0000] "GET /images/logo.png HTTP/1.1"
    304 0
    192.168.1.3 - - [15/Mar/2024:10:30:48 +0000] "GET /admin/dashboard HTTP/1.1"
    403 0
    192.168.1.2 - - [15/Mar/2024:10:30:49 +0000] "POST /api/login HTTP/1.1" 200
    1234
    192.168.1.4 - - [15/Mar/2024:10:30:50 +0000] "GET /products HTTP/1.1" 200
    15234
    192.168.1.1 - - [15/Mar/2024:10:30:51 +0000] "GET /contact HTTP/1.1" 404 0
    """
    # TODO: Parse log entries to extract:
    # - IP address
    # - Timestamp
    # - HTTP method (GET, POST, etc.)
    # - URL path
    # - Status code
    # - Response size
    # a) Create pattern to parse log lines
    log_pattern = r" (\d+\.\d+\.\d+\.\d+) - - \[(.*?)\] \"(.*?)\" (\d+) (\d+)"
    # b) Extract all log entries as structured  data
    parsed_logs = []
    # pattern: ip, timestamp, method, path, status, size
    matches = re.findall(r'(\d+\.\d+\.\d+\.\d+)\s+- -\s+\[(.*?)\]\s+"(\w+)\s+([^\s"]+)[^"]*"\s+(\d{3})\s+(\d+)', log_data, flags=re.MULTILINE)
    for ip, timestamp, method, path, status, size in matches:
        parsed_logs.append({
            'ip': ip,
            'timestamp': timestamp,
            'method': method,
            'path': path,
            'status_code': int(status),
            'response_size': int(size)
        })
    # c) Analyze the logs
    analysis = {
        'total_requests': 0,
        'unique_ips': [],  
        'error_count': 0,
        'total_bytes': 0,
        'methods_used': []
    }
    path_counts = {}
    for entry in parsed_logs:
        analysis['total_requests'] += 1
        if entry['ip'] not in analysis['unique_ips']:
            analysis['unique_ips'].append(entry['ip'])
        if 400 <= entry['status_code'] < 600:
            analysis['error_count'] += 1
        analysis['total_bytes'] += entry['response_size']
        if entry['path'] not in path_counts:
            path_counts[entry['path']] = 0
        path_counts[entry['path']] += 1
        if entry['method'] not in analysis['methods_used']:
            analysis['methods_used'].append(entry['method'])
    # TODO: Implement log parsing and analysis
    return {
    'parsed_logs': parsed_logs,
    'analysis': analysis
    }
# Add this at the bottom of your file to test all problems
if __name__ == "__main__":
    print("Problem 1 Results:")
    print(problem1())
    print("\nProblem 2 Results:")
    print(problem2())
    print("\nProblem 3 Results:")
    print(problem3())
    print("\nProblem 4 Results:")
    print(problem4())
    print("\nProblem 5 Results:")
    print(problem5())
    print("\nProblem 6 Results:")
    print(problem6())
    # Uncomment if attempting bonus
    # print("\nBonus Challenge Results:")
    # print(bonus_challenge())