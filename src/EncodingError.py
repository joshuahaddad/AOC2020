#Day 9 Encoding Error

def get_data():
    with open("../assets/XMASdata.txt", 'r') as f:
        return [int(line) for line in f.readlines()]

def find_error(xmas_data, preamble_length = 25):
    for i in range(preamble_length, len(xmas_data)):
        num = xmas_data[i]
        addends = set(xmas_data[i-preamble_length:i])
        valid = False

        for addend in addends:
            if not(num-addend in addends and num-addend != addend):
                continue
            else:
                valid = True
                break

        if not valid:
            return num

def get_weakness():
    xmas_data = get_data()
    error = find_error(xmas_data)

    for i in range(len(xmas_data)):
        addends = []
        for j in range(i, len(xmas_data)):
            addends.append(xmas_data[j])

            if sum(addends) == error:
                return min(addends) + max(addends)
            elif sum(addends) > error:
                break


print(find_error(get_data()))
print(get_weakness())