
file = "C:\\Users\\shaij\\Documents\\AoC_day_3\\input.txt"
sample = "C:\\Users\\shaij\\Documents\\AoC_day_3\\sample_input.txt"

def file_reader():
    with open(file) as f:
        data = f.readlines()
        # new line, bye bye bye
        data = [x.rstrip() for x in data]
    return data


def day_3():
    diag_report = file_reader()
    ones_column_count = {}
    zeros_column_count = {}
    
    columns = len(diag_report[0])
    for col in range(columns):
        ones_column_count[col] = 0

    for col in range(columns):
        zeros_column_count[col] = 0

    for i in range(len(diag_report)):
        for j in range(len(diag_report[i])):
            if int(diag_report[i][j]) == 1:
                ones_column_count[j] += int(diag_report[i][j])
            elif int(diag_report[i][j]) == 0:
                zeros_column_count[j] += 1

    gamma_rate = []
    for i in range(columns):
        if ones_column_count[i] > zeros_column_count[i]:
            gamma_rate.append("1")
        else:
            gamma_rate.append("0")
    gamma = "".join(gamma_rate)

    epsilon_rate = []
    for i in range(columns):
        if zeros_column_count[i] < ones_column_count[i]:
            epsilon_rate.append("0")
        else:
            epsilon_rate.append("1")

    epsilon_rate = "".join(epsilon_rate)

    print(gamma)
    print(epsilon_rate)
    print(int(gamma, 2) * int(epsilon_rate, 2))

def day_3_part_two():
    diag_report = file_reader(sample)
    # diag_report = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
    ones_column_count = {}
    zeros_column_count = {}
    oxy = 0
    c02 = 0

    columns = len(diag_report[0])
    for col in range(columns):
        ones_column_count[col] = 0

    for col in range(columns):
        zeros_column_count[col] = 0

    for i in range(len(diag_report)):
        for j in range(len(diag_report[i])):
            if int(diag_report[i][j]) == 1:
                ones_column_count[j] += 1 # one of the most common bit for all bits in that position
            elif int(diag_report[i][j]) == 0:
                zeros_column_count[j] += 1

    most_common_in_pos = {}
    least_common_in_pos = {}
    for i in range(columns):
        if ones_column_count[i] >= zeros_column_count[i]:
            most_common_in_pos[i] = 1
            least_common_in_pos[i] = 0
        else:
            most_common_in_pos[i] = 0
            least_common_in_pos[i] = 1

    # haven't seen if else inside list comprehension before, thought I would try it out
    most_common_arr = [1 if ones_column_count[i] >= zeros_column_count[i] else 0 for i in range(columns)]
    least_common_arr = [0 if ones_column_count[i] >= zeros_column_count[i] else 1 for i in range(columns)]

    print(most_common_in_pos)
    print(least_common_in_pos)
    print(most_common_arr)
    print(least_common_arr)
    print(diag_report[0])
    print(diag_report[0][0])

    nums_left = []
    for colIndex, val in enumerate(diag_report[0]):
        for row in diag_report:
            bit = int(row[colIndex])
            most_common_value = most_common_arr[colIndex]
            if bit == most_common_value:
                nums_left.append(row)
            # have the first bit working

if __name__ == '__main__':
    day_3() #4191876
    day_3_part_two()#WIP
