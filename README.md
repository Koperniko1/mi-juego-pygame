# Mi Juego en Python con Pygame

¡Bienvenido a **Mi Juego**! Este es un sencillo pero desafiante juego de obstáculos desarrollado en Python usando la biblioteca **Pygame**. La meta del juego es evitar las colisiones con los obstáculos mientras tu personaje cruza los espacios vacíos, acumulando puntos en el proceso.

## Características del juego
- **Física de salto**: Controla a tu personaje y úsalo para cruzar obstáculos movibles con gravedad e impulso de salto.
- **Sistema de puntuación y récord**: Gana puntos cada vez que cruzas un obstáculo exitosamente, y trata de superar tu récord anterior.
- **Pantalla de bienvenida**: La pantalla inicial ofrece una bienvenida al jugador antes de comenzar el juego.
- **Colisiones**: Si el personaje colisiona con un obstáculo, el juego termina.
- **Pantalla de game over**: Permite reiniciar el juego con la tecla `ESPACIO` o cerrar la ventana.

## Instrucciones de juego
1. **Salta** a través de los obstáculos presionando la tecla `ESPACIO`.
2. Evita los obstáculos superiores e inferiores para **acumular puntos**.
3. ¡Sigue jugando y tratando de **superar tu récord**!

## Controles
- **Espacio**: Salta
- **Cerrar ventana**: Termina el juego

## Requisitos
- Python 3.x
- Biblioteca `pygame`

## Instalación
1. Clona este repositorio en tu máquina local:
    ```bash
    git clone https://github.com/tu-usuario/mi-juego.git
    ```
2. Navega al directorio del juego:
    ```bash
    cd mi-juego
    ```
3. Instala las dependencias con:
    ```bash
    pip install pygame
    ```

## Ejecución
Para iniciar el juego, ejecuta el archivo principal con el siguiente comando:
```bash
python game.py
