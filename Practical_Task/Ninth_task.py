import math

from matplotlib import pyplot as plt

from Dft_idft.Dft_idft import DftIdft
from Task4.FourthTask import FourthTask
from test import ConvTest, Compare_Signals
from utils.GlobalFunctions.FileReader import FileReader
from utils.GlobalFunctions.plotSignal import plotSignal


class NinthTask:

    @staticmethod
    def FastConvolution():
        IsPeriodic1, signalType1, noOfSample1, indices1, listOfSamples1 = FileReader.browse_signal_file()
        IsPeriodic2, signalType2, noOfSample2, indices2, listOfSamples2 = FileReader.browse_signal_file()

        # Padding the Signals
        padding = int(noOfSample1) + int(noOfSample2) - 1

        pad_len1 = padding - int(noOfSample1)
        pad_len2 = padding - int(noOfSample2)

        # Pad the signals
        listOfSamples1 = listOfSamples1 + [0] * pad_len1
        listOfSamples2 = listOfSamples2 + [0] * pad_len2

        frequency1 = FourthTask.ComputeFrequencies("DFT", listOfSamples1)
        frequency2 = FourthTask.ComputeFrequencies("DFT", listOfSamples2)

        # Perform convolution in frequency domain
        outputFrequency = []
        for i in range(len(frequency1)):
            outputFrequency.append(frequency1[i] * frequency2[i])  # Corrected convolution in frequency domain

        amplitudeList = []
        phaseShiftList = []
        for i in range(len(outputFrequency)):
            amplitudeList.append(round(math.sqrt(outputFrequency[i].real ** 2 + outputFrequency[i].imag ** 2), 13))
            phaseShiftList.append(math.atan2(outputFrequency[i].imag, outputFrequency[i].real))

        # computing the DFT component by (real = A*cos(Phase Shift)) and (imag = A*sin(Phase Shift))
        signalComponents = [complex(amp * math.cos(phase), amp * math.sin(phase))
                            for amp, phase in zip(amplitudeList, phaseShiftList)]

        # Compute Sequence in time domain X(n)
        frequencies = FourthTask.ComputeFrequencies("IDFT", signalComponents)

        output_samples =[]
        for i in range(len(signalComponents)):
            frequencies[i] /= len(signalComponents)

            output_samples.append(round(frequencies[i].real))

        min_index = int(indices1[0] + indices2[0])
        max_index = int(indices1[int(noOfSample1) - 1] + indices2[int(noOfSample2) - 1])


        # Computing the indices
        indices_output = []
        for n in range(min_index, max_index + 1):
            indices_output.append(int(n))

        # Testing
        ConvTest(indices_output, output_samples)

    @staticmethod
    def FastAutoCorrelation():
        no_of_sample, indices_list, samples_list = FileReader.browse_signal_file()

        # Apply DFT
        frequencies_list = DftIdft.Dft(samples_list)

        # Find conjugation
        conjugate_list = [num.conjugate() for num in frequencies_list]

        # Elements multiplication
        output_frequency = []
        for i in range(len(frequencies_list)):
            output_frequency.append(frequencies_list[i] * conjugate_list[i])

        amplitudeList = []
        phaseShiftList = []
        for i in range(len(output_frequency)):
            amplitudeList.append(round(math.sqrt(output_frequency[i].real ** 2 + output_frequency[i].imag ** 2), 13))
            phaseShiftList.append(math.atan2(output_frequency[i].imag, output_frequency[i].real))

        # Apply IDFT
        indices, samples = DftIdft.Idft(amplitudeList, phaseShiftList)

        # Divide Samples by N
        output_samples = [(1 / len(samples)) * float(sample) for sample in samples]

        # Testing
        print("Indices: ", indices_list)
        print("Samples: ", output_samples)

        # Plotting
        fig, (ax1) = plt.subplots(1, 1, figsize=(12, 5))
        plotSignal(indices_list, output_samples, "Fast Cross Correlation", ax1)

        plt.show()

    @staticmethod
    def FastCrossCorrelation():
        no_of_sample1, indices_list1, samples_list1 = FileReader.browse_signal_file()
        no_of_sample2, indices_list2, samples_list2 = FileReader.browse_signal_file()

        # Apply DFT
        frequencies_list1 = DftIdft.Dft(samples_list1)
        frequencies_list2 = DftIdft.Dft(samples_list2)

        # Find conjugation
        conjugate_list = [num.conjugate() for num in frequencies_list1]

        # Elements multiplication
        output_frequency = []
        for i in range(len(frequencies_list1)):
            output_frequency.append(conjugate_list[i] * frequencies_list2[i])

        amplitudeList = []
        phaseShiftList = []
        for i in range(len(output_frequency)):
            amplitudeList.append(round(math.sqrt(output_frequency[i].real ** 2 + output_frequency[i].imag ** 2), 13))
            phaseShiftList.append(math.atan2(output_frequency[i].imag, output_frequency[i].real))

        # Apply IDFT
        indices, samples = DftIdft.Idft(amplitudeList, phaseShiftList)

        # Divide Samples by N
        output_samples = [round((1 / len(samples)) * float(sample), 6) for sample in samples]

        # Testing
        print("Output samples: ", output_samples)
        Compare_Signals("test/Corr_Output.txt", indices_list1, output_samples)

        # Plotting
        fig, (ax1) = plt.subplots(1, 1, figsize=(12, 5))
        plotSignal(indices_list1, output_samples, "Fast Cross Correlation", ax1)
        plt.show()
