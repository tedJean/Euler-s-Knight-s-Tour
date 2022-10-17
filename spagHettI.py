"""This code for the Knight's Tour problem contains no classes or modules. Just codes."""
import csv
file_name = "board.csv"

def main():
    count = 1
    end, space, possibility, endThisLoop = False, True, False, False
    board = [[0 for j in range(8)] for i in range(8)] # setting up 8 x 8 arrays
    print("*" * 4, "The board", "*" * 4) # populates board with zeros
    for r in board:
        for c in r:
            print(f'0{c}  ', end='')
        print('')

    # first move
    row = int(input("Enter the row (e.g., 1 - 8) of where to start the knight: ")) - 1
    column = int(input("Enter the column: ")) - 1

    # check that inputs are in range, i.e., space
    if (row < 0) or (row > 7) or (column < 0) or (column > 7):
        space = False
    while space == False:
        row = int(input("Enter an integer between 1 & 8 for the row: ")) - 1
        column = int(input("Enter an integer between 1 & 8 for the column: ")) - 1
        if (row >= 0) and (row < 8) and (column >= 0) and (column < 8):
            space = True

    board[row][column] = count
    print("*" * 8, "Updated board", "*" * 8)
    # print current version of board
    for r in board:
        for c in r:
            print(f'0{c}  ', end='')
        print("")
    count = 2

    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(board)

    # second move and beyond
    while (count != 64) or (end != True):
        possibility = False
        newCol =int(input("How many spaces to the left (e.g., -1 or -2) or the right (e.g., 1 or 2): "))
        # make sure the appropriate number of moves is made
        while (newCol != -2 and newCol != -1 and newCol != 1 and newCol != 2):
            newCol = int(input("Enter either a -2, -1, 1, or 2: "))
            # check
            #if newCol == -2 or newCol == -1 or newCol == 1 or newCol == 2:
            #    print('this should have worked.')

        # determine if input is a possible move, otherwise repeat possibility board and command
        newRow = int(input("How many spaces up or down (remember, if you entered a \"2\", then you can only enter "
              + "a \"1\" and vice versa: "))
        while (newRow != -1) and (newRow != -2) and (newRow != 2) and (newRow != 1): # check for appropriate value
            newRow = int(input("Enter how many spaces up or down (remember, if you entered a \"2\", then you can only enter" + "a \"1\" and vice versa: "))
        if (newCol == -1) or (newCol == 1):
            while ((newRow != -2) and (newRow != 2)):
                newRow = int(input("Enter how many spaces up or down (remember, if you entered a \"2\", then you can only enter"
                      + "a \"1\" and vice versa: "))
        if ((newCol == -2) or (newCol == 2)):
            while ((newRow != -1) and (newRow != 1)):
                newRow = int(input("Enter how many spaces up or down (remember, if you entered a \"2\", then you can only enter"
                        + "a \"1\" and vice versa: "))

        # check to make sure that the move is possible & the space is empty
        while (possibility == False):
            print("You have entered the possibility check.")
            if (row + newRow >= 0) and (row + newRow < 8) and (column + newCol >= 0) and (column + newCol < 8) \
                    and (board[row + newRow][column + newCol] == 0):
                possibility = True
                print("This is a possible move.")
                board[row + newRow][column + newCol] = count
                count += 1
                for r in board:
                    for c in r:
                        if count < 10:
                            print(f'0{c}  ', end='')
                        else:
                            print(f'{c}  ', end='')
                    print('')
                row += newRow
                column += newCol
            else:
                print("This move is not possible. Please find a new space and enter the moves to navigate to it.")
                newCol = int(input("Enter how many spaces to the left (e.g., -1 or -2) or the right (e.g., 1 or 2): "))
                while ((newCol != -2) and (newCol != -1) and (newCol != 1) and (newCol != 2)):
                    # make sure the appropriate number of moves is made
                    newCol = int(input("Enter either a -2, -1, 1, or 2: "))

                newRow = int(input("Enter how many spaces up or down (remember, if you entered a \"2\", then you can only enter "
                              + "a \"1\" and vice versa: "))
                while ((newRow != -1) and (newRow != -2) and (newRow != 2) and (newRow != 1)): # check to determine that appropriate value is entered.
                    newRow = int(input("Enter how many spaces up or down (remember, if you entered a \"2\", then you can only"
                              + " enter" + "a \"1\" and vice versa: "))

                if ((newCol == -1) or (newCol == 1)):
                    while ((newRow != -2) and (newRow != 2)):
                        newRow = int(input("Enter how many spaces up or down (remember, if you entered a \"2\", then you can only"
                                  + " enter" + "a \"1\" and vice versa: "))
                if ((newCol == -2) or (newCol == 2)):
                    while ((newRow != -1) and (newRow != 1)):
                        newRow = int(input("Enter how many spaces up or down (remember, if you entered a \"2\", then you can only"
                                      + " enter" + "a \"1\" and vice versa: "))
                for r in board:
                    for c in r:
                        if count < 10:
                            print(f'0{c}  ', end='')
                        else:
                            print(f'{c}  ', end='')
                    print('')
                print("")
                # loop to determine if there are any more possible moves
                endThisLoop = False

        # this needs the ability to discern whether a move is possible or not
        possible = 0
        row_indices = [-1, -1, 1, 1, 2, 2, -2, -2]
        col_indices = [-2, 2, -2, 2, -1, 1, -1, 1]
        for i in range(8):
            possibleRow = row + row_indices[i]
            possibleCol = column + col_indices[i]
            if (possibleRow >= 0) and (possibleRow < 8) and (possibleCol >= 0) and (possibleCol < 8)\
                    and board[possibleRow][possibleCol] == 0:
                possible += 1
                print(f'Row {possibleRow + 1}; column {possibleCol + 1} is a potential move')
        if count < 64 and possible > 0:
            print(f'You are currently located at row => {row + 1}; column => {column + 1}\n')
            end = False
            print(f'There are {possible} possible moves.')
        else:
            end = True
            print(f'There are no more possible moves. The count = {count}')


if __name__ == "__main__":
    main()
