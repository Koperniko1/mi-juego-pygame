import pygame
import sys
import random     

# Inicializa pygame
pygame.init()

# Configuración de la pantalla
ANCHO, ALTO = 700, 700
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mi Juego")

# Colores
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)  # Color para la puntuación

# Configuración del personaje
tamaño_personaje = 50
posicion_personaje_x = ANCHO // 2 - tamaño_personaje // 2
posicion_personaje_y = ALTO // 2 - tamaño_personaje // 2

# Física del personaje
gravedad = 0.5
velocidad_y = 0
impulso_salto = -8   # Fuerza del salto cuando se presiona la barra espaciadora

# Limites de pantalla
limite_suelo = ALTO - tamaño_personaje
limite_techo = 0  # La posición en Y del techo

# Configuración de obstáculos
ancho_obstaculo = 50
altura_obstaculo = ALTO  # La altura del obstáculo es igual a la altura de la pantalla
tamano_agujero = 150  # Altura del agujero
posicion_obstaculo_x = ANCHO  # Comienzan fuera de la pantalla, a la derecha
posicion_agujero_y = random.randint(0, ALTO - tamano_agujero)  # Inicializar la posición del agujero

# Inicializar puntuación
conteo_cruces = 0  # Contador de cruces
puntuacion = 0  # Puntuación total
puntuacion_maxima = 0  # Variable para almacenar el récord


# Variable para controlar si ya se cruzó el agujero
ya_cruzado = False

def manejar_colisiones(personaje_rect, obstaculos):
    for obstaculo in obstaculos:
        if personaje_rect.colliderect(obstaculo):
            game_over()  # Llamar a la función game_over cuando el personaje colisione

def actualizar_record(puntuacion):
    global puntuacion_maxima  # Modificar la puntuación máxima globalmente
    if puntuacion > puntuacion_maxima:
        puntuacion_maxima = puntuacion  # Actualizar el récord
        print("¡Nuevo récord establecido!")  # Mensaje de depuración
        return True  # Retornar True si hay nuevo récord
    return False  # Retornar False si no hay nuevo récord

