import tkinter as tk

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400

CELL_SIZE = 40
ERASER_SIZE = 20

def erase_objects(canvas, eraser):
    # Get eraser's current position
    eraser_coords = canvas.coords(eraser)
    overlapping = canvas.find_overlapping(*eraser_coords)
    
    for obj in overlapping:
        if obj != eraser:
            canvas.itemconfig(obj, fill='white')

def move_eraser(event, canvas, eraser):
    x = event.x
    y = event.y
    canvas.coords(eraser, x, y, x + ERASER_SIZE, y + ERASER_SIZE)
    erase_objects(canvas, eraser)

def main():
    root = tk.Tk()
    root.title("Eraser Canvas")
    
    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
    canvas.pack()

    num_rows = CANVAS_HEIGHT // CELL_SIZE
    num_cols = CANVAS_WIDTH // CELL_SIZE
    
    for row in range(num_rows):
        for col in range(num_cols):
            left_x = col * CELL_SIZE
            top_y = row * CELL_SIZE
            right_x = left_x + CELL_SIZE
            bottom_y = top_y + CELL_SIZE
            
            canvas.create_rectangle(left_x, top_y, right_x, bottom_y, fill='blue')

    label = tk.Label(root, text="Click anywhere to place the eraser, then move your mouse!")
    label.pack()

    def on_click(event):
        eraser = canvas.create_rectangle(
            event.x, event.y, 
            event.x + ERASER_SIZE, event.y + ERASER_SIZE, 
            fill='pink'
        )
        canvas.bind('<Motion>', lambda e: move_eraser(e, canvas, eraser))

        label.config(text="")

    canvas.bind('<Button-1>', on_click)

    root.mainloop()

if __name__ == '__main__':
    main()
