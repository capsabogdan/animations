from manim import *

# class MovingGroupToDestination(Scene):
#     def construct(self):
#         group = VGroup(Dot(LEFT), Dot(ORIGIN), Dot(RIGHT, color=RED), Dot(2 * RIGHT)).scale(1.4)
#         dest = Dot([4, 3, 0], color=YELLOW)
#         self.add(group, dest)
#         self.play(group.animate.shift(dest.get_center() - group[2].get_center()))
#         self.wait(0.5)

from manim import *

class MovingDots(Scene):
    # def construct(self):
    #     dots = self.create_grid(6, 6)
    #     #lines = self.create_lines(dots)

    #     # Move the entire VGroup from left to right
    #     self.play(dots.animate.shift(RIGHT * 5), run_time=3)
    #     self.wait()

    def construct(self):
        dots = self.create_grid(6, 6)
        # Calculate the center of the dots
        center_of_dots = dots.get_center()
        # Shift the dots to make the center coincide with the origin
        self.play(dots.animate.shift(-center_of_dots * 2), run_time=1)
        self.wait()

    def create_grid(self, rows, cols, spacing=1):
        dots = VGroup()
        for i in range(rows):
            for j in range(cols):
                dot = Dot().move_to([i, j, 0])
                dots.add(dot)
        self.add(dots)
        return dots

    def create_lines(self, dots):
        lines = VGroup()
        for i in range(len(dots) - 1):
            line = Line(dots[i].get_center(), dots[i + 1].get_center()).set_color(RED)
            lines.add(line)
        self.add(lines)
        return lines

