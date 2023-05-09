# import random
#
# names=["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]
#
# student_scores={student :random.randint(1,100) for student in names}
#
# passed_students={student:score for (student,score) in student_scores.items() if score>=60}
# print(student_scores)
# print(passed_students)


sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

words={word: len(word) for word in sentence.split() }
print(words)


weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f={day:(c*1.8+32) for (day,c) in weather_c.items()}
print(weather_f)