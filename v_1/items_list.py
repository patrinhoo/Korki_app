import pygame

# COLORs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
LIGHT_GRAY = (240, 240, 240)

# FONTS
pygame.font.init()
FNT15 = pygame.font.SysFont('comicsans', 15)


class ItemsList:
    def __init__(self, x_pos, y_pos, width, height, columns, data):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.row_height = 30
        self.frame_width = 2
        self.columns = columns
        self.first_column_width = 48
        self.next_columns_width = (
            self.width - self.first_column_width) / (len(columns) - 1)
        self.data = data
        self.first_row = 0

        self.scroll_button_1 = pygame.image.load(
            'v_1/image1.png')
        self.scroll_button_2 = pygame.image.load(
            'v_1/image2.png')

    def draw_list(self, win):
        self.draw_list_bg(win)
        self.draw_header(win)
        self.draw_data(win)
        self.draw_buttons(win)

    def draw_list_bg(self, win):

        pygame.draw.rect(win, BLACK, (self.x_pos,
                         self.y_pos, self.width, self.height))
        pygame.draw.rect(win, WHITE, (self.x_pos + self.frame_width, self.y_pos + self.frame_width + 2*self.row_height,
                         self.first_column_width - 2*self.frame_width, self.height - 2*self.frame_width - 3*self.row_height))

        y_pos = self.y_pos + self.frame_width + 2*self.row_height
        width = self.next_columns_width - self.frame_width
        height = self.height - 2*self.frame_width - 3*self.row_height

        for i in range(len(self.columns) - 1):
            x_pos = self.x_pos + self.first_column_width + self.next_columns_width * i

            pygame.draw.rect(win, WHITE, (x_pos, y_pos, width, height))

    def draw_header(self, win):
        pygame.draw.rect(win, GRAY, (self.x_pos + self.frame_width, self.y_pos + self.frame_width,
                         self.first_column_width - 2*self.frame_width, self.row_height - self.frame_width))

        text = FNT15.render(str(self.columns[0]), True, BLACK)

        text_x = self.x_pos + \
            (self.first_column_width - text.get_width()) // 2
        text_y = self.y_pos + \
            (self.row_height - text.get_height()) // 2

        win.blit(text, (text_x, text_y))

        for i in range(len(self.columns) - 1):
            x_pos = self.x_pos + self.first_column_width + self.next_columns_width * i
            y_pos = self.y_pos + self.frame_width
            width = self.next_columns_width - self.frame_width
            height = self.row_height - self.frame_width

            pygame.draw.rect(win, GRAY, (x_pos, y_pos, width, height))

            text = FNT15.render(str(self.columns[i + 1]), True, BLACK)

            text_x = self.x_pos + self.first_column_width + i * self.next_columns_width + \
                (self.next_columns_width - text.get_width()) // 2
            text_y = self.y_pos + (self.row_height - text.get_height()) // 2
            win.blit(text, (text_x, text_y))

    def draw_data(self, win):
        n_rows = min(7, len(self.data))

        for nr, row in enumerate(self.data[self.first_row: n_rows + self.first_row], start=1):
            pygame.draw.rect(win, LIGHT_GRAY, (self.x_pos + self.frame_width, self.y_pos + self.frame_width +
                             self.row_height * (nr + 1), self.first_column_width - 2*self.frame_width, self.row_height - self.frame_width))

            text = FNT15.render(str(nr + self.first_row), True, BLACK)

            text_x = self.x_pos + \
                (self.first_column_width - text.get_width()) // 2
            text_y = self.y_pos + (nr + 1) * self.row_height + \
                (self.row_height - text.get_height()) // 2

            win.blit(text, (text_x, text_y))

            for i, value in enumerate(row.values()):
                x_pos = self.x_pos + self.frame_width + \
                    self.first_column_width + i * self.next_columns_width
                y_pos = self.y_pos + self.frame_width + \
                    self.row_height * (nr + 1)
                width = self.next_columns_width - 2*self.frame_width
                height = self.row_height - self.frame_width

                pygame.draw.rect(
                    win, LIGHT_GRAY, (x_pos, y_pos, width, height))

                text = FNT15.render(str(value), True, BLACK)

                text_x = self.x_pos + self.first_column_width + i * self.next_columns_width + \
                    (self.next_columns_width - text.get_width()) // 2
                text_y = self.y_pos + (nr + 1) * self.row_height + \
                    (self.row_height - text.get_height()) // 2
                win.blit(text, (text_x, text_y))

    def draw_buttons(self, win):
        self.button1_rect = pygame.Rect(self.x_pos + self.frame_width, self.y_pos + self.frame_width + self.row_height,
                                        self.width - 2*self.frame_width, self.row_height - self.frame_width)

        win.blit(self.scroll_button_1, self.button1_rect)

        self.button2_rect = pygame.Rect(self.x_pos + self.frame_width, self.y_pos + self.height - self.row_height,
                                        self.width - 2*self.frame_width, self.row_height - self.frame_width)

        win.blit(self.scroll_button_2, self.button2_rect)

    def update(self):
        mpos = pygame.mouse.get_pos()
        if self.button1_rect.collidepoint(mpos):
            if self.first_row > 0:
                self.first_row -= 1

        if self.button2_rect.collidepoint(mpos):
            if self.first_row < len(self.data) - 7:
                self.first_row += 1
