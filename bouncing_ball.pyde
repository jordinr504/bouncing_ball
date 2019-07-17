ball_y = 100 #ball 1 up and down
y_speed = 4 #ball 1 up and down speed
ball_x = 100 #ball 1 left and right
x_speed = 5 # ball 1 left and right speed

ball_a = 0 #ball 2 up and down
a_speed = 4 #ball 2  up and down speed
ball_b = 250 #ball 2 left and right
b_speed = 5 #ball 2 left and right speed
r = random(0,255)
g = random(0,255)
b = random(0,255)

def setup():
    size(500,500)
    background(255,255,255)
    
def draw():
    global ball_y
    global y_speed
    global ball_x
    global x_speed
    global r
    global g
    global b
    global ball_a
    global ball_b
    global a_speed
    global b_speed
    
    background(255,255,255)
    fill(r,g,b)
    ellipse(ball_x,ball_y,100,100)
    ellipse(ball_b,ball_a,100,100)
    line(0,500,500,500)
    line(500,0,500,500)
    

    ball_y = ball_y + y_speed
    ball_x = ball_x + x_speed
    ball_a = ball_a + a_speed
    ball_b = ball_b + b_speed
    
    if ball_y > 450:
        print("bounce")
        y_speed = -4
        r = random(0,255)
        g = random(0,255)
        b = random(0,255)
    elif ball_y < 50:
        y_speed = 4
        r = random(0,255)
        g = random(0,255)
        b = random(0,255)
    
    if ball_x > 450:
        x_speed = -5
        r = random(0,255)
        g = random(0,255)
        b = random(0,255)
    
    elif ball_x < 50:
        x_speed = 5  
        r = random(0,255) 
        g = random(0,255)
        b = random(0,255) 
        
    if ball_a > 450:
        a_speed = -4 
        r = random(0,255)
        g = random(0,255)
        b = random(0,255)
    elif ball_a < 50:
        a_speed = 4
        r = random(0,255)
        g = random(0,255)
        b = random(0,255)
        
    if ball_b > 450:
        b_speed = -5
        r = random(0,255)
        g = random(0,255)
        b = random(0,255)
    elif ball_b < 50:
        b_speed = 5
        r = random(0,255)
        g = random(0,255)
        b = random(0,255)
    
