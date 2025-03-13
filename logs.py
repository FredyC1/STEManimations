from manim import *
config.background_color = BLACK
class math(Scene):
    def construct(self): 
        exponent = MathTex(r"n^a", color=BLACK, stroke_width=3.5).set_height(2)
        exponent2 = MathTex(r"2",r"^3", color=BLACK, stroke_width=3.5).set_height(2)
        logsex = MathTex(r"2",r"^?",r"=8", color=BLACK, stroke_width=3.5).set_height(2)
        equals = MathTex(r"=","?", color=BLACK, stroke_width=3.5).set_height(2).shift(RIGHT*.8)
        equals[1].set_color(RED)
        logsex[1].set_color(RED)
        log = MathTex(r"\log_n x=a", color=BLACK, stroke_width=3.5).set_height(1.5)

        self.play(Transform(exponent,log), run_time=2.2)

        # 2 to the power of 3]
        self.play(FadeOut(exponent))
        self.play(FadeIn(exponent2))
        self.play(exponent2[0].animate.set_color(RED).scale(1.2),run_time=0.4)
        self.play(exponent2[0].animate.set_color(BLACK).scale(1/1.2),run_time=0.4)
        self.play(exponent2[1].animate.set_color(RED).scale(1.2).set_text("4"),run_time=0.4)
        self.play(exponent2[1].animate.set_color(BLACK).scale(1/1.2),run_time=0.4)
        self.play(exponent2.animate.shift(LEFT*2))
        self.play(Write(equals), run_time=0.2)
        # switch to 2 to the 
        self.play(Transform(exponent2, logsex), FadeOut(equals), run_time=2)
        self.wait(3)
        self.play(FadeOut(exponent2))
        log8 = MathTex(r"\log_2 8=?", color=BLACK, stroke_width=3.5).set_height(2)
        self.play(FadeIn(log8))
        self.play(FadeOut(log8))
        # Log Rules
        Product = MathTex("\\log_b(n \cdot m) = \\log_b n + \\log_b m", color=WHITE, stroke_width=3.5).set_height(1)
        Quotient = MathTex("\\log_b\\left(\\frac{n}{m}\\right) = \\log_b n - \\log_b m", color=WHITE, stroke_width=3.5).set_height(2)
        Power = MathTex("\\log_b(n^m) = m \\cdot \\log_b n", color=WHITE, stroke_width=3.5).set_height(1)
        move = MathTex("\\log m ^n = n \\log m", color=WHITE, stroke_width=3.5).set_height(1)
        base =  MathTex("\\log_b b = 1", color=WHITE, stroke_width=3.5).set_height(1)
        base1 = MathTex("\\log_b 1 = 0", color=BLACK, stroke_width=3.5).set_height(1)
        self.wait(2.2)
        self.play(FadeIn(Product))
        self.wait(1)
        self.play(FadeOut(Product))
        self.play(FadeIn(Quotient))
        self.wait(3)
        self.play(FadeOut(Quotient))
        self.play(FadeIn(move))
        self.wait(1)
        self.play(FadeOut(move))
        self.play(FadeIn(base))
        self.wait(3)
        self.play(FadeOut(base))
        self.play(FadeIn(base1))
        self.wait(2)
        self.play(FadeOut(base1))

