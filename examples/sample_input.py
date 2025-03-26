"""
This is a long Python script used to test obfuscation.
It contains functions, classes, string literals, and dummy logic.
"""

import math
import time

# Greeting message
def greet_user(name):
    print("Welcome to PyScramble Tester,", name)

def compute_area(radius):
    """Computes the area of a circle"""
    if radius <= 0:
        return 0
    return math.pi * radius ** 2

def countdown(n):
    while n > 0:
        print("Counting down:", n)
        n -= 1
        time.sleep(0.5)
    print("Blast off!")

class User:
    def __init__(self, name, access_level="guest"):
        self.name = name
        self.access_level = access_level

    def display_info(self):
        print(f"User: {self.name}")
        print(f"Access Level: {self.access_level}")

    def promote(self):
        if self.access_level == "guest":
            self.access_level = "admin"
        print(f"{self.name} has been promoted to {self.access_level}")

def handle_login(username, password):
    print("Authenticating...")
    # This is just placeholder logic
    if username == "admin" and password == "pass123":
        print("Login successful!")
        return True
    print("Access denied.")
    return False

def main():
    greet_user("Fahad")

    area = compute_area(5)
    print("Computed area:", area)

    user = User("Fahad")
    user.display_info()
    user.promote()

    countdown(3)

    result = handle_login("admin", "pass123")
    if result:
        print("Access granted to the system.")
    else:
        print("Shutting down.")

if __name__ == "__main__":
    main()
