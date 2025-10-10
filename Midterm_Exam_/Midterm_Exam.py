import numpy as np
import re

#Midterm Exam
#Cody Fancil, 10/10/2025
"""
# Chosen problem 1, Dictionary:
Create a shopping cart with these functions:
1. add_item(cart, item_name, price, quantity)
 - Add item to cart (or update quantity if exists)
 - Price must be positive (> 0)
 - Quantity must be positive integer
 - Return True if added/updated, False if invalid
2. calculate_total(cart)
 - Calculate total cost of all items
 - Formula: sum of (price * quantity) for each item
 - Return 0 if cart is empty
3. apply_discount(cart, discount_percent)
 - Apply discount to all prices (0-100%)
 - Example: 20% discount means multiply prices by 0.8
 - Return True if valid discount, False otherwise
Example:
 cart = {}
 add_item(cart, "Apple", 0.50, 6)
 add_item(cart, "Bread", 2.00, 2)

 print(calculate_total(cart)) # Should print 7.00
 apply_discount(cart, 10) # 10% off
 print(calculate_total(cart)) # Should print 6.30
"""

# Write your code here:
cart = {
    "Apple": {"price": 0.50, "quantity": 6},
    "Fish": {"price": 2.00, "quantity": 2}
}
def add_item(cart, item_name, price, quantity):
    if item_name in cart:
        cart[item_name]["quantity"] += quantity
    else:
        cart[item_name] = {"price": price, "quantity": quantity}
    
    if price <= 0:
        return False
    elif quantity <=0:
        return False
    else:
        return True
def calculate_total(cart):
    if cart == {}:
        return 0
    return sum(item["price"] * item["quantity"] for item in cart.values())
def apply_discount(cart, discount_percent):
    for item in cart.items():
        item[1]["price"] *= (1 - discount_percent / 100)
    return True

# Test your functions
if __name__ == "__main__":
 cart = {}

 # Test adding items
 print(add_item(cart, "Milk", 3.50, 2)) # Should print True
 print(add_item(cart, "Eggs", -1.00, 1)) # Should print False (negative price)
 print(add_item(cart, "Bread", 2.00, 3)) # Should print True

 # Test total
 print(f"Total: ${calculate_total(cart):.2f}")

 # Test discount
 print(apply_discount(cart, 20)) # 20% off
 print(f"After discount: ${calculate_total(cart):.2f}")
 
# Problem 3: Score Analysis with NumPy
"""
Analyze student test scores across multiple exams.
Write functions to:
1. create_score_array(num_students, num_exams)
 - Create array of random scores between 60-100
 - Shape should be (num_students, num_exams)
 - Use np.random.randint(60, 101, size=...)
2. find_struggling_students(scores, threshold)
 - Find students whose average is below threshold
 - Return array of boolean variables
3. curve_scores(scores, bonus_points)
 - Add bonus points to all scores
 - Cap maximum score at 100 (use np.minimum)
 - Return curved scores array
4. get_exam_statistics(scores)
 - Return dictionary with statistics for each exam:
 - {"exam_0": {"mean": x, "max": y, "min": z}, ...}
Example:
 scores = create_score_array(5, 3) # 5 students, 3 exams
 print(scores)

 struggling = find_struggling_students(scores, 70)
 print(f"Struggling students: {struggling}")

 curved = curve_scores(scores, 5) # Add 5 points
 print(f"After curve: {curved}")
"""

# Write your code here:
def create_score_array(num_students, num_exams):
    return np.random.randint(60, 101, size=(num_students, num_exams))
def find_struggling_students(scores, threshold):
    return np.mean(scores, axis=1) < threshold
def curve_scores(scores, points):
    curved = scores + points
    return np.clip(curved, 60, 100)
def get_exam_statistics(scores):
    #Couldnt finish this one in time
    pass


# Problem 4: Text Message Cleaner
"""
Clean and analyze text messages.
Write these functions:
1. clean_message(message)
 - Convert to lowercase
 - Remove extra spaces (use split and join)
 - Remove punctuation at the end (. ! ?)
 - Return cleaned message
2. expand_abbreviations(message)
 - Replace common abbreviations:
 "u" -> "you"
 "ur" -> "your"
 "r" -> "are"
 "thx" -> "thanks"
 - Return expanded message
3. count_words(message)
 - Split message into words
 - Return dictionary with word counts
 - Example: "hello world hello" -> {"hello": 2, "world": 1}
4. censor_numbers(message)
 - Replace any sequence of digits with "XXX"
 - Example: "Call 1234567890" -> "Call XXX"
 - Keep other text unchanged
Example:
 msg = " Hello WORLD!!! "
 clean = clean_message(msg)
 print(clean) # "hello world"

 msg2 = "thx u r great"
 expanded = expand_abbreviations(msg2)
 print(expanded) # "thanks you are great"
"""
message = "HeY! Would u LIKE to gO to Johns place nxt WEEKEND, THX! My Number is 1234567890"
# Write your code here:
def clean_message(message):
    message = message.lower().split(" ")
    print (f"This is lowered split: {message}")
    message = [word.strip("!?.") for word in message]
    finalmessage = " ".join(message)
    print (f"This is the final joined message: {finalmessage}")
    return finalmessage
def expand_abbreviations(finalmessage):
    abbreviated_message = finalmessage.replace(" u ", " you ").replace(" r ", " are ").replace(" THX", " thanks").replace(" nxt ", " next ")
    print (f"This is the abbreviated message: {abbreviated_message}")
    return abbreviated_message
def count_words(message):
    pattern = r'\b\w+\b'
    words = re.findall(pattern, message.lower())
    total = len(words)
    print (f"This is the word count: {total}")
    return total
def censor_numbers(message):
    print (f"This is the original message: {message}")
    censored_message = re.sub(r'\d+', 'XXX', message)
    print (f"This is the censored message: {censored_message}")
    return censored_message
clean_message(message)
expand_abbreviations(message)
count_words(message)
censor_numbers(message)