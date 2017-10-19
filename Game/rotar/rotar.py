# coding=utf-8

# provee funcionalidad dependiente del sistema operativo
import os

# importa la librería Pygame
import pygame

# colores
black = (0, 0, 0)


def main():
    # inicializa Pygame
    pygame.init()

    # establece el título de la ventana
    window_title = u'Rotar imagen mejorado'
    pygame.display.set_caption(window_title)

    # establece el tamaño de la ventana
    window_size = (400, 400)
    screen = pygame.display.set_mode(window_size)

    # obtiene el rectángulo que ocupa la pantalla
    screen_rect = screen.get_rect()

    # obtiene el centro de la pantalla
    screen_center = screen_rect.center

    # carga una imagen
    image = pygame.image.load(os.path.join('imagenes', 'logo_pygame.png'))

    # convierte la imagen al mismo formato que la pantalla para dibujarla más rápido
    image = image.convert_alpha()

    # copiar imagen
    image_copy = image.copy()

    # ángulo de rotación
    rotation_angle = 0

    # crea un reloj
    clock = pygame.time.Clock()

    # ¿la aplicación está ejecutándose?
    is_running = True

    # si la aplicación está ejecutándose
    while is_running:
        # limita las actualizaciones a 30 cuadros por segundo (FPS)
        clock.tick(30)

        # retorna todos los eventos de la cola de eventos
        for event in pygame.event.get():
            # si se presiona el botón 'cerrar' de la ventana
            if event.type == pygame.QUIT:
                # detiene la aplicación
                is_running = False

            # si se presiona alguna tecla
        if event.type == pygame.KEYDOWN:
            # si se presiona la tecla 'espacio'
            if event.key == pygame.K_LEFT:
                # aumenta el ángulo de rotación 45 grados sexagesimales
                rotation_angle += 50

                # mantiene el ángulo de rotación en el rango [0, 360)
                rotation_angle %= 360
                print u'ángulo rotado: {}°'.format(rotation_angle)

                # rota la imagen y la almacena en una copia
                image_copy = pygame.transform.rotate(image, rotation_angle)
            if event.key == pygame.K_RIGHT:
                rotation_angle -= 50
                rotation_angle %= 360
                print u'ángulo rotado: {}°'.format(rotation_angle)
                image_copy = pygame.transform.rotate(image,rotation_angle)
        # obtiene el rectángulo que ocupa de la imagen
        img_rect = image_copy.get_rect()
        # centra el rectángulo que ocupa la imagen en el centro de la pantalla
        img_rect.center = screen_center
        # establece el color de fondo
        screen.fill(black)

        # dibuja la imagen centrada
        screen.blit(image_copy, img_rect)

        # actualiza la pantalla
        pygame.display.flip()

    # finaliza Pygame
    pygame.quit()


if __name__ == '__main__':
    main()
