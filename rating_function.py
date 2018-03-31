def scores_to_rating(score1,score2,score3,score4,score5):
    """
    Turns five scores into a rating by averaging the
    middle three of the five scores and assigning this average
    to a written rating.
    """
    #STEP 1 convert scores to numbers
    score1 = convert_to_numeric(score1)
    score2 = convert_to_numeric(score2)
    score3 = convert_to_numeric(score3)
    score4 = convert_to_numeric(score4)
    score5 = convert_to_numeric(score5)

    #STEP 2 and STEP 3 find the average of the middle three scores
    average_score = sum_of_middle_three(score1,score2,score3,score4,score5)/3

    #STEP 4 turn average score into a rating
    rating = score_to_rating_string(average_score)

    return rating

def convert_to_numeric(score):
    """Converts the entered input to float type"""
    return float(score)

def sum_of_middle_three(score1,score2,score3,score4,score5):
    """Finds the sum of the middle three elements out of the entered 5 inputs"""
    l=[score1,score2,score3,score4,score5]
    return sum(l) - max(l) -min(l)

def score_to_rating_string(score):
    """Converts the score to a rating string"""
    if score<1:
        return "Terrible"
    elif score<2:
        return "Bad"
    elif score<3:
        return "OK"
    elif score<4:
        return "Good"
    elif score<=5:
        return "Excellent"