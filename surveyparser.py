import pandas as pd
import tkinter as tk
from tkinter.filedialog import askopenfilename

tk.Tk().withdraw()

print("Please select a .csv file")
print('\n')
print('\n')
# TODO: add file type enforcement
# fn = askopenfilename() 
fn = "./testresponse.csv"

# prepare data for use
responses = pd.read_csv(fn)
responses = responses.drop('Timestamp', axis=1)

print("Ingested response data. This is the current table:")
print(responses)
print('\n')
print('\n')

print("Filtering irrelevant data form table...")
def prepare_data(table):
    working_data = table.copy()
    filter_questions = {
        "consent": "I Do Not Agree", 
        "What is your age group?": ["35 - 44", "55 - 64", "65 or older"], 
        "What is your current relationship status?": "Single"
        }
    
    for key, value in filter_questions.items():
        if (isinstance(value, str)):
            working_data = working_data[working_data[key].str.contains(value) == False]
        if (isinstance(value, list)):
            i = 0
            while i < len(value):
                if (value[i] in value):
                    working_data = working_data[working_data[key].str.contains(value[i]) == False]
                i += 1

    working_data = working_data.reset_index(drop=True)
    return working_data

responses = prepare_data(responses)
print("Done! New table looks like this:")
print(responses)
print('\n')
print('\n')

def invert_asq_values(data):
    working_data = data.copy()
    inverted_values_map = {
        1.0: 6.0,
        2.0: 5.0,
        3.0: 4.0,
        4.0: 3.0,
        5.0: 2.0,
        6.0: 1.0
    }

    idx = 0
    while idx < len(working_data):
        first_question_value = working_data.iat[idx, 18]
        working_data.iat[idx, 18] = inverted_values_map[first_question_value]

        second_question_value = working_data.iat[idx, 19]
        working_data.iat[idx, 19] = inverted_values_map[second_question_value]

        third_question_value = working_data.iat[idx, 29]
        working_data.iat[idx, 29] = inverted_values_map[third_question_value]

        idx += 1

    return working_data

responses = invert_asq_values(responses)

print("table with corrected values is as follows:")
print(responses)
