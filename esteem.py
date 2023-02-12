# 06 Team Activity: Troubleshooting Functions
'''
This program is an implementation of the Rosenberg
Self-Esteem Scale. This program will show you ten
statements that you could possibly apply to yourself.
Please rate how much you agree with each of the
statements by responding with one of these four letters:
'''

def main():

    # positive = one, two, four, six, seven
    # negative = three, five, eight, nine, ten
    score = 0

    print('''
    SELF ESTEEM TEST:
    Key:
    D means you strongly disagree with the statement.
    d means you disagree with the statement.
    a means you agree with the statement.
    A means you strongly agree with the statement.
    ''')

    print("1. I feel that I am a person of worth, at least on an equal plane with others.")
    one = input("Enter D, d, a, or A: ")

    print("2. I feel that I have a number of good qualities.")
    two = input("Enter D, d, a, or A: ")

    print("3. All in all, I am inclined to feel that I am a failure.")
    three = input("Enter D, d, a, or A: ")

    print("4. I am able to do things as well as most other people.")
    four = input("Enter D, d, a, or A: ")

    print("5. I feel I do not have much to be proud of.")
    five = input("Enter D, d, a, or A: ")

    print("6. I take a positive attitude toward myself.")
    six = input("Enter D, d, a, or A: ")

    print("7. On the whole, I am satisfied with myself.")
    seven = input("Enter D, d, a, or A: ")

    print("8. I wish I could have more respect for myself.")
    eight = input("Enter D, d, a, or A: ")

    print("9. I certainly feel useless at times.")
    nine = input("Enter D, d, a, or A: ")

    print("10. At times I think I am no good at all.")
    ten = input("Enter D, d, a, or A: ")



    print(f"\n Your score is {score}.")
    print("A score below 15 may indicate problematic low self-esteem.")



# positive = one, two, four, six, seven
def compute_positive_score(positive):
    score = 0
    if positive == "D":
        score += 0
    elif positive == "d":
        score += 1
    elif positive == "a":
        score += 2
    elif positive == "A":
        score += 3
    return score

# negative = three, five, eight, nine, ten
def compute_negative_score(negative):
    score = 0
    if negative == "D":
        score += 3
    elif negative == "d":
        score += 2
    elif negative == "a":
        score += 1
    elif negative == "A":
        score += 0
    return score

if __name__ == "__main__":
    main()
