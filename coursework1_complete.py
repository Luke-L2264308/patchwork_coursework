from graphix import Circle,Window,Point,Rectangle,Line,Text,Polygon
from time import sleep

def draw_triangle(win,point_1,point_2,point_3,fill_colour,outline_colour):
    point_list = [point_1,point_2,point_3]
    triangle = Polygon(point_list)
    triangle.fill_colour = fill_colour
    triangle.outline_colour = outline_colour
    triangle.draw(win)
    return triangle
def draw_patch_penultimate_digit(win,location,colour):
    triangle_list = []
    for j in range(0,81,40):
        for i in range(0,81,20):
            triangle_list.append(draw_triangle(win,Point(location.x+i,location.y+j),Point(location.x+10+i,location.y+20+j),Point(location.x+20+i,location.y+j),colour,colour))
    for j in range(20,61,40):
        for i in range(10,71,20):
            triangle_list.append(draw_triangle(win,Point(location.x+i,location.y+j),Point(location.x+10+i,location.y+20+j),Point(location.x+20+i,location.y+j),colour,colour))
        triangle_list.append(draw_triangle(win,Point(location.x,location.y+j),Point(location.x,location.y+20+j),Point(location.x+10,location.y+j),colour,colour))
        triangle_list.append(draw_triangle(win,Point(location.x+90,location.y+j),Point(location.x+100,location.y+20+j),Point(location.x+100,location.y+j),colour,colour))
    return triangle_list

def draw_plain_square(win,point,colour):
    square_list = []
    square = Rectangle(point,Point(point.x+100,point.y+100))
    square.fill_colour = colour
    square.draw(win)
    square_list.append(square)
    return square_list
def draw_line(win,my_line,colour):
    my_line.outline_width = 10
    my_line.outline_colour = colour
    my_line.draw(win)
    return my_line

def draw_patch(win,point_x,point_y,colour): 
    vert_startX = 100+point_x
    hor_startY = point_y+110
    my_line_list = []
    for i in range(15,115,20):
        my_line = Line(Point(vert_startX-i,point_y+i),Point(vert_startX-i,point_y+100))
        my_line = draw_line(win,my_line,colour)
        my_line_list.append(my_line)
        my_line = Line(Point(point_x,hor_startY-i),Point(point_x+i-5,hor_startY-i))
        my_line = draw_line(win,my_line,colour)
        my_line_list.append(my_line)
    
    return my_line_list
#gets the user inputs that the program needs
def get_inputs():
    available_sizes = ["5","7","9"]
    user_size = 0
    while not user_size in available_sizes:
        user_size = input("What size would you like to choose out of 5,7 or 9: ")
        if not user_size in available_sizes:
            print("Enter a valid user size")
    available_colours = ["red","green","blue","magenta","orange","purple"]
    user_inputted_colours = []
    num_colour = ["1st","2nd","3rd"]
    for i in range(3):
        user_input = ""
        while True:
            user_input = input(f"Enter the {num_colour[i]} colour: ")
            if user_input in available_colours and user_input not in user_inputted_colours:
                user_inputted_colours.append(user_input)
                break
            else:
                print("Enter a valid colour that has not already been inputted")
                print("Valid colours are red, green, blue, magenta, orange and purple")
    return (user_size,user_inputted_colours)
    patchwork_pattern(user_size,user_inputted_colours)

#gets and returns the colour
def get_colour(x,y,midpoint,user_inputted_colours, user_key):
    if user_key != "0":
        return user_inputted_colours[int(user_key)-1]
    elif x == midpoint or y == midpoint:
        return user_inputted_colours[1]
    elif (x<midpoint and y<midpoint) or (x>midpoint and y>midpoint):
        return user_inputted_colours[0]
    elif (x>midpoint and y<midpoint) or (x<midpoint and y>midpoint):
        return user_inputted_colours[2]

#generates the pattern
def patchwork_pattern(user_size, user_inputted_colours,win):
    patch_data = []
    mid_patch_start = round(user_size/2-50)
    patch_no = 0
    for y in range(0,user_size,100):
        for x in range(0,user_size,100):
            colour = get_colour(x,y,mid_patch_start,user_inputted_colours,"0")
            if x%200 == 0:
                patch_data.append(dict(patchno = patch_no, patchstart = Point(x,y), patchcontents = draw_patch(win,x,y,colour)))
            elif x%200 != 0 and (y!=0 and y!= user_size-100):
                patch_data.append(dict(patchno = patch_no, patchstart = Point(x,y), patchcontents = draw_patch_penultimate_digit(win,Point(x,y),colour)))
            else:
                patch_data.append(dict(patchno = patch_no, patchstart = Point(x,y),patchcontents = draw_plain_square(win,Point(x,y),colour)))
            patch_no +=1 
    
    return patch_data

#draws the square that appears when the user selects a patch
def draw_select_square(point,win):
    square = Rectangle(point,Point(point.x+100,point.y+100))
    square.outline_width = 10
    square.draw(win) 
    return square
    
def get_key_colour(key):
    key = (int(key)%3)
    if key == 0:
        key = 3
    return key

def select_square_function(win,select_square):
    click_location = win.get_mouse()
    if select_square != 0:
        select_square.undraw()
    click_location_x = (click_location.x//100)*100
    click_location_y = (click_location.y//100)*100
    select_square = draw_select_square(Point(click_location_x,click_location_y),win)
    return select_square,click_location_x,click_location_y

def move_patch(patch_data,move_x,move_y,num_add,i):
    if patch_data[i+num_add]["patchcontents"][0] == "Empty" and patch_data[i]["patchcontents"][0] != "Empty":
        for m in range(100):
            for k in range(len(patch_data[i]["patchcontents"])):
                patch_data[i]["patchcontents"][k].move(move_x,move_y)
                                
        for j in range(len(patch_data[i+num_add]["patchcontents"])):
            patch_data[i+num_add]["patchcontents"].pop(-1)
        for j in range(len(patch_data[i]["patchcontents"])):
            patch_data[i+num_add]["patchcontents"].append(patch_data[i]["patchcontents"][j])
        patch_data[i]["patchcontents"][0] = "Empty"
        return patch_data[i]["patchcontents"],patch_data[i+num_add]["patchcontents"]

def while_running(window_size,user_colours,patch_size,win,patch_data):
    select_square = 0
    while True:
        select_square,click_location_x,click_location_y = select_square_function(win,select_square)
        key = win.get_key()
        for i in range (round((patch_size/100)**2)):
            if click_location_x == patch_data[i]["patchstart"].x and click_location_y == patch_data[i]["patchstart"].y :
                if key == "x":
                    if type(patch_data[i]["patchcontents"]) != Rectangle:
                        for j in range(len(patch_data[i]["patchcontents"])):
                            if patch_data[i]["patchcontents"][j] != "Empty":
                                patch_data[i]["patchcontents"][j].undraw()
                                patch_data[i]["patchcontents"][j] = "Empty"      
                    else:
                        patch_data[i]["patchcontents"][0].undraw()
                        patch_data[i]["patchcontents"][0] = "Empty"
                elif key == "1" or key == "2" or key == "3":
                    colour = get_colour(click_location_x,click_location_x,round(patch_size/2-50),user_colours,key)
                    if patch_data[i]["patchcontents"][0] == "Empty":
                        patch_data[i]["patchcontents"] = draw_patch_penultimate_digit(win,Point(click_location_x,click_location_y),colour)
                elif key == "4" or key == "5" or key == "6":
                    key = get_key_colour(key)
                    colour = get_colour(click_location_x,click_location_x,round(patch_size/2-50),user_colours,key)
                    if patch_data[i]["patchcontents"][0] == "Empty":
                        patch_data[i]["patchcontents"] = draw_patch(win,click_location_x,click_location_y,colour)
                elif key == "7" or key == "8" or key == "9":
                    key = get_key_colour(key)
                    colour = get_colour(click_location_x,click_location_x,round(patch_size/2-50),user_colours,key)

                    if patch_data[i]["patchcontents"][0] == "Empty":
                        patch_data[i]["patchcontents"] = draw_plain_square(win,Point(click_location_x,click_location_y),colour) 
                    
                elif key == "Up":
                    if i-int(window_size)>=0:
                        if patch_data[i-int(window_size)]["patchcontents"][0] == "Empty" and patch_data[i]["patchcontents"][0] != "Empty":
                            patch_data[i]["patchcontents"],patch_data[i-int(window_size)]["patchcontents"] = move_patch(patch_data,0,-1,-int(window_size),i)

                elif key == "Down":
                    if i+int(window_size)<= int(window_size) ** 2 and patch_data[i+int(window_size)]["patchcontents"][0] == "Empty" and patch_data[i]["patchcontents"][0] != "Empty":
                        patch_data[i]["patchcontents"],patch_data[i+int(window_size)]["patchcontents"] = move_patch(patch_data,0,1,int(window_size),i)
                    
                elif key == "Left":
                    if i% int(window_size) != 0 and patch_data[i-1]["patchcontents"][0] == "Empty" and patch_data[i]["patchcontents"][0] != "Empty":
                        patch_data[i]["patchcontents"],patch_data[i-1]["patchcontents"] = move_patch(patch_data,-1,0,-1,i)
                  
                elif key == "Right":
                    if (i+1)% int(window_size) != 0 and patch_data[i+1]["patchcontents"][0] == "Empty" and patch_data[i]["patchcontents"][0] != "Empty":
                        patch_data[i]["patchcontents"],patch_data[i+1]["patchcontents"] = move_patch(patch_data,1,0,1,i)
                elif key == "Escape":
                    select_square.undraw()
                    select_square = 0

def main():
    window_size,user_colours = get_inputs()
    patch_size = int(window_size) * 100
    win = Window("Patchworks",patch_size,patch_size)
    patch_data = patchwork_pattern(patch_size,user_colours,win)
    while_running(window_size,user_colours,patch_size,win,patch_data)

main()
            
        
    