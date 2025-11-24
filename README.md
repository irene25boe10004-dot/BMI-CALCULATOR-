# BMI-CALCULATOR-
A BMI calculator is a medical screening tool used to estimate a person's body fat based on their weight relative to their height.  I have created a BMI calculator to provide an easy, quick, and accessible way for individuals and healthcare providers to estimate body fat. It helps identify potential health for a quicker and effective cure.
Over view of the project: 
This is a basic command-line utility designed to calculate a user's Body Mass Index (BMI) and provide a corresponding weight status classification based on the calculated value.
Functionality
Inputs: User provides height (cm) and weight (kg).
Calculation: The script converts height to meters and calculates BMI using the formula: BMI = {weight}/{height (m)}^2}.
Output: Prints the calculated BMI score and the corresponding weight status.
Features:
User Input: Accepts height (cm) and weight (kg) from the user.
Unit Conversion: Converts height from centimeters to meters for the BMI formula.
BMI Calculation: Attempts to compute the Body Mass Index (BMI = {weight}}\{height}^2}).
Result Display: Prints the calculated BMI score.
Conditional Classification: Uses if/elif/else statements to assign a weight status (Underweight, Healthy, Overweight, or Obese).
Technologies/Tools used:
The BMI Calculator script uses Python as the programming language, relying exclusively on standard built-in functions and structures such as:
Functions: print(), input(), float().
Operators: Arithmetic (/, *) and Comparison (<=, >=).
Control Flow: if, elif, else statements.
It requires no external libraries or advanced tools.
Steps to install and run the project:
Install Python: Ensure Python 3.x is installed on your system.
Create Script: Save the code as a Python file (e.g., bmi.py).
Run: Open your terminal, navigate to the file's location, and execute it using the command:
Input: Enter the requested height and weight when prompted.
Instructions for Testing:
Test the BMI Calculator script by running it multiple times to cover all output conditions.
Test Cases & Expected Results
Run the script (python bmi.py) with specific inputs to verify the BMI calculation and the classification logic (if/elif/else).
Underweight: Use inputs like 170 cm and 50 kg to get a BMI approx 17.3, verifying the status prints Underweight.
Healthy: Use inputs like 175 cm and 70 kg to get a BMI approx 22.9, verifying the status prints Healthy.
Overweight: Use inputs like 170 cm and 80 kg to get a BMI approx 27.7, verifying the status prints Overweight.
Obese: Use inputs like 160 cm and 77 kg to get a BMI approx 30.1, verifying the status prints Obese.
After each run, verify two things: the displayed BMI number must be mathematically accurate, and the final printed status must correctly correspond to that BMI category.