def game_over():
    global conteo_cruces  # Asegúrate de usar la variable global correcta
    global puntuacion  # Asegúrate de usar la puntuación global

    # Actualizar la puntuación final
    puntuacion = conteo_cruces * 10
    print(f"Puntuación final: {puntuacion}")  # Mensaje de depuración

    # Verificar si se ha establecido un nuevo récord
    nuevo_record = actualizar_record(puntuacion)  # Esto debe devolver True si es un nuevo récord
    print(f"¿Nuevo récord?: {nuevo_record}")  # Mensaje de depuración

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    main_game()  # Reiniciar el juego si se presiona ESPACIO
                    return  # Salir de la función game_over para reiniciar el juego
                else:
                    pygame.quit()
                    sys.exit()  # Cerrar el juego para cualquier otro input

        fuente = pygame.font.SysFont(None, 48)

        pantalla.fill(BLANCO)  # Rellenar la pantalla con color blanco

        if nuevo_record:
            texto_felicidades = fuente.render("¡Nuevo Récord! ¡Felicidades!", True, ROJO)
            texto_puntuacion = fuente.render(f"Puntuación: {puntuacion}", True, ROJO)
            pantalla.blit(texto_felicidades, (ANCHO // 2 - texto_felicidades.get_width() // 2, ALTO // 2 - texto_felicidades.get_height() // 2 - 20))
            pantalla.blit(texto_puntuacion, (ANCHO // 2 - texto_puntuacion.get_width() // 2, ALTO // 2 + texto_felicidades.get_height() // 2))
        else:
            texto_game_over_1 = fuente.render("Perdiste,", True, ROJO)
            texto_game_over_2 = fuente.render("presiona ESPACIO para jugar de nuevo", True, ROJO)
            pantalla.blit(texto_game_over_1, (ANCHO // 2 - texto_game_over_1.get_width() // 2, ALTO // 2 - texto_game_over_1.get_height() // 2 - 10))
            pantalla.blit(texto_game_over_2, (ANCHO // 2 - texto_game_over_2.get_width() // 2, ALTO // 2 + texto_game_over_1.get_height() // 2))

        # Mostrar el récord actual
        texto_record_actual = fuente.render(f"Récord: {puntuacion_maxima}", True, AZUL)
        pantalla.blit(texto_record_actual, (ANCHO - texto_record_actual.get_width() - 10, 10))

        pygame.display.flip()

def actualizar_puntuacion(personaje_rect, agujero_rect):
    global conteo_cruces, ya_cruzado  # Usar variables globales
    
    # Verificar si el personaje ha cruzado el agujero
    if personaje_rect.right > agujero_rect.left and personaje_rect.left < agujero_rect.right:
        if personaje_rect.bottom > agujero_rect.top and personaje_rect.top < agujero_rect.bottom:
            if not ya_cruzado:  # Solo contar si no se ha cruzado antes
                conteo_cruces += 1  # Incrementar el contador de cruces
                ya_cruzado = True  # Marcar que se ha cruzado el agujero
                actualizar_record(conteo_cruces * 10)  # Actualizar el récord
                return True  # Indicar que se cruzó el agujero
    else:
        ya_cruzado = False  # Resetear si el personaje no está cruzando el agujero
    return False  # Indicar que no se cruzó


def pantalla_bienvenida():
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    return  # Salir de la pantalla de bienvenida cuando se presiona la barra espaciadora
        
        pantalla.fill(BLANCO)
        fuente = pygame.font.SysFont(None, 48)
        texto_bienvenido = fuente.render("Bienvenido", True, NEGRO)
        texto_presiona = fuente.render("presiona ESPACIO para comenzar", True, NEGRO)
        pantalla.blit(texto_bienvenido, (ANCHO // 2 - texto_bienvenido.get_width() // 2, ALTO // 2 - texto_bienvenido.get_height() // 2 - 10))
        pantalla.blit(texto_presiona, (ANCHO // 2 - texto_presiona.get_width() // 2, ALTO // 2 + texto_bienvenido.get_height() // 2))
        pygame.display.flip()

def main_game():
    global posicion_personaje_y, velocidad_y, posicion_obstaculo_x, posicion_agujero_y, conteo_cruces, puntuacion, ya_cruzado
    
    # Reiniciar las variables del juego
    posicion_personaje_y = ALTO // 2 - tamaño_personaje // 2
    velocidad_y = 0
    posicion_obstaculo_x = ANCHO
    posicion_agujero_y = random.randint(0, ALTO - tamano_agujero)
    conteo_cruces = 0
    puntuacion = 0
    ya_cruzado = False

    while True:
        # Manejo de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    # Aplicar un impulso hacia arriba cuando se presiona la barra espaciadora
                    velocidad_y = impulso_salto

        # Aplicar gravedad
        velocidad_y += gravedad
        posicion_personaje_y += velocidad_y

        # Limitar el personaje al suelo
        if posicion_personaje_y >= limite_suelo:
            posicion_personaje_y = limite_suelo
            velocidad_y = 0  # Detener la caída cuando llega al suelo

        # Limitar el personaje al techo
        if posicion_personaje_y <= limite_techo:
            posicion_personaje_y = limite_techo
            velocidad_y = 0  # Detener el movimiento hacia arriba cuando llega al techo

        # Mover el obstáculo hacia la izquierda
        posicion_obstaculo_x -= 5   # Velocidad del obstáculo

        # Resetear el obstáculo cuando sale de la pantalla
        if posicion_obstaculo_x < -ancho_obstaculo:
            posicion_obstaculo_x = ANCHO
            posicion_agujero_y = random.randint(0, ALTO - tamano_agujero)  # Generar nueva posición para el agujero
            ya_cruzado = False  # Resetear el estado al crear un nuevo agujero

        # Verificar colisiones
        personaje_rect = pygame.Rect(posicion_personaje_x, int(posicion_personaje_y), tamaño_personaje, tamaño_personaje)
        
        # Crear los rectángulos de los obstáculos
        agujero_rect = pygame.Rect(posicion_obstaculo_x, posicion_agujero_y, ancho_obstaculo, tamano_agujero)  # Rectángulo del agujero

        obstaculo_superior_rect = pygame.Rect(posicion_obstaculo_x, 0, ancho_obstaculo, posicion_agujero_y)  # Parte superior del obstáculo
        obstaculo_inferior_rect = pygame.Rect(posicion_obstaculo_x, posicion_agujero_y + tamano_agujero, ancho_obstaculo, altura_obstaculo - (posicion_agujero_y + tamano_agujero))  # Parte inferior del obstáculo

        # Llamar a la función de manejo de colisiones
        manejar_colisiones(personaje_rect, [obstaculo_superior_rect, obstaculo_inferior_rect])

        # Actualizar puntuación
        cruzo_agujero = actualizar_puntuacion(personaje_rect, agujero_rect)
        if cruzo_agujero:
            puntuacion = conteo_cruces * 10  # Actualizar la puntuación total

        # Rellenar la pantalla con el color blanco
        pantalla.fill(BLANCO)

        # Dibujar la barrera
        pygame.draw.rect(pantalla, NEGRO, obstaculo_superior_rect)  # Dibuja la parte superior del obstáculo
        pygame.draw.rect(pantalla, NEGRO, obstaculo_inferior_rect)  # Dibuja la parte inferior del obstáculo

        # Dibujar el personaje (debe dibujarse al final)
        pygame.draw.rect(pantalla, ROJO, (posicion_personaje_x, int(posicion_personaje_y), tamaño_personaje, tamaño_personaje))

        # Dibujar la puntuación y el récord
        fuente = pygame.font.SysFont(None, 36)
        texto_puntuacion = fuente.render(f"Puntuación: {puntuacion}", True, AZUL)
        texto_record = fuente.render(f"Récord: {puntuacion_maxima}", True, AZUL)
        pantalla.blit(texto_puntuacion, (10, 10))  # Mostrar la puntuación
        pantalla.blit(texto_record, (10, 50))      # Mostrar el récord en otra posición


        # Actualizar la pantalla
        pygame.display.flip()
        pygame.time.Clock().tick(60)  # Limitar a 45 FPS

# Mostrar la pantalla de bienvenida
pantalla_bienvenida()

# Iniciar el juego
main_game()