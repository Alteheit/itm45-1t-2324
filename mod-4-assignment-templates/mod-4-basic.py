'''Module 2: Individual Programming Assignment 1

Useful Business Calculations

This assignment covers your basic proficiency with Python.
'''

def savings(gross_pay, tax_rate, expenses):
    '''Savings.
    2 points.

    This function calculates the money remaining
        for an employee after taxes and expenses.
    
    To get the take-home pay of an employee, we will
        follow the following process:
        1. Apply the tax rate to the gross pay of the employee; round down
        2. Subtract the expenses from the after-tax pay of the employee

    Parameters
    ----------
    gross_pay: int
        the gross pay of an employee for a certain time period, expressed in centavos
    tax_rate: float
        the tax rate for a certain time period, expressed as a number between 0 and 1 (e.g., 0.12)
    expenses: int
        the expenses of an employee for a certain time period, expressed in centavos

    Returns
    -------
    int
        the number of centavos remaining from an employee's pay after taxes and expenses
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
import math

def savings(gross_pay, tax_rate, expenses):

    if not (0 <= tax_rate <= 1):
        raise ValueError("Tax rate must be a decimal between 0 and 1.")
    if gross_pay < 0 or expenses < 0:
        raise ValueError("Gross pay and expenses must be non-negative values.")

    non_roundeddown_aftertax = gross_pay * tax_rate
    roundeddown_aftertax = math.floor(non_roundeddown_aftertax)
    savings = gross_pay - roundeddown_aftertax - expenses

    return savings

try:
    gross_pay = int(input("Enter the gross pay in centavos: "))
    tax_rate = float(input("Enter the tax rate (as a decimal between 0 and 1): "))
    expenses = int(input("Enter the expenses in centavos: "))

    result = savings(gross_pay, tax_rate, expenses)
    print("Your total savings is " + str(result) + " centavos")
except ValueError as e:
    print("Input error:", e)
except Exception as e:
    print("An error occurred:", e)



def material_waste(total_material, material_units, num_jobs, job_consumption):
    '''Material Waste.
    2 points.

    This function calculates how much material input will be wasted
        after running a certain number of jobs that consume
        a set amount of material.

    To get the waste of a set of jobs:
        1. Multiply the number of jobs by the material consumption per job.
        2. Subtract the total material consumed from the total material available.

    The users of this function also want you to format the output as a string, annotated with the
        units in which the material is expressed. Do not add a space between the number and the unit.

    Parameters
    ----------
    total_material: int
        the total material available
    material_units: str
        the units used to express a quantity of the material (e.g., "kg", "L", etc.)
    num_jobs: int
        the number of jobs to run
    job_consumption: int
        the amount of material consumed per job

    Returns
    -------
    str
        the amount of remaining material expressed with its unit (e.g., "10kg").
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
import re 

def material_waste(total_material, material_units, num_jobs, job_consumption):
    if total_material < 0:
        raise ValueError("Total Material should be more than or equal to 0")
    if not re.match("^[a-zA-Z]+$", material_units):
        raise ValueError("Material Units should contain only alphabetic characters.")
    if num_jobs < 0:
        raise ValueError("Number of jobs should be more than or equal to 0")
    if job_consumption < 0:
        raise ValueError("Job consumption should be more than or equal to 0")
    
    total_consumed = num_jobs * job_consumption
    material_waste = total_material - total_consumed
    return material_waste

try:
    total_material = int(input("Enter total material available: "))
    material_units = input("Enter material unit: ")
    num_jobs = int(input("Enter number of jobs: "))
    job_consumption = int(input("Enter the amount of material consumed per job: "))

    result = material_waste(total_material, material_units, num_jobs, job_consumption)
    print(result, material_units, sep="")
except ValueError as e:
    print("Input error:", e)
except Exception as e:
    print("An error occurred:", e)

-----

def interest(principal, rate, periods):
    '''Interest.
    3 points.

    This function calculates the final value of an investment after
        gaining simple interest over a number of periods.

    To calculate simple interest, simply multiply the principal to the quantity (rate * time). 
        Add this amount to the principal to get the final value.

    Round down the final amount.

    Parameters
    ----------
    principal: int
        the principal (i.e., starting) amount invested, expressed in centavos
    rate: float
        the interest rate per period, expressed as a decimal representation of a percentage (e.g., 3% is 0.03)
    periods: int
        the number of periods invested

    Returns
    -------
    int
        the final value of the investment
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
import re
import math

def interest(principal, rate, periods):
    if principal < 0:
        raise ValueError("Principal should be more than or equal to 0")
    if not (0 <= rate <= 1):
        raise ValueError("Rate must be a decimal between 0 and 1.")
    if periods < 0:
        raise ValueError("Periods should be more than or equal to 0")
    
    simple_interest = principal * rate * periods
    final_amount = simple_interest + principal
    interest = math.floor(final_amount)
    return interest
    
try:
    principal = int(input("Enter the principal amount invested, expressed in centavos here: "))
    rate = float(input("Enter rate per period, expressed as a decimal representation of a percentage here: "))
    periods = int(input("Enter number of periods invested here: "))

    result = interest(principal, rate, periods) 
    print(result)
except ValueError as e:
    print("Input error:", e)
except Exception as e:
    print("An error occurred:", e)

#next item

def body_mass_index(weight, height):
    '''Body Mass Index.
    3 points.

    This function calculates the body mass index (BMI) of a person
        given their weight and height.

    The formula for BMI is: kg / (m ^ 2)
        (i.e., kilograms over meters squared)

    Unfortunately, the users of this function use the imperial system.
        You will need to first convert their arguments to the metric system.
    
    Parameters
    ----------
    weight: float
        the weight of the person, in pounds
    height: list
        the height of the person, expressed as a list of two integers.
        the first integer is the foot component of their height.
        the second integer is the inches component of their height.
        for example, 5'10" would be passed as [5, 10].

    Returns
    -------
    float
        the BMI of the person.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    def body_mass_index(weight, height):
    if weight < 0:
        raise ValueError("Weight should be more than or equal to 0")
    if height[0] < 0 or height[1] < 0:
        raise ValueError("Feet and inches should be more than or equal to 0")

    pounds_convert_kg = 0.453592
    feet_convert_meters = 0.3048
    inches_convert_meters = 0.0254

    kg_weight = weight * pounds_convert_kg

    meters_height = (height[0] * feet_convert_meters) + (height[1] * inches_convert_meters)

    BMI = kg_weight / (meters_height ** 2)

    return BMI

try:
    weight = float(input("Enter weight in pounds here: "))
    feet = int(input("Enter your height in feet: "))
    inches = int(input("Enter the remaining inches: "))

    result = body_mass_index(weight, [feet, inches])
    print(result)
except ValueError as e:
    print("Input error:", e)
except Exception as e:
    print("An error occurred:", e)
