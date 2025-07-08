from manim import *
import numpy as np

class NormalDistributionScene(Scene):
    def construct(self):
        # Step 1: Axes
        axes = Axes(
            x_range=[-10, 10, 1],
            y_range=[0, 0.5, 0.1],
            x_length=10,
            y_length=5,
            axis_config={"include_numbers": True}
        )
        labels = axes.get_axis_labels(x_label="x", y_label="f(x)")
        self.play(FadeIn(axes), FadeIn(labels))

        # Step 2: ValueTrackers for μ and σ
        mu = ValueTracker(0)
        sigma = ValueTracker(1)

        # Step 3: Normal distribution graph
        def get_graph():
            return axes.plot(
                lambda x: (1 / (sigma.get_value() * np.sqrt(2 * np.pi))) * 
                          np.exp(-0.5 * ((x - mu.get_value()) / sigma.get_value())**2),
                color=BLUE
            )

        graph = always_redraw(get_graph)
        self.play(Create(graph))

        # Step 4: Equation
        equation = MathTex(
            r"f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{1}{2} \left(\frac{x - \mu}{\sigma}\right)^2}",
            font_size=32
        ).to_corner(UL)
        self.play(Write(equation))

        # Step 5: μ and σ labels
        mu_label = always_redraw(lambda: 
            MathTex(r"\mu = " + f"{mu.get_value():.2f}", font_size=30).next_to(equation, DOWN, aligned_edge=LEFT)
        )
        sigma_label = always_redraw(lambda: 
            MathTex(r"\sigma = " + f"{sigma.get_value():.2f}", font_size=30).next_to(mu_label, DOWN, aligned_edge=LEFT)
        )
        self.play(Write(mu_label), Write(sigma_label))

        # Step 6: Animate all transitions in sequence
        self.play(mu.animate.set_value(2), run_time=2)      # μ: 0 -> 2
        self.play(sigma.animate.set_value(1.5), run_time=2) # σ: 1 -> 1.5
        self.play(mu.animate.set_value(-3.5), run_time=2)   # μ: 2 -> -3.5
        self.play(sigma.animate.set_value(0.5), run_time=2) # σ: 1.5 -> 0.5
        self.play(mu.animate.set_value(1), run_time=2)      # μ: -3.5 -> 1
        self.play(sigma.animate.set_value(1), run_time=2)   # σ: 0.5 -> 1

        self.wait(2)
