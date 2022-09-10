import pygame
import time
import sys

chess_board = [['  ' for i in range(8)] for i in range(8)]

class chess_peice:
    def __init__(self, team, type, image, dead=False):
        self.team = team
        self.type = type
        self.dead = dead
        self.image = image



bp = chess_peice('b', 'p', '1.png')
wp = chess_peice('w', 'p', '2.png')
bk = chess_peice('b', 'k', '3.png')
wk = chess_peice('w', 'k', '4.png')
br = chess_peice('b', 'r', '5.png')
wr = chess_peice('w', 'r', '6.png')
b = chess_peice('b', 'b', '7.png')
wb = chess_peice('w', 'b', '8.png')
bq = chess_peice('b', 'q', '9.png')
wq = chess_peice('w', 'q', '10.png')
bkn = chess_peice('b', 'kn', '11.png')
wkn = chess_peice('w', 'kn', '12.png')


starting_order = {(0, 6): pygame.image.load(wp.image), (1, 6): pygame.image.load(wp.image),
                  (2, 6): pygame.image.load(wp.image), (3, 6): pygame.image.load(wp.image),
                  (4, 6): pygame.image.load(wp.image), (5, 6): pygame.image.load(wp.image),
                  (6, 6): pygame.image.load(wp.image), (7, 6): pygame.image.load(wp.image),
                  (0, 7): pygame.image.load(wr.image), (1, 7): pygame.image.load(wkn.image),
                  (2, 7): pygame.image.load(wb.image), (3, 7): pygame.image.load(wk.image),
                  (4, 7): pygame.image.load(wq.image), (5, 7): pygame.image.load(wb.image),
                  (6, 7): pygame.image.load(wkn.image), (7, 7): pygame.image.load(wr.image),


                  (0, 0): pygame.image.load(br.image), (1, 0): pygame.image.load(bkn.image),
                  (2, 0): pygame.image.load(b.image), (3, 0): pygame.image.load(bk.image),
                  (4, 0): pygame.image.load(bq.image), (5, 0): pygame.image.load(b.image),
                  (6, 0): pygame.image.load(bkn.image), (7, 0): pygame.image.load(br.image),
                  (0, 1): pygame.image.load(bp.image), (1, 1): pygame.image.load(bp.image),
                  (2, 1): pygame.image.load(bp.image), (3, 1): pygame.image.load(bp.image),
                  (4, 1): pygame.image.load(bp.image), (5, 1): pygame.image.load(bp.image),
                  (6, 1): pygame.image.load(bp.image), (7, 1): pygame.image.load(bp.image),

                  (0, 2): None, (1, 2): None, (2, 2): None, (3, 2): None,
                  (4, 2): None, (5, 2): None, (6, 2): None, (7, 2): None,
                  (0, 3): None, (1, 3): None, (2, 3): None, (3, 3): None,
                  (4, 3): None, (5, 3): None, (6, 3): None, (7, 3): None,
                  (0, 4): None, (1, 4): None, (2, 4): None, (3, 4): None,
                  (4, 4): None, (5, 4): None, (6, 4): None, (7, 4): None,
                  (0, 5): None, (1, 5): None, (2, 5): None, (3, 5): None,
                  (4, 5): None, (5, 5): None, (6, 5): None, (7, 5): None,

                  }


def create_board(chess_board):
    chess_board[7] = [chess_peice('w', 'r', '6.png'), chess_peice('w', 'kn', '12.png'), chess_peice('w', 'b', '8.png'), \
               chess_peice('w', 'q', '10.png'), chess_peice('w', 'k', '4.png'), chess_peice('w', 'b', '8.png'), \
               chess_peice('w', 'kn', '12.png'), chess_peice('w', 'r', '6.png')]


    chess_board[0] = [chess_peice('b', 'r', '5.png'), chess_peice('b', 'kn', '11.png'), chess_peice('b', 'b', '7.png'), \
               chess_peice('b', 'q', '9.png'), chess_peice('b', 'k', '3.png'), chess_peice('b', 'b', '7.png'), \
               chess_peice('b', 'kn', '11.png'), chess_peice('b', 'r', '5.png')]

    

    for i in range(8):
        chess_board[6][i] = chess_peice('w', 'p', '2.png')
        chess_board[1][i] = chess_peice('b', 'p', '1.png')
        
    return chess_board







def convert_to_readable(chess_board):
    output = ''

    for i in chess_board:
        for j in i:
            try:
                output += j.team + j.type + ', '
            except:
                output += j + ', '
        output += '\n'
    return output

def on_board(place_position):
    if place_position[0] > -1 and place_position[1] > -1 and place_position[0] < 8 and place_position[1] < 8:
        return True

def deselect():
    for row in range(len(chess_board)):
        for column in range(len(chess_board[0])):
            if chess_board[row][column] == 'x ':
                chess_board[row][column] = '  '
            else:
                try:
                    chess_board[row][column].dead = False
                except:
                    pass
    return convert_to_readable(chess_board)



