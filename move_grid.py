from manim import *

# class MovingGroupToDestination(Scene):
#     def construct(self):
#         group = VGroup(Dot(LEFT), Dot(ORIGIN), Dot(RIGHT, color=RED), Dot(2 * RIGHT)).scale(1.4)
#         dest = Dot([4, 3, 0], color=YELLOW)
#         self.add(group, dest)
#         self.play(group.animate.shift(dest.get_center() - group[2].get_center()))
#         self.wait(0.5)

from manim import *

class MovingGrid(Scene):
    # def construct(self):
    #     dots = self.create_grid(6, 6)
    #     #lines = self.create_lines(dots)

    #     Move the entire VGroup from left to right
    #     self.play(dots.animate.shift(RIGHT * 5), run_time=3)
    #     self.wait()

    def construct(self):

        # Title
        title = Text("Moving the Grid")  # Use Text instead of a plain string
        basel = Text("Wind effect")

        # Arrange title in the upper left corner
        #title.to_corner(UL)

        VGroup(title).arrange(UP)  # Adjust buff according to your preference
        self.play(
           # Write(title),
            FadeOut(title, shift= DOWN),
           # Write(basel, shift=UP),
        )
        self.wait()

        dots = self.create_grid(4, 4)
        dots.move_to(ORIGIN)
        # Calculate the vector pointing from the lower left corner to the upper right
        diagonal_vector = RIGHT * 3 + DOWN * 2

        # Animate the dots from the lower left corner to the upper right
        self.play(dots.animate.move_to(diagonal_vector), run_time=3)

        rows, cols = 4, 4
        height, width = 6, 6

        # Add text in the top-left corner
        apply_weights_text = Text("Apply Weights").to_corner(UL)
        self.play(Write(apply_weights_text))

        # Draw a bell curve under the title
        bell_curve = self.create_bell_curve().next_to(apply_weights_text, DOWN, buff=0.5)
        self.play(Create(bell_curve))


        # diagonal_vector = RIGHT * 4 + UP * 2
        # self.play(dots.animate.move_to(diagonal_vector), run_time=2)
        for col in range(3, -1, -1):
            for row in range(rows):
                print("col:", col, " | row", row)
                dot = dots[row * cols + col]
                self.play(
                    Create(dot),
                    Flash(dot, flash_radius=0.1, line_length=0.2, color=WHITE),
                    run_time=0.5
                )
                self.wait(0.1)  # Adjust the wait time as needed

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


    def create_bell_curve(self):
        bell_curve = ParametricFunction(
            lambda t: np.array([t, 1.5 * np.exp(-0.5 * (t - 2)**2), 0]),
            t_range=[-1, 5],
            color=YELLOW,
            stroke_width=2,
        )
        bell_curve.scale(0.6)
        return bell_curve
