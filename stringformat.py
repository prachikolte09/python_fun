data = "race a car"
print(data[0].isalnum())

def format_string(data):
    f_string = [char.lower() for char in data if char.isalnum()]
    f_string = "".join(f_string)
    return f_string

def check_palindrome(data):
    return format_string(data) == format_string(data)[::-1]


print(check_palindrome(data))