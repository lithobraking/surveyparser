import pandas as pd
import tkinter as tk
from tkinter.filedialog import askopenfilename
import AttachmentScore as asq
import RelationshipQuality as rq

tk.Tk().withdraw()

print("Please select a .csv file")
print('\n')
print('\n')
# TODO: add file type enforcement
fn = askopenfilename() 

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
        # removes responses with disqualifying data
        if (isinstance(value, str)):
            working_data = working_data[working_data[key].str.contains(value) == False]
        # handles age group filtering
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

responses = asq.invert_asq_values(responses)

print("table with corrected values is as follows:")
print(responses)
print('\n')
print('\n')

def score_responses(data):
    working_data = data.copy()
    output_data = {
        "avoidant score": [],
        "avoidant rating": [],
        "anxious score": [],
        "anxious rating": [],
        "attachment style": [],
        "relationship score": [],
        "relationship quality": [],
        "satisfaction score": [],
        "satisfaction rating": [],
        "intimacy score": [],
        "intimacy rating": [],
        "trust score": [],
        "trust rating": []
    }
    
    idx = 0
    # yes yes yes i know that iterating over dataframes is bad practice this is just for the sake of completing the assignment
    while (idx < len(working_data.index)):
        print("ASQ-SF scores for index ", idx) 
        avoidant_score = asq.get_avoidant_score(working_data, idx)
        avoidant_rating = asq.get_avoidant_rating(avoidant_score)
        output_data["avoidant score"].append(avoidant_score)
        output_data["avoidant rating"].append(avoidant_rating)

        anxious_score = asq.get_anxious_score(working_data, idx)
        anxious_rating = asq.get_anxious_rating(anxious_score)
        output_data["anxious score"].append(anxious_score)
        output_data["anxious rating"].append(anxious_rating)

        attachment_style = asq.get_attachment_style(avoidant_rating, anxious_rating)
        output_data["attachment style"].append(attachment_style)

        adjustment = rq.get_love_score(data, idx)
        relationship_score = rq.get_relationship_quality_score(working_data, idx, adjustment)
        output_data["relationship score"].append(relationship_score)
        output_data["relationship quality"].append(rq.get_overall_satisfaction(relationship_score))

        satisfaction_score = rq.get_satisfaction_score(working_data, idx)
        output_data["satisfaction score"].append(satisfaction_score)
        output_data["satisfaction rating"].append(rq.evaluate_subscore(satisfaction_score))

        intimacy_score = rq.get_intimacy_score(working_data, idx)
        output_data["intimacy score"].append(intimacy_score)
        output_data["intimacy rating"].append(rq.evaluate_subscore(intimacy_score))

        trust_score = rq.get_trust_score(working_data, idx)
        output_data["trust score"].append(trust_score)
        output_data["trust rating"].append(rq.evaluate_subscore(trust_score))

        idx += 1

    final_scores = pd.DataFrame(output_data)
    return final_scores

processed_data = score_responses(responses)
print(processed_data)
