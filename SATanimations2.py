 
from manim import *
from manimpango import list_fonts
config.background_color = WHITE
class math(Scene):
    def construct(self): 
        # function notation
        functionText = MathTex("f(", "x", ")", "=5","x","+4", color=BLACK, stroke_width=3).set_height(0.9)
        functionUpdate = MathTex("f(", "3", ")", "=5","(","3",")","+4", color=BLACK, stroke_width=3).set_height(0.9)
        functionUpdate[1].set_color(RED)
        functionUpdate[5].set_color(RED)
        # function = MathTex(r"=5x+4").next_to(functionText, RIGHT).set_height(0.7)
        arrow = Arrow(start=LEFT, end=RIGHT, stroke_width=4, color=RED).next_to(functionText, LEFT)
        arrow2 = Arrow(start=LEFT, end=RIGHT, stroke_width=4, color=RED, buff=0.2).next_to(functionText, RIGHT)
        input = MathTex("3", color=RED).set_height(0.7).next_to(arrow, LEFT).shift(LEFT*0.1)
        output = MathTex("19", color=RED).set_height(0.7).next_to(arrow2, RIGHT).shift(RIGHT*0.1)
        box = SurroundingRectangle(input, color=RED, stroke_width=4, buff=0.2)
        box2 = SurroundingRectangle(output, color=RED, stroke_width=4, buff=0.2)
        # self.add(axes) 
        self.play(Write(functionText), run_time=3)
        # self.play(Write(function))
        self.play(Write(input), run_time=2)
        self.play(Write(box))
        self.play(Write(arrow),run_time=0.2)
        # self.wait(0.4)
        #change to 3
        self.play(FadeOut(functionText), run_time=0.05)
        self.play(FadeIn(functionUpdate), runtime=0.05)
        # y value
        self.play(Write(arrow2),run_time=0.2)
        self.play(Write(output), run_time=0.2)
        self.play(Write(box2), run_time=0.2)
        # Fade out
        self.play(FadeOut(arrow, arrow2, input, output, box, box2, functionUpdate), run_time=0.4)
        #exponents Rules
        multiplying = MathTex(r"x^a*x^b=x^{a+b}", color=BLACK, stroke_width=3).set_height(1.2)
        dividing = MathTex(r"\frac{x^a}{x^b}=x^{a-b}", color=BLACK, stroke_width=3).set_height(2.5)
        powertopower = MathTex(r"(x^a)^b=x^{ab}", color=BLACK, stroke_width=3).set_height(1.2)
        negative = MathTex(r"x^{-a}=\frac{1}{x^a}", color=BLACK, stroke_width=3).set_height(2.5)
        self.wait(1.4)
        self.play(Write(multiplying))
        self.wait(1)
        self.play(FadeOut(multiplying))
        self.play(Write(dividing))
        self.wait(1)
        self.play(FadeOut(dividing))
        self.play(Write(powertopower))
        self.wait(1)
        self.play(FadeOut(powertopower))
        self.play(Write(negative))
        self.wait(1)
        self.play(FadeOut(negative))






