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

def prepare_data(table):
    working_data = table.copy()
    filter_questions = {
        "consent": "I Do Not Agree", 
        "What is your age group?": "55 - 64", 
        "What is your current relationship status?": "Single"
        }
    
    for key, value in filter_questions.items():
        print(type(value))
        working_data = working_data[working_data[key].str.contains(value) == False]

    working_data = working_data.reset_index(drop=True)
    return working_data

responses = prepare_data(responses)
print("Removed irrelevant data. New table looks like this:")
print(responses)

