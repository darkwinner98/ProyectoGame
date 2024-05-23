# -*- coding: utf-8 -*-
"""
Created on Thu May 23 16:35:47 2024

@author: darwi
"""

# Mi Juego con PyGame

## Descripción

Este es un juego simple creado con PyGame. El objetivo del juego es evitar a los enemigos que caen desde la parte superior de la pantalla y conseguir la mayor puntuación posible.

## Funcionalidad

- **Menú Principal**: Al iniciar el juego, se muestra el menú principal. Presiona cualquier tecla para comenzar el juego.
- **Juego Principal**: Controla al jugador con las teclas de flecha izquierda y derecha. Evita a los enemigos que caen y gana puntos cada vez que un enemigo sale de la pantalla.
- **Puntuación**: La puntuación se muestra en la parte superior de la pantalla durante el juego.

## Instrucciones

1. Instalar Pygame si no lo tienes: `pip install pygame`.
2. Ejecutar el archivo `main.py` para iniciar el juego.

## Funciones Personalizadas

- `draw_text(text, font, color, surface, x, y)`: Dibuja texto en la pantalla.
- `main_menu()`: Muestra el menú principal.
- `game_loop()`: Ejecuta el bucle principal del juego.
