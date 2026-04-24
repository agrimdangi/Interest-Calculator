```python
def simple_interest(p, r, t):
    return (p * r * t) / 100


def compound_interest(p, r, t):
    return p * (1 + r / 100) ** t - p


def main():
    print("💰 Interest Calculator")
    print("------------------------")

    while True:
        print("\nChoose an option:")
        print("1. Simple Interest")
        print("2. Compound Interest")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "3":
            print("👋 Exiting... Thank you!")
            break

        if choice not in ["1", "2"]:
            print("❌ Invalid choice! Try again.")
            continue

        try:
            p = float(input("Enter Principal Amount: "))
            r = float(input("Enter Rate of Interest (%): "))
            t = float(input("Enter Time (years): "))
        except ValueError:
            print("❌ Please enter valid numeric values!")
            continue

        if choice == "1":
            si = simple_interest(p, r, t)
            print(f"\n✅ Simple Interest = {si:.2f}")

        elif choice == "2":
            ci = compound_interest(p, r, t)
            print(f"\n✅ Compound Interest = {ci:.2f}")

        # Ask user to continue
        cont = input("\nDo you want to calculate again? (y/n): ").lower()
        if cont != 'y':
            print("👋 Thank you for using the calculator!")
            break


if __name__ == "__main__":
    main()
```
