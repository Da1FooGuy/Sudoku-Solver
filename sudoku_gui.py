import pygame
import sudoku_solver
pygame.font.init()

WIDTH, HEIGHT = 800, 900
OFFSET = 100
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Solver")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

BACKGROUND = pygame.Rect(0, 0, WIDTH, HEIGHT-OFFSET)
HUD = pygame.Rect(0, HEIGHT-OFFSET, WIDTH, HEIGHT-OFFSET)
SELECTED = pygame.Rect(0, 0, WIDTH//9 - 5, (HEIGHT-OFFSET)//9 -5)
CELLS = []
BOARD = [
    [0,0,3,0,0,0,0,0,6],
    [0,0,0,9,8,0,0,2,0],
    [9,4,2,6,0,0,7,0,0],
    [4,5,0,0,0,6,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [1,0,9,0,5,0,4,7,0],
    [0,0,0,0,2,5,0,4,0],
    [6,0,0,0,7,8,5,0,0],
    [0,0,0,0,0,0,0,0,0]
]
BOARD_OLD = [x[:] for x in BOARD]
BOARD_SOLVED = [x[:] for x in BOARD]
sudoku_solver.idliketosolvethepuzzle(BOARD_SOLVED)



def fill_board(board):
    filled = []
    font = pygame.font.SysFont('rage', 100)
    index = 0
    for row in board:
        for cell in row:
            if cell > 0:
                filled.append((font.render(str(cell), True, BLACK), index))
            index += 1
    return filled



def draw_window(strikes, txt_input="", clicked_cell=None, clicked_idx=-1):
    pygame.draw.rect(WIN, BLACK, BACKGROUND)
    pygame.draw.rect(WIN, WHITE, HUD)
    filled = fill_board(BOARD)
    gap = WIDTH//9
    fnt = pygame.font.SysFont('comicsans', 40)


    for cell in CELLS:
        pygame.draw.rect(WIN, WHITE, cell)
    for i in range(3, 8, 3):
        pygame.draw.line(WIN, BLACK, (0, i*gap), (WIDTH, i*gap), 4)
        pygame.draw.line(WIN, BLACK, (i*gap, 0), (i*gap, HEIGHT-OFFSET-1), 4)
    if clicked_cell is not None:
        SELECTED.x = clicked_cell.x +1
        SELECTED.y = clicked_cell.y +1
        pygame.draw.rect(WIN, RED, SELECTED, 3)
        if [item for item in filled if item[1] == clicked_idx] == []:
            font = pygame.font.SysFont('impact', 32)
            txt_surface = font.render(txt_input, True, BLACK)
            WIN.blit(txt_surface, (clicked_cell.x+4, clicked_cell.y+1))

    controls = fnt.render("Click and type a number to fill in puzzle", True, BLACK)
    controls2 = fnt.render("Strikes left:" + str(10-strikes), True, BLACK)
    controls3 = fnt.render("Press SPACE to solve puzzle instantly", True, BLACK)
    xs = fnt.render("X "*strikes, True, RED)
    WIN.blit(controls, (HUD.x+2, HUD.y+2))
    WIN.blit(controls2, (HUD.x+2, HUD.y+32))
    WIN.blit(xs, (HUD.x+180, HUD.y+32))
    WIN.blit(controls3, (HUD.x+2, HUD.y+62))

    for pair in filled:
        WIN.blit(pair[0], (CELLS[pair[1]].x+10, CELLS[pair[1]].y-5))
    pygame.display.update()

def main():
    run = True
    #input_box = pygame.Rect(0,0,100,32)
    clicked = []
    text = ''
    strikes = 0
    for i in range(81):
        row = i//9
        col = i%9
        CELLS.append(pygame.Rect(col*(WIDTH//9)+6, row*((HEIGHT-OFFSET)//9)+6, \
                                    (WIDTH//9)-3, ((HEIGHT-OFFSET)//9)-3))
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                text = ''
                pos = pygame.mouse.get_pos()
                clicked = [c for c in CELLS if c.collidepoint(pos)]
                clicked_idx = -1
                for i in range(81):
                    if CELLS[i].collidepoint(pos):
                        clicked_idx = i
                
            if event.type == pygame.KEYDOWN:
                if clicked != []:
                    if event.key == pygame.K_RETURN:
                        if BOARD[clicked_idx//9][clicked_idx%9] == 0 and text != '' \
                        and sudoku_solver.check_safe(BOARD, int(text), clicked_idx//9, clicked_idx%9) \
                        and BOARD_SOLVED[clicked_idx//9][clicked_idx%9] == int(text):
                            BOARD[clicked_idx//9][clicked_idx%9] = int(text)
                            print("Correct")
                        else:
                            strikes += 1
                            print("Wrong")
                        #print(text)
                        text = ''
                        #sudoku_solver.print_grid(BOARD)
                    elif event.key == pygame.K_BACKSPACE:
                        #text = text[:-1]
                        if BOARD_OLD[clicked_idx//9][clicked_idx%9] == 0:
                            BOARD[clicked_idx//9][clicked_idx%9] = 0
                    else:
                        if event.unicode.isnumeric() and event.unicode != '0':
                            text = event.unicode
                if event.key == pygame.K_SPACE:
                    sudoku_solver.idliketosolvethepuzzle(BOARD)
        if clicked != []:
            draw_window(strikes, text, clicked[0], clicked_idx)
        else:
            draw_window(strikes)



if __name__ == "__main__":
    main()