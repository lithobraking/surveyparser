import pandas as pd
import tkinter as tk
from tkinter.filedialog import askopenfilename

tk.Tk().withdraw()

print("Please select a .csv file")
# TODO: add file type enforcement
fn = askopenfilename() 

# prepare data for use
responses = pd.read_csv(fn)
responses = responses.drop('Timestamp', axis=1)

print("Ingested response data. This is the current table:")
print(responses)

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

