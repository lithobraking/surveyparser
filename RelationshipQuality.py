def get_relationship_quality_score(data, idx):
    total = 0
    i = 0
    items = list(range(30, 40))
    
    while i < len(items):
        total += data.iat[idx, (items[i] + 4)]
        total += data.iat[idx, (items[i] + 3)]
        i += 1

    return total - get_love_score

def get_satisfaction_score(data, idx):
    total = 0
    i = 0
    items = [30, 34, 37]
    
    while i < len(items):
        total += data.iat[idx, (items[i] + 4)]
        total += data.iat[idx, (items[i] + 3)]
        i += 1

    return total / len(items)

def get_intimacy_score(data, idx):
    total = 0
    i = 0
    items = [31, 35, 38]
    
    while i < len(items):
        total += data.iat[idx, (items[i] + 4)]
        total += data.iat[idx, (items[i] + 3)]
        i += 1

    return total / len(items)

def get_trust_score(data, idx):
    total = 0
    i = 0
    items = [32, 36, 39]
    
    while i < len(items):
        total += data.iat[idx, (items[i] + 4)]
        total += data.iat[idx, (items[i] + 3)]
        i += 1

    return total / len(items)

def get_love_score(data, idx):
    # i messed up my survey design so this data is rendered kind of 
    # useless because it's missing one datapoint and i can't make any
    # meaningful calculations with it, so now this function just serves
    # to help remove this data from the score total :(
    total = 0
    i = 0
    items = [33, 40]
    
    while i < len(items):
        total += data.iat[idx, (items[i] + 4)]
        total += data.iat[idx, (items[i] + 3)]
        i += 1

    return total

def evaluate_subscore(subscore):
    result = "blank"
    if (subscore < 3):
        result = "LOW"
    elif (subscore >= 3 and subscore <= 5):
        result = "MODERATE"
    else:
        result = "HIGH"
    
    return result

def get_overall_satisfaction():
    result = "blank"
    relationship_quality = get_relationship_quality_score
    if (relationship_quality >= 3 and relationship_quality < 10):
        result = "LOW"
    elif (relationship_quality >=10 and relationship_quality <= 17):
        result = "MODERATE"
    elif (relationship_quality >= 17 and relationship_quality <= 24):
        result = "HIGH"
    
    return result
