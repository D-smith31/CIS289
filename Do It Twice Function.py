# Define the decorator
def run_twice(func):
    def wrapper(*args, **kwargs):
        print("Running the function twice...")
        func(*args, **kwargs)  # Run the function once
        func(*args, **kwargs)  # Run the function again
    return wrapper

# Apply the decorator
@run_twice
def say_hello(name):
    print(f"Hello, {name}!")

# Call the decorated function
say_hello("Donovan")
