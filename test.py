from manim import *
import numpy as np

from manim import *

class RotationDemo(Scene):
    def construct(self):
        # --- Rotation Matrix (Plain Text, NO LATEX) ---
        matrix_text = Text(
            "[[ cos(theta), -sin(theta) ],\n [ sin(theta),  cos(theta) ]]",
            font_size=32
        )
        matrix_text.to_corner(UL)

        # --- A Square Robot ---
        robot = Square(side_length=2, color=BLUE)
        robot.set_fill(BLUE, opacity=0.4)

        self.play(FadeIn(matrix_text), FadeIn(robot))

        # --- Rotate Robot While Updating Matrix ---
        angle_tracker = ValueTracker(0)

        # Updated matrix display (pure text)
        def update_matrix(m):
            theta = angle_tracker.get_value()
            m.text = (
                f"[[ {np.cos(theta): .2f}, { -np.sin(theta): .2f} ],\n"
                f" [ {np.sin(theta): .2f}, {  np.cos(theta): .2f} ]]"
            )
            m.become(Text(m.text, font_size=32).to_corner(UL))

        matrix_text.add_updater(update_matrix)

        # Rotate the robot 360 degrees
        self.play(
            angle_tracker.animate.set_value(TAU),
            Rotate(robot, angle=TAU, run_time=5),
        )

        matrix_text.remove_updater(update_matrix)
        self.wait()



class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen