def calculate_bmi(weight, height):
    return weight / (height ** 2)

def get_health_status(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    while True:
        print("\nBMI Calculator & Health Advisor")
        try:
            weight = float(input("Enter weight in kg (or 0 to exit): "))
            if weight == 0:
                print("Exiting program...")
                break
            height = float(input("Enter height in meters: "))
            
            bmi = calculate_bmi(weight, height)
            status = get_health_status(bmi)
            
            print(f"\nYour BMI: {bmi:.1f}")
            print(f"Health Status: {status}")
            
        except ValueError:
            print("Please enter valid numbers.")
        except ZeroDivisionError:
            print("Height cannot be zero.")

if __name__ == "__main__":
    main()