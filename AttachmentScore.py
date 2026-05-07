def get_discomfort_score(score, idx):
    total = 0
    i = 0
    items = [2, 3, 11, 12, 15, 16, 20, 27]
    
    while i < len(items):
        total += score.iat[idx, (items[i] + 4)] # column positions are offset by 4 due to demographic questions
        i += 1

    return total
