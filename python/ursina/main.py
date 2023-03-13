from ursina import *                    # Import the ursina engine
import random                           # Import the random library

random_generator = random.Random()
cubes = []                                          # Create the list

def update():
    # for entity in cubes:
    #     entity.rotation_y += time.dt * 100
    if held_keys['q']:
        camera.position += (0, time.dt*10, 0)
    if held_keys['a']:
        camera.position -= (0, time.dt*10, 0)
    if held_keys['w']:
        camera.position += (0, 0, time.dt*10)
    if held_keys['s']:
        camera.position -= (0, 0, time.dt*10)
    if held_keys['e']:
        camera.position += (time.dt*10, 0, 0)
    if held_keys['d']:
        camera.position -= (time.dt*10, 0, 0)

x=y=z=s=0
cube = None

def input(key):
    if key == 'c':
        x = random_generator.random() * 10 - 5     # Value between -5 and 5
        y = random_generator.random() * 10 - 5     # Value between -5 and 5
        z = random_generator.random() * 10 - 5     # Value between -5 and 5
        s = random_generator.random() * 1          # Scale between 0 and 1
        # Create the new cube and add it to the list
        cube = Entity(model='cube', color=color.orange, scale=(2,2,2), texture="texture.jpg")
        cubes.append(cube)

    if key == 'space':
        red = random_generator.random() * 255
        green = random_generator.random() * 255
        blue = random_generator.random() * 255
        newcube = Entity(parent=cube, model='cube', color=color.rgb(red, green, blue), position=(x, y, z), scale=(s,s,s))
        cubes.append(newcube)

app = Ursina()


window.title = 'My Game'                # The window title
window.borderless = False               # Show a border
window.fullscreen = False               # Do not go Fullscreen
window.exit_button.visible = False      # Do not show the in-game red X that loses the window
window.fps_counter.enabled = True       # Show the FPS (Frames per second) counter

app.run()
