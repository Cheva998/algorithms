#http://www.codeskulptor.org/#user39_YZfoLIXVEV_26.py

# program template for Spaceship
import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time = 0.#5
c_fric = 0.05
accel = [.7, .7]
thrust = False
angle_vel_sh = 0
ast_vel = 2		#maximum asteroid velocity
an_mvel = 0.08	#maximum angular velocity
mis_vel = 7		#velocity of the missile
rock_group = set()
started = False
god_mode = False 

#Class for managing the info of the images
class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated


# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim

# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# ship with thrusters on image
ship_thr_info = ImageInfo([90+45, 45], [90, 90], 35)

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# animated ship's explosion
ship_explosion_info = ImageInfo([50, 50], [100, 100], 35, 81, True)
ship_explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/explosion.hasgraphics.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

#Functions for controling the ship
def Thruster(c):
    global thrust
    choice = [True, False]
    thrust = choice[c]
    
def angle_up(c):
    global angle_vel_sh
    choice = [an_mvel, 0]
    angle_vel_sh = choice[c]
    
def angle_down(c):
    global angle_vel_sh
    choice = [-an_mvel, 0]
    angle_vel_sh = choice[c]

def shot(c):
    if c == 0 and started:
        global missile_group
        pos_ship = my_ship.get_pos()
        vel_ship = my_ship.get_vel()
        angle_ship = my_ship.get_angle()
        radius_ship = ship_info.get_radius()
        vector = angle_to_vector(angle_ship)
        missile_pos = []
        missile_vel = []
        for i in range(2):
            missile_pos.append(pos_ship[i] + radius_ship * vector[i])
            missile_vel.append(vel_ship[i] + mis_vel * vector[i])
        missile_group.add(Sprite(missile_pos, missile_vel, 0, 0,
                           missile_image, missile_info, missile_sound))
    
#Key handlers and a dictionary with the functions
inputs = {"up": Thruster,
          "right": angle_up,
          "left": angle_down,
          "space": shot,}

def keydown(key):
    global space_down
    for i in inputs:
        if key == simplegui.KEY_MAP[i]:
            inputs[i](0)
            if i == "space":
                space_down = True
            break

def keyup(key):
    global space_down
    for i in inputs:
        if key == simplegui.KEY_MAP[i]:
            inputs[i](1)
            if i == "space":
                space_down = False
            break

def mouse_handler(posit):
    global started, lives, score, my_ship, rock_group, missile_group, ship_exp, expl_group
    if not started:
        started = True
        lives = 3
        score = 0
        my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info, c_fric, accel, thrust, angle_vel_sh)
        rock_group = set()
        missile_group = set()
        expl_group = set()
        ship_exp = set()
        soundtrack.play()

#Check if the item has reach the edge of the canvas
def edge_check(pos):
    new_pos = []
    if pos[0] > WIDTH or pos[0] < 0:
        new_pos.append(pos[0] % WIDTH)
    else:
        new_pos.append(pos[0])
    if pos[1] > HEIGHT or pos[1] < 0:
        new_pos.append(pos[1] % HEIGHT)
    else:
        new_pos.append(pos[1])
    return new_pos

# Function for choosing velocity and direction of the asteroids
def rn_vel(ini, stop, chan_sign = True):
    delta = stop - ini
    vel = random.random() * delta + ini
    if chan_sign:
        r = random.randrange(2)
        if r == 0:
            vel = vel * -1
    return vel

#Process the sprites, update and draw
def process_group_sprite(canvas, groups):
    remove_set = set(groups)
    for item in remove_set:
        be_or_not = item.update()
        if be_or_not:
            groups.remove(item)
        item.draw(canvas)

#Detect collisions of groups of objects against other object
def group_colli(group, moving_obj):
    item_remo = set(group)
    collision = False
    for item in item_remo:
        if item.collision(moving_obj):
            collision = True
            group.discard(item)
    return collision, group

def group_ofgroup_colli(group1, group2):
    copy_group = set(group2)
    any_coll = False
    pos = list()
    for item in copy_group:
        coll, group1 = group_colli(group1, item)
        if coll:
            pos.append(item.get_pos())
            group2.discard(item)
            any_coll = True
    return group1, group2, any_coll, pos

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)

# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info, c_fric, accel, thrust, angle_vel_sh, space_down = False):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = thrust
        self.angle = angle
        self.angle_vel = angle_vel_sh
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.c_fric = c_fric 
        self.accel = accel
        self.space_down = space_down
    def draw(self,canvas):
        canvas.draw_image(self.image, self.image_center, self.image_size, 
                          self.pos, self.image_size, self.angle)
        self.pos = edge_check(self.pos)
    
    def shooter(self):
        self.space_down = space_down
        if space_down:
            shot(0)

    def update(self):
        self.thrust = thrust
        if self.thrust:
            self.image_center = ship_thr_info.get_center()
            ship_thrust_sound.play()
        else:
            self.image_center = ship_info.get_center()
            ship_thrust_sound.rewind()
            ship_thrust_sound.pause()
        self.angle += angle_vel_sh
        vec = angle_to_vector(self.angle)
        for i in range(2):
            if self.thrust:
                accel_comp = self.accel[i] * vec[i]
            else:
                accel_comp = 0
            self.vel[i] = (1 - c_fric) * self.vel[i] + accel_comp
            self.pos[i] += self.vel[i]
    
    def get_pos(self):
        return self.pos
    
    def get_vel(self):
        return self.vel
    
    def get_angle(self):
        return self.angle
    
    def get_radius(self):
        return self.radius
    
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None, dim = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        self.dim = dim
        self.c_fric = 0.1
        if sound:
            sound.rewind()
            sound.play()
   
    def draw(self, canvas):
        if self.animated and self.dim == None:
            center = list(self.image_center)
            center[0] += self.image_size[0] * self.age
