## Task 1.1
class DiscreteContinuousSignalDisplayer:
    @staticmethod
    def display_continuous_signal(samples, axis):
        x = list(range(len(samples)))
        axis.plot(x, samples, label='Continuous Signal', color='b')
        axis.set_xlabel('X-axis')
        axis.set_ylabel('Y-axis')
        axis.set_title('Continuous Signal')
        axis.legend()

    @staticmethod
    def display_discrete_signal(samples, axis):
        x = list(range(len(samples)))
        axis.scatter(x, samples, label='Data Points', color='b', marker='o')
        axis.set_xlabel('X-axis')
        axis.set_ylabel('Y-axis')
        axis.set_title('Discrete Signal')

        # Making the vertical line
        for i in range(len(samples)):
            axis.plot([x[i], x[i]], [0, samples[i]], color='b', linestyle='-')

        axis.legend()
        axis.axhline(0, color='black', linestyle='-', label='X-axis')