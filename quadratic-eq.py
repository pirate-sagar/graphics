from matplotlib import pyplot


def plotQudaratic(constant, x_raised_to):
    x_coord=[]
    y_coord=[]
    for i in range(-100,100):
        x=i
        y = x ** x_raised_to + constant
        x_coord.append(x)
        y_coord.append(y)

    pyplot.plot(x_coord, y_coord, marker="o",
                markersize=1, markerfacecolor="blue")
    pyplot.show()


if __name__ == "__main__":
    plotQudaratic(99,2)
