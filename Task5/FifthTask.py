import math
import statistics

from test import SignalSamplesAreEqual
from utils.FileReader import FileReader


class FifthTask:
    @staticmethod
    def DCT():
        IsPeriodic, signalType, noOfSample, indices, listOfSamples = FileReader.browse_signal_file()

        frequencies = []
        for k in range(len(listOfSamples)):
            summation = 0
            for n in range(len(listOfSamples)):
                angle = (math.pi / 4 * len(listOfSamples)) * (2 * n - 1) * (2 * k - 1)
                summation += (listOfSamples[n] * math.cos(angle))

            result = summation * math.sqrt(2 / len(listOfSamples))
            frequencies.append(result)

        print(frequencies)
        SignalSamplesAreEqual("DCT", "utils/DCT_output.txt", indices, listOfSamples)

    @staticmethod
    def RemoveDcComponent():
        IsPeriodic, signalType, noOfSample, indices, listOfSamples = FileReader.browse_signal_file()

        listOfSamples_Mean = statistics.mean(listOfSamples)
        for i in range(len(listOfSamples)):
            listOfSamples[i] = round(listOfSamples[i] - listOfSamples_Mean, 3)

        print(listOfSamples)
        SignalSamplesAreEqual("DC Remover", "utils/DC_component_output.txt", indices, listOfSamples)
