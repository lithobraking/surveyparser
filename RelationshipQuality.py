def get_relationship_quality_score(data, idx):
    total = 0
    i = 0
    items = list(range(30, 40))
    
    while i < len(items):
        total += data.iat[idx, (items[i] + 4)]
        i += 1

    return total

def get_satisfaction_score(data, idx):
    total = 0
    i = 0
    items = [30, 34, 37]
    
    while i < len(items):
        total += data.iat[idx, (items[i] + 4)]
        i += 1

    return total / len(items)

def get_intimacy_score(data, idx):
    total = 0
    i = 0
    items = [31, 35, 38]
    
    while i < len(items):
        total += data.iat[idx, (items[i] + 4)]
        i += 1

    return total / len(items)

def get_trust_score(data, idx):
    total = 0
    i = 0
    items = [32, 36, 39]
    
    while i < len(items):
        total += data.iat[idx, (items[i] + 4)]
        i += 1

    return total / len(items)

def get_love_score(data, idx):
    total = 0
    i = 0
    items = [33, 40]
    
    while i < len(items):
        total += data.iat[idx, (items[i] + 4)]
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