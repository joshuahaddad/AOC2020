#Day 6 Custom Customs

def get_answers():
    with open("../assets/answers.txt", 'r') as f:
        lines = [b[:-1] for b in f.readlines()]
        f.close()

    group_answers = ""
    individual_answers = []
    group_unison = set()
    sum_pt1 = 0
    sum_pt2 = 0

    for line in lines:

        if line == "":
            sum_pt1 += len(set(group_answers))

            group_unison = individual_answers[0]
            for A in individual_answers:
                group_unison &= A

            sum_pt2 += len(group_unison)

            group_answers = ""
            individual_answers = []
            group_unison = set()
            continue

        group_answers += line
        individual_answers.append(set(line))

    group_unison = individual_answers[0]
    for A in individual_answers:
        group_unison &= A

    sum_pt1 += len(set(group_answers))
    sum_pt2 += len(group_unison)

    return sum_pt1, sum_pt2

print(get_answers())