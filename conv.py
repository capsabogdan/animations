from manim import *

class ConvolutionExample(Scene):
    def construct(self):
        # Define input signal and kernel
        input_signal = [1, 2, -1, 3]
        kernel = [0.5, -1]

        # Create Manim Text objects to display input and kernel
        input_text = Text("Input Signal:").to_edge(UP)
        kernel_text = Text("Kernel:").to_edge(UP).shift(2 * DOWN)

        input_array = MathTex(*input_signal).next_to(input_text, DOWN, aligned_edge=LEFT)
        kernel_array = MathTex(*kernel).next_to(kernel_text, DOWN, aligned_edge=LEFT)

        # Display input signal and kernel
        self.play(
            Write(input_text),
            Write(kernel_text),
            Write(input_array),
            Write(kernel_array),
        )
        self.wait()

        # Convolve input signal with the kernel
        result = [sum(input_signal[i:i+len(kernel)]) for i in range(len(input_signal)-len(kernel)+1)]

        # Create Manim Text object to display convolution result
        result_text = Text("Result of Convolution:").to_edge(UP).shift(4 * DOWN)
        result_array = MathTex(*result).next_to(result_text, DOWN, aligned_edge=LEFT)

        # Display convolution result
        self.play(
            Write(result_text),
            Write(result_array),
        )
        self.wait()
