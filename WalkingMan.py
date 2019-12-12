# -*- coding: utf8 -*-
import pygame

X_SIZE = 800
Y_SIZE = 600
WIN_SIZE = (X_SIZE, Y_SIZE)

# Цвета игры
COLOR_WHITE = (255, 255, 255)

# Другие константы
Y_GROUND = 500

# Класс динозавр
class Man:
    def __init__(self, screen, x, y):
        # Инициализация динозавра (экран, на котором рисуется динозавр и его начальная позиция)
        self.x = x
        self.y = y
        self.screen = screen
        self.step = 0
        self.sprites = []
        self.sprites.append(pygame.image.load('man1.png'))
        self.sprites.append(pygame.image.load('man2.png'))
        self.sprites.append(pygame.image.load('man3.png'))
        self.sprites.append(pygame.image.load('man4.png'))

    def draw(self):
        self.screen.blit(self.sprites[self.step], (self.x, self.y))

    def walk(self):
        self.step += 1
        if self.step >= 3:
            self.step = 0

def main():
    # Программа должна начинаться с инициализации pygame
    pygame.init()
    screen = pygame.display.set_mode(WIN_SIZE)
    pygame.display.set_caption("Walking Man")
    clock = pygame.time.Clock()

    # Другие инициализации, специфичные для игры
    do_pygame = True
    do_pause = False
    man = Man(screen, 100, 100)

    # Главный цикл программы. Каждую итерацию опрашиваются и обрабатываются события,
    # изменяются объекты и перерисовываются на экране
    while do_pygame:

        # Обработка событий
        for event in pygame.event.get():  # Обрабатываем все события, которые случились с предыдущей итерации
            if event.type == pygame.QUIT:  # Если нажата кнопка ЗАКРЫТЬ - выход из программы
                do_pygame = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    do_pause = True
                elif not do_pause:  # Все остальные кнопки не работают, пока игра на паузе
                    if event.key == pygame.K_RIGHT:
                        # Если нажата клавиша ВПРАВО
                        print('Right')
                    elif event.key == pygame.K_LEFT:
                        # Если нажата клавиша ВЛЕВО
                        print('Left')

        # Здесь перерисовывуются все объекты
        screen.fill(COLOR_WHITE)
        man.draw()

        # Обрабатываем другие изменения объектов, не связанные с событиями
        man.walk()

        # Каждая итерация заканчивается этими двумя командами
        pygame.display.flip()  # Отображаем перерисованное на экране
        clock.tick(10)  # Каждая итерация занимает 10 кадров в секунду

        # Освобождаем память по окончании игры
    pygame.quit()


if __name__ == "__main__":
    main()