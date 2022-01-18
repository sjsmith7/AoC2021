sample = "C:\\Users\\shaij\\Documents\\AoC_day_4\\sample_input.txt"
file = "C:\\Users\\shaij\\Documents\\AoC_day_4\\input.txt"


def calculate_sum_of_unchecked(board):
    unmarked = []
    for i, row in enumerate(board):
        [unmarked.append(cell) for cell in row if cell != -1]
    return sum(unmarked)


def check_for_winner(boards):
    col = []
    #print("current boards", boards)
    current_board = None
    for i, board in enumerate(boards):
        for i2, row in enumerate(board):
            if len(set(row)) == 1: #check if the row has all of the same elements ( if all -1 than the set will only have 1 remaining element)
                return board

        for ind in range(len(board[0])):
            column = [row2[ind] for row2 in board]
            if len(set(column)) == 1:  # check if the colum has all of the same elements ( if all -1 than the set will only have 1 remaining element)
                return board


def day_4_part_1():
    nums_to_draw = []
    boards = []
    total_unmarked = 0
    num_that_was_called = None
    with open(file) as f:
        data = f.readlines()
        data = [x.strip() for x in data]
        nums = data[0]
        test = []

        nums_to_draw = [int(x) for x in nums.split(",")]

        for i, val in enumerate(data):
            if data[i] == '':
                board = data[i+1: i + 6]
                board_with_ints = []
                for ind, row in enumerate(board):
                    new_list = row.split(" ")
                    formatted_row = [int(x) for x in new_list if x != ""]
                    board_with_ints.append(formatted_row)

                boards.append(board_with_ints)

    # now have a list of all of the numbers to be drawn

    # now have a list of list of list (pls wake me up from this nightmare)
    # so boards[0] is a board, boards[0][0] is the first row in the board (board has 5 rows)
    # which means board[0][0][0] will contain the first value


    for num in nums_to_draw:
        for i, board in enumerate(boards):
            for ind, row in enumerate(board):
                for index, item in enumerate(row):
                    if item == num:
                        row[index] = -1 #marked
                        winning_board = check_for_winner(boards)
                        if winning_board:
                            total_unmarked = calculate_sum_of_unchecked(winning_board)
                            num_that_was_called = num
                            return total_unmarked * num_that_was_called

if __name__ == '__main__':
    print(day_4_part_1()) #51776
