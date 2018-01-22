"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of TWO-DIMENSIONAL GRAPHICS.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Ethan Baker.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to test them. """
    run_test_draw_upside_down_wall()


def run_test_draw_upside_down_wall():
    """ Tests the    draw_upside_down_wall    function. """
    # Tests 1 and 2 are ALREADY DONE (here).
    window = rg.RoseWindow(550, 300, 'Upside-down wall, Tests 1 and 2')

    rectangle = rg.Rectangle(rg.Point(125, 230), rg.Point(155, 250))
    draw_upside_down_wall(rectangle, 8, window)

    rectangle = rg.Rectangle(rg.Point(375, 175), rg.Point(425, 225))
    draw_upside_down_wall(rectangle, 4, window)

    window.close_on_mouse_click()


def draw_upside_down_wall(rectangle, n, window):
    """
    See   MoreWalls.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an "upside-down wall" on the given window, where:
      -- The BOTTOM of the wall is a single "brick"
            that is the given rg.Rectangle.
      -- There are n rows in the wall.
      -- Each row is a row of "bricks" that are the same size
            as the given rg.Rectangle.
      -- Each row has one more brick than the row below it.
      -- Each row is centered on the bottom row.

    Preconditions:
      :type rectangle: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
    and n is nonnegative.
    """
    # ------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #     Some tests are already written for you (above).
    # ------------------------------------------------------------------

    height = rectangle.get_height()
    width = rectangle.get_width()
    upper_left_corner = rectangle.get_upper_left_corner()
    lower_right_corner = rectangle.get_lower_right_corner()
    x_ul = upper_left_corner.x
    y_ul = upper_left_corner.y
    x_lr = lower_right_corner.x
    y_lr = lower_right_corner.y

    original_x_ul = upper_left_corner.x
    original_y_ul = upper_left_corner.y
    original_x_lr = lower_right_corner.x
    original_y_lr = lower_right_corner.y

    for k in range(n):
        for j in range(k + 1):
            rect = rg.Rectangle(rg.Point(x_ul, y_ul), rg.Point(x_lr, y_lr))
            rect.attach_to(window)
            window.render()
            x_ul = x_ul + width
            x_lr = x_lr + width
        x_ul = original_x_ul
        y_ul = original_y_ul
        x_lr = original_x_lr
        y_lr = original_y_lr

        x_ul = x_ul - (width / 2)
        y_ul = y_ul - height
        x_lr = x_lr - (width / 2)
        y_lr = y_lr - height

        original_x_ul = x_ul
        original_y_ul = y_ul
        original_x_lr = x_lr
        original_y_lr = y_lr

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
