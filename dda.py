from matplotlib import pyplot


def dda(x0, y0, x1, y1):
    dx = abs(x0 - x1)
    dy = abs(y0 - y1)

    steps = max(dx, dy)

    xinc = dx / steps
    yinc = dy / steps

    x = float(x0)
    y = float(y0)

    x_coorinates = []
    y_coorinates = []

    for i in range(steps):
        x_coorinates.append(x)
        y_coorinates.append(y)

        x = x + xinc
        y = y + yinc

    pyplot.plot(x_coorinates, y_coorinates, marker="o",
                markersize=1, markerfacecolor="green")
    pyplot.show()


if __name__ == "__main__":
    x0y0 = input("Enter x0 y0 respectively separated by a coma: ")
    x0, y0 = int(x0y0.split(",")[0]), int(x0y0.split(",")[1])
    x1y1 = input("Enter x1 y1 respectively separated by a coma: ")
    x1, y1 = int(x1y1.split(",")[0]), int(x1y1.split(",")[1])
    dda(x0, y0, x1, y1)
