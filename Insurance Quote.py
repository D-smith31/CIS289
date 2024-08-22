{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Connected to Python 3.11.9"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7c1fd704-a279-4747-b954-f4b77745bf22",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "..\n",
      "----------------------------------------------------------------------\n",
      "Ran 2 tests in 0.001s\n",
      "\n",
      "OK\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Annual insurance cost for Donny: $621.90\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "Donovan Smith\n",
    "8/22/2024\n",
    "Description: This program calculates the annual auto insurance cost based on user input including driver age, coverage level, and any additional factors such as accidents and upfront payment discounts.\n",
    "\"\"\"\n",
    "\n",
    "def get_insurance_rate(age, coverage):\n",
    "    \"\"\" Returns the insurance rate based on age and coverage level. \"\"\"\n",
    "    age_brackets = [16, 25, 35, 45, 55, 65]\n",
    "    state_minimum = [2593, 608, 552, 525, 494, 515]\n",
    "    liability_coverage = [2957, 691, 627, 596, 560, 585]\n",
    "    full_coverage = [6930, 1745, 1564, 1469, 1363, 1402]\n",
    "\n",
    "    if age < 16:\n",
    "        raise ValueError(\"Age must be at least 16.\")\n",
    "    \n",
    "    age_index = next((i for i, bracket in enumerate(age_brackets) if age < bracket), len(age_brackets))\n",
    "    \n",
    "    coverage_rates = {\n",
    "        'SM': state_minimum,\n",
    "        'L': liability_coverage,\n",
    "        'F': full_coverage\n",
    "    }\n",
    "    \n",
    "    if coverage not in coverage_rates:\n",
    "        raise ValueError(\"Invalid coverage level. Choose from 'SM', 'L', 'F'.\")\n",
    "    \n",
    "    return coverage_rates[coverage][age_index]\n",
    "\n",
    "def calculate_final_cost(base_cost, had_accidents, pay_upfront):\n",
    "    \"\"\" Calculates the final insurance cost considering accidents and upfront payment discount. \"\"\"\n",
    "    if had_accidents:\n",
    "        base_cost *= 1.41\n",
    "    \n",
    "    if pay_upfront:\n",
    "        base_cost *= 0.90\n",
    "    \n",
    "    return base_cost\n",
    "\n",
    "def main():\n",
    "    \"\"\" Main function to gather user input and output the insurance cost. \"\"\"\n",
    "    user_info = {}\n",
    "    \n",
    "    try:\n",
    "        user_info['Driver Name'] = input(\"Enter the driver name: \")\n",
    "        user_info['Driver Age'] = int(input(\"Enter the driver age: \"))\n",
    "        coverage_level = input(\"Enter coverage level (SM, L, F): \").strip().upper()\n",
    "        \n",
    "        user_info['Coverage Level'] = coverage_level\n",
    "        user_info['Coverage Cost'] = get_insurance_rate(user_info['Driver Age'], coverage_level)\n",
    "        \n",
    "        had_accidents = input(\"Have you had any accidents? (yes/no): \").strip().lower()\n",
    "        user_info['Had Accidents'] = had_accidents == 'yes'\n",
    "        \n",
    "        pay_upfront = input(\"Do you want to pay up front for a 10% discount? (yes/no): \").strip().lower()\n",
    "        user_info['Pay Upfront'] = pay_upfront == 'yes'\n",
    "        \n",
    "        final_cost = calculate_final_cost(user_info['Coverage Cost'], user_info['Had Accidents'], user_info['Pay Upfront'])\n",
    "        \n",
    "        print(f\"\\nAnnual insurance cost for {user_info['Driver Name']}: ${final_cost:.2f}\")\n",
    "        \n",
    "    except ValueError as e:\n",
    "        print(f\"Input error: {e}\")\n",
    "\n",
    "# Unit tests\n",
    "import unittest\n",
    "\n",
    "class TestInsuranceCalculator(unittest.TestCase):\n",
    "    \n",
    "    def test_get_insurance_rate(self):\n",
    "        self.assertEqual(get_insurance_rate(20, 'SM'), 608)\n",
    "        self.assertEqual(get_insurance_rate(40, 'L'), 596)\n",
    "        self.assertEqual(get_insurance_rate(60, 'F'), 1402)\n",
    "        with self.assertRaises(ValueError):\n",
    "            get_insurance_rate(15, 'SM')\n",
    "        with self.assertRaises(ValueError):\n",
    "            get_insurance_rate(30, 'X')\n",
    "    \n",
    "    def test_calculate_final_cost(self):\n",
    "        self.assertAlmostEqual(calculate_final_cost(1000, True, True), 1000 * 1.41 * 0.90)\n",
    "        self.assertAlmostEqual(calculate_final_cost(1000, False, True), 1000 * 0.90)\n",
    "        self.assertAlmostEqual(calculate_final_cost(1000, True, False), 1000 * 1.41)\n",
    "        self.assertAlmostEqual(calculate_final_cost(1000, False, False), 1000)\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    main()\n",
    "    unittest.main(argv=[''], exit=False)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.11.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
