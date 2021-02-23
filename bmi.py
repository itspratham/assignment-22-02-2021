# dictionary_people_list = [{'Gender': 'Male', 'HeightCm': 171, 'WeightKg': 96},
#                           {'Gender': 'Male', 'HeightCm': 161, 'WeightKg': 85},
#                           {'Gender': 'Male', 'HeightCm': 180, 'WeightKg': 77},
#                           {'Gender': 'Female', 'HeightCm': 166, 'WeightKg': 62},
#                           {'Gender': 'Female', 'HeightCm': 150, 'WeightKg': 70},
#                           {'Gender': 'Female', 'HeightCm': 167, 'WeightKg': 82}
#                           ]
# dictionary_people_list = [{'Gender': 'Male', 'HeightCm': 171, 'WeightKg': 40},
#                           {'Gender': 'Male', 'HeightCm': 161, 'WeightKg': 30},
#                           {'Gender': 'Male', 'HeightCm': 180, 'WeightKg': 22},
#                           {'Gender': 'Female', 'HeightCm': 166, 'WeightKg': 22},
#                           {'Gender': 'Female', 'HeightCm': 150, 'WeightKg': 40},
#                           {'Gender': 'Female', 'HeightCm': 167, 'WeightKg': 33}
#                           ]


def calculate_bmi(dictionary_people_list):
    new_list = []
    for people in dictionary_people_list:
        new_dict = {}
        if people['HeightCm'] <= 0:
            return "Please enter a valid height"
        if people['WeightKg'] <= 0:
            return "Please enter a valid weight"
        # Considering world's tallest man height ie 273 cm
        if people["HeightCm"] >= 273:
            return "Please enter a valid height"
        # Considering world's heaviest man weight ie 442 kg
        if people["WeightKg"] >= 442:
            return "Please enter a valid weight"
        convert_into_mt = people['HeightCm'] / 100
        bmi_index = people['WeightKg'] / convert_into_mt
        new_dict['BMIIndex'] = round(bmi_index, 2)
        if bmi_index < 18.5:
            new_dict['BMICategory'] = 'Underweight'
            new_dict['HealthRisk'] = 'Malnutrition Risk'
        elif 18.5 <= bmi_index < 25:
            new_dict['BMICategory'] = 'Normal Weight'
            new_dict['HealthRisk'] = 'Low Risk'
        elif 25 <= bmi_index < 30:
            new_dict['BMICategory'] = 'Overweight'
            new_dict['HealthRisk'] = 'Enhanced Risk'
        elif 30 <= bmi_index < 35:
            new_dict['BMICategory'] = 'Moderately Obese'
            new_dict['HealthRisk'] = 'Medium Risk'
        elif 35 <= bmi_index < 40:
            new_dict['BMICategory'] = 'Severely Obese'
            new_dict['HealthRisk'] = 'High Risk'
        elif bmi_index >= 40:
            new_dict['BMICategory'] = 'Very Severely Obese'
            new_dict['HealthRisk'] = 'Very High Risk'
        new_list.append(new_dict)
    for i in range(len(dictionary_people_list)):
        dictionary_people_list[i].update(new_list[i])

    return dictionary_people_list


def count_of_overweight_people(dictionary_people_list):
    dictionary_people = calculate_bmi(dictionary_people_list)
    count = 0
    for people in dictionary_people:
        if 25 <= people['BMIIndex'] < 30:
            count = count + 1
    return count

# print(count_of_overweight_people(dictionary_people_list))
# calculate_bmi(dictionary_people_list)
