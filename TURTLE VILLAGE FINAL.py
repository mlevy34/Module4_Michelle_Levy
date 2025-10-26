
# Turtle Village — Lite (Student Scaffold)
# Focus: loops, decisions, try/except, and small functions.
# Run this file locally (IDLE/Thonny/PyCharm).

# ===>>>  REMOVE PASS IN ALL METHODS TO CODE

# NOTE about Turtle coordinate axis.
# turtle centers the origin (x == 0, y == 0 ) in the center of the canvas
# so if our default screen size is : CANVAS_W, CANVAS_H = 800, 600
#  the corners of your screen are :
# Top-left: (-CANVAS_W/2, CANVAS_H/2) → (-400, 300)
# Top-right: ( CANVAS_W/2, CANVAS_H/2) → ( 400, 300)
# Bottom-left: (-CANVAS_W/2, -CANVAS_H/2) → (-400, -300)
# Bottom-right: ( CANVAS_W/2, -CANVAS_H/2) → ( 400, -300)

import turtle as T
import random

"""
Pseudocode:
main()
1. Display to the user: "Welcome To Turtle Village - Lite!"
2. Ask user how many houses per row [2 or 3]
3. Ask user how many rows
4. Ask user what size they want the house to be
5. Ask user which color theme they would like (pastel or primary)
6. Ask the user which roof style they would like (triangle or flat)
7. Ask the user if they would like a sun in the corner
8. Set up the canvas/window the village will be drawn on
9. Draw the turtle village with all user inputs

ask_choice_int(prompt, allowed)
1. Define the allowed set
2. Ask the user to enter a number until it is 
valid and in the allowed set.
3. If the user input is not a integer and can't
be converted into an int, the user will be told
their input is invalid.
4. If the number is an integer, then it will check if the 
number is in the allowed choices. If not, the user will be 
told they need to choose a number from the set.
5. If the number is an integer and in the allowed set, it 
will be returned.

ask_choice_str(prompt, allowed)
1. Convert allowed options to lowercase
2. Ask the user to enter a string until it is 
valid and in the allowed set.
3. If the user input is not in the allowed set 
the user will be told their input is invalid.
4. If valid, the string will be returned.

draw_roads(col, rows, cell_w, cell_h)
1. set pencolor to gray and pensize to 5
2. draw horizontal lines between the rows
3. For each row, the y value will be the same 
and the x value will be calculated and a line will 
be drawn.
4. draw vertical lines between the columns of houses
5. for each column, the y value will be calculated
and the x value will be constant and the line will be drawn.

draw_house_centered(cx, cy, size_key, theme_key, roof_style)
1. Get the size of the house and the color theme
2. create the body of the house as the rectangle 
3. draw the roof of the house depending on the roof
style: if triangle, make a triangular rooftop. Otherwise, 
make it as a thin rectangle.
4. draw door centered at bottom of the house
5. draw a window towards the left side of the house

draw_tree_near(cx, cy, size_key)
1. Get the width and height of the house (size)
2. Place tree randomly either to left or the right
3. calculate trunk position
4. draw the trunk
5. draw the green circle on top

draw_village(cols, rows, size_key, theme_key, sun_flag, roof_style)
1. Draw the roads
2. Calculate the center coordinates (cx, cy) for each cell
3. In a for loop, draw a house in each cell and a tree near the 
house in each cell
4. if the user chooses t have a sun, draw a sun in the corner
"""
# ---------- constants ----------
CANVAS_W, CANVAS_H = 800, 600
TOP_MARGIN, BOTTOM_MARGIN = 40, 40


# size of houses 
SIZES = {
    "s": (120, 80),
    "m": (150, 100),
    "l": (180, 120),
}

'''
How to use Themes : 
# Use a theme like this:
colors = THEMES[theme_key]          # where theme_key is either "pastel" or "primary"
body_c  = colors["body"]            # we then can access the colors for the body of the house
roof_c  = colors["roof"]            # color of the roof of the house 
door_c  = colors["door"]            # door 
win_c   = colors["window"]          # window -- feel free to add or change the colors 
                                    # there is are beautiful pallette choices at coolors.co

# how to apply :
fill_rect_center(cx, cy, w, h, body_c)  # house body
'''
THEMES = {
    "pastel": dict(body="#ffd1dc", roof="#c1e1c1", door="#b5d3e7", window="#fff7ae"),
    "primary": dict(body="red", roof="blue", door="gold", window="#aee3ff"),
}

# ---------- tiny turtle helpers (provided) ----------
def move_to(x, y):
    '''
    x - position on x coordinate axis
    y - position on y coordinate axis
    '''
    T.penup(); T.goto(x, y); T.pendown()

def draw_line(x1, y1, x2, y2):
    '''
       we draw a line from x1,y1
       x1 - position on x coordinate axis
       y1 - position on y coordinate axis
       
       to x2, y2
       x2 - position on x coordinate axis
       y2 - position on y coordinate axis
       '''
    move_to(x1, y1); T.goto(x2, y2)

def fill_rect_center(cx, cy, w, h, color):
    '''
    cx - center of rectangle x coordinate 
    cy - center of rectangle y coordinate 
    w - width of rectangle 
    h - height of rectangle 
    color - color of rectangle 
    '''
    T.fillcolor(color); T.pencolor("black")
    move_to(cx - w/2, cy + h/2)
    T.begin_fill()
    for _ in range(2):
        T.forward(w); T.right(90); T.forward(h); T.right(90)
    T.end_fill()

def fill_triangle(p1, p2, p3, color):
    """
    Draw a filled triangle defined by three points.
    
    p1 — point 1 (x1, y1)
    p2 — point 2 (x2, y2)
    p3 — point 3 (x3, y3)
    color — fill color for the triangle
    
    Notes:
    - Each point is an (x, y) tuple.
    - Depending on your triangle, some x’s or y’s may be equal (e.g., flat base).
    
    Example:
    p1 = (x1, y1)
    p2 = (x2, y2)
    p3 = (x3, y3)
    fill_triangle(p1, p2, p3, color)
    """

    T.fillcolor(color); T.pencolor("black")
    move_to(*p1); T.begin_fill()
    T.goto(*p2); T.goto(*p3); T.goto(*p1)
    T.end_fill()

def fill_circle_center(cx, cy, r, color):
    '''
    a circle is defined by 
    cx - the center of your circle, x coordinate 
    cy - center of your circle, y coordinate 
    r - radius 
    color - color of circle 
    '''
    T.fillcolor(color); T.pencolor("black")
    move_to(cx, cy - r)  # turtle draws circles from the bottom
    T.begin_fill(); T.circle(r); T.end_fill()

# ---------- input helpers (complete; you may extend) ----------
def ask_choice_int(prompt, allowed):
    """Ask for an integer in the allowed set; reprompt on error.
        in a while loop, ask for a valid number from allowed list, exception is printed if incorrect number given,
        while loop continues until true 
        
        prompt for : 
        1. houses per roq
        2. how many houses
        """
    '''
        verifies the user input to make sure it isan integer and included in allowed list
        
        
        Args:
            The question that is being displayed to the user and the list of possible answers
        the user can respond.

        Return: 
            The integer the user types after it is checked to see if it is valid.
        Notes:
            Uses a while loop where the question will keep on being asked until the user 
            enters a valid answer that can be used in the program.
        '''

    # a set is a list which only allows one unique item to exist, not any duplicates
    # if duplicates are given, set removes all duplicates
    # This is a list that contains the possible answers the user can use.
    allowed_set = set(allowed)
    # will keep asking the user the prompt until the user types a valid answer and the
    # return statement is reached.
    while True:
        # Takes in user input
        user_input = input(f"{prompt} {allowed}:")
        # makes sure user input is an integer
        try:
            num = int(user_input)
            # if user input isan integer, the program will then also make sure
            # user input is one of the items in the allowed list. Then, the answer
            # can be used.
            if num in allowed_set:
                return num
            # If the number is not from the allowed list, user will be reprompted.
            else:
                print(f"Entry should be from the allowed numbers: {allowed}.")
        # If user input is invalid for any other reason, user will be told and will
        # have to reenter a response.
        except ValueError:
            print("Invalid, Please enter an integer.")

def ask_choice_str(prompt, allowed):
    """Ask for a string in the allowed list (case-insensitive); reprompt on error.
    in a while loop, ask for a valid string from allowed list, exception is printed if incorrect number given,
        while loop continues until true
        
        prompt for : 
        1. house size 
        2. color theme
        3. roof type 
        4. sun 
    """
    '''
    Args:
        The question that is being displayed to the user and the list of possible answers
    the user can respond.
    
    Return: 
        The string the user types after it is checked to see if it is valid.
    Notes:
        Uses a while loop where the question will keep on being asked until the user 
        enters a valid answer that can be used in the program.
    '''
    # converting to lower case all in allowed list so it can be appropriately be compared
    # with the user input which will also be converted into lowercase.
    allowed_lower = [a.lower() for a in allowed] # converting to lower case all in allowed list
    # will keep running until user puts in valid response and the return statement will be reached
    while True:
        # takes in user input to the question displayed
       user_input = input(f"{prompt} {allowed}:").lower()
        # If the user's response is within the allowed list, it will be used.
       if user_input in allowed_lower:
            return user_input
       # If user's input is not valid, the user will be reprompted and would need to
       # give an appropriate answer.
       else:
            print(f"{user_input} should be from the allowed list: {allowed}.")


# ---------- TODO: draw_roads ----------
def draw_roads(cols, rows, cell_w, cell_h):
    """Draw straight separator lines between rows and columns (simple roads)."""
    '''
    Draws the vertical and horizontal lines between each row/column which are 
    going to be used as roads
    
    Args:
        Cols - number of columns 
        Rows - number of rows 
        Cell_w - width of each grid cell
        Cell_h - height of the each grid cell.
    Return:
        None
    Notes:
        Uses a for loop, makes rows - 1 rows and cols - 1 columns. 
        Uses turtle graphics to draw the roads
    '''
    # defines the top, left, bottom and right of the drawing area.
    top_y = CANVAS_H / 2 - TOP_MARGIN
    bot_y = -CANVAS_H / 2 + BOTTOM_MARGIN
    left_x = -CANVAS_W / 2
    right_x = CANVAS_W / 2


    # TODO: set pen color + pensize
    # roads will be drawn in gray with a thick pensize for visibility
    T.pensize(5)
    T.pencolor("gray")
    # TODO: HORIZONTAL separators for r in 1..rows-1 at y = CANVAS_H/2 - TOP_MARGIN - r*cell_h
    #           here are are we vary y across rows (y = top_y - r*cell_h) and then
    #           drawing a line from (left_x, y) to (right_x, y)
    # Draws the horizontal lines between the rows.
    # for each row, a line will be drawn with a constant y value that
    # will be calculated.
    for r in range(1, rows):
        y = CANVAS_H / 2 - TOP_MARGIN - r * cell_h
        draw_line(left_x, y, right_x, y)



    # TODO: VERTICAL separators for c in 1..cols-1 at x = -CANVAS_W/2 + c*cell_w
    #           here we vary x across columns(x=left_x + c * cell_w) and
    #           then draw from (x, top_y) to(x, bot_y).
    # Vertical lines will be drawn between the columns.
    # For each column, the line will be drawn with a constant x value that will be
    # calculated.
    for c in range(1, cols):
        x = -CANVAS_W / 2 + c * cell_w
        draw_line(x, top_y, x, bot_y)

# ---------- TODO: draw_house_centered ----------
def draw_house_centered(cx, cy, size_key, theme_key, roof_style):
    """Draw a simple house centered at (cx, cy)."""
    '''
    Args:
        cx - The x coordinate of the center of your house.
        cy - The y coordinate of the center of your house.
        size_key - the size of the house entered by the user. ('s',
        'm', 'l'). 
        theme_key - the theme entered by the user, either 'pastel'
        or 'primary'.
        roof_style - the roof style of the house entered by the user. 
        Either a triangle or a flat rectangle.
    Return:
        None
    Notes:
        - House will have a body, roof, door, window.
        - A rectangle will be drawn at the centered at the center 
        coordinates of the house. The height and width of this 
         rectangle will vary depending on the height and width 
         the user enters. This will be the body of the house.
        - If the user wants the roof to be a triangle, a triangle
        will be drawn. If not, then a flat rectangle will be.
    '''
    # width/height depending on user input regarding size
    # of the house.
    w, h = SIZES[size_key]
    # Color of the houses depending on which color theme
    # the user chooses.
    colors = THEMES[theme_key]

    # TODO: body as centered rectangle
    # creates the body of the house given user input
    fill_rect_center(cx, cy, w, h, colors["body"])
    # TODO: roof: if roof_style is a 'triangle' draw a triangle; otherwise draw a thin flat rectangle
    y_top = cy + h / 2
    # roof will be drawn as triangle if that's what user chooses.
    if roof_style == "triangle":
        # top of triangle
        apex = (cx, y_top + h * 0.5)
        # left point of triangle
        left = (cx - w / 2, y_top)
        # right point of triangle
        right = (cx + w / 2, y_top)
        fill_triangle(left, apex, right, colors["roof"])
    else:  # flat roof
        fill_rect_center(cx, y_top + 5, w, 10, colors["roof"])
    # if yT = cy + h/2
    # Suggestion is that the roof apex at (cx, yT + 0.5*h) where 
    
    # TODO: add a small door centered on x=cx
    # draws door given size of the house
    dw, dh = w * 0.2, h * 0.35
    fill_rect_center(cx, cy - h * 0.25, dw, dh, colors["door"])
    # (optional) add one window off to the left
    # draws window
    ww, wh = w * 0.2, h * 0.2
    fill_rect_center(cx - w * 0.25, cy + h * 0.1, ww, wh, colors["window"])


# ---------- TODO: draw_tree_near ----------
def draw_tree_near(cx, cy, size_key):
    """Draw a small tree near the house (left or right)."""
    '''
    Draws a tree either  to the left or the right of each house.
    Args:
        cx - The x coordinate of the center of the house.
        cy - The y coordinate of the center of the house.
        size_key - the size of the house entered by the user. ('s', 'm', 'l') 
        used to help determine the size of the tree.
    Notes:
        Tree has a brown rectangular body and a green circle on top
        Using random.choice, the house is randomly places either on the left or right
        
        
    '''
    # trunk
    # Tree size is based on the house size dimensions the user enters.
    w, h = SIZES[size_key]
    # trunk size (ratios)
    tw, th = w*0.10, h*0.40
    # place to left or right of the house randomly
    side = random.choice([-1, 1])
    tx = cx + side * (w*0.45)
    ty = cy - h*0.5 + th/2
    # TODO: trunk: use fill_rect_center(tx, ty, tw, th, color)
    # draws the trunk as a brown rectangle
    fill_rect_center(tx, ty, tw, th, "brown")
    # TODO: canopy: use fill_circle_center(...) above trunk
    # Draws the top of the tree as a green circle
    fill_circle_center(tx, ty + th / 2 + w * 0.12, w * 0.20, "green")

# ---------- TODO: draw_village (orchestration) ----------
def draw_village(cols, rows, size_key, theme_key, sun_flag, roof_style):
    """Compute cell sizes, draw roads, and loop over grid to place houses/trees."""
    '''
    Draws the entire house village.
    
    Args:
        Cols - The number of columns in the house.
        Rows - The number of rows in the house.
        Size_key - the size of the house entered by the user. ('s', 'm', 'l') 
        Theme_key - the theme entered by the user, either 'pastel' or 'primary'.
        roof_style - the roof style of the house entered by the user. (triangle or flat)
        
    Return:
        None
    Notes:
        The cx and cy formulas ensure that each house is centered 
          correctly in its grid cell.
    '''
    cell_w = CANVAS_W / cols
    cell_h = (CANVAS_H - TOP_MARGIN - BOTTOM_MARGIN) / rows

    # TODO: draw roads first
    # Draws the roads/lines between the houses
    draw_roads(cols, rows, cell_w, cell_h)
    # TODO: nested loops over r, c
    #   compute cx, cy (center per formulas)
    #   draw_house_centered(...)
    #   draw_tree_near(...)
    # With all the choices the user picked, a house and a tree
    # will be drawn in each cell.
    for r in range(rows):
        for c in range(cols):
            # Center position for each cell
            cx = -CANVAS_W / 2 + (c + 0.5) * cell_w
            cy = CANVAS_H / 2 - TOP_MARGIN - (r + 0.5) * cell_h
            # Draws the house centered at (cx,cy)
            draw_house_centered(cx, cy, size_key, theme_key, roof_style)
            # Draws the tree near the house
            draw_tree_near(cx, cy, size_key)


    # sun (optional)
    if sun_flag == 'y':
        r = 35
        cx = CANVAS_W/2 - r - 20
        cy = CANVAS_H/2 - r - 20
        fill_circle_center(cx, cy, r, "yellow")

# ---------- main ----------
def main():
    print("Welcome to Turtle Village — Lite!")
    cols = ask_choice_int("How many houses per row?", [2, 3])
    rows = ask_choice_int("How many rows?", [2])  # you may change to [2, 3]
    size_key = ask_choice_str("House size", ["S","M","L"]).lower()
    theme_key = ask_choice_str("Color theme", ["pastel","primary"])
    roof_style = ask_choice_str("Roof type", ["triangle","flat"]).lower()
    sun_flag = ask_choice_str("Draw a sun?", ["y","n"]).lower()

    # window
    T.setup(CANVAS_W, CANVAS_H); T.speed(0); T.tracer(False)

    # the size of the property
    cell_w = CANVAS_W / cols
    cell_h = (CANVAS_H - TOP_MARGIN - BOTTOM_MARGIN) / rows

    # TODO: call draw_village with inputs
    draw_village(cols, rows, size_key, theme_key, sun_flag, roof_style)
    # TODO: finalize
    T.tracer(True); T.hideturtle(); T.done()

if __name__ == "__main__":
    main()
