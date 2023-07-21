import re

def validate_credit_card(card_number):
    # Check if the card number matches the specified pattern
    pattern = r'^[456]\d{3}(-?\d{4}){3}$'
    if not re.match(pattern, card_number):
        return 'Invalid'

    # Remove any hyphens from the card number
    card_number = card_number.replace('-', '')

    # Check for consecutive repeated digits
    for i in range(len(card_number) - 3):
        if card_number[i] == card_number[i+1] == card_number[i+2] == card_number[i+3]:
            return 'Invalid'

    return 'Valid'


# Read the number of credit card numbers to validate
n = int(input())

# Validate each credit card number
for _ in range(n):
    card_number = input()
    result = validate_credit_card(card_number)
    print(result)
