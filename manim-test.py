from manim import *

# execution command
# manim -pql main.py(filename) CreateCircle

class CreateCircle(Scene):
    def construct(self):
        circle = Circle(radius=0.75)
        box = Square()
        circle.set_fill(BLUE, opacity=0.75)
        # self.add(box)


        self.play(Create(circle))

        circle.set_fill(GREEN, opacity=0.5)  # set color and transparency

        box.rotate(PI / 4)  # rotate a certain amount

        self.play(Create(box))  # animate the creation of the square
        self.play(Transform(box, circle))  # interpolate the square into the circle
        self.play(FadeOut(box))  #