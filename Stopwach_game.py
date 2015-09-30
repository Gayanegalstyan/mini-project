
# template for "Stopwatch: The Game"
# one of my first games

import simplegui
# define global variables

a=0
b=0
c=0
d=0
x=0
y=0
count=0
clock= ""
result=str(x) + "/" + str(y)
def counter():
    global count
    count += 1

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    a = t/600
    b = int(t/100)%6
    c=int(t/10)%10
    d=t%10

    clock=str(a) + ":"+ str(b) + str(c) + "." +str (d)
    return clock

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()


def stop():
    global x,y,result

    if (timer.is_running() == True):
        if ( d == 0 ):
            x =x + 1
        y =y +1
    result = str(x) + '/' + str(y)
    timer.stop()

def reset():
    global x,y,count,result
    count = 0
    format(count)
    x = 0
    y = 0
    result = str(x) + '/' + str(y)
    timer.stop()


# define event handler for timer with 0.1 sec interval
timer=simplegui.create_timer(100,counter)

# define draw handler
def draw(canvas):
    canvas.draw_text(format(count),[150,150],32,"Pink")
    canvas.draw_text(result,[200,200],30,"Blue")

# create frame
frame=simplegui.create_frame("stopwatch game",300,300)

# register event handlers
frame.set_draw_handler(draw)
frame.add_button("Start",start,80)
frame.add_button("Stop",stop,80)
frame.add_button("Reset",reset,80)
# start frame
frame.start()
timer.start()
