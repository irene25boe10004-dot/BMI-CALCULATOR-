Problem Statemen
The current healthcare system requires quick, automated tools for preliminary patient assessment. The problem is to develop a robust and error-resistant computational tool that accepts a user's standard physical metrics (height in cm, weight in kg) and performs a physiologically accurate calculation of Body Mass Index (BMI). The primary objective is not just to output the raw number, but to categorize the individual's result against globally accepted weight status standards (Underweight, Healthy/Normal, Overweight, and Obese) to provide an immediate, actionable health risk indicator. This tool must correctly handle data types and ensure that the conditional logic for classification uses non-overlapping, mutually exclusive ranges to prevent misdiagnosis.

Scope of the Project:
The project's scope is to create a basic Command Line Interface (CLI) BMI Calculator with the following functions:
Input: Get height in cm and weight in kg.
Calculation: Convert height to meters and calculate the Body Mass Index (BMI). 
Output: Display the calculated BMI value.
Classification: Print a health status (Underweight, Healthy, Overweight, or Obese) based on the BMI value using the specific, but flawed, if/elif logic provided.

Target Users:
General Public: Individuals who want an instant calculation of their BMI (Underweight, Healthy, Overweight, Obese).
Health Trackers: People monitoring their weight loss or fitness goals who use BMI as a tracking metric.
Python Learners: Students or beginners looking for a hands-on project demonstrating fundamental concepts like input/output and conditional logic.

High Level Features
Interactive Data Capture: Takes Height (cm) and Weight (kg) from the user via the command line.
Unit Handling: Performs centimeter-to-meter conversion for accurate calculation.
BMI Computation: Calculates the Body Mass Index using the {weight}\{height}^2} formula.
Categorization Logic: Classifies the numerical BMI into a definitive weight status (Underweight, Healthy, Overweight, or Obese).
Clear Output: Displays both the calculated BMI score and the corresponding weight status.
