import turtle
from enum import Enum


class states(Enum):
    ADD_GOAT = 1
    SELECT_GOAT = 2
    MOVE_GOAT = 3
    SELECT_TIGER = 4
    MOVE_TIGER = 5


class Board(turtle.Turtle):
    def __init__(self):
        self.filled_pos = [0] * 25
        self.pos_list = {}
        self.tigerStamp = "tiger.gif"
        self.goatStamp = "goat.gif"
        self.tiger_ids = []
        self.X = -200
        self.Y = 200
        self.current_step = 12
        self.floating_pos = None
        self.game_state = states.ADD_GOAT
        self.next_x = self.X
        self.next_y = self.Y
        super().__init__()
        self.myscreen = self.getscreen()
        self.myscreen.tracer(1,1)
        self.myscreen.bgpic("board.png")
        self.shape("turtle")
        self.penup()
        self.color("red")
        self.penup()
        for i in range(5):
            for j in range(5):
                self.setpos(self.next_x, self.next_y)
                key = 5 * i + j
                self.pos_list[key] = [self.next_x, self.next_y] 
                self.next_x = self.next_x + 100
            self.next_x = self.X
            self.next_y = self.next_y - 100
            self.myscreen.register_shape(self.tigerStamp)
            self.myscreen.register_shape(self.goatStamp)
    def initial_bagh_setup(self):
        keys = self.pos_list.keys()
        tiger_ids = []
        self.shape(self.tigerStamp)
        for key in keys:
            if (key == 0 or key == 4 or key == 20 or key == 24):
                [x, y] = self.pos_list[key] 
                self.setpos(x,y)
                s_id = self.stamp()
                tiger_ids.append(s_id)
                self.filled_pos[key] = True
        self.shape("turtle")
        [x, y] = self.pos_list[self.current_step]
        self.setpos(x,y)
    def setup_key_events(self):
        self.myscreen.onkey(self.move_up, "Up")
        self.myscreen.onkey(self.move_down, "Down")
        self.myscreen.onkey(self.move_left, "Left")
        self.myscreen.onkey(self.move_right, "Right")
        self.myscreen.onkey(self.pressed_enter, "Return")
        self.myscreen.listen()

    #events Methods
    def move_up(self):
        if(self.current_step > 4):
            #print("DEBUG:1")
            self.current_step = self.current_step - 5
            [x, y] = self.pos_list[self.current_step]
            self.setpos(x,y)
    def move_down(self):
        if(self.current_step < 20):
            self.current_step = self.current_step + 5
            [x, y] = self.pos_list[self.current_step]
            self.setpos(x,y)
    def move_left(self):
        if((self.current_step > 0) or (self.current_step < 24)):
            self.current_step = self.current_step - 1
            [x, y] = self.pos_list[self.current_step]
            self.setpos(x,y)
    def move_right(self):
        if((self.current_step > 0) or (self.current_step < 24)):
            #print("DEBUG:2")
            self.current_step = self.current_step + 1
            [x, y] = self.pos_list[self.current_step]
            self.setpos(x,y)
    def pressed_enter(self):
        #print("DEBUG:3", states.ADD_GOAT)
        if(self.game_state==states.ADD_GOAT):
            #print("DEBUG:3")
            self.shape(self.goatStamp)
            self.stamp()
            self.shape("turtle")
        elif(self.game_state == states.SELECT_GOAT):
            self.shape(self.goatStamp)
            self.floating_pos = self.current_step
        elif(self.game_state == states.MOVE_GOAT):
            self.stamp()
            self.shape("turtle")
        elif(self.game_state == states.SELECT_TIGER):
            self.shape(self.tigerStamp)
            self.shape(self.goatStamp)
            self.floating_pos = self.current_step
        elif(self.game_state == states.MOVE_TIGER):
            self.stamp()
            self.shape("turtle")
        
def main():
    board = Board()
    board.initial_bagh_setup()
    board.setup_key_events()
    board.myscreen.mainloop()
if __name__ == "__main__":
    main()