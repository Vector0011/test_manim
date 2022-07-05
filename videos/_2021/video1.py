from manim import *
from ...common import test_utils

class TestText(Scene):
    def construct(self):
        t = Text(str(test_utils.add(1, 3)))
        self.play(Create(t))
        self.wait()
