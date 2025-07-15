import random
import time
import os

WIDTH = 20
HEIGHT = 10
INITIAL_SNAKE_LENGTH = 3
GAME_SPEED = 0.2

class SnakeGame:
    def __init__(self):
        self.snake = []
        self.food = None
        self.direction = 'right'
        self.score = 0
        self.game_over = False
        self.init_game()

    def init_game(self):
        start_x = WIDTH // 2
        start_y = HEIGHT // 2
        self.snake = []
        for i in range(INITIAL_SNAKE_LENGTH):
            self.snake.append((start_y, start_x - i))
        self.place_food()
        self.direction = 'right'
        self.score = 0
        self.game_over = False

    def place_food(self):
        while True:
            r = random.randint(0, HEIGHT - 1)
            c = random.randint(0, WIDTH - 1)
            if (r, c) not in self.snake:
                self.food = (r, c)
                break

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def draw_board(self):
        self.clear_screen()
        print('+' + '-' * (WIDTH * 2 + 1) + '+')
        for r in range(HEIGHT):
            row_str = '|'
            for c in range(WIDTH):
                if (r, c) == self.food:
                    row_str += ' F '
                elif (r, c) == self.snake[0]:
                    row_str += ' O '
                elif (r, c) in self.snake:
                    row_str += ' o '
                else:
                    row_str += '   '
            row_str += '|'
            print(row_str)
        print('+' + '-' * (WIDTH * 2 + 1) + '+')
        print(f"Score: {self.score}")
        if self.game_over:
            print("GAME OVER! Press 'R' to restart or 'Q' to quit.")

    def move_snake(self):
        head_y, head_x = self.snake[0]

        if self.direction == 'up':
            new_head = (head_y - 1, head_x)
        elif self.direction == 'down':
            new_y = head_y + 1
            new_head = (new_y, head_x)
        elif self.direction == 'left':
            new_head = (head_y, head_x - 1)
        elif self.direction == 'right':
            new_head = (head_y, head_x + 1)

        if (new_head[0] < 0 or new_head[0] >= HEIGHT or
            new_head[1] < 0 or new_head[1] >= WIDTH or
            new_head in self.snake):
            self.game_over = True
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.score += 1
            self.place_food()
        else:
            self.snake.pop()

    def change_direction(self, new_direction):
        if new_direction == 'up' and self.direction != 'down':
            self.direction = 'up'
        elif new_direction == 'down' and self.direction != 'up':
            self.direction = 'down'
        elif new_direction == 'left' and self.direction != 'right':
            self.direction = 'left'
        elif new_direction == 'right' and self.direction != 'left':
            self.direction = 'right'

    def run(self):
        while True:
            self.draw_board()
            if self.game_over:
                key = input().lower()
                if key == 'r':
                    self.init_game()
                    continue
                elif key == 'q':
                    break
                else:
                    continue

            self.move_snake()
            time.sleep(GAME_SPEED)
            pass

if __name__ == "__main__":
    game = SnakeGame()
    game.run()
