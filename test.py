from manim import *
import numpy as np

class Example(Scene):
    def construct(self):
        formula = MathTex(r"\int_{2}^{3} x^{2}",
                          color = BLUE,
                          font_size = 80)
        self.play(Write(formula))
        self.wait(10)