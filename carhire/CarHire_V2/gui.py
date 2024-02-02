import PySimpleGUI as sg
from alogrithm import CarHireCalculator

class CarHireGUI:
    def __init__(self):
        sg.theme('DefaultNoMoreNagging')  # Set the theme

        layout = [
            [sg.Text("Select vehicle type:(S – Saloon, HP – High Performance, V - Van): "), sg.InputCombo(values=['s', 'hp', 'V'], key='vehicle_type')],
            [sg.Text("Select number of days hire required (max. limit 10 days):"),
             sg.InputCombo(values=[str(i) for i in range(1, 11)], key='hiring_days')],
            [sg.Text("Select if insurance cover is required (Yes or No):"),
             sg.InputCombo(values=['Yes', 'No'], key='insurance')],
            [sg.Text("Select if quote is for a new or existing customer:"),
             sg.InputCombo(values=['New', 'Existing'], key='customer_type')],
            [sg.Text("Select the loyalty card type (Bronze, Silver, or Gold):"),
             sg.InputCombo(values=['Bronze', 'Silver', 'Gold'], key='loyalty_card')],
            [sg.Button("Calculate"), sg.Button("Exit")],
            [sg.Text("", size=(50, 5), key='result')]
        ]

        self.window = sg.Window('Car Hire Quote', layout)

    def run(self):
        calculator = CarHireCalculator()

        while True:
            event, values = self.window.read()

            if event in (sg.WIN_CLOSED, 'Exit'):
                break

            if event == 'Calculate':
                vehicle_type = values['vehicle_type'].upper()  # No need to convert to uppercase for car type
                days = values['hiring_days']
                insurance = values['insurance'].capitalize()
                customer_type = values['customer_type'].lower()
                loyalty_card = values['loyalty_card'].capitalize() if customer_type == 'existing' else None

                try:
                    total_cost = calculator.calculate_cost(vehicle_type, days, insurance, customer_type, loyalty_card)
                    result_text = f"Cost Summary:\nVehicle Type: {vehicle_type}\nNo. of days hired: {days}\nCustomer type: {customer_type.capitalize()}\nThe total hire cost: £{total_cost:.2f}\nIndication if insurance cover is included: {insurance}\n "
                except ValueError as e:
                    result_text = f"Error: {e}"

                self.window['result'].update(result_text)

        self.window.close()

if __name__ == "__main__":
    gui = CarHireGUI()
    gui.run()
