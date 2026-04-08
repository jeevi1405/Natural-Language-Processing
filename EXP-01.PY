import re

text = "My phone number is 9876543210 and email is test@gmail.com"

# Match digits (phone number)
phone = re.search(r"\d{10}", text)
if phone:
    print("Phone number found:", phone.group())

# Match email
email = re.search(r"\S+@\S+", text)
if email:
    print("Email found:", email.group())
