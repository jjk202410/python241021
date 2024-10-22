import pygame
import random

# 색상 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
PURPLE = (255, 0, 255)
RED = (255, 0, 0)

# 게임 설정
BLOCK_SIZE = 30
BOARD_WIDTH = 10
BOARD_HEIGHT = 20
SCREEN_WIDTH = BOARD_WIDTH * BLOCK_SIZE
SCREEN_HEIGHT = BOARD_HEIGHT * BLOCK_SIZE

# 테트로미노 모양
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]]
]

COLORS = [CYAN, YELLOW, PURPLE, BLUE, ORANGE, GREEN, RED]

class Tetromino:
    def __init__(self):
        self.shape = random.choice(SHAPES)
        self.color = random.choice(COLORS)
        self.x = BOARD_WIDTH // 2 - len(self.shape[0]) // 2
        self.y = 0

def create_board():
    return [[BLACK for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]

def draw_board(screen, board):
    for y, row in enumerate(board):
        for x, color in enumerate(row):
            pygame.draw.rect(screen, color, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)

def draw_tetromino(screen, tetromino):
    for y, row in enumerate(tetromino.shape):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, tetromino.color,
                                 ((tetromino.x + x) * BLOCK_SIZE, (tetromino.y + y) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)

def check_collision(board, tetromino):
    for y, row in enumerate(tetromino.shape):
        for x, cell in enumerate(row):
            if cell:
                if (tetromino.y + y >= BOARD_HEIGHT or
                    tetromino.x + x < 0 or
                    tetromino.x + x >= BOARD_WIDTH or
                    board[tetromino.y + y][tetromino.x + x] != BLACK):
                    return True
    return False

def merge_tetromino(board, tetromino):
    for y, row in enumerate(tetromino.shape):
        for x, cell in enumerate(row):
            if cell:
                board[tetromino.y + y][tetromino.x + x] = tetromino.color

def remove_full_rows(board):
    full_rows = [i for i, row in enumerate(board) if all(cell != BLACK for cell in row)]
    for row in full_rows:
        del board[row]
        board.insert(0, [BLACK for _ in range(BOARD_WIDTH)])
    return len(full_rows)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("테트리스")
    clock = pygame.time.Clock()

    board = create_board()
    current_tetromino = Tetromino()
    fall_time = 0
    fall_speed = 0.5
    score = 0

    running = True
    while running:
        fall_time += clock.get_rawtime()
        clock.tick()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_tetromino.x -= 1
                    if check_collision(board, current_tetromino):
                        current_tetromino.x += 1
                if event.key == pygame.K_RIGHT:
                    current_tetromino.x += 1
                    if check_collision(board, current_tetromino):
                        current_tetromino.x -= 1
                if event.key == pygame.K_DOWN:
                    current_tetromino.y += 1
                    if check_collision(board, current_tetromino):
                        current_tetromino.y -= 1
                if event.key == pygame.K_UP:
                    current_tetromino.shape = list(zip(*current_tetromino.shape[::-1]))
                    if check_collision(board, current_tetromino):
                        current_tetromino.shape = list(zip(*current_tetromino.shape[::1]))

        if fall_time / 1000 > fall_speed:
            current_tetromino.y += 1
            if check_collision(board, current_tetromino):
                current_tetromino.y -= 1
                merge_tetromino(board, current_tetromino)
                rows_cleared = remove_full_rows(board)
                score += rows_cleared * 100
                current_tetromino = Tetromino()
                if check_collision(board, current_tetromino):
                    running = False
            fall_time = 0

        screen.fill(BLACK)
        draw_board(screen, board)
        draw_tetromino(screen, current_tetromino)
        pygame.display.flip()

    pygame.quit()
    print(f"게임 오버! 최종 점수: {score}")

if __name__ == "__main__":
    main()