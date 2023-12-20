from matplotlib import pyplot as plt

from test import ConvTest
from utils.GlobalFunctions.FileReader import FileReader
from utils.GlobalFunctions.plotSignal import plotSignal


class SeventhTask:

    @staticmethod
    def Convolution():
        IsPeriodic1, signalType1, noOfSample1, indices1, x = FileReader.browse_signal_file()
        IsPeriodic2, signalType2, noOfSample2, indices2, h = FileReader.browse_signal_file()

        min_index = int(indices1[0] + indices2[0])
        max_index = int(indices1[int(noOfSample1) - 1] + indices2[int(noOfSample2) - 1])

        indices_output = []
        samples_output = []
        indices_count = 0

        # Computing the indices
        for n in range(min_index, max_index + 1):
            indices_output.append(int(n))
            indices_count += 1

        # Computing the samples
        for n in range(indices_count):
            summation = 0
            for k in range(n + 1):
                if k < int(noOfSample1) and n - k < int(noOfSample2):
                    summation += x[k] * h[n - k]

            # Adding the final Summation to the samples list
            samples_output.append(int(summation))

        # Testing
        print("Output indices: ", indices_output)
        print("Output samples: ", samples_output)
        ConvTest(indices_output, samples_output)

        #Plotting
        fig, (ax1) = plt.subplots(1, 1, figsize=(12, 5))
        plotSignal(indices_output, samples_output, "Convolution", ax1)

        plt.show()