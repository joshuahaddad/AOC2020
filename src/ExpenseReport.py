# Day one challenges

# Simple solution
def simple_solution(expenses, answer):
    for num1 in expenses:
        for num2 in expenses:
            if num1 == num2:
                continue

            if num1 + num2 == 2020:
                answer = f'Num1: {num1} \nNum2: {num2} \nAnswer: {num1 * num2}'
    return answer


# Slightly Faster solution
def fast_solution(expenses, answer):
    length = len(expenses)
    answer_found = False
    for i in range(length):
        if (answer_found): break

        for j in range(length - 1, i + 1, -1):
            if expenses[i] + expenses[j] > 2020:
                length -= 1
                continue
            if expenses[i] + expenses[j] < 2020:
                break
            if expenses[i] + expenses[j] == 2020:
                answer = f'Num1: {expenses[i]} \nNum2: {expenses[j]} \nAnswer: {expenses[i] * expenses[j]}'
                answer_found = True
                break
    return answer


# This is the best solution I could think of after speaking with a friend about sets having O(1) lookup time.
# This solution should have O(n) complexity for part 1 and O(n^2) for part 2 instead of O(n^2) and O(n^3)
def fastest_solution(expense_set, answer):
    for num1 in expense_set:
        if 2020 - num1 in expense_set:
            answer = f'Num1: {num1} \nNum2: {2020 - num1} \nAnswer: {(2020 - num1) * num1}'

    return answer


def part2(expense_set, answer):
    for num1 in expense_set:
        for num2 in expense_set:
            if 2020 - num1 - num2 in expense_set:
                answer = f'Num1: {num1} \nNum2: {num2} \nNum3: {2020 - num1 - num2} \nAnswer: {(2020 - num1 - num2) * num1 * num2}'
    return answer


if __name__ == '__main__':

    Expenses = []
    Answer = "No Answer Found"
    filepath = "../assets/chal1expense.txt"

    with open(filepath, 'r') as f:
        for line in f:
            Expenses.append(int(line))
        Expenses.sort()
        f.close()

    with open(filepath, 'r') as f:
        Expense_Set: set = {int(line) for line in f.readlines()}
        f.close()

    print("Simple Solution:\n", simple_solution(Expenses, Answer), "\n")
    print("Faster Solution:\n", fast_solution(Expenses, Answer), "\n")
    print("Fastest Solution:\n", fastest_solution(Expense_Set, Answer), "\n")
    print("Part2 Solution:\n", part2(Expense_Set, Answer), "\n")
