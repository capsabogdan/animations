from manim import *


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(GRAY, opacity=0.5)  # set the color and transparency
        circle.set_stroke(WHITE, width=2)  # set the border color to white and width
        self.play(Create(circle))  # show the circle on screen