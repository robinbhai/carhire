class CarHireCalculator:
    def __init__(self):
        self.vehicle_rates = {'S': 22.50, 'HP': 28.00, 'V': 35.00}
        self.max_days = 10
        self.discount_percentage = 0.10
        self.insurance_premium = 15.50
        self.deposit = 50.00
        self.high_performance_discount = 18.00

    def calculate_cost(self, vehicle_type, hiring_days, insurance, customer_type, loyalty_card=None):
        if vehicle_type not in self.vehicle_rates:
            raise ValueError("Invalid vehicle type")

        if not (1 <= int(hiring_days) <= self.max_days):
            raise ValueError("Invalid number of days")

        if customer_type not in ('new', 'existing'):
            raise ValueError("Invalid customer type")

        if customer_type == 'existing' and loyalty_card not in ('Bronze', 'Silver', 'Gold'):
            raise ValueError("Invalid loyalty card type")

        daily_rate = self.vehicle_rates[vehicle_type]

        if int(hiring_days) > 7:
            total_cost = int(hiring_days) * daily_rate * (1 - self.discount_percentage)
        else:
            total_cost = int(hiring_days)* daily_rate

        if vehicle_type == 'HP' and customer_type == 'existing' and loyalty_card == 'Gold':
            total_cost -= self.high_performance_discount

        if insurance == 'Yes':
            total_cost += self.insurance_premium

        total_cost += self.deposit

        return total_cost