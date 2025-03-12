from manim import *
config.background_color = WHITE
class exponent(Scene):
    def construct(self):
        # 1st scene
        exponent = MathTex(r"a", r"^n", color=BLACK, stroke_width=3.5).set_height(1.5)
        self.play(Write(exponent), run_time=1.5)
        box = SurroundingRectangle(exponent[1], color=RED, stroke_width=6, buff=0.1)
        box2 = SurroundingRectangle(exponent[0], color=RED, stroke_width=6, buff=0.1)
        self.play(FadeIn(box))
        self.play(FadeOut(box))
        self.play(FadeIn(box2))
        self.play(FadeOut(box2))
        # 2nd scene
        self.play(exponent[0].animate.set_color(RED).scale(1.2),run_time=1)
        self.play(exponent[0].animate.set_color(BLACK).scale(1/1.2),run_time=1.3)
        self.play(exponent[1].animate.set_color(RED).scale(1.2).set_text("4"),run_time=1)
        self.play(exponent[1].animate.set_color(BLACK).scale(1/1.2),run_time=1)
        self.play(exponent.animate.shift(LEFT*3))
        ex = MathTex(r"=",r"a*a*a*a", color=BLACK, stroke_width=3.5).set_height(0.5).next_to(exponent)
        self.play(Write(ex))
        brace = Brace(ex[1], color=BLACK, direction=DOWN) 
        n_text = MathTex("n", color=BLACK, stroke_width=2).next_to(brace, DOWN).set_height(0.4)
        self.play(Write(brace))
        self.play(Write(n_text))
        self.play(FadeOut(n_text, brace, ex, exponent))
        # 3rd scene
        zero = MathTex(r"a^0=1", color=BLACK, stroke_width=3.5).set_height(1.5)
        self.play(Write(zero), run_time=2)
        self.play(zero.animate.shift(LEFT*3), run_time=2)
        one = MathTex(r"a^1=a", color=BLACK, stroke_width=3.5).set_height(1.5).shift(RIGHT*3)
        self.play(Write(one) ,run_time=3)
        self.wait(2)
        self.play(FadeOut(one,zero))
        #exponents Rules
        multiplying = MathTex(r"x^a*x^b=x^{a+b}", color=BLACK, stroke_width=3).set_height(1.2)
        dividing = MathTex(r"\frac{x^a}{x^b}=x^{a-b}", color=BLACK, stroke_width=3).set_height(2.5)
        powertopower = MathTex(r"(x^a)^b=x^{a*b}", color=BLACK, stroke_width=3).set_height(1.2)
        negative = MathTex(r"x^{-a}=\frac{1}{x^a}", color=BLACK, stroke_width=3).set_height(2.5)
        squareroot = MathTex(r"a^{\frac{b}{c}}=\sqrt[n]{a^b}", color=BLACK, stroke_width=3).set_height(1.5)
        agrument = MathTex(r"(ab)^n=a^n*b^n", color=BLACK, stroke_width=3).set_height(1.3)
        self.play(Write(negative))
        self.wait(4)
        self.play(FadeOut(negative))
        self.play(Write(squareroot))
        self.wait(7)
        self.play(FadeOut(squareroot))
        self.play(Write(multiplying))
        self.wait(2)
        self.play(FadeOut(multiplying))
        self.play(Write(dividing))
        self.wait(2)
        self.play(FadeOut(dividing))
        self.play(Write(powertopower))
        self.wait(2)
        self.play(FadeOut(powertopower))
        self.play(Write(agrument))
        self.wait(6)
        self.play(FadeOut(agrument))


        


