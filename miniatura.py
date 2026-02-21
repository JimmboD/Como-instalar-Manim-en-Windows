from manim import *
import numpy as np

class miniatura(Scene):
    def construct(self):
        # 1. Crear los ejes de referencia
        axes = Axes(
            x_range=[-6, 6, 1],
            y_range=[-6, 6, 1],
            x_length=10,
            y_length=10,
            axis_config={"color": WHITE, "stroke_width": 2},
        )

        # 2. Definir la función matemática del campo
        def calc_field(pos):
            x, y = pos[:2]
            
            # Condición de seguridad: evitar la división entre cero en el origen (0,0)
            if x == 0 and y == 0:
                return np.array([0, 0, 0])
            
            # Calculamos el denominador: (x^2 + y^2)^0.5
            denominator = np.sqrt(x**2 + y**2)
            
            # P(x,y) y Q(x,y)
            u = -y / denominator
            v = x / denominator
            
            return np.array([u, v, 0])

        # 3. Crear el campo vectorial en Manim
        vector_field = ArrowVectorField(
            calc_field,
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            color=YELLOW,
            length_func=lambda x: 0.5  # Mantiene el tamaño de las flechas uniforme visualmente
        )

        # 4. Animar la escena
        self.play(Create(axes), run_time=1.5)
        self.play(Create(vector_field), run_time=3)
        self.wait(2)