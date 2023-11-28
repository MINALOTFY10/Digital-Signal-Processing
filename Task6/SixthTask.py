import math
import statistics

from test import SignalSamplesAreEqual
from utils.FileReader import FileReader


class SixthTask:
    @staticmethod
    def Smoothing(windowSizeEntry):
        IsPeriodic, signalType, noOfSample, indices, listOfSamples = FileReader.browse_signal_file()
        newSignal = []
        for i in range(len(listOfSamples) - int(windowSizeEntry) + 1):
            summation = 0
            for j in range(int(windowSizeEntry) - 1):
                summation += listOfSamples[i + j]
            newSignal[i] = summation / int(windowSizeEntry)

        print("new signal : ", newSignal)
    # SignalSamplesAreEqual("DCT", "utils/DCT_output.txt", indices, listOfSamples)
