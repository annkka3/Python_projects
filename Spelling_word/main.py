import pandas as pd
#
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
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

data = pd.read_csv('nato_phonetic_alphabet.csv')
phoenetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

def generate():
    word = input("Please input your word: ").upper()
    try:
        list_for_word = [phoenetic_dict[letter] for letter in word]
    except KeyError:
        print('Sorry, only letters in the alphabet please')
        generate()
    else:
        print(list_for_word)

generate()