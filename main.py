# Categorize New Member
def open_or_senior(data):
    new_list = []
    for i in data:
        if i[0] >= 55 and i[1] > 7:
            new_list.append("Senior")
        else:
            new_list.append("Open")
    return new_list