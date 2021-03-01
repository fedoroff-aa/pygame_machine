import random
import pygame

Start = True
coin_visible = True
coin_active = True
coin_count = 0


def start():
    global accelerate, world_speed, Start
    if Start:
        my_font = pygame.font.Font('fonts/pixel.ttf', 70)
        text_image4 = my_font.render('FAST & FURIOUS 10', True, (0, 255, 10))
        game_display.blit(text_image4, (100, 200))
        myy_font = pygame.font.Font('fonts/pixel.ttf', 50)
        text_image5 = myy_font.render(
            'TO START PRESS *SPACE*', True, (0, 255, 10))
        game_display.blit(text_image5, (100, 280))
        accelerate = 0
        world_speed = 0
        coin_count = 0


def level():
    global distance
    if distance <= 2:
        pygame.draw.rect(game_display, (10, 10, 10), (0, 550, 800, 30))
        pygame.draw.rect(game_display, (0, 250, 10),
                         (5, 555, (790 * distance / 2), 20))


def victory():
    global distance, accelerate, world_speed, VICTORY
    if distance >= 2:
        VICTORY = True
        my_font = pygame.font.Font('fonts/pixel.ttf', 70)
        text_image4 = my_font.render('VICTORY', True, (0, 255, 10))
        game_display.blit(text_image4, (250, 250))
        myy_font = pygame.font.Font('fonts/pixel.ttf', 50)
        text_image5 = myy_font.render(
            'TO RESTART PRESS *SPACE*', True, (0, 255, 10))
        game_display.blit(text_image5, (100, 320))
        world_speed = 0
        accelerate = 0
        coin_count = 0


VICTORY = False
boost_visible = False
fuel_count = 0
coin = pygame.image.load('img/coin.gif')
coin = pygame.transform.scale(coin, (70, 70))
background1 = pygame.image.load('img/background.png')
background2 = pygame.image.load('img/background.png')
max_fuel = 200
fuel = max_fuel
game_over = False
max_hp = 10
hp = max_hp
hp_img = pygame.image.load('img/hp_icon.png')
fuel_img = pygame.image.load('img/fuel_icon.png')
display_w = 800
display_h = 600
game_exit = False
boost_active = False
boost_active_check = 1
boost_place = 1
boost_type = 2
boost_y = -100
boost_sprite = fuel_img


def boost():
    global boost_active, boost_place, boost_type, boost_active_check, boost_y, boost_sprite, boost_visible
    boost_y += (world_speed + accelerate)
    if boost_active_check == 1:
        boost_active = True
    if boost_active_check != 1:
        boost_active = False
    if boost_active:
        if boost_type == 1:
            boost_sprite = fuel_img
            if boost_visible:
                game_display.blit(fuel_img, (270 + boost_place * 75, boost_y))

        if boost_type == 2:
            boost_sprite = hp_img
            if boost_visible:
                game_display.blit(hp_img, (270 + boost_place * 75, boost_y))

    if boost_y > 600:
        boost_y = -100
        boost_visible = True
        boost_place = random.randint(1, 2)
        boost_type = random.randint(1, 2)
        boost_active_check = random.randint(0, 10)
        boost_active = False


coin_active = False
coin_place = 1
coin_visible = False
coin_y = -100
coin_active_check = 10


def coIn():
    global coin_active, coin_place, coin_active_check, coin_y, coin_sprite, coin_visible
    coin_y += (world_speed + accelerate)
    if coin_active_check == 1:
        coin_active = True
    if coin_active_check != 1:
        coin_active = False
    if coin_active:
        coin_sprite = coin
        if coin_visible:
            game_display.blit(coin, (270 + coin_place * 75, coin_y))
    if coin_y > 600:
        coin_y = -100
        coin_visible = True
        coin_place = random.randint(1, 2)
        coin_type = random.randint(1, 2)
        coin_active_check = random.randint(0, 10)
        coin_active = False


def GAME_OVER():
    global game_over, hp, accelerate, world_speed, fuel
    if hp <= 0 or fuel <= 0:
        game_over = True
        my_font = pygame.font.Font('fonts/pixel.ttf', 70)
        text_image4 = my_font.render('GAME OVER', True, (0, 255, 10))
        game_display.blit(text_image4, (250, 250))
        myy_font = pygame.font.Font('fonts/pixel.ttf', 50)
        text_image5 = myy_font.render(
            'TO RESTART PRESS *SPACE*', True, (0, 255, 10))
        game_display.blit(text_image5, (100, 320))
        world_speed = 0
        accelerate = 0


def hp_check():
    global hp, max_hp
    pygame.draw.rect(game_display, (10, 10, 10), (10, 30, 210, 30))
    if hp > 0:
        if hp > 7:
            pygame.draw.rect(game_display, (0, 250, 0), (15, 35, 20 * hp, 20))
        if hp <= 7:
            if hp <= 4:
                pygame.draw.rect(
                    game_display, (250, 0, 0), (15, 35, 20 * hp, 20))

            if hp > 4:
                pygame.draw.rect(
                    game_display, (250, 250, 0), (15, 35, 20 * hp, 20))

        game_display.blit(hp_img, (220, 25))


def fuel_check():
    global fuel, max_fuel, fuel_count, Start
    pygame.draw.rect(game_display, (10, 10, 10), (10, 130, 210, 30))
    if fuel > 0:
        pygame.draw.rect(game_display, (190, 255, 10), (15, 135, 1 * fuel, 20))

        game_display.blit(fuel_img, (220, 125))
        fuel_count += 0.03
        if fuel_count >= 1 and not Start:
            fuel_count = 0
            fuel -= 1


pygame.init()
game_display = pygame.display.set_mode((display_w, display_h))
my_font = pygame.font.Font("fonts/Pixel.ttf", 24)

# глобальные переменные
background_h = 2356
background_y = display_h - background_h
world_speed = 7
accelerate = 0
score = 0
distance = 0


class OurCar():
    def __init__(self):
        self.sprite = pygame.image.load('img/car.png')
        self.x = 0
        self.y = (display_h * 0.6)


class OtherCar1():
    def __init__(self):
        self.sprite = pygame.image.load('img/car_red2.png')
        self.x = 1
        self.y = -100
        self.visible = 0
        self.speed = -4


class OtherCar2():
    def __init__(self):
        self.sprite = pygame.image.load('img/car_red1.png')
        self.x = 0
        self.y = -100
        self.visible = 0
        self.speed = 4


car = OurCar()

other_cars = [OtherCar1(), OtherCar2(), OtherCar1()]
pygame.display.set_caption('Fast & Furious 10')
clock = pygame.time.Clock()
boost_rect = 0
boost_visible = True


def check_collision():
    global score, hp, boost_x, boost_y, hp_img, fuel_img, boost_sprite, \
        boost_visible, boost_rect, fuel, hp, max_hp, max_fuel, boost_active, \
        coin_active, coin_rect, coin_visible, coin_sprite, coin_count
    car_rect = car.sprite.get_rect().move((335 + car.x * 75, car.y))

    for idx in range(len(other_cars)):
        other_rect = other_cars[idx].sprite.get_rect().move(
            (335 + other_cars[idx].x * 75, other_cars[idx].y))
        if other_cars[idx].visible == 1:
            if car_rect.colliderect(other_rect):
                other_cars[idx].visible = 0
                score -= 200
                hp -= 1
                if score < 0:
                    score = 0
    if boost_visible:
        if boost_active:
            boost_rect = boost_sprite.get_rect().move((270 + boost_place * 75, boost_y))
            if boost_rect.colliderect(car_rect):
                if boost_type == 1:
                    fuel = max_fuel
                    boost_visible = False
                if boost_type == 2:
                    hp = max_hp
                    boost_visible = False
    if coin_visible:
        if coin_active:
            coin_rect = coin.get_rect().move((270 + boost_place * 75, boost_y))
            if coin_rect.colliderect(car_rect):
                coin_count += 1
                coin_visible = False


def draw_background():
    global background_y, distance

    game_display.blit(background1, (0, background_y))
    game_display.blit(background2, (0, background_y - background_h))
    background_y += world_speed + accelerate

    if background_y >= display_h:
        background_y = display_h - background_h
        distance += 1


def draw_ui():
    text_image = my_font.render(str(score), True, (255, 255, 255))
    game_display.blit(text_image, (720, 20))

    text_image = my_font.render(str(distance), True, (255, 255, 255))
    game_display.blit(text_image, (720, 40))

    text_image = my_font.render(str(coin_count), True, (255, 255, 255))
    game_display.blit(text_image, (720, 60))


def draw_car():
    global distance
    game_display.blit(car.sprite, (335 + car.x * 75, car.y))


def draw_other_car():
    global other_car, score

    for idx in range(len(other_cars)):
        if other_cars[idx].visible == 1:
            # машинка есть и едет
            game_display.blit(
                other_cars[idx].sprite,
                (335 + other_cars[idx].x * 75,
                 other_cars[idx].y))
            other_cars[idx].y += world_speed + \
                                 accelerate - other_cars[idx].speed

        else:
            rnd = random.randint(0, 300)
            if rnd == 1:
                # машинки нет и мы создаем ее заново
                car_x = random.randint(0, 1)
                if car_x == 0:
                    other_cars[idx] = OtherCar1()
                else:
                    other_cars[idx] = OtherCar2()
                other_cars[idx].visible = 1
        # условие исчезновения автомобиля
        if other_cars[idx].y > display_h + 300:
            if other_cars[idx].visible == 1:
                score += 100
                other_cars[idx].visible = 0


def process_keyboard(event):
    global accelerate, game_over, hp, max_hp, fuel, max_fuel, VICTORY, distance, score, Start
    if not game_over and not VICTORY:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                car.x = 0
            if event.key == pygame.K_RIGHT:
                car.x = 1
            if event.key == pygame.K_UP:
                accelerate += 2
                if accelerate > 100:
                    accelerate = 10
            if event.key == pygame.K_SPACE:
                accelerate = 0
    if event.type == pygame.KEYDOWN:
        if game_over:
            if event.key == pygame.K_SPACE:
                hp = max_hp
                fuel = max_fuel
                game_over = False
                world_speed = 7
                accelerate = 1
        if VICTORY:
            if event.key == pygame.K_SPACE:
                hp = max_hp
                fuel = max_fuel
                VICTORY = False
                world_speed = 7
                accelerate = 1
                distance = 0
                score = 0
        if Start:
            if event.key == pygame.K_SPACE:
                hp = max_hp
                fuel = max_fuel
                Start = False
                world_speed = 7
                accelerate = 1
                distance = 0
                score = 0


def game_loop(update_time):
    global game_exit, boost_active_check
    while not game_exit:
        for event in pygame.event.get():
            process_keyboard(event)
            if event.type == pygame.QUIT:
                game_exit = True

        # Функции поведения
        check_collision()

        # Функции отрисовки
        draw_background()
        draw_car()
        draw_ui()
        hp_check()
        fuel_check()
        victory()
        if not Start:
            draw_other_car()
            level()
            boost()
            coIn()
            GAME_OVER()
        start()
        pygame.display.update()
        clock.tick(update_time)


if __name__ == '__main__':
    game_loop(120)
    pygame.quit()
