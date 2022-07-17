GRADE_PAIRS = {
    'A': 4,
    'B': 3,
    'C': 2,
    'D': 1,
    'F': 0
}

if __name__ == "__main__":

    # get grades list
    grades = input("Enter grades: ").strip().split(' ')

    # get pi_number
    pi_number = input("Enter PI number: ")

    # get first digit from the pi_number
    pi_digit = int(pi_number[1])

    if pi_digit == 0:
        grades.append('A')  # if the digit is 0
    elif pi_digit % 2 == 0:
        grades.append('B')  # if the digit is non-zero even number
    else:
        grades.append('C')  # digit is non-zero odd number

    grade_number = [GRADE_PAIRS[g] for g in grades if g in GRADE_PAIRS]

    print(grade_number)

