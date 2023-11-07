def plotSignal(x, y, axis):
    # Plot the Signal
    axis.scatter(x, y, label='Data Points', color='b', marker='o')
    axis.plot(x, y, marker='o', color='b', linestyle='-')
    axis.legend()