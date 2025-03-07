
from manim import *
from manimpango import list_fonts
config.background_color = WHITE
class math(Scene):
    def construct(self):
        # Axes for Cordinates
        slopeAxes = Axes(x_range=[-5,5,1], y_range=[-5,5,1],
        x_length=5, y_length=5, tips=False, axis_config={"color": BLACK})
        # Slope intercept form
        slope = MathTex(r"y=","m","x+","b", color=BLACK, stroke_width=3).set_height(1).shift(RIGHT*3)
        box = SurroundingRectangle(slope[1], color=RED, stroke_width=4)
        box2 = SurroundingRectangle(slope[3], color=RED, stroke_width=4)
        self.play(Create(slopeAxes), run_time=2)
        self.play(slopeAxes.animate.shift(LEFT*3), run_time=2)
        m=1
        b=0
        b_tracker = ValueTracker(0)
        m_tracker = ValueTracker(1)
        graph = always_redraw(lambda: slopeAxes.plot(lambda x: m_tracker.get_value()*x + b_tracker.get_value()
        ,x_range=[-3.5,3.5],
        use_smoothing=False,
        discontinuities=[-2,2],
        stroke_width=3,
        color=BLACK))
        self.play(Create(graph))
        self.wait(0.2)
        self.play(Write(slope))
        self.wait(0.5)
        self.play(Write(box))
        self.play(m_tracker.animate.set_value(-1), run_time=0.5) 
        self.play(m_tracker.animate.set_value(1), run_time=0.5) 
        self.play(Unwrite(box), run_time=0.5)
        self.play(Write(box2), run_time=0.5)
        self.play(b_tracker.animate.set_value(2), run_time=0.5) 
        self.play(b_tracker.animate.set_value(-3), run_time=0.5) 
        self.play(b_tracker.animate.set_value(0), run_time=0.5) 
        
        #Flash of slope formula
        self.play(FadeOut(graph, slope, box2, slopeAxes))
        slope_formula = MathTex(r"\frac{y_2 - y_1}{x_2 - x_1} = m", color=BLACK, stroke_width=3).set_height(2.5)
        self.play(Write(slope_formula), run_time=1.4)
        self.play(FadeOut(slope_formula), run_time=2)
        #quadratic formula
        quadratic_formula = MathTex(r"x =", r"\frac{-b \pm \sqrt{b^2 - 4ac}}{2a}", color=BLACK, stroke_width=3).set_height(1.2)
        self.play(Write(quadratic_formula))
        self.play(quadratic_formula.animate.shift(LEFT*3))
        quadratic = MathTex(r"ax^2 + bx + c = 0", color=BLACK, stroke_width=2).shift(RIGHT*3).set_height(0.7)
        quadraticBox = SurroundingRectangle(quadratic, color=RED, stroke_width=3)
        plusMinusBox = SurroundingRectangle(quadratic_formula[1][2], color=RED, stroke_width=3)
        self.play(Write(quadratic), run_time=4)
        self.play(Write(quadraticBox))
        self.wait(1)
        self.play(Write(plusMinusBox))
        self.wait(2.1)
        self.play(FadeOut(quadratic, quadraticBox, plusMinusBox, quadratic_formula))

# manim -pqm SATanimations.py math --transparent