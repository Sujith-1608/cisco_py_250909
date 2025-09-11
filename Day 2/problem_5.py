def main():
    numbers = input("Enter numbers separated by spaces: ")
    num_list = [int(x) for x in numbers.split()]
    maximum = max(num_list)
    minimum = min(num_list)
    with open("minmax_data.txt", "w") as f:
        f.write(f"Numbers: {num_list}\n")
        f.write(f"Maximum: {maximum}\n")
        f.write(f"Minimum: {minimum}\n")
    print("\nData read from file:")
    with open("minmax_data.txt", "r") as f:
        content = f.read()
        print(content)

if __name__ == "__main__":
    main()