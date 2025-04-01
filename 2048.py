from tkinter import Frame, Label, CENTER  
import LogicFinal
import constants as c

class Game2048(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.grid()
        self.master.title('2048')
        self.master.bind_all("<Key>", self.key_down)

        # Use arrow keys instead of WASD
        self.commands = {
            "Up": LogicFinal.move_up, 
            "Down": LogicFinal.move_down,
            "Left": LogicFinal.move_left, 
            "Right": LogicFinal.move_right
        }

        self.grid_cells = []
        self.init_grid()
        self.init_matrix()
        self.update_grid_cells()

        self.mainloop()

    def init_grid(self):
        background = Frame(self, bg=c.BACKGROUND_COLOR_GAME,
                       width=c.SIZE, height=c.SIZE)
        background.grid()
        for i in range(c.GRID_LEN):
            grid_row = []
            for j in range(c.GRID_LEN):
                cell = Frame(background, bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                            width=c.SIZE / c.GRID_LEN,
                            height=c.SIZE / c.GRID_LEN)

                cell.grid(row=i, column=j, padx=c.GRID_PADDING,
                        pady=c.GRID_PADDING)
                t = Label(master=cell, text="",
                        bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                        justify=CENTER, font=c.FONT, width=5, height=2)
                t.grid()
                grid_row.append(t)
            self.grid_cells.append(grid_row)

    def init_matrix(self):
        self.matrix = LogicFinal.start_game()
        LogicFinal.add_new_2(self.matrix)
        LogicFinal.add_new_2(self.matrix)

    def update_grid_cells(self):
        for i in range(c.GRID_LEN):
            for j in range(c.GRID_LEN):
                new_number = self.matrix[i][j]
                if new_number == 0:
                    self.grid_cells[i][j].configure(
                        text="", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                else:
                    self.grid_cells[i][j].configure(
                        text=str(new_number), 
                        bg=c.BACKGROUND_COLOR_DICT.get(new_number, "#3c3a32"), 
                        fg=c.CELL_COLOR_DICT.get(new_number, "#f9f6f2"))

        self.update_idletasks()
        
    def key_down(self, event):
        print(f"Key Pressed: {event.keysym}")  
        key = event.keysym  
        if key in self.commands:
            self.matrix, changed = self.commands[key](self.matrix)
            
            if changed:
                LogicFinal.add_new_2(self.matrix)
                self.update_grid_cells()
            
            # Check game state
            game_state = LogicFinal.current_state(self.matrix)
            if game_state == "WON":
                self.grid_cells[1][1].configure(text="You", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                self.grid_cells[1][2].configure(text="Win!", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
            elif game_state == "LOST":
                self.grid_cells[1][1].configure(text="You", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                self.grid_cells[1][2].configure(text="Lose!", bg=c.BACKGROUND_COLOR_CELL_EMPTY)


# Run the game
game_grid = Game2048()
