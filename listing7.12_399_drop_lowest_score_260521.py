def main():
    scores = get_scores()
    print('Scores from the exams are:',scores)
    sum = sum_s(scores)
    print('Sum of all scores is:', sum)
    lowest = min(scores)
    print('The lowest score is:',lowest)
    sum2 = sum - lowest
    average = sum2 / (len(scores) -1)
    print('After rejecting the lowest result, the average of the results is:',average)

def get_scores():
    another = 't'
    scores = []
    while another == 't':
        score = float(input('Enter the result from the exam:'))
        scores.append(score)
        another = input(rturn scores

def sum_s(vals):
    total = 0.0
    for num in vals:
        total += num
    return total

main()