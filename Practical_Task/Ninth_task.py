import math

from matplotlib import pyplot as plt

from Dft_idft.Dft_idft import DftIdft
from test import ConvTest, Compare_Signals
from utils.FileReader import FileReader
from utils.plotSignal import plotSignal


class NinthTask:

    @staticmethod
    def FastConvolution():
        IsPeriodic1, signalType1, noOfSample1, indices1, listOfSamples1 = FileReader.browse_signal_file()
        IsPeriodic2, signalType2, noOfSample2, indices2, listOfSamples2 = FileReader.browse_signal_file()

        # Padding the Signals
        padd = int(noOfSample1) + int(noOfSample2) - 1

        pad_len1 = padd - int(noOfSample1)
        pad_len2 = padd - int(noOfSample2)

        # Pad the signals
        listOfSamples1 = listOfSamples1 + [0] * pad_len1
        listOfSamples2 = listOfSamples2 + [0] * pad_len2

        frequency1 = DftIdft.Dft(listOfSamples1)
        frequency2 = DftIdft.Dft(listOfSamples2)

        # Perform convolution in frequency domain
        outputFrequency = []
        for i in range(len(frequency1)):
            outputFrequency.append(frequency1[i] * frequency2[i])  # Corrected convolution in frequency domain

        amplitudeList = []
        phaseShiftList = []
        for i in range(len(outputFrequency)):
            amplitudeList.append(round(math.sqrt(outputFrequency[i].real ** 2 + outputFrequency[i].imag ** 2), 13))
            phaseShiftList.append(math.atan2(outputFrequency[i].imag, outputFrequency[i].real))


        indices, Samples = DftIdft.Idft(amplitudeList, phaseShiftList)

        # Testing
        print("indices: ", indices)
        print("Samples: ", Samples)
        ConvTest(indices, Samples)

    # @staticmethod
    # def FastConvolution():
    #     IsPeriodic1, signalType1, noOfSample1, indices1, listOfSamples1 = FileReader.browse_signal_file()
    #     IsPeriodic2, signalType2, noOfSample2, indices2, listOfSamples2 = FileReader.browse_signal_file()
    #
    #     # Padding the Signals
    #     padd = int(noOfSample1) + int(noOfSample2) - 1
    #
    #     pad_len1 = padd - int(noOfSample1)
    #     pad_len2 = padd - int(noOfSample2)
    #
    #     # Pad the signals
    #     listOfSamples1 = listOfSamples1 + [0] * pad_len1
    #     listOfSamples2 = listOfSamples2 + [0] * pad_len2
    #
    #     amplitudeList1, phaseShiftList1 = DftIdft.Dft(listOfSamples1)
    #     amplitudeList2, phaseShiftList2 = DftIdft.Dft(listOfSamples2)
    #
    #     outputAmplitude = []
    #     outputPhaseShift = []
    #     for i in range(len(amplitudeList1)):
    #         outputAmplitude.append(amplitudeList1[i] * amplitudeList2[i])
    #         outputPhaseShift.append(phaseShiftList1[i] * phaseShiftList2[i])
    #
    #     indices, Samples = DftIdft.Idft(outputAmplitude, outputPhaseShift)
    #
    #     # Testing
    #     print("indices: ", indices)
    #     print("Samples: ", Samples)
    #     ConvTest(indices, Samples)

    @staticmethod
    def FastCorrelation():
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
        print("Output indices: ", indices_output)
        print("Output samples: ", samples_output)
        Compare_Signals("test/CorrOutput.txt", indices_output, samples_output)

        # Plotting
        fig, (ax1) = plt.subplots(1, 1, figsize=(12, 5))
        ax1.set_title("Correlation")
        plotSignal(indices_output, samples_output, ax1)

        plt.show()

