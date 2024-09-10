# Tip Calculator

# Function to calculate tip and total amount per person
def calculate_tip(total_bill, tip_percentage, num_people):
 
    
    # Calculate tip amount
    tip_amount = (tip_percentage / 100) * total_bill
    
    # Calculate the total bill including the tip
    total_with_tip = total_bill + tip_amount
    
    # Calculate the amount each person has to pay
    amount_per_person = total_with_tip / num_people
    
    # Return results as a dictionary
    return {
        "tip_amount": tip_amount,
        "total_with_tip": total_with_tip,
        "amount_per_person": amount_per_person
    }

# User inputs
try:
    # Get the total bill amount from the user
    total_bill = float(input("Enter the total bill amount: $"))
    
    # Get the desired tip percentage
    tip_percentage = float(input("Enter the tip percentage you'd like to give (e.g., 15 for 15%): "))
    
    # Get the number of people splitting the bill
    num_people = int(input("Enter the number of people splitting the bill: "))
    
    # Validate inputs
    if total_bill <= 0 or tip_percentage < 0 or num_people <= 0:
        raise ValueError("Please enter valid positive numbers for the bill, tip, and number of people.")
    
    # Call the function to calculate the tip and total amounts
    result = calculate_tip(total_bill, tip_percentage, num_people)
    
    # Output the results
    print("\n--- Bill Summary ---")
    print(f"Tip Amount: ${result['tip_amount']:.2f}")
    print(f"Total Bill (with tip): ${result['total_with_tip']:.2f}")
    print(f"Amount per person: ${result['amount_per_person']:.2f}")

except ValueError as e:
    print(f"Error: {e}")
