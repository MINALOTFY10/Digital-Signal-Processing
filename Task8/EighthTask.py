from matplotlib import pyplot as plt

from test import Compare_Signals
from utils.GlobalFunctions.FileReader import FileReader
from utils.GlobalFunctions.plotSignal import plotSignal


class EighthTask:

    @staticmethod
    def NormalizedCrossCorrelation():
        noOfSample1, indicesList1, samplesList1 = FileReader.browse_signal_file()
        noOfSample2, indicesList2, samplesList2 = FileReader.browse_signal_file()
        indices_output = []
        samples_output = []

        # To solve denominator
        summationSquaresOfSamples1 = sum([x ** 2 for x in samplesList1])
        summationSquaresOfSamples2 = sum([x ** 2 for x in samplesList2])
        denominatorEquation = ((summationSquaresOfSamples1 * summationSquaresOfSamples2) ** 0.5) / int(noOfSample1)

        # To solve numerator
        for i in range(int(noOfSample1)):
            if i != 0:
                samplesList2.append(samplesList2.pop(0))

            summation = 0
            for j in range(int(noOfSample1)):
                summation += samplesList1[j] * samplesList2[j]

            r = int(summation) / int(noOfSample1)

            # Final Output List
            indices_output.append(i)
            samples_output.append(round(r / denominatorEquation, 8))

        # Testing
        Compare_Signals("test/CorrOutput.txt", indices_output, samples_output)

        # Plotting
        fig, (ax1) = plt.subplots(1, 1, figsize=(12, 5))
        plotSignal(indices_output, samples_output, "Correlation", ax1)
        plt.show()
