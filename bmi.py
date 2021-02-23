dictionary_people_list = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96},
                          {"Gender": "Male", "HeightCm": 161, "WeightKg": 85},
                          {"Gender": "Male", "HeightCm": 180, "WeightKg": 77},
                          {"Gender": "Female", "HeightCm": 166, "WeightKg": 62},
                          {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
                          {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}
                          ]


def calculate_bmi(dictionary_people_list):
    for people in dictionary_people_list:
        new_dict = {}
        convert_into_mt = people["HeightCm"] / 100
        bmi_index = people["WeightKg"] / convert_into_mt
        new_dict["BMIIndex"] = round(bmi_index, 2)
        if bmi_index < 18.5:
            new_dict["BMICategory"] = "underweight"
            new_dict["HealthRisk"] = "malnutrition risk"
        elif 18.5 <= bmi_index < 25:
            new_dict["BMICategory"] = "normal weight"
            new_dict["HealthRisk"] = "low risk"
        elif 25 <= bmi_index < 30:
            new_dict["BMICategory"] = "overweight"
            new_dict["HealthRisk"] = "enhanced risk"
        elif 30 <= bmi_index < 35:
            new_dict["BMICategory"] = "moderately obese"
            new_dict["HealthRisk"] = "medium risk"
        elif 35 <= bmi_index < 40:
            new_dict["BMICategory"] = "severely obese"
            new_dict["HealthRisk"] = "high risk"
        elif bmi_index >= 40:
            new_dict["BMICategory"] = "very severely obese"
            new_dict["HealthRisk"] = "very high risk"
        people.update(new_dict)

    return dictionary_people_list


def count_of_overweight_people(dictionary_people_list):
    dictionary_people = calculate_bmi(dictionary_people_list)
    print(dictionary_people)
    count = 0
    for people in dictionary_people:
        if 25 <= people["BMIIndex"] < 30:
            count = count + 1
    return count


print(count_of_overweight_people(dictionary_people_list))
