from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

for z in range(10):
    for x in range(10):
        Entity(
            model="cube",
            color=color.red,
            collider="box",
            ignore=True,
            position=(x, 0, z),
            parent=scene,
            origin_y=0.5,
            texture="white_cube"
        )

class TextureBox(Button):
    def __init__(self, position=(5,2,5)):
        super().__init__(
            parent=scene,
            position=position,
            model="cube",
            origin_y=0.5,
            texture="fox.png",
            color=color.color(0,0,1)
        )

        self.texture_choice = 1
        self.textures = ["texture.jpg", "fox.png"]
    
    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                self.texture_choice += 1
                self.texture_choice %= len(self.textures)
                self.texture = self.textures[self.texture_choice]
            if key == "right mouse down":
                player.enabled = False
            if key == 'escape':
                quit()


TextureBox()

cam = FirstPersonController()
ground = Entity(model='plane', scale=(100,1,100), color=color.yellow.tint(-.2), texture='white_cube', texture_scale=(100,100), collider='box')
player = Button(parent=cam, model='cube', color=color.blue, origin_y=-0.5, position=(0,0,3), collider='box')
app.run()