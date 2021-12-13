import pygame
import sys
import json
import os.path

from items_list import ItemsList
from option_box import OptionBox
from input_box import InputBox

WIDTH = 800
HEIGHT = 600

# COLORS
AQUAMARINE = (0, 200, 150)
LIGHT_BLUE = (100, 150, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 200, 255)
ORANGE = (255, 200, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# FONTS
pygame.font.init()
FNT15 = pygame.font.SysFont('comicsans', 15)
FNT25 = pygame.font.SysFont('comicsans', 25)


class App:
    def __init__(self, width, height):
        # WINDOW DISMENSIONS
        self.WIDTH = width
        self.HEIGHT = height

        # DATA
        if os.path.exists("v_1/data.json"):
            with open("v_1/data.json", "r") as file:
                self.data = json.loads(file.read())
        else:
            self.data = {}

        self.handle_data()

        # OPTION BOX
        self.address_box = OptionBox(
            25, 60, 360, 30, GRAY, WHITE, FNT15, [data[0] + ', ' + data[1] + ' ' + data[2] for data in self.addresses], selected=0)

        self.delete_box = OptionBox(
            25, 475, 150, 30, LIGHT_BLUE, GRAY, FNT15, ['NR LEKCJI', 'NR WPŁATY', 'NR ADRESU'], selected=0)
        # 0 - delete lesson, 1 - delete donation, 2 - delete address
        self.selected_delete = 0

        # LISTS
        self.list_1 = ItemsList(
            25, 125, 360, 302, ('Nr.', 'Data', 'Godzina', 'Czas trwania'), self.lessons)
        self.list_2 = ItemsList(
            415, 125, 360, 302, ('Nr.', 'Data', 'Kwota'), self.donations)

        # INPUT BOXES
        self.input_1 = InputBox(25, 525, 150, 30)
        self.input_2 = InputBox(225, 525, 150, 30)
        self.input_3 = InputBox(425, 525, 150, 30)

        # 0 - default, 1 - add_lesson, 2 - add_donation, 3 - add_address, 4 - delete
        self.action = 0

# DRAWING
    def draw_items(self, win):
        win.fill(AQUAMARINE)
        self.draw_address(win)
        self.draw_number_of_lessons(win)
        self.draw_paid_lessons(win)
        self.list_1.draw_list(win)
        self.list_2.draw_list(win)
        if self.action == 0:
            self.draw_buttons(win)
        if self.action == 1:
            self.draw_add_lesson(win)
        if self.action == 2:
            self.draw_add_payment(win)
        if self.action == 3:
            self.draw_add_address(win)
        if self.action == 4:
            self.draw_delete(win)

        self.address_box.draw(win)

    def draw_buttons(self, win):
        self.draw_add_lesson_button(win)
        self.draw_add_payment_button(win)
        self.draw_delete_button(win)
        self.draw_add_address_button(win)
        self.draw_save_button(win)

    def draw_add_lesson(self, win):
        self.draw_rect(win, LIGHT_BLUE, 25, 475, 150, 30, 2)
        self.draw_text_in_rect(win, FNT15, 'DATA', 25, 475, 150, 30, True)
        self.draw_rect(win, LIGHT_BLUE, 225, 475, 150, 30, 2)
        self.draw_text_in_rect(win, FNT15, 'GODZINA', 225, 475, 150, 30, True)
        self.draw_rect(win, LIGHT_BLUE, 425, 475, 150, 30, 2)
        self.draw_text_in_rect(win, FNT15, 'CZAS TRWANIA',
                               425, 475, 150, 30, True)

        self.draw_rect(win, LIGHT_BLUE, 625, 460, 150, 40, 2)
        self.draw_text_in_rect(win, FNT25, 'ANULUJ',
                               625, 460, 150, 40, True)
        self.draw_rect(win, ORANGE, 625, 525, 150, 40, 2)
        self.draw_text_in_rect(win, FNT25, 'DODAJ',
                               625, 525, 150, 40, True)

        self.input_1.draw(win)
        self.input_2.draw(win)
        self.input_3.draw(win)

    def draw_add_payment(self, win):
        self.draw_rect(win, LIGHT_BLUE, 25, 475, 150, 30, 2)
        self.draw_text_in_rect(win, FNT15, 'DATA', 25, 475, 150, 30, True)
        self.draw_rect(win, LIGHT_BLUE, 225, 475, 150, 30, 2)
        self.draw_text_in_rect(win, FNT15, 'KWOTA', 225, 475, 150, 30, True)

        self.draw_rect(win, LIGHT_BLUE, 625, 460, 150, 40, 2)
        self.draw_text_in_rect(win, FNT25, 'ANULUJ',
                               625, 460, 150, 40, True)
        self.draw_rect(win, ORANGE, 625, 525, 150, 40, 2)
        self.draw_text_in_rect(win, FNT25, 'DODAJ',
                               625, 525, 150, 40, True)

        self.input_1.draw(win)
        self.input_2.draw(win)

    def draw_add_address(self, win):
        self.draw_rect(win, LIGHT_BLUE, 25, 475, 150, 30, 2)
        self.draw_text_in_rect(win, FNT15, 'MIEJSCOWOSC',
                               25, 475, 150, 30, True)
        self.draw_rect(win, LIGHT_BLUE, 225, 475, 150, 30, 2)
        self.draw_text_in_rect(win, FNT15, 'ULICA', 225, 475, 150, 30, True)
        self.draw_rect(win, LIGHT_BLUE, 425, 475, 150, 30, 2)
        self.draw_text_in_rect(win, FNT15, 'NUMER DOMU',
                               425, 475, 150, 30, True)

        self.draw_rect(win, LIGHT_BLUE, 625, 460, 150, 40, 2)
        self.draw_text_in_rect(win, FNT25, 'ANULUJ',
                               625, 460, 150, 40, True)
        self.draw_rect(win, ORANGE, 625, 525, 150, 40, 2)
        self.draw_text_in_rect(win, FNT25, 'DODAJ',
                               625, 525, 150, 40, True)

        self.input_1.draw(win)
        self.input_2.draw(win)
        self.input_3.draw(win)

    def draw_delete(self, win):
        self.draw_rect(win, LIGHT_BLUE, 625, 460, 150, 40, 2)
        self.draw_text_in_rect(win, FNT25, 'ANULUJ',
                               625, 460, 150, 40, True)
        self.draw_rect(win, ORANGE, 625, 525, 150, 40, 2)
        self.draw_text_in_rect(win, FNT25, 'USUŃ',
                               625, 525, 150, 40, True)
        self.draw_rect(win, GRAY, 300, 460, 200, 65, 2)
        self.draw_text_in_rect(win, FNT15, 'WYBIERZ Z LISTY',
                               300, 460, 200, 40, True)
        self.draw_text_in_rect(win, FNT15, 'CO CHCESZ USUNĄĆ',
                               300, 485, 200, 40, True)

        self.input_1.draw(win)
        self.delete_box.draw(win)

    def draw_rect(self, win, rect_color, x_pos, y_pos, width, height, line_size):
        pygame.draw.rect(win, BLACK, (x_pos, y_pos, width, height))
        pygame.draw.rect(win, rect_color, (x_pos + line_size, y_pos +
                                           line_size, width - 2*line_size, height - 2*line_size))

    def draw_text_in_rect(self, win, fnt, text, rect_x, rect_y, rect_width, rect_height, middle):
        first_text = fnt.render(str(text), True, BLACK)
        if middle:
            first_text_x = rect_x + (rect_width - first_text.get_width()) // 2
        else:
            first_text_x = rect_x + 15
        first_text_y = rect_y + (rect_height - first_text.get_height()) // 2
        win.blit(first_text, (first_text_x, first_text_y))

    def draw_address(self, win):
        self.draw_rect(win, LIGHT_BLUE, 25, 25, 80, 30, 2)
        self.draw_text_in_rect(win, FNT15, 'ADRES', 25, 25, 80, 30, False)

    def draw_number_of_lessons(self, win):
        self.draw_rect(win, LIGHT_BLUE, 415, 25, 145, 30, 2)
        self.draw_rect(win, GRAY, 415, 60, 145, 30, 2)
        self.draw_text_in_rect(
            win, FNT15, 'LICZBA GODZIN', 415, 25, 145, 30, True)
        self.draw_text_in_rect(
            win, FNT15, self.lesson_hours, 415, 60, 145, 30, True)

    def draw_paid_lessons(self, win):
        self.draw_rect(win, LIGHT_BLUE, 590, 25, 185, 30, 2)
        self.draw_rect(win, GRAY, 590, 60, 185, 30, 2)
        self.draw_text_in_rect(
            win, FNT15, 'OPŁACONYCH GODZIN', 590, 25, 185, 30, True)
        self.draw_text_in_rect(
            win, FNT15, self.paid_lessons, 590, 60, 185, 30, True)

    def draw_add_lesson_button(self, win):
        self.draw_rect(win, BLUE, 25, 450, 240, 50, 2)
        self.draw_text_in_rect(
            win, FNT25, 'DODAJ LEKCJĘ', 25, 450, 240, 50, True)

    def draw_add_payment_button(self, win):
        self.draw_rect(win, BLUE, 535, 450, 240, 50, 2)
        self.draw_text_in_rect(win, FNT25, 'DODAJ WPŁATĘ',
                               535, 450, 240, 50, True)

    def draw_delete_button(self, win):
        self.draw_rect(win, ORANGE, 25, 525, 240, 50, 2)
        self.draw_text_in_rect(win, FNT25, 'USUŃ',
                               25, 525, 240, 50, True)

    def draw_add_address_button(self, win):
        self.draw_rect(win, BLUE, 280, 450, 240, 50, 2)
        self.draw_text_in_rect(win, FNT25, 'DODAJ ADRES',
                               280, 450, 240, 50, True)

    def draw_save_button(self, win):
        self.draw_rect(win, ORANGE, 535, 525, 240, 50, 2)
        self.draw_text_in_rect(win, FNT25, 'ZAPISZ', 535, 525, 240, 50, True)

    def draw_wrong_inputs(self, win):
        self.draw_rect(win, ORANGE, 300, 525, 200, 50, 2)
        self.draw_text_in_rect(win, FNT25, 'BŁĘDNE DANE',
                               300, 525, 200, 50, True)
        pygame.display.update()
        pygame.time.delay(500)

# ACTION
    def handle_data(self):
        self.numbers = [nr for nr in self.data]
        if self.numbers:
            try:
                self.actual_number
            except:
                self.actual_number = self.numbers[0]

            self.actual_data = self.data[self.actual_number]

            self.addresses = [(self.data[i]["city"], self.data[i]
                               ["street"], self.data[i]["number"]) for i in self.numbers]

            self.actual_address = self.addresses[int(self.actual_number)]
            self.lesson_hours = self.actual_data["hours_of_lessons"]
            self.paid_lessons = self.actual_data["number_of_paid_hours"]

            self.lessons = [
                lesson for lesson in self.actual_data['lessons'].values()]
            self.donations = [
                donation for donation in self.actual_data['donations'].values()]
        else:
            self.actual_data = {}
            self.addresses = []
            self.actual_address = ()
            self.lesson_hours = 0
            self.paid_lessons = 0
            self.lessons = []
            self.donations = []

    def change_address(self, nr):
        if self.actual_address != self.addresses[nr]:
            self.actual_address = self.addresses[nr]

            self.actual_number = self.numbers[nr]
            self.handle_data()

            self.list_1.data = self.lessons
            self.list_2.data = self.donations
            self.list_1.first_row = 0
            self.list_2.first_row = 0

    def handle_inputs(self, event):
        self.input_1.handle_event(event)
        self.input_2.handle_event(event)
        self.input_3.handle_event(event)

    def add_lesson(self, event, win):
        try:
            duration = int(self.input_3.text)
            nr = 0
            while True:
                if str(nr) in self.data[self.actual_number]['lessons']:
                    nr += 1
                else:
                    self.data[self.actual_number]['lessons'][str(nr)] = {
                        'date': self.input_1.text, 'hour': self.input_2.text, 'duration': duration}
                    break

            self.data[self.actual_number]['hours_of_lessons'] += duration
            self.handle_data()
            self.list_1.data = self.lessons

            self.action = 0
            self.clear_inputs()
            self.handle_inputs(event)
        except:
            self.clear_inputs()
            self.handle_inputs(event)
            self.draw_wrong_inputs(win)

    def add_donation(self, event, win):
        try:
            amount = int(self.input_2.text)
            nr = 0
            while True:
                if str(nr) in self.data[self.actual_number]['donations']:
                    nr += 1
                else:
                    self.data[self.actual_number]['donations'][str(
                        nr)] = {'date': self.input_1.text, 'amount': amount}
                    break

            self.data[self.actual_number]['number_of_paid_hours'] += amount // 50
            self.handle_data()
            self.list_2.data = self.donations

            self.action = 0
            self.clear_inputs()
            self.handle_inputs(event)
        except:
            self.handle_inputs(event)
            self.clear_inputs()
            self.draw_wrong_inputs(win)

    def add_address(self, event, win):
        good = True
        if self.input_1.text == '' or self.input_2.text == '' or self.input_3.text == '':
            good = False

        if good:
            nr = 0
            while True:
                if str(nr) in self.numbers:
                    nr += 1
                else:
                    self.numbers.append(str(nr))
                    break

            self.data[str(nr)] = {'city': self.input_1.text, 'street': self.input_2.text, 'number': self.input_3.text,
                                  'hours_of_lessons': 0, 'number_of_paid_hours': 0, 'lessons': {}, 'donations': {}}

            self.handle_data()
            self.address_box.option_list = [
                data[0] + ', ' + data[1] + ' ' + data[2] for data in self.addresses]

            self.action = 0
            self.handle_inputs(event)
            self.clear_inputs()
        else:
            self.draw_wrong_inputs(win)

    def clear_inputs(self):
        self.input_1.clear_input()
        self.input_2.clear_input()
        self.input_3.clear_input()

    def save(self, win):
        try:
            with open("v_1/data.json", "w") as file:
                json.dump(self.data, file)
            self.draw_rect(win, LIGHT_BLUE, 300, 525, 200, 50, 2)
            self.draw_text_in_rect(
                win, FNT25, 'ZAPISANO', 300, 525, 200, 50, True)
            pygame.display.update()
            pygame.time.delay(500)
        except:
            self.draw_rect(win, LIGHT_BLUE, 300, 525, 200, 50, 2)
            self.draw_text_in_rect(
                win, FNT25, 'BŁĄD ZAPISU', 300, 525, 200, 50, False)
            pygame.display.update()
            pygame.time.delay(500)

    def delete(self, event, win):
        try:
            nr = int(self.input_1.text) - 1
            if self.selected_delete == 0:
                self.data[self.actual_number]['hours_of_lessons'] -= self.data[self.actual_number]['lessons'][str(
                    nr)]['duration']
                del self.data[self.actual_number]['lessons'][str(nr)]
                self.renumber_lessons()

            elif self.selected_delete == 1:
                self.data[self.actual_number]['number_of_paid_hours'] -= self.data[self.actual_number]['donations'][str(
                    nr)]['amount'] // 50
                del self.data[self.actual_number]['donations'][str(nr)]
                self.renumber_donations()

            elif self.selected_delete == 2:
                self.actual_number = self.numbers[0]
                self.address_box.selected = 0
                del self.data[str(nr)]
                self.renumber_addresses()

            self.handle_data()
            self.list_1.data = self.lessons
            self.list_2.data = self.donations
            self.address_box.option_list = [
                data[0] + ', ' + data[1] + ' ' + data[2] for data in self.addresses]

            self.action = 0
            self.handle_inputs(event)
            self.clear_inputs()
        except:
            self.handle_inputs(event)
            self.clear_inputs()
            self.draw_wrong_inputs(win)

    def renumber_lessons(self):
        next_nr = 0
        lessons_dict = {}

        for nr, item in self.data[self.actual_number]['lessons'].items():
            lessons_dict[str(next_nr)] = item
            next_nr += 1
        self.data[self.actual_number]['lessons'] = lessons_dict

    def renumber_donations(self):
        next_nr = 0
        donations_dict = {}

        for nr, item in self.data[self.actual_number]['donations'].items():
            donations_dict[str(next_nr)] = item
            next_nr += 1
        self.data[self.actual_number]['donations'] = donations_dict

    def renumber_addresses(self):
        next_nr = 0
        addresses_dict = {}

        for nr, item in self.data.items():
            addresses_dict[str(next_nr)] = item
            next_nr += 1
        self.data = addresses_dict

# START APP
    def play(self):
        run = True
        pygame.init()
        win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('Korki')
        clock = pygame.time.Clock()

        self.draw_items(win)
        pygame.display.update()

        while run:
            event_list = pygame.event.get()

            mouse_pos = pygame.mouse.get_pos()
            for event in event_list:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.list_1.update()
                    self.list_2.update()
                    if self.action == 0:
                        if (mouse_pos[0] >= 25) and (mouse_pos[0] <= 265) and (mouse_pos[1] >= 450) and (mouse_pos[1] <= 500):
                            self.action = 1
                        elif (mouse_pos[0] >= 535) and (mouse_pos[0] <= 775) and (mouse_pos[1] >= 450) and (mouse_pos[1] <= 500):
                            self.action = 2
                        elif (mouse_pos[0] >= 280) and (mouse_pos[0] <= 520) and (mouse_pos[1] >= 450) and (mouse_pos[1] <= 500):
                            self.action = 3
                        elif (mouse_pos[0] >= 25) and (mouse_pos[0] <= 265) and (mouse_pos[1] >= 525) and (mouse_pos[1] <= 575):
                            self.action = 4
                        elif (mouse_pos[0] >= 535) and (mouse_pos[0] <= 775) and (mouse_pos[1] >= 525) and (mouse_pos[1] <= 575):
                            self.save(win)

                    elif self.action == 1:
                        if (mouse_pos[0] >= 625) and (mouse_pos[0] <= 775) and (mouse_pos[1] >= 525) and (mouse_pos[1] <= 565):
                            self.add_lesson(event, win)
                        elif (mouse_pos[0] >= 625) and (mouse_pos[0] <= 775) and (mouse_pos[1] >= 460) and (mouse_pos[1] <= 500):
                            self.action = 0
                            self.handle_inputs(event)
                            self.clear_inputs()
                        elif (mouse_pos[0] >= 25) and (mouse_pos[0] <= 175) and (mouse_pos[1] >= 525) and (mouse_pos[1] <= 555):
                            self.handle_inputs(event)
                        elif (mouse_pos[0] >= 225) and (mouse_pos[0] <= 375) and (mouse_pos[1] >= 525) and (mouse_pos[1] <= 555):
                            self.handle_inputs(event)
                        elif (mouse_pos[0] >= 425) and (mouse_pos[0] <= 575) and (mouse_pos[1] >= 525) and (mouse_pos[1] <= 555):
                            self.handle_inputs(event)
                        else:
                            self.handle_inputs(event)

                    elif self.action == 2:
                        if (mouse_pos[0] >= 625) and (mouse_pos[0] <= 775) and (mouse_pos[1] >= 525) and (mouse_pos[1] <= 565):
                            self.add_donation(event, win)
                        elif (mouse_pos[0] >= 625) and (mouse_pos[0] <= 775) and (mouse_pos[1] >= 460) and (mouse_pos[1] <= 500):
                            self.action = 0
                            self.handle_inputs(event)
                            self.clear_inputs()
                        elif (mouse_pos[0] >= 25) and (mouse_pos[0] <= 175) and (mouse_pos[1] >= 525) and (mouse_pos[1] <= 555):
                            self.handle_inputs(event)
                        elif (mouse_pos[0] >= 225) and (mouse_pos[0] <= 375) and (mouse_pos[1] >= 525) and (mouse_pos[1] <= 555):
                            self.handle_inputs(event)
                        else:
                            self.handle_inputs(event)

                    elif self.action == 3:
                        if (mouse_pos[0] >= 625) and (mouse_pos[0] <= 775) and (mouse_pos[1] >= 525) and (mouse_pos[1] <= 565):
                            self.add_address(event, win)
                        elif (mouse_pos[0] >= 625) and (mouse_pos[0] <= 775) and (mouse_pos[1] >= 460) and (mouse_pos[1] <= 500):
                            self.action = 0
                            self.handle_inputs(event)
                            self.clear_inputs()
                        elif (mouse_pos[0] >= 25) and (mouse_pos[0] <= 175) and (mouse_pos[1] >= 525) and (mouse_pos[1] <= 555):
                            self.handle_inputs(event)
                        elif (mouse_pos[0] >= 225) and (mouse_pos[0] <= 375) and (mouse_pos[1] >= 525) and (mouse_pos[1] <= 555):
                            self.handle_inputs(event)
                        elif (mouse_pos[0] >= 425) and (mouse_pos[0] <= 575) and (mouse_pos[1] >= 525) and (mouse_pos[1] <= 555):
                            self.handle_inputs(event)
                        else:
                            self.handle_inputs(event)

                    elif self.action == 4:
                        if (mouse_pos[0] >= 625) and (mouse_pos[0] <= 775) and (mouse_pos[1] >= 525) and (mouse_pos[1] <= 565):
                            self.delete(event, win)
                        elif (mouse_pos[0] >= 625) and (mouse_pos[0] <= 775) and (mouse_pos[1] >= 460) and (mouse_pos[1] <= 500):
                            self.action = 0
                            self.handle_inputs(event)
                            self.clear_inputs()
                        elif (mouse_pos[0] >= 25) and (mouse_pos[0] <= 175) and (mouse_pos[1] >= 525) and (mouse_pos[1] <= 555):
                            self.handle_inputs(event)
                        else:
                            self.handle_inputs(event)

                elif event.type == pygame.KEYDOWN:
                    if self.input_1.active:
                        self.input_1.handle_event(event)
                    elif self.input_2.active:
                        self.input_2.handle_event(event)
                    elif self.input_3.active:
                        self.input_3.handle_event(event)

            selected_delete = self.delete_box.update(event_list)
            if selected_delete != self.selected_delete and selected_delete in range(3):
                self.selected_delete = selected_delete

            selected_address = self.address_box.update(event_list)
            try:
                if selected_address != self.actual_number:
                    for nr in range(len(self.addresses)):
                        if selected_address == nr:
                            self.change_address(nr)
            except:
                pass

            self.draw_items(win)
            pygame.display.update()
            clock.tick(60)


if __name__ == '__main__':
    my_app = App(WIDTH, HEIGHT)
    my_app.play()
