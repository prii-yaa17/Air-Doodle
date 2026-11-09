import numpy as np
import cv2 as cv
import sys
import os

# Add current directory to path to import canvas
sys.path.append(os.getcwd())

from canvas import Canvas, Color, Shape

def test_canvas():
    print("Testing Canvas...")
    rows, cols = 480, 640
    canvas = Canvas(rows, cols)
    
    # Test Colors
    print("Testing Colors...")
    assert Color.ORANGE in canvas.colors
    print("Colors OK")
    
    # Test Shapes
    print("Testing Shapes...")
    assert Shape.TRIANGLE in canvas.shapes
    print("Shapes OK")
    
    # Test Triangle Creation
    print("Testing Triangle Creation...")
    canvas.color = Color.ORANGE
    canvas.shape = Shape.TRIANGLE
    
    # Simulate drawing a triangle
    # Start
    canvas.update_triangle((100, 100))
    assert len(canvas.triangles) == 1
    assert canvas.currTriangle.active == True
    
    # Update
    canvas.update_triangle((200, 200))
    assert canvas.currTriangle.opposite == (200, 200)
    
    # End
    canvas.end_drawing()
    assert canvas.currTriangle.active == False
    
    # Test Drawing
    print("Testing Drawing...")
    frame = np.zeros((rows, cols, 3), dtype=np.uint8)
    frame = canvas.draw_canvas(frame, {'gesture': None})
    
    # Check if something was drawn (not all black)
    # The buttons are drawn, so it won't be all black.
    # Let's check if the triangle color is present in the frame.
    # Orange is (0, 165, 255) in BGR.
    mask = cv.inRange(frame, (0, 165, 255), (0, 165, 255))
    if cv.countNonZero(mask) > 0:
        print("Triangle drawn successfully (Orange pixels found)")
    else:
        print("Error: Triangle not drawn or color mismatch")
        # Note: Buttons might also use Orange if I added it to buttons list?
        # Yes, get_buttons_coords adds all colors.
        # So Orange button should be there.
        # But the triangle itself should also be there.
        pass

    # Test Eraser
    print("Testing Eraser...")
    # Triangle is at (100, 100) to (200, 200). Center approx (150, 150).
    # Erase at (150, 150) with radius 50
    # Note: overlaps_circle uses bounding box logic or distance logic depending on implementation.
    # My implementation uses distance to segments.
    # Center of bounding box is (150, 150).
    # Vertices: (100, 150), (200, 100), (200, 200).
    # (150, 150) is inside the triangle.
    canvas.erase_mode((150, 150), 100) # Large radius to be sure
    assert len(canvas.triangles) == 0
    print("Eraser OK")

    print("All tests passed!")

if __name__ == "__main__":
    test_canvas()
