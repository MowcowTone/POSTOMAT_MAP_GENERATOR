class generat():
    def squares(x,y):
        squares = []
        for i in range(x):
            for j in range(y):
                squares.append([
                    [37.03+j*0.03, 56.015+i*0.015],
                    [37.03+j*0.03, 56.0+i*0.015],
                    [37.0+j*0.03, 56.0+i*0.015],
                    [37.0+j*0.03, 56.015+i*0.015]
                ])
        return squares
    def points(x,y):
        points = []
        for i in range(x):
            for j in range(y):
                points.append([37.01+j*0.03, 56.005+i*0.015])
        return points
