

grid = [
    {i : ' ' for i in range(3)},
    {i : ' ' for i in range(3)},
    {i : ' ' for i in range(3)},
]

n_choice = 0
choice = {0 : 'X', 1 : 'O'}


def reset_board():
    global grid

    grid = [
        {i : ' ' for i in range(3)},
        {i : ' ' for i in range(3)},
        {i : ' ' for i in range(3)},
    ]

def show():
    for item in grid:
        line = ''
        for key, value in item.items():
            line += f"| {value} "
        line += '|'
        print(line)
        print('- - - - - - -')

def check_winner() -> bool:
    
    cross_1 = grid[0][0] + grid[1][1] + grid[2][2]
    cross_2 = grid[0][2] + grid[1][1] + grid[2][0]    

    if check(cross_1):
        return True
    
    if check(cross_2):
        return True
    
    for i in range(len(grid)):
        line_x = ''
        line_y = ''
        for j in range(len(grid[i])):
            line_x += grid[i][j]
            line_y += grid[j][i]
        
        if check(line_x): 
            return True
        
        if check(line_y):
            return True

    return False

def check(chars)->bool:
    if (chars == 'XXX' or chars == 'OOO'):
        print(f"Winner is {chars[0]}")
        return True
    else:
        return False
    
def check_draw():
    for item in grid:
        for key, value in item.items():
            if value == ' ':
                return False
    
    return True

def get_user_input():
    global n_choice
    while True:
        print(f'Player: {choice[n_choice]}')
        row = int(input('Pick a row: '))
        col = int(input('Pick a col: '))

        if grid[row][col] == 'X' or grid[row][col] == 'O':
            print(grid[row][col])
            print(f"{row} : {col}")
            print("That point is already selected")
        else:
            grid[row][col] = choice[n_choice]
            if n_choice == 0:
                n_choice = 1
            else:
                n_choice = 0
            break

          
print("Text Based Tic-Toc-Toe")
show()
while True:
    get_user_input()
    show()

    if check_winner():
        break
    
    if check_draw():
        reset_board()


