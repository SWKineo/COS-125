def draw_grid(gridsize):
    gridBar = "+ - - - " * gridsize + "+"
    gridBlock = "|       " * gridsize + "|"
    
    for i in range(gridsize):
        print gridBar
        for i in range(3):
            print gridBlock
    print gridBar

draw_grid(5)
