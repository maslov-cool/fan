import pygame
import math

if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    # размеры окна:
    size = width, height = 201, 201
    # screen — холст, на котором нужно рисовать:
    screen = pygame.display.set_mode(size)
    # формирование кадра:
    # команды рисования на холсте
    pygame.display.set_caption('Вентилятор')

    angles = [5 * math.pi / 6, 3 * math.pi / 2, - 11 * math.pi / 6]
    speed = 0
    cnt = 0
    running = True
    clock = pygame.time.Clock()
    while running:
        screen.fill('black')
        pygame.draw.circle(screen, 'white', [width / 2, height / 2], 10)
        for i in angles:
            pygame.draw.polygon(screen, 'white', [[width / 2, height / 2],
                                                  [math.cos(math.radians(cnt) + i - math.radians(15)) * 70 + width / 2,
                                                   math.sin(
                                                       math.radians(cnt) + i - math.radians(15)) * 70 + height / 2],
                                                  [math.cos(math.radians(cnt) + i + math.radians(15)) * 70 + width / 2,
                                                   math.sin(
                                                       math.radians(cnt) + i + math.radians(15)) * 70 + height / 2]])
        # внутри игрового цикла ещё один цикл
        # приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                speed -= 50
                cnt -= 1
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
                speed += 50
                cnt -= 1
        clock.tick(abs(speed))
        # обновление экрана
        pygame.display.flip()
        if speed < 0:
            cnt -= 1
        elif speed > 0:
            cnt += 1
    # завершение работы:
    pygame.quit()
