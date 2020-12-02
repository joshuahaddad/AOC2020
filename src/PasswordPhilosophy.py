def parse_password(password):
    """
    Passwords are of the format (int1)-(int2) (char): (string)
    This function separates the criteria (int1, int2, char) from the password (string) and returns both
    """
    password = password.split(": ")
    criteria = password[0].split()
    criteria = [criteria[1], int(criteria[0].split("-")[0]), int(criteria[0].split("-")[1])]
    password = password[1]

    return criteria, password


def password_check(filepath) -> str:
    count_pt1 = 0
    count_pt2 = 0

    with open(filepath, 'r') as f:
        passwords = f.readlines()
        f.close()

    for password in passwords:
        criteria, password = parse_password(password)

        #Part 1, check if the occurrences of the letter criteria are > min and < max
        num_letter = password.count(criteria[0])
        if criteria[1] <= num_letter <= criteria[2]:
            count_pt1 += 1

        #Part2, check if the letter criteria occurs in either int1 position or int2 position, adjust for 0 indexing
        if (password[criteria[1]-1] == criteria[0]) ^ (password[criteria[2]-1] == criteria[0]):
            count_pt2 += 1

    return f'Part One: {count_pt1} \nPart Two: {count_pt2}'


if __name__ == '__main__':
    print(password_check("../assets/passwords.txt"))
