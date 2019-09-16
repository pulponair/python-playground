import tkinter
from random import randrange


def draw(tk, iterations):
    colors = ['green', 'red', 'blue']
    points = [[tk.width / 2, 1], [1, tk.height], [tk.width, tk.height]]
    tk.canvas.delete("all")
    currentPoint = [0, 0]
    for i in range(iterations):
        pIndex = randrange(3)
        currentPoint = [
            (points[pIndex][0] + currentPoint[0]) / 2,
            (points[pIndex][1] + currentPoint[1]) / 2
        ]

        tk.canvas.create_line(currentPoint[0], currentPoint[1], currentPoint[0] + 1, currentPoint[1],
                              fill=colors[pIndex])


tk = tkinter.Tk()
tk.title("Sierpinski Triangle")
tk.width = 800
tk.height = 600
tk.margin = 0

tk.canvas = tkinter.Canvas(tk, width=tk.width + (2 * tk.margin), height=tk.height + (2 * tk.margin), bg="white")
tk.canvas.pack()

tk.label = tkinter.Label(tk, text="Iterations:")
tk.label.pack(padx=5, pady=5, side=tkinter.LEFT)

tk.iterations = tkinter.Entry(tk, width=10, justify=tkinter.CENTER)
tk.iterations.insert(tkinter.INSERT, "10000")
tk.iterations.pack(padx=5, pady=5, side=tkinter.LEFT)

tk.btn = tkinter.Button(tk, text="Go!", command=lambda: draw(tk, int(tk.iterations.get())))
tk.btn.pack(padx=5, pady=5, side=tkinter.LEFT)

tk.mainloop()