#            print "image_center", self.image_center, "center", center
            canvas.draw_image(self.image, center, self.image_size, self.pos, self.image_size)
        elif self.animated and len(self.dim) == 2:
            center = list(self.image_center)
            ind_center = [self.age % self.dim[0] , self.age // self.dim[1]]
            center[0] = self.image_size[0] * ind_center[0] + self.image_center[0]
            center[1] = self.image_size[1] * ind_center[1] + self.image_center[1]
#            print center
            canvas.draw_image(self.image, center, self.image_size, self.pos, self.image_size)
        else:
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
            self.pos = edge_check(self.pos)

    def update(self):
        self.angle += self.angle_vel
        for i in range(2):
            if self.dim == None:
                self.pos[i] += self.vel[i]
            else:
                self.pos[i] += (1 - self.c_fric) * self.vel[i]
        self.age += 1
        if self.age >= self.lifespan:
            return True
        else:
            return False
    
    def get_age(self):
        return self.age
    
    def get_pos(self):
        return self.pos
    
    def get_radius(self):
        return self.radius
    
    def collision(self, other_obj):
        distance = dist(self.pos, other_obj.get_pos())
        if (self.radius + other_obj.get_radius()) > distance:
            return True
        else:
            return False
        
def draw(canvas):
    global time, lives, rock_group, missile_group, started, my_ship, score, god_mode, ship_exp
    
    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))

    # draw  ship and sprites
    if started:
        my_ship.draw(canvas)
        process_group_sprite(canvas, rock_group)
        process_group_sprite(canvas, missile_group)
        process_group_sprite(canvas, ship_exp)
#        canvas.draw_circle(my_ship.get_pos(), my_ship.get_radius() * 4, 1, 'White')
    
        #update ship and sprites, and collisions between rocks and the ship
        my_ship.update()
        if time % (60 / 5) == 0:
            my_ship.shooter()
        rock_group, missile_group, hit, pos_expl = group_ofgroup_colli(rock_group, missile_group)
        if hit:
            score += 10
            for each_exp in pos_expl:
                expl_group.add(Sprite(each_exp, [0,0], 0, 0, explosion_image, explosion_info, explosion_sound))
#                print expl_group
        process_group_sprite(canvas, expl_group)
        #update collisions between rocks and the ship
        collision, rock_group = group_colli(rock_group, my_ship)
#        if len(ship_exp) == 0:
            
        if collision and not god_mode:
            lives -= 1
            ship_exp.add(Sprite(my_ship.get_pos(), my_ship.get_vel(), 0, 0, ship_explosion_image, ship_explosion_info, explosion_sound, [9, 9]))
            expl_group.add(Sprite(my_ship.get_pos(), [0,0], 0, 0, explosion_image, explosion_info, explosion_sound))
            my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info, c_fric, accel, thrust, angle_vel_sh)
            god_mode = True
        elif len(ship_exp) == 0 and god_mode:
            god_mode = False

    else:
        #Draw intro image
        canvas.draw_image(splash_image, splash_info.get_center(), splash_info.get_size(), 
                          [WIDTH / 2, HEIGHT / 2], splash_info.get_size())
    
    #Check if the game is over
    if lives < 1:
        started = False
        my_ship = set()
        rock_group = set()
        missile_group = set()
        ship_thrust_sound.rewind()
        soundtrack.rewind()
        
    #Draw lives and score
    canvas.draw_text('Lives: ' + str(lives), (20, 40), 20, 'White')
    canvas.draw_text('Score: ' + str(score), (WIDTH - 120, 40), 20, 'White')

# timer handler that spawns a rock    
def rock_spawner():
    global rock_group
    lev = score / 100
    if len(rock_group) < 12 and started:
        pos = [rn_vel(0, WIDTH, False), rn_vel(0, HEIGHT, False)]
        vel = [rn_vel(0 + lev, ast_vel + lev), rn_vel(0 + lev, ast_vel + lev)]
        distance = dist(pos, my_ship.get_pos())
        if distance > (my_ship.get_radius() * 4):
            rock_group.add(Sprite(pos, vel, 0, rn_vel(0,an_mvel), asteroid_image, 
                                  asteroid_info))
#            posis_rocks = pos
            
#        else:
#            pos_sh = my_ship.get_pos()
#            pos[0] += pos[0] - pos_sh[0]
#            pos[1] += pos[1] - pos_sh[1]
#            rock_group.add(Sprite(pos, [rn_vel(0,ast_vel), rn_vel(0,an_mvel)], 0, 
#                      rn_vel(0,an_mvel), asteroid_image, asteroid_info))
    
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info, c_fric, accel, thrust, angle_vel_sh)
rock_group = set()
missile_group = set()
expl_group = set()
ship_exp = set()
space_down = False

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_mouseclick_handler(mouse_handler)
timer = simplegui.create_timer(1000.0, rock_spawner)
#shooter = simplegui.create_timer(200, shot)
# get things rolling
timer.start()
frame.start()
