"""
Donovan Smith
8/22/2024
Description: This program calculates the annual auto insurance cost based on user input including driver age, coverage level, and any additional factors such as accidents and upfront payment discounts.
"""

def get_insurance_rate(age, coverage):
    """ Returns the insurance rate based on age and coverage level. """
    age_brackets = [16, 25, 35, 45, 55, 65]
    state_minimum = [2593, 608, 552, 525, 494, 515]
    liability_coverage = [2957, 691, 627, 596, 560, 585]
    full_coverage = [6930, 1745, 1564, 1469, 1363, 1402]

    if age < 16:
        raise ValueError("Age must be at least 16.")
    
    age_index = next((i for i, bracket in enumerate(age_brackets) if age < bracket), len(age_brackets))
    
    coverage_rates = {
        'SM': state_minimum,
        'L': liability_coverage,
        'F': full_coverage
    }
    
    if coverage not in coverage_rates:
        raise ValueError("Invalid coverage level. Choose from 'SM', 'L', 'F'.")
    
    return coverage_rates[coverage][age_index]

def calculate_final_cost(base_cost, had_accidents, pay_upfront):
    """ Calculates the final insurance cost considering accidents and upfront payment discount. """
    if had_accidents:
        base_cost *= 1.41
    
    if pay_upfront:
        base_cost *= 0.90
    
    return base_cost

def main():
    """ Main function to gather user input and output the insurance cost. """
    user_info = {}
    
    try:
        user_info['Driver Name'] = input("Enter the driver name: ")
        user_info['Driver Age'] = int(input("Enter the driver age: "))
        coverage_level = input("Enter coverage level (SM, L, F): ").strip().upper()
        
        user_info['Coverage Level'] = coverage_level
        user_info['Coverage Cost'] = get_insurance_rate(user_info['Driver Age'], coverage_level)
        
        had_accidents = input("Have you had any accidents? (yes/no): ").strip().lower()
        user_info['Had Accidents'] = had_accidents == 'yes'
        
        pay_upfront = input("Do you want to pay up front for a 10% discount? (yes/no): ").strip().lower()
        user_info['Pay Upfront'] = pay_upfront == 'yes'
        
        final_cost = calculate_final_cost(user_info['Coverage Cost'], user_info['Had Accidents'], user_info['Pay Upfront'])
        
        print(f"\nAnnual insurance cost for {user_info['Driver Name']}: ${final_cost:.2f}")
        
    except ValueError as e:
        print(f"Input error: {e}")

# Unit tests
import unittest

class TestInsuranceCalculator(unittest.TestCase):
    
    def test_get_insurance_rate(self):
        self.assertEqual(get_insurance_rate(20, 'SM'), 608)
        self.assertEqual(get_insurance_rate(40, 'L'), 596)
        self.assertEqual(get_insurance_rate(60, 'F'), 1402)
        with self.assertRaises(ValueError):
            get_insurance_rate(15, 'SM')
        with self.assertRaises(ValueError):
            get_insurance_rate(30, 'X')
    
    def test_calculate_final_cost(self):
        self.assertAlmostEqual(calculate_final_cost(1000, True, True), 1000 * 1.41 * 0.90)
        self.assertAlmostEqual(calculate_final_cost(1000, False, True), 1000 * 0.90)
        self.assertAlmostEqual(calculate_final_cost(1000, True, False), 1000 * 1.41)
        self.assertAlmostEqual(calculate_final_cost(1000, False, False), 1000)

if __name__ == '__main__':
    main()
    unittest.main(argv=[''], exit=False)
