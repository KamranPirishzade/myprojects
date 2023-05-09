# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     pass

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
nato=pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict={row.letter:row.code for (index,row) in nato.iterrows()}
# print(nato_dict)

# try :
#     word=input("Enter a word:")
#     nato_list=[nato_dict[z.upper()] for z in word]
#     print(nato_list)
# except KeyError:
#     error=True
#     while error:
#         print("Sorry, only letters in alphabet please.")
#         try:
#             word = input("Enter a word:")
#             nato_list = [nato_dict[z.upper()] for z in word]
#             print(nato_list)
#         except:
#             pass
#         else:
#             error=False

def generate_phonetic():
    word = input("Enter a word:")
    try :
        nato_list=[nato_dict[z.upper()] for z in word]
        print(nato_list)
    except KeyError:
      print("Sorry, only letters in alphabet please.")
      generate_phonetic()


generate_phonetic()



