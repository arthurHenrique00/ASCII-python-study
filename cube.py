import os
import math
import time
import shutil

def draw_cube(A, B, width, height):
    output = [" "] * (width * height)
    zbuffer = [0] * (width * height)

    # Definindo os vértices do cubo (8 pontos)
    vertices = [
        [-1, -1, -1],
        [1, -1, -1],
        [1, 1, -1],
        [-1, 1, -1],
        [-1, -1, 1],
        [1, -1, 1],
        [1, 1, 1],
        [-1, 1, 1]
    ]
    
    # Definindo as arestas que conectam os vértices
    edges = [
        [0, 1], [1, 2], [2, 3], [3, 0],  # Frente
        [4, 5], [5, 6], [6, 7], [7, 4],  # Trás
        [0, 4], [1, 5], [2, 6], [3, 7]   # Conexões entre frente e trás
    ]
    
    # Para cada vértice, aplicamos a rotação 3D
    rotated_vertices = []
    for vertex in vertices:
        x, y, z = vertex
        
        # Rotação ao redor do eixo X
        x_rot = x * math.cos(A) - z * math.sin(A)
        z_rot = x * math.sin(A) + z * math.cos(A)
        x, z = x_rot, z_rot
        
        # Rotação ao redor do eixo Y
        y_rot = y * math.cos(B) - z * math.sin(B)
        z_rot = y * math.sin(B) + z * math.cos(B)
        y, z = y_rot, z_rot
        
        # Armazenar as coordenadas rotacionadas
        rotated_vertices.append([x, y, z])

    # Projeção dos vértices 3D para 2D
    for edge in edges:
        x1, y1, z1 = rotated_vertices[edge[0]]
        x2, y2, z2 = rotated_vertices[edge[1]]

        # Projeção simples em perspectiva
        p1_x = int(width / 2 + width * x1 / (z1 + 5))
        p1_y = int(height / 2 + height * y1 / (z1 + 5))
        p2_x = int(width / 2 + width * x2 / (z2 + 5))
        p2_y = int(height / 2 + height * y2 / (z2 + 5))

        # Desenhando as arestas do cubo
        if 0 <= p1_x < width and 0 <= p1_y < height:
            output[p1_y * width + p1_x] = "#"
        if 0 <= p2_x < width and 0 <= p2_y < height:
            output[p2_y * width + p2_x] = "#"

    return output

def animate_cube():
    # Obtém o tamanho do terminal
    cols, rows = shutil.get_terminal_size()
    width = cols - 1
    height = rows - 1

    A = 0  # Inicializa o ângulo de rotação ao redor do eixo X
    B = 0  # Inicializa o ângulo de rotação ao redor do eixo Y

    while True:
        # Limpa o terminal
        os.system("cls" if os.name == "nt" else "clear")
        
        # Desenha o cubo
        output = draw_cube(A, B, width, height)

        # Exibe o cubo no terminal
        print("\n".join("".join(output[i:i + width]) for i in range(0, len(output), width)))

        # Atualiza os ângulos para girar
        A += 0.05
        B += 0.05

        # Pausa para animação
        time.sleep(0.03)

# Inicia a animação
animate_cube()
