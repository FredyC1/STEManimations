
from manim import *

class math(Scene):
    def construct(self):
        # Axes for Cordinates
        slopeAxes = Axes(x_range=[-5,5,1], y_range=[-5,5,1],
        x_length=5, y_length=5, tips=False)
        # Slope intercept form
        slope = MathTex("y=mx+b").set_height(1)
        self.play(Create(slopeAxes), run_time=2)
        self.play(slopeAxes.animate.shift(LEFT*3), run_time=2)
        m=1
        b=0
        b_tracker = ValueTracker(1)
        m_tracker = ValueTracker(1)
        graph = always_redraw(lambda: slopeAxes.plot(lambda x: m_tracker.get_value()*x + b_tracker.get_value()
        ,x_range=[-4,4],
        use_smoothing=False,
        discontinuities=[-2,2]))
        self.play(Create(graph))
        self.play(b_tracker.animate.set_value(5), run_time=2) 
        self.play(b_tracker.animate.set_value(-5), run_time=2) 
        self.play(b_tracker.animate.set_value(0), run_time=2) 
        self.play(m_tracker.animate.set_value(2), run_time=2) 
        self.play(m_tracker.animate.set_value(-3), run_time=2) 

        self.play(slope.animate.shift(RIGHT*3), run_time=2)

