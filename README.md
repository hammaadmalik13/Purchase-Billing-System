# Purchase-Billing-System
A Python program designed to calculate the bill summary for a given number of purchases, applying discount rates based on the purchase amount. The program provides a detailed bill summary, including the original price, discount, and final bill for each item, as well as a total bill summary.

Features

- Calculates discount rates based on the purchase amount:
    - 20% discount for purchases ≥ ₹5000
    - 15% discount for purchases ≥ ₹3000
    - 10% discount for purchases ≥ ₹1000
    - No discount for purchases < ₹1000
- Displays a detailed bill summary for each item, including:
    - Original price
    - Discount amount and percentage
    - Final bill
- Displays a total bill summary, including:
    - Total original price
    - Total discount
    - Total final bill

 Code Structure

The program consists of a single Python file, purchase_billing_system.py, which contains the following classes and functions:

- Purchase class: represents a single purchase, with attributes for the item name, purchase amount, discount rate, discount amount, and final bill.
- main function: prompts the user for the number of purchases, item names, and purchase amounts, and calculates the bill summary.

Example Use Case

1. Run the program and enter the number of purchases: 2
2. Enter the item name and purchase amount for each item:
    - Item 1: Item A, ₹5000
    - Item 2: Item B, ₹2000
3. The program displays the bill summary:
    - Total Original Price: ₹7000.00
    - Total Discount: ₹1150.00
    - Total Final Bill: ₹5850.00
    - Item Bill Summary:
        - Item 1: Item A
            - Original Price: ₹5000.00
            - Discount: ₹1000.00 (20.0%)
            - Final Bill: ₹4000.00
        - Item 2: Item B
            - Original Price: ₹2000.00
            - Discount: ₹150.00 (15.0%)
            - Final Bill: ₹1850.00

