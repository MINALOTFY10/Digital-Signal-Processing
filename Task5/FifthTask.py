import math
import statistics

from Task4.FourthTask import FourthTask
from test import SignalSamplesAreEqual
from utils.GlobalFunctions.FileReader import FileReader
from utils.GlobalFunctions.SaveInTxtFileInPolarForm import SaveInTxtFileInPolarForm


class FifthTask:
    @staticmethod
    # Computing DCT for a given input and display the result
    def DCT(coefficients):
        # Reading the input and output files
        IsPeriodic, signalType, noOfSample, indices, listOfSamples = FileReader.browse_signal_file()
        noOfSampleTest, indicesTest, listOfSamplesTest = FileReader.readTask5TestFile()

        # Computing DCT for a given input
        frequencies = []
        DCTIndices = []
        for k in range(len(listOfSamples)):
            summation = 0
            for n in range(len(listOfSamples)):
                angle = (math.pi / (4 * len(listOfSamples))) * (2 * n - 1) * (2 * k - 1)
                summation += (listOfSamples[n] * math.cos(angle))

            result = summation * math.sqrt(2 / len(listOfSamples))

            digits_after_decimal_test = len(str(listOfSamplesTest[k]).split('.')[1])

            frequencies.append(round(result, digits_after_decimal_test))
            DCTIndices.append(0)

        # Saving the first m coefficients in .txt file
        newSamples = []
        newIndices = []
        for i in range(int(coefficients)):
            newSamples.append(frequencies[i])
            newIndices.append(0)

        SaveInTxtFileInPolarForm(IsPeriodic, 1, coefficients, newIndices, newSamples, "DCT m coefficients Output.txt")

        SignalSamplesAreEqual("DCT", "TestCases/Task5/DCT/DCT_output.txt", DCTIndices, frequencies)

    @staticmethod
    def RemoveDcComponentTimeDomain():
        IsPeriodic, signalType, noOfSample, indices, listOfSamples = FileReader.browse_signal_file()

        listOfSamples_Mean = statistics.mean(listOfSamples)
        for i in range(len(listOfSamples)):
            listOfSamples[i] = round(listOfSamples[i] - listOfSamples_Mean, 3)

        SignalSamplesAreEqual("DC Remover", "TestCases/Task5/Remove DC component/DC_component_output.txt", indices,
                              listOfSamples)
