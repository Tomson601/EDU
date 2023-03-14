from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()

grass_color = color.rgb(1, 235, 113)
stone_color = color.rgb(138,141,143)
dirt_color = color.rgb(200, 157, 124)

block_pick = 1

def update():
    if held_keys['escape']:
        quit()

    global block_pick

    if held_keys['1']: block_pick = 1
    if held_keys['2']: block_pick = 2
    if held_keys['3']: block_pick = 3

class Voxel(Button):
    def __init__(self, position = (0,0,0), color = color.white):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = 0.5,
            texture = 'white_cube',
            color = color,
            highlight_color = color,
                    )

    def input(self,key):
        if self.hovered:
            if key == 'right mouse down':
                if block_pick == 1:voxel = Voxel(position = self.position + mouse.normal, color = grass_color)
                if block_pick == 2:voxel = Voxel(position = self.position + mouse.normal, color = stone_color)
                if block_pick == 3:voxel = Voxel(position = self.position + mouse.normal, color = dirt_color)
            if key == 'left mouse down':
                destroy(self)
    def update(self):
        if player.y < -80:
            print('You fell to death!')
            quit()

for z in range(20):
    for x in range(20):
        voxel = Voxel(position=(x,0,z), color = grass_color)

for y in range(3):
    for x in range(20):
        for z in range(20):
            voxel = Voxel(position=(x,y + -3,z), color = dirt_color)

player = FirstPersonController()
app.run()