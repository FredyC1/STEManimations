from manim import *
from manimpango import list_fonts

print(list_fonts())  # Lists all available fonts

class test(Scene):
    def construct(self):
        text = MathTex("Hello", font='Comic Sans MS')
        self.play(Write(text))