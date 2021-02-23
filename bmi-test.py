from unittest import TestCase
from bmi import calculate_bmi

dictionary_people_list_height = [{'Gender': 'Male', 'HeightCm': -171, 'WeightKg': 40},
                                 {'Gender': 'Male', 'HeightCm': 161, 'WeightKg': 30},
                                 {'Gender': 'Male', 'HeightCm': 180, 'WeightKg': 22},
                                 {'Gender': 'Female', 'HeightCm': 166, 'WeightKg': 22},
                                 {'Gender': 'Female', 'HeightCm': 150, 'WeightKg': 40},
                                 {'Gender': 'Female', 'HeightCm': 167, 'WeightKg': 33}
                                 ]
dictionary_people_list_weight = [{'Gender': 'Male', 'HeightCm': 171, 'WeightKg': 40},
                                 {'Gender': 'Male', 'HeightCm': 161, 'WeightKg': -30},
                                 {'Gender': 'Male', 'HeightCm': 180, 'WeightKg': 22},
                                 {'Gender': 'Female', 'HeightCm': 166, 'WeightKg': 22},
                                 {'Gender': 'Female', 'HeightCm': 150, 'WeightKg': 40},
                                 {'Gender': 'Female', 'HeightCm': 167, 'WeightKg': 33}
                                 ]
dictionary_people_list_heaviest_weight = [{'Gender': 'Male', 'HeightCm': 171, 'WeightKg': 40},
                                          {'Gender': 'Male', 'HeightCm': 161, 'WeightKg': 444},
                                          {'Gender': 'Male', 'HeightCm': 180, 'WeightKg': 22},
                                          {'Gender': 'Female', 'HeightCm': 166, 'WeightKg': 22},
                                          {'Gender': 'Female', 'HeightCm': 150, 'WeightKg': 40},
                                          {'Gender': 'Female', 'HeightCm': 167, 'WeightKg': 33}
                                          ]

dictionary_people_list_tallest = [{'Gender': 'Male', 'HeightCm': 274, 'WeightKg': 40},
                                  {'Gender': 'Male', 'HeightCm': 161, 'WeightKg': 44},
                                  {'Gender': 'Male', 'HeightCm': 180, 'WeightKg': 22},
                                  {'Gender': 'Female', 'HeightCm': 166, 'WeightKg': 22},
                                  {'Gender': 'Female', 'HeightCm': 150, 'WeightKg': 40},
                                  {'Gender': 'Female', 'HeightCm': 167, 'WeightKg': 33}
                                  ]


class TestOverWeight(TestCase):
    def test_for_less_than_zero_height(self):
        actual = calculate_bmi(dictionary_people_list=dictionary_people_list_height)
        expected = "Please enter a valid height"
        self.assertEqual(actual, expected, "Failed for validation for height")

    def test_for_less_than_zero_weight(self):
        actual = calculate_bmi(dictionary_people_list=dictionary_people_list_weight)
        expected = "Please enter a valid weight"
        self.assertEqual(actual, expected, "Failed for validation for weight")

    def test_for_less_than_heaviest_weight(self):
        actual = calculate_bmi(dictionary_people_list=dictionary_people_list_heaviest_weight)
        expected = "Please enter a valid weight"
        self.assertEqual(actual, expected, "Failed for validation for weight")

    def test_for_the_tallest(self):
        actual = calculate_bmi(dictionary_people_list=dictionary_people_list_tallest)
        expected = "Please enter a valid height"
        self.assertEqual(actual, expected, "Failed for validation for height")
