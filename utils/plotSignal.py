def plotSignal(x, y, axis):
    # Plot the Signal
    axis.scatter(x, y, label='Data Points', color='b', marker='o')
    axis.plot(x, y, marker='o', color='b', linestyle='-')
    axis.legend()


def plotDiscreteSignal(x, y, axis):
    # Plot the Signal
    axis.scatter(x, y, label='Data Points', color='b', marker='o')

    for i in range(len(y)):
        axis.plot([x[i], x[i]], [0, y[i]], color='b', linestyle='-')

    axis.legend()