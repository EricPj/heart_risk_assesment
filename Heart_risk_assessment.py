# Calculating the risk of heart attack based on user input
import time



# Greet the user
def greet_user(): 
    print("Welcome to Heart Risk Calculator!")
    time.sleep(3)
    print("This will help you assess your risk of a heart attack and give you tips to reduce it.")
    time.sleep(3)

# Ask for user's name
def ask_name():
    name = input("First lets start with your name: ")
    print("Hello " + name + "! Im going to ask you a few questions to get started.")
    time.sleep(2)

# Ask for user's age and assign risk points
def ask_age():
    print("How old are you?")
    age = int(input("Age here: "))
    if age < 30:
        return 0
    elif 30 <= age < 45:
        return 1
    elif 45 <= age < 60:
        return 2
    else:
        return 3

#ask for user's gender
def ask_gender():
    gender = input("What is the gender you were assigned at birth? (M/F): ").upper()
    if gender == "M":
        return 1
    else: 
        return 2


#Ask for user's weight and height to calculate BMI
def ask_BMI():
    weight = float(input("What is your weight (lbs)?: "))

    converted_weight = weight * 0.453592
    weight = converted_weight

    height = float(input("How tall are you (example: 5.5)?: "))
    converted_height = height * 0.3048
    height = converted_height

    BMI = weight / height**2
    print("Thanks! Your BMI is " +str(round(BMI)))
    if BMI <= 18.5:
        return 5
    elif 18.5 < BMI <= 25:
        return 0
    elif 25 <BMI <= 30:
        return 3
    elif 30 < BMI <= 39.9:
        return 4
    else:
        return 5
      



#Ask about exercise habits
def ask_exercise():
    exercise = input("Do you exercise regularly? (yes/no): ").lower()
    if exercise == "yes":
        print("Great! Regular exercise is crucial for heart health.")
    else:
        print("Consider incorporating regular exercise into your routine to improve heart health. Even light activities like walking can make a difference.")
    if exercise == "yes":
        return 0
    else:
        return 2

#Ask about smoking habits
def ask_smoking():
    smoke = input("Do you smoke? (yes/no): ").lower()
    if smoke == "yes":
        print("Smoking increases your risk of heart disease. Consider quitting.")
    else:
        print("Great! Avoiding smoking is one of the best things you can do for your heart health.")
    if smoke == "yes":
        return 5
    else:
        return 0

#Ask about family history of heart disease
def ask_family_history():
    family = input("Have you heard of anyone in your family having any kind of heart disease? (yes/no): ").lower()
    if family == "yes":
        print("A family of history of heart disease can increase your risk. Make sure to monitor your heart regularly with your healthcare provider.")
        return 1
    else:
        print("Great! that lowers your risk.")
        return 0

#Ask about shortness of breath
def ask_shortness_of_breath():
    breath = input ("Have you ever experienced any shortness of breath while doing any activities or around the house? (yes/no): ").lower()
    if breath == "yes":
        print("Shortness of breath can be a sign of heart problems. Consult with your doctor and just make sure to moniter this.")
        return 2
    else:
        print("Great! Keep monitoring your health and stay active.")
        return 0

#Ask about chest pain
def ask_chest_pain():
    chest_pain = input("Have you experinced any chest pain? (yes/no): ").lower()
    if chest_pain == "yes":
        print("Chest pain can be a serious symptom. Please seek medical attention immediately.")
        return 4
    else:
        print("Great! Keep monitoring your health and stay active.")
        return 0
    





def main():
    greet_user()
    ask_name()
    
    total_risk_number = 0

    total_risk_number += ask_age()
    total_risk_number += ask_gender()
    total_risk_number += ask_BMI()
    total_risk_number += ask_exercise()
    total_risk_number += ask_smoking()
    total_risk_number += ask_family_history()
    total_risk_number += ask_shortness_of_breath()
    total_risk_number += ask_chest_pain()
    number_ceiling = 24 
    
    risk_percentage = (total_risk_number / number_ceiling) * 100

    print("Calculating your risk score...")
    time.sleep(2)
    print("Your estimated risk is " + str(round(risk_percentage)) + "%")
    time.sleep(2)


main()

