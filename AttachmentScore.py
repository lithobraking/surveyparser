# # # SUBSCORE HELPER FUNCTIONS # # #

# discomfort with closeness: items 2, 3, 11, 12, 15, 16, 20, 27 (score range 9 - 54)
# relationships as secondary: items 4, 5, 6, 9 (score range 4 -24)
# preoccupation with relationships: items 13, 17, 22, 23, 25 (score range 5 - 30)
# need for approval: items 7, 8, 10, 19, 21 (score range 5 - 30)
# confidence in interpersonal interactions: items 1, 14, 24, 26, 28,29 (score range 6 - 36)

def get_discomfort_score(score, idx): # idx corresponds to the row
    total = 0
    i = 0
    items = [2, 3, 11, 12, 15, 16, 20, 27]
    
    while i < len(items):
        total += score.iat[idx, (items[i] + 4)] # column positions are offset by 4 due to demographic questions
        i += 1

    return total  

def get_relationships_as_secondary_score(score, idx):
    total = 0
    i = 0
    items = [4, 5, 6, 9]
    
    while i < len(items):
        total += score.iat[idx, (items[i] + 4)]
        i += 1

    return total

def get_preoccupation_with_relationships_score(score, idx):
    total = 0
    i = 0
    items = [13, 17, 22, 23, 25]
    
    while i < len(items):
        total += score.iat[idx, (items[i] + 4)]
        i += 1

    return total  

def get_need_for_approval_score(score, idx):
    total = 0
    i = 0
    items = [7, 8, 10, 19, 21]
    
    while i < len(items):
        total += score.iat[idx, (items[i] + 4)]
        i += 1

    return total 

def get_confidence_score_one(score, idx):
    total = 0
    i = 0
    items = [1, 14, 28]
    
    while i < len(items):
        total += score.iat[idx, (items[i] + 4)]
        i += 1

    return total 

def get_confidence_score_two(score, idx):
    total = 0
    i = 0
    items = [24, 26, 29]
    
    while i < len(items):
        total += score.iat[idx, (items[i] + 4)]
        i += 1

    return total 

# # # MAIN SCORE HELPER FUNCTIONS # # #

def get_avoidant_score(values, idx):
    discomfort_with_closeness = get_discomfort_score(values, idx)
    relationships_as_secondary = get_relationships_as_secondary_score(values, idx)
    confidence_in_interpersonal_interactions = get_confidence_score_one(values, idx)
    return (discomfort_with_closeness + relationships_as_secondary) - confidence_in_interpersonal_interactions

def get_anxious_score(values, idx):
    preoccupation_with_relationships = get_preoccupation_with_relationships_score(values, idx)
    need_for_approval = get_need_for_approval_score(values, idx)
    confidence_in_interpersonal_interactions = get_confidence_score_two(values, idx)
    return (preoccupation_with_relationships + need_for_approval) - confidence_in_interpersonal_interactions

def get_avoidant_rating(score):
    descriptor = "blank"

    if (score <= 20):
        descriptor = "LOW"
    elif (score > 20 and score < 36):
        descriptor = "AVG"
    elif (score >= 36):
        descriptor = "HIGH"

    return descriptor

def get_anxious_rating(score):
    descriptor = "blank"

    if (score <= 14):
        descriptor = "LOW"
    elif (score >= 15 and score <= 27):
        descriptor = "AVG"
    elif (score >= 28):
        descriptor = "HIGH"

    return descriptor

# # # ATTACHMENT STYLE FUNCTION # # # 

def get_attachment_style(avoidant_rating, anxious_rating):
    attachment_style = "blank"
    if (avoidant_rating == "HIGH" ):
        if (anxious_rating == "HIGH"):
            attachment_style = "DISORGANISED"
        else:
            attachment_style = "AVOIDANT"
    elif (avoidant_rating == "AVG"):
        if (anxious_rating == "HIGH"):
            attachment_style = "ANXIOUS"
        else:
            attachment_style = "SECURE"
    elif (avoidant_rating == "LOW"):
        if (anxious_rating == "HIGH"):
            attachment_style = "ANXIOUS"
        else:
            attachment_style = "SECURE"
    
    return attachment_style

# # # DATA PREP FUNCTIONS # # #

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



