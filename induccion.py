from manim import *

class induccion(Scene):
    def construct(self):

        # Definimos dos ecuaciones
        eq0= MathTex(r"\frac{1}{4}Tronco =1Tablon")
        eq1 = MathTex(r"0+\frac{1}{4}Tronco =1Tablon")
        eq2 = MathTex(r"0+\frac{2}{4}Tronco =1Tablon")
        eq3 = MathTex(r"k=4q+r")
        eq4 = MathTex(r"r \in \{0,1,2,3\}")


        # Agregamos animación
        self.wait(3)
        self.play(Write(eq0))
        self.wait(3)
        self.play(ReplacementTransform(eq0,eq1))
        self.wait(3)
        self.play(ReplacementTransform(eq1,eq2))
        self.wait(3)
        self.play(ReplacementTransform(eq2,eq3))
        self.wait(5)
        self.play(ReplacementTransform(eq3,eq4))
        self.wait(5)