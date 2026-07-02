from manim import *
import numpy as np

class SectorScene(Scene):
    def construct(self):
        sector = Sector(radius=3.0, angle=60*DEGREES)

        shift = np.array([-1.5, -0.7, 0])

        sector.shift(shift)

        arc = Arc(angle=60*DEGREES)

        arc.shift(shift)

        arc.set_color(PINK)
        
        sector.set_color(BLUE)

        s = MathTex("s").move_to([2.9, 1.6, 0]).shift(shift)
        r = MathTex("r").move_to([1.5,-0.3,0]).shift(shift)
        theta = MathTex(r"\theta").move_to([1.1, 0.7, 0]).shift(shift)

        circumference = MathTex(r"C=2\pi r").move_to([-0.5, 2, 0]).shift(shift)

        arc_length = MathTex(r"s=\frac{\theta}{2\pi}\cdot 2\pi r").move_to([1.5,-1.7, 0]).shift(shift)

        slash = Line([2.7, 0.7, 0], [1, 0, 0],
                     color = RED).move_to(arc_length.get_center()).shift(RIGHT*0.2, DOWN*0.2)

        # self.add_sound("in depth vid 14.m4a")

        self.wait(0.7)
        self.play(Create(sector), 
                  run_time = 0.5)
        
        self.wait(0.8)

        self.play(Create(r))

        self.play(Create(arc),
                  run_time = 0.3)

        self.play(Create(theta))

        self.wait(1)

        self.play(Create(s))

        self.wait(2.3)

        self.play(Create(circumference), 
                  run_time = 0.5,
                  rate_func = linear)
        
        self.wait(1)
        
        self.play(Create(arc_length),
                  run_time = 1.5,
                  rate_func = linear)
        
        self.wait(3)
        
        self.play(Create(slash),
                  run_time = 0.2)
        
        self.wait(1)

        self.play(FadeOut(arc_length, slash),
                  run_time = 0.4)

        arc_length = MathTex(r"s=r\theta").shift(arc_length.get_center())

        self.play(Create(arc_length),
                  run_time = 0.5,
                  rate_func = linear)

        self.wait(1.4)

        self.play(*[FadeOut(mob) for mob in self.mobjects], 
                  run_time = 0.7)

