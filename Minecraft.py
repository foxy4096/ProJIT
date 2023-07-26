'''
Disclaimer: This solution is not scalable for creating a big world.
Creating a game like Minecraft requires specialized knowledge and is not as easy
to make as it looks.

You'll have to do some sort of chunking of the world and generate a combined mesh
instead of separate blocks if you want it to run fast. You can use the Mesh class for this.

You can then use blocks with colliders like in this example in a small area
around the player so you can interact with the world.
'''

from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d


app = Ursina()

# Define a Voxel class.
# By setting the parent to scene and the model to 'cube' it becomes a 3d button.

class Voxel(Button):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = .5,
            texture = 'white_cube',
            color = color.color(0, 0, random.uniform(.9, 1.0)),
            highlight_color = color.dark_gray,
        )


    def input(self, key):
        if self.hovered:
            if key == 'right mouse down':
                voxel = Voxel(position=self.position + mouse.normal)

            if key == 'left mouse down':
                destroy(self)


for x in range(9):
    for y in range(9):
        for z in range(9):
            voxel = Voxel(position=(x,y,z))


player = PlatformerController2d()
app.run()
