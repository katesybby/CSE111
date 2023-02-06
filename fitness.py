# 03 Team Activity: Writing Functions

from datetime import datetime

def main():
    gender = input('Gender (F/M): ')
    birthdate = input('Birth date (YYYY-MM-DD): ')
    pounds = float(input('Weight (pounds): '))
    inches = float(input('Height (inches): ')) 
    
    years = compute_age(birthdate)
    weight = kg_from_lb(pounds)
    height = cm_from_in(inches)
    BMI = body_mass_index(weight, height)
    BMR = basal_metabolic_rate(gender, weight, height, years)

    print (f'Age: {years}')
    print (f'Weight (kg): {weight:.2f}')
    print (f'Height (cm): {height:.1f}')
    print (f'Body Mass Index (BMI): {BMI:.1f}')
    print (f'Basal Metabolic Rate (BMR): {BMR:.0f}')


def compute_age(birth_str):

    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    years = today.year - birthdate.year

    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years


def kg_from_lb(pounds):
    weight = pounds * 0.45359237
    return weight


def cm_from_in(inches):
    height = inches * 2.54
    return height


def body_mass_index(weight, height):
    BMI = (10000 * weight) / height ** 2
    return BMI


def basal_metabolic_rate(gender, weight, height, age):
    if gender.upper() == 'F':
        BMR = 447.593 + 9.247 * weight + 3.098 * height - 4.330 * age
    else:
        BMR = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
    return BMR

main()