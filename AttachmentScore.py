def get_discomfort_score(score, idx):
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
        total += score.iat[idx, (items[i] + 4)] # column positions are offset by 4 due to demographic questions
        i += 1

    return total

def get_preoccupation_with_relationships_score(score, idx):
    total = 0
    i = 0
    items = [13, 17, 22, 23, 25]
    
    while i < len(items):
        total += score.iat[idx, (items[i] + 4)] # column positions are offset by 4 due to demographic questions
        i += 1

    return total  

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

def score_asq(values):
    discomfort_with_closeness = 0 # items 2, 3, 11, 12, 15, 16, 20, 27 (score range 9 - 54)
    relationships_as_secondary = 0 # items 4, 5, 6, 9 (score range 4 -24)
    preoccupation_with_relationships = 0 # items 13, 17, 22, 23, 25 (score range 5 - 30)
    need_for_approval = 0 # items 7, 8, 10, 19, 21 (score range 5 - 30)
    confidence_in_interpersonal_interactions = { # items 1, 14, 24, 26, 28,29 (score range 6 - 36)
        "subscore1": 0,
        "subscore2": 0
    }

    # main attachment scores
    avoidant_score = (discomfort_with_closeness + relationships_as_secondary) - confidence_in_interpersonal_interactions["subscore1"]
    anxious_score = (preoccupation_with_relationships + need_for_approval) - confidence_in_interpersonal_interactions["subscore2"]