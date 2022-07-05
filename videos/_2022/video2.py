from manim import *
from ...common import test_utils

class TestText2(Scene):
    def construct(self):
        t = Text(str(test_utils.add(6, 8)))
        self.play(Create(t))
        self.wait()