def highlight(chess_board):
    highlighted = []
    for i in range(len(chess_board)):
        for j in range(len(chess_board[0])):
            if chess_board[i][j] == 'x ':
                highlighted.append((i, j))
            else:
                try:
                    if chess_board[i][j].dead:
                        highlighted.append((i, j))
                except:
                    pass
    return highlighted

def check_team(mvs, inx):
    row, col = inx
    if mvs%2 == 0:
        if chess_board[row][col].team == 'w':
            return True
    else:
        if chess_board[row][col].team == 'b':
            return True


def select_moves(chess_peice, inx, mvs):
    if check_team(mvs, inx):
        if chess_peice.type == 'p':
            if chess_peice.team == 'b':
                return highlight(pawn_moves_b(inx))
            else:
                return highlight(pawn_w_moves(inx))

        if chess_peice.type == 'k':
            return highlight(king_moves_in_board(inx))

        if chess_peice.type == 'r':
            return highlight(rook_moves_in_board(inx))

        if chess_peice.type == 'b':
            return highlight(bishop_moves_in_board(inx))

        if chess_peice.type == 'q':
            return highlight(queen_moves_in_board(inx))

        if chess_peice.type == 'kn':
            return highlight(knight_moves(inx))



def pawn_moves_b(inx):
    if inx[0] == 1:
        if chess_board[inx[0] + 2][inx[1]] == '  ' and chess_board[inx[0] + 1][inx[1]] == '  ':
            chess_board[inx[0] + 2][inx[1]] = 'x '
    bottom3 = [[inx[0] + 1, inx[1] + i] for i in range(-1, 2)]

    for place_positions_in_board in bottom3:
        if on_board(place_positions_in_board):
            if bottom3.inx(place_positions_in_board) % 2 == 0:
                try:
                    if chess_board[place_positions_in_board[0]][place_positions_in_board[1]].team != 'b':
                        chess_board[place_positions_in_board[0]][place_positions_in_board[1]].dead = True
                except:
                    pass
            else:
                if chess_board[place_positions_in_board[0]][place_positions_in_board[1]] == '  ':
                    chess_board[place_positions_in_board[0]][place_positions_in_board[1]] = 'x '
    return chess_board

def pawn_w_moves(inx):
    if inx[0] == 6:
        if chess_board[inx[0] - 2][inx[1]] == '  ' and chess_board[inx[0] - 1][inx[1]] == '  ':
            chess_board[inx[0] - 2][inx[1]] = 'x '
    top3 = [[inx[0] - 1, inx[1] + i] for i in range(-1, 2)]

    for place_positions_in_board in top3:
        if on_board(place_positions_in_board):
            if top3.inx(place_positions_in_board) % 2 == 0:
                try:
                    if chess_board[place_positions_in_board[0]][place_positions_in_board[1]].team != 'w':
                        chess_board[place_positions_in_board[0]][place_positions_in_board[1]].dead = True
                except:
                    pass
            else:
                if chess_board[place_positions_in_board[0]][place_positions_in_board[1]] == '  ':
                    chess_board[place_positions_in_board[0]][place_positions_in_board[1]] = 'x '
    return chess_board



def king_moves_in_board(inx):
    for y in range(3):
        for x in range(3):
            if on_board((inx[0] - 1 + y, inx[1] - 1 + x)):
                if chess_board[inx[0] - 1 + y][inx[1] - 1 + x] == '  ':
                    chess_board[inx[0] - 1 + y][inx[1] - 1 + x] = 'x '
                else:
                    if chess_board[inx[0] - 1 + y][inx[1] - 1 + x].team != chess_board[inx[0]][inx[1]].team:
                        chess_board[inx[0] - 1 + y][inx[1] - 1 + x].dead = True
    return chess_board



def rook_moves_in_board(inx):
    cross = [[[inx[0] + i, inx[1]] for i in range(1, 8 - inx[0])],
             [[inx[0] - i, inx[1]] for i in range(1, inx[0] + 1)],
             [[inx[0], inx[1] + i] for i in range(1, 8 - inx[1])],
             [[inx[0], inx[1] - i] for i in range(1, inx[1] + 1)]]

    for direction in cross:
        for place_positions_in_board in direction:
            if on_board(place_positions_in_board):
                if chess_board[place_positions_in_board[0]][place_positions_in_board[1]] == '  ':
                    chess_board[place_positions_in_board[0]][place_positions_in_board[1]] = 'x '
                else:
                    if chess_board[place_positions_in_board[0]][place_positions_in_board[1]].team != chess_board[inx[0]][inx[1]].team:
                        chess_board[place_positions_in_board[0]][place_positions_in_board[1]].dead = True
                    break
    return chess_board



def bishop_moves_in_board(inx):
    diagonals = [[[inx[0] + i, inx[1] + i] for i in range(1, 8)],
                 [[inx[0] + i, inx[1] - i] for i in range(1, 8)],
                 [[inx[0] - i, inx[1] + i] for i in range(1, 8)],
                 [[inx[0] - i, inx[1] - i] for i in range(1, 8)]]

    for direction in diagonals:
        for place_positions_in_board in direction:
            if on_board(place_positions_in_board):
                if chess_board[place_positions_in_board[0]][place_positions_in_board[1]] == '  ':
                    chess_board[place_positions_in_board[0]][place_positions_in_board[1]] = 'x '
                else:
                    if chess_board[place_positions_in_board[0]][place_positions_in_board[1]].team != chess_board[inx[0]][inx[1]].team:
                        chess_board[place_positions_in_board[0]][place_positions_in_board[1]].dead = True
                    break
    return chess_board



def queen_moves_in_board(inx):
    chess_board = rook_moves_in_board(inx)
    chess_board = bishop_moves_in_board(inx)
    return chess_board



def knight_moves(inx):
    for i in range(-2, 3):
        for j in range(-2, 3):
            if i ** 2 + j ** 2 == 5:
                if on_board((inx[0] + i, inx[1] + j)):
                    if chess_board[inx[0] + i][inx[1] + j] == '  ':
                        chess_board[inx[0] + i][inx[1] + j] = 'x '
                    else:
                        if chess_board[inx[0] + i][inx[1] + j].team != chess_board[inx[0]][inx[1]].team:
                            chess_board[inx[0] + i][inx[1] + j].dead = True
    return chess_board


WIDTH = 800

WON = pygame.display.set_mode((WIDTH, WIDTH))



pygame.display.set_caption("Chess")
WHITE = (255, 255, 255)
GREEN = (128, 128, 128)
PINK = (204, 204, 0)
Grey = (50, 255, 255)
bLACK = (0, 0, 0)


class Node:
    def __init__(self, row, col, width):
        self.row = row
        self.col = col
        self.x = int(row * width)
        self.y = int(col * width)
        self.colour = WHITE
        self.occupied = None

    def draw(self, WON):
        pygame.draw.rect(WON, self.colour, (self.x, self.y, WIDTH / 8, WIDTH / 8))

    def setup(self, WON):
        if starting_order[(self.row, self.col)]:
            if starting_order[(self.row, self.col)] == None:
                pass
            else:
                WON.blit(starting_order[(self.row, self.col)], (self.x, self.y))

        


def make_grid(rows, width):
    grid = []
    gap = WIDTH // rows
    print(gap)
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(j, i, gap)
            grid[i].append(node)
            if (i+j)%2 ==1:
                grid[i][j].colour = GREEN
    return grid



def draw_grid(win, rows, width):
    gap = width // 8
    for i in range(rows):
        pygame.draw.line(win, bLACK, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, bLACK, (j * gap, 0), (j * gap, width))

    

def update_display(win, grid, rows, width):
    for row in grid:
        for spot in row:
            spot.draw(win)
            spot.setup(win)
    draw_grid(win, rows, width)
    pygame.display.update()


def Find_Node(pos, WIDTH):
    interval = WIDTH / 8
    y, x = pos
    rows = y // interval
    columns = x // interval
    return int(rows), int(columns)


def display_potential_moves(place_positions_in_board, grid):
    for i in place_positions_in_board:
        x, y = i
        grid[x][y].colour = Grey
        


def Do_Move(OriginalPos, Finalplace_position, WON):
    starting_order[Finalplace_position] = starting_order[OriginalPos]
    starting_order[OriginalPos] = None


def remove_highlight(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i+j)%2 == 0:
                grid[i][j].colour = WHITE
            else:
                grid[i][j].colour = GREEN
    return grid


create_board(chess_board)


def main(WON, WIDTH):
    mvs = 0
    selected = False
    chess_peice_to_move=[]
    grid = make_grid(8, WIDTH)
    while True:
        pygame.time.delay(50) ##stops cpu dying
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            

            if event.type == pygame.MOUSEbUTTONDOWN:
                pos = pygame.mouse.get_pos()
                y, x = Find_Node(pos, WIDTH)
                if selected == False:
                    try:
                        possible = select_moves((chess_board[x][y]), (x,y), mvs)
                        for place_positions_in_board in possible:
                            row, col = place_positions_in_board
                            grid[row][col].colour = Grey
                        chess_peice_to_move = x,y
                        selected = True
                    except:
                        chess_peice_to_move = []
                        print('Can\'t select')
                    

                else:
                    try:
                        if chess_board[x][y].dead == True:
                            row, col = chess_peice_to_move 
                            chess_board[x][y] = chess_board[row][col]
                            chess_board[row][col] = '  '
                            deselect()
                            remove_highlight(grid)
                            Do_Move((col, row), (y, x), WON)
                            mvs += 1
                            print(convert_to_readable(chess_board))
                        else:
                            deselect()
                            remove_highlight(grid)
                            selected = False
                            print("De-Selected")
                    except:
                        if chess_board[x][y] == 'x ':
                            row, col = chess_peice_to_move
                            chess_board[x][y] = chess_board[row][col]
                            chess_board[row][col] = '  '
                            deselect()
                            remove_highlight(grid)
                            Do_Move((col, row), (y, x), WON)
                            mvs += 1
                            print(convert_to_readable(chess_board))
                        else:
                            deselect()
                            remove_highlight(grid)
                            selected = False
                            print("in-valid move")
                    selected = False

            update_display(WON, grid, 8, WIDTH)


main(WON, WIDTH)
