'''
def lbs_to_kg(weight):
    return weight * 0.45

def kg_to_lbs(weight):
    return weight / 0.45
'''

#Task12_extended

def find_max(list):
    max = list[0]
    for number in list:
        if number> max:
            max = number

    return max