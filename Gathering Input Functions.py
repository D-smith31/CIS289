def get_number_of_integers():
    while True:
        try:
            num = int(input("How many integers do you want to input? "))
            if num < 1:
                print("Please enter a number greater than 0.")
            else:
                return num
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_integers(num, last_prompt="Enter integer: "):
    integers = []
    for i in range(num):
        while True:
            prompt = last_prompt if i == num - 1 else "Enter integer: "
            try:
                integer = int(input(prompt))
                integers.append(integer)
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
    return integers

def calculate_average(integers):
    return sum(integers) / len(integers) if integers else 0

def main():
    num_integers = get_number_of_integers()
    integers = get_integers(num_integers)
    print(f"The list of integers is: {integers}")
    average = calculate_average(integers)
    print(f"The average of the integers is: {average}")

if __name__ == "__main__":
    main()
