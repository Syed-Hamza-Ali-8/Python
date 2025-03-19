def main():
 celsius_temps : float = float(input("Enter a temperature to convert : "))
 fahrenheit_temps = ((celsius_temps * 9/5) + 32)
 print(f"{celsius_temps}°C = {fahrenheit_temps:.2f}°F")
if __name__ == '__main__':
    main()
