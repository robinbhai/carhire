class CarHireCalculator:
    def __init__(self):
        self.vehicle_rates = {'S': 22.50, 'HP': 28.00, 'V': 35.00}
        self.limit_days = 10
        self.discount = 0.10
        self.insurance = 15.50
        self.deposit = 50.00
        self.hp_discount = 18.00

    def calculate_cost(self, vehicle_type, hiring_days, car_insurance, customer_type, loyalty_card=None):
        if vehicle_type not in self.vehicle_rates:
            raise ValueError("Invalid vehicle type")

        if not (1 <= hiring_days <= self.limit_days):
            raise ValueError("Invalid number of days")

        if customer_type not in ('new', 'existing'):
            raise ValueError("Invalid customer type")

        if customer_type == 'existing' and loyalty_card not in ('Bronze', 'Silver', 'Gold'):
            raise ValueError("Invalid loyalty card type")

        daily_rate = self.vehicle_rates[vehicle_type]

        if hiring_days > 7:
            total_cost = hiring_days * daily_rate * (1 - self.discount)
        else:
            total_cost = hiring_days * daily_rate

        if vehicle_type == 'HP' and customer_type == 'existing' and loyalty_card == 'Gold':
            total_cost -= self.hp_discount

        if car_insurance == 'Yes':
            total_cost += self.insurance

        total_cost += self.deposit

        return total_cost

def main():
    calculator = CarHireCalculator()

    # Input details from the user
    vehicle_type = input("Enter which vehicle type you want :(S – Saloon, HP – High Performance, V - Van): ").upper()
    days = int(input("How many days you wanna hire for? (max. limit 10 days): "))
    customer_type = input("Are you new or existing customer: ").lower()
    insurance = input("Do you have car insurance (Yes or No): ").capitalize()
    

    if customer_type == 'existing':
        loyalty_card = input("Enter the loyalty card type (Bronze, Silver or Gold): ").capitalize()
    else:
        loyalty_card = None

    try:
        total_cost = calculator.calculate_cost(vehicle_type, days, insurance, customer_type, loyalty_card)
        print("\nQuote Summary:")
        print(f"Vehicle Type: {vehicle_type}")
        print(f"No. of days hired: {days}")
        print(f"New or existing customer: {customer_type.capitalize()}")
        print(f"Insurance covered: {insurance}")
        if customer_type == 'existing':
            print(f"Loyalty Card: {loyalty_card}")

        print(f"The total hire cost: £{total_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
