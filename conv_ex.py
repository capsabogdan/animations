from manim import *

class ConvolutionAnimation(Scene):
    def construct(self):
        # Create a grid representing an image
        image_grid = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]

        # Create a kernel
        kernel = [
            [1, 0],
            [0, -1]
        ]

        # Display the image grid
        image_grid_tex = MathTex(
            "\\begin{bmatrix} 1 & 2 & 3 & 4 \\\\ 5 & 6 & 7 & 8 \\\\ 9 & 10 & 11 & 12 \\\\ 13 & 14 & 15 & 16 \\end{bmatrix}"
        ).to_edge(UP)

        self.play(Write(image_grid_tex))
        self.wait()

        # Display the kernel
        kernel_tex = MathTex(
            "\\begin{bmatrix} 1 & 0 \\\\ 0 & -1 \\end{bmatrix}"
        ).next_to(image_grid_tex, DOWN, aligned_edge=LEFT)

        self.play(Write(kernel_tex))
        self.wait()

        # Move the kernel over the image and perform convolution
        result_grid = [[0, 0, 0, 0] for _ in range(4)]

        for i in range(3):
            for j in range(3):
                # Highlight the current position of the kernel
                kernel_tex_copy = kernel_tex.copy().shift(i * RIGHT + j * DOWN)
                self.play(Create(kernel_tex_copy), run_time=0.3)
                self.wait()

                # Perform convolution at the current position
                for m in range(2):
                    for n in range(2):
                        result_grid[i + m][j + n] += image_grid[i + m][j + n] * kernel[m][n]

                # Unhighlight the current position
                self.play(FadeOut(kernel_tex_copy), run_time=0.3)
                self.wait()

        # Display the result of convolution
        result_grid_tex = MathTex(
            "\\begin{bmatrix} {} & {} & {} & {} \\\\ {} & {} & {} & {} \\\\ {} & {} & {} & {} \\\\ {} & {} & {} & {} \\end{bmatrix}"
        ).next_to(kernel_tex, DOWN, aligned_edge=LEFT)

        for i in range(4):
            for j in range(4):
                result_grid_tex[0][4 * i + j].animate.set_value(result_grid[i][j])

        self.play(Write(result_grid_tex))
        self.wait()

        # Clean up
        self.play(FadeOut(image_grid_tex), FadeOut(kernel_tex), FadeOut(result_grid_tex))
        self.wait()
