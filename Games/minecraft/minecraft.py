from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

sky_texture = load_texture('assets/skybox.png')
arm_texture = load_texture('assets/arm_texture.png')
punch_sound = Audio("assets/punch_sound", loop = False, autoplay= False)

texture = [ load_texture('assets/grass_block.png'), 
            load_texture('assets/dirt_block.png'),
            load_texture('assets/stone_block.png'),
            load_texture('assets/brick_block.png') 
]
block_pick = 0

window.fps_counter.enabled = False
window.exit_button.visible = False

def update():
    global block_pick
    if held_keys['1']: block_pick = 0
    if held_keys['2']: block_pick = 1
    if held_keys['3']: block_pick = 2
    if held_keys['4']: block_pick = 3
    
    if held_keys['left mouse'] or held_keys["right mouse"]: hand.active()
    else: hand.passive()
    

class Voxel(Button):
    def __init__(self, position = (0, 0, 0), texture = texture[0]):
        super().__init__(
            parent=scene,
            position=position,
            model = "assets/block",
            origin_y = 0.5,
            texture = texture,
            color=color.color(0, 0, random.uniform(0.9, 1)),
            scale = 0.5
        )
    
    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                voxel = Voxel(position = self.position + mouse.normal, texture = texture[block_pick])
                punch_sound.play()
                
            if key == "right mouse down":
                destroy(self)
                punch_sound.play()

class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model = "sphere",
            texture = sky_texture,
            scale = 150,
            double_sided = True
        )

class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = "assets/arm",
            texture = arm_texture,
            scale = 0.2,
            rotation = Vec3(150, -10, 0),
            position = Vec2(0.4, -0.6)
        )
    
    def active(self):
        self.position = Vec2(0.3, -0.5)
    
    def passive(self):
        self.position = Vec2(0.4, -0.6)

for y in range(3):
    for z in range(40):
        for x in range(40):
            voxel = Voxel(position=(x, y - 1, z), texture=texture[2 - y])

player = FirstPersonController()
sky = Sky()
hand = Hand()

app.run()