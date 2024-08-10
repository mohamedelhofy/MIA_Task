import pygame 
import os 

pygame.init()
WIDTH = 500
HEIGHT = 450
pygame.display.set_caption('Two-Player Pygame Chess!')
screen = pygame.display.set_mode([WIDTH, HEIGHT])
big_font = pygame.font.SysFont(None, 25)
timer = pygame.time.Clock()
fps = 60

# Game variables and images
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
captured_pieces_white = []
captured_pieces_black = []
turn_step = 0 # 0 - whites turn no selection: 1-whites turn piece selected: 2- black turn no selection, 3 - black turn piece selected
selection = 100 ## select of the pieces
valid_moves = []

# load images (queen, king, rook, bishop, knight, pawn)
def load_image(file_name, size, small_size):
    # Load the image 
    image = pygame.image.load(os.path.join(os.getcwd(), 'image', file_name))
    # Scale the image 
    image_scaled = pygame.transform.scale(image, size)
    image_small = pygame.transform.scale(image, small_size)    
    return image_scaled, image_small

black_queen, black_queen_small = load_image('black_qu.png', (30, 40), (17, 22))
black_king, black_king_small = load_image('black_king.png', (30, 40), (17, 22))
black_rook, black_rook_small = load_image('black_rook.png', (30, 40), (17, 22))
black_bishop, black_bishop_small = load_image('black_bishop.png', (30, 40), (17, 22))
black_knight, black_knight_small = load_image('black_knight.png', (30, 40), (17, 22))
black_pawn, black_pawn_small = load_image('black_pawn.png', (24, 32), (17, 22))
    
white_queen, white_queen_small = load_image('white_qu.png', (30, 40), (17, 22))
white_king, white_king_small = load_image('white_king.png', (30, 40), (17, 22))
white_rook, white_rook_small = load_image('white_rook.png', (30, 40), (17, 22))
white_bishop, white_bishop_small = load_image('white_Bishop.png', (30, 40), (17, 22))
white_knight, white_knight_small = load_image('white_knight.png', (30, 40), (17, 22))
white_pawn, white_pawn_small = load_image('white_pawn.png', (24, 32), (17, 22))
white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]
small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small,
                      white_rook_small, white_bishop_small]
black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]
small_black_images = [black_pawn_small, black_queen_small, black_king_small, black_knight_small,
                      black_rook_small, black_bishop_small]
piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']
# check variables/ flashing counter
counter = 0
winner = ''
game_over = False


# Draw game board
def draw_board():
    for i in range(32):
        col = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, 'light gray', [300 - (col * 100), row * 50, 50, 50]) ## even row
        else:
            pygame.draw.rect(screen, 'light gray', [350 - (col * 100), row * 50, 50, 50]) ## odd row

    pygame.draw.rect(screen, 'gray', [0, 400, WIDTH, 100]) ## color for lower board
    pygame.draw.rect(screen, 'gold', [0, 400, WIDTH, 50], 5) ## gold color for fram of board
    pygame.draw.rect(screen, 'gold', [400, 0, 100, HEIGHT], 5)
    status_text = ['White: Select a Piece to Move!', 'White: Select a Destination!',
                   'Black: Select a Piece to Move!', 'Black: Select a Destination!']
    screen.blit(big_font.render(status_text[turn_step], True, 'black'), (20, 410))
    screen.blit(big_font.render('exit', True, 'black'), (415, 415)) ## eixt buttom
    for i in range(9): ## black line in board
            pygame.draw.line(screen, 'black', (0, 50 * i), (400, 50 * i), 1)
            pygame.draw.line(screen, 'black', (50 * i, 0), (50 * i, 400), 1)

def draw_pieces():
    for i in range(len(white_pieces)):
        index=piece_list.index(white_pieces[i])
        if white_pieces[i] == 'pawn': ## if it pawn
            screen.blit(white_pawn, (white_locations[i][0] * 50 + 11, white_locations[i][1] * 50 + 15))
        else: # other pieces
            screen.blit(white_images[index], (white_locations[i][0] * 50+ 5, white_locations[i][1] * 50 + 5))
        if turn_step < 2: ## if it turn of white
            if selection == i: ## if the pieces is select make it in red fram
                pygame.draw.rect(screen, 'red', [white_locations[i][0] * 50 + 1, white_locations[i][1] * 50 + 1,50, 50], 2)

    for i in range(len(black_pieces)):   
        index = piece_list.index(black_pieces[i])
        if black_pieces[i] == 'pawn':## if it pawn
            screen.blit(black_pawn, (black_locations[i][0] * 50 + 11, black_locations[i][1] * 50 + 15))
        else:# other pieces
            screen.blit(black_images[index], (black_locations[i][0] * 50 + 10, black_locations[i][1] * 50 + 5))    
        if turn_step >= 2:## if it turn of black
            if selection == i:## if the pieces is select make it in red fram
                pygame.draw.rect(screen, 'blue', [black_locations[i][0] * 50 + 1, black_locations[i][1] * 50 + 1,50, 50], 2)

# function to check all pieces valid options on board
def check_options(pieces, locations, turn):
    moves_list = []
    all_moves_list = []
    for i in range((len(pieces))):
        location = locations[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = check_pawn(location, turn)
        elif piece == 'rook':
            moves_list = check_rook(location, turn)
        elif piece == 'knight':
            moves_list = check_knight(location, turn)
        elif piece == 'bishop':
            moves_list = check_bishop(location, turn)
        elif piece == 'queen':
           moves_list = check_queen(location, turn)
        elif piece == 'king':
           moves_list = check_king(location, turn)
        all_moves_list.append(moves_list)
    return all_moves_list

# check queen valid moves
def check_queen(position, color):
    ## qu can move as bishop and rook only
    moves_list = check_bishop(position, color)
    second_list = check_rook(position, color)
    for i in range(len(second_list)):
        moves_list.append(second_list[i])
    return moves_list

# check valid knight moves
def check_knight(position, color):
    moves_list = []
    # Define enemy and friend   
    if color == 'white': 
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    # 8 squares to check for knights
    targets = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        #if there isn't frind in new postion and there isn't out board so can move
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list

# check king valid moves
def check_king(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    # 8 squares to check for kings, they can go one square any direction
    targets = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list

# check rook moves
def check_rook(position, color):
    moves_list = []
    # Define enemy and friend   
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    # Define the four possible directions for a rook
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] # up, down, right, left
    for direction in directions:
        path = True
        chain = 1
        x, y = direction
        while path:
            new_position = (position[0] + (chain * x), position[1] + (chain * y))
            #find vaild path
            if new_position not in friends_list and 0 <= new_position[0] <= 7 and 0 <= new_position[1] <= 7:
                moves_list.append(new_position)
                if new_position in enemies_list:
                    path = False  # Stop if an enemy piece and append this postion
                chain += 1 ## chain plus it meaning plus one move also in this directions
            else:
                path = False  # Stop in friend piece and last append after this friend 
    return moves_list

## pawn check
def check_pawn(position, color):
    moves_list = []
    if color == 'white': ## if white turn
        if (position[0], position[1] + 1) not in white_locations and \
                (position[0], position[1] + 1) not in black_locations and position[1] < 7:  ##  check it not in white_locations and black_locations also not go out baerd
            moves_list.append((position[0], position[1] + 1))
        if (position[0], position[1] + 2) not in white_locations and \
                (position[0], position[1] + 2) not in black_locations and position[1] == 1: ## it can move to if start of game
            moves_list.append((position[0], position[1] + 2)) 
        if (position[0] + 1, position[1] + 1) in black_locations: ## eat black 
            moves_list.append((position[0] + 1, position[1] + 1))
        if (position[0] - 1, position[1] + 1) in black_locations: ## eat black 
            moves_list.append((position[0] - 1, position[1] + 1))
    else: ## black the same thing put by negative beacouse it in lower
        if (position[0], position[1] - 1) not in white_locations and \
                (position[0], position[1] - 1) not in black_locations and position[1] > 0:
            moves_list.append((position[0], position[1] - 1))
        if (position[0], position[1] - 2) not in white_locations and \
                (position[0], position[1] - 2) not in black_locations and position[1] == 6:
            moves_list.append((position[0], position[1] - 2))
        if (position[0] + 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] + 1, position[1] - 1))
        if (position[0] - 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] - 1, position[1] - 1))
    return moves_list

# check bishop moves
def check_bishop(position, color):
    moves_list = []
    # Define enemy and friend 
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    # Define the four diagonal directions
    directions = [(1, -1), (-1, -1), (1, 1), (-1, 1)] # up-right, up-left, down-right, down-left
    for direction in directions:
        path = True
        chain = 1
        x, y = direction
        while path:
            new_position = (position[0] + (chain * x), position[1] + (chain * y))
            if new_position not in friends_list and 0 <= new_position[0] <= 7 and 0 <= new_position[1] <= 7:
                moves_list.append(new_position)
                if new_position in enemies_list:
                    path = False   # Stop if an enemy piece and append this postion
                chain += 1 ## chain plus it meaning plus one move also in this directions
            else:
                path = False  # Stop in friend piece and last append after this friend 
    return moves_list

# choose  valid moves for just selected piece 
def choose_valid_moves():
    if turn_step < 2: # check it turn black or white
        options_list = white_options
    else:
        options_list = black_options
    valid_options = options_list[selection]
    return valid_options

# draw valid moves on screen
def draw_valid(moves):
    if turn_step < 2:
        color = 'red'
    else:
        color = 'blue'
    for i in range(len(moves)):
        pygame.draw.circle(screen, color, (moves[i][0] * 50 + 25, moves[i][1] * 50 + 25), 3)

# draw captured pieces on side of screen
def draw_captured():
    for i in range(len(captured_pieces_white)):
        captured_piece = captured_pieces_white[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_black_images[index], (412, 5 + 25 * i)) ## draw lest 
    for i in range(len(captured_pieces_black)):
        captured_piece = captured_pieces_black[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_white_images[index], (462, 5 + 25 * i))## draw rigth

# draw a flashing square around king if in check
def draw_check():
    if turn_step < 2:
        if 'king' in white_pieces: ## check is there king or not 
            king_index = white_pieces.index('king')
            king_location = white_locations[king_index]
            for i in range(len(black_options)):
                if king_location in black_options[i]: ## check king in scope of enemy or not
                    if counter < 15: ## flash (counter change in main loop)
                        pygame.draw.rect(screen, 'dark red', [white_locations[king_index][0] * 50 + 1,
                                                              white_locations[king_index][1] * 50 + 1, 50, 50], 3)
    else:## same thing but black
        if 'king' in black_pieces:
            king_index = black_pieces.index('king')
            king_location = black_locations[king_index]
            for i in range(len(white_options)):
                if king_location in white_options[i]:
                    if counter < 15:
                        pygame.draw.rect(screen, 'dark blue', [black_locations[king_index][0] * 50 + 1,
                                                               black_locations[king_index][1] * 50 + 1, 50, 50], 3)

## print
def draw_game_over():
    pygame.draw.rect(screen, 'black', [200, 180, 250, 70])
    screen.blit(big_font.render(f'{winner} won the game!', True, 'white'), (210, 190))
    screen.blit(big_font.render(f'Press ENTER to Restart!', True, 'white'), (210, 210))
# main loop
black_options = check_options(black_pieces, black_locations, 'black')
white_options = check_options(white_pieces, white_locations, 'white')
run=True
while run:
    timer.tick(fps)
    if counter<30:
        counter+=1
    else:
        counter=0    
    screen.fill('dark gray')
    draw_board()
    draw_pieces()
    draw_captured()
    draw_check()
    if selection != 100: ## if it select pieces print valid moves
        valid_moves = choose_valid_moves()
        draw_valid(valid_moves)
    #event handling
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over: ## select pieces by mouse
            ## postion of select
            x_coord = event.pos[0] // 50 
            y_coord = event.pos[1] // 50
            click_coords = (x_coord, y_coord)
            if turn_step <= 1:## white turn
                if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = 'black'  ## if you want exit press in exit
                if click_coords in white_locations:
                    selection = white_locations.index(click_coords)
                    if turn_step == 0:
                        turn_step = 1## turn white to move
                if click_coords in valid_moves and selection != 50:
                    white_locations[selection] = click_coords## change postion of selected pieace to new postion
                    ## white eat black pieces
                    if click_coords in black_locations:
                        black_piece = black_locations.index(click_coords)
                        captured_pieces_white.append(black_pieces[black_piece])
                        if black_pieces[black_piece] == 'king':
                            winner = 'white' ## white eat king and win
                        black_pieces.pop(black_piece) 
                        black_locations.pop(black_piece)
                    black_options = check_options(black_pieces, black_locations, 'black') ## find possible option 
                    white_options = check_options(white_pieces, white_locations, 'white') ## find possible option
                    turn_step = 2
                    selection = 100
                    valid_moves = []
            if turn_step > 1: #smae thing but to black
                if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = 'white' ## if you want exit press in exit
                if click_coords in black_locations:
                    selection = black_locations.index(click_coords)
                    if turn_step == 2:
                        turn_step = 3
                if click_coords in valid_moves and selection != 50:
                    black_locations[selection] = click_coords
                    if click_coords in white_locations:
                        white_piece = white_locations.index(click_coords)
                        captured_pieces_black.append(white_pieces[white_piece])
                        if white_pieces[white_piece] == 'king':
                            winner = 'black' ##black eat king and win 
                        white_pieces.pop(white_piece)
                        white_locations.pop(white_piece)
                    black_options = check_options(black_pieces, black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'white')
                    turn_step = 0
                    selection = 100
                    valid_moves = []
        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_RETURN: ## restart very thing from first
                game_over = False
                winner = ''
                white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
                black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
                captured_pieces_white = []
                captured_pieces_black = []
                turn_step = 0
                selection = 100
                valid_moves = []
                black_options = check_options(black_pieces, black_locations, 'black')
                white_options = check_options(white_pieces, white_locations, 'white')
    if winner != '':## there is winner
        game_over = True
        draw_game_over()
    #update display
    pygame.display.flip()
pygame.quit()
