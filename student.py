another = {
    "name": "John Doe",
    "age": 30,
    "is_student": False,
    "courses": ["Math", "Science", "History"],
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "zip": "12345",
        "co-ordinates": {
            "latitude": 40.7128,
            "longitude": -74.0060
        }
    }
}

# create a function called get_full_address which returns the full address as a single string use get()

def get_full_address(student):
    address = student.get("address", "Address not found")
    return f"{address.get('street')}, {address.get('city')}, {address.get('zip')}"

print(get_full_address(another))

# John Doe does Math, Science, and History
def get_courses(student):
    name = student.get("name")
    courses = student.get("courses")
    math = courses[0]
    science = courses[1]
    history = courses[2]
    return f"{name} does {math}, {science}, and {history}"

print(get_courses(another))