import math
import os
from tkinter import filedialog

from matplotlib import pyplot as plt

from test import SignalComapreAmplitude, SignalComaprePhaseShift, SignalSamplesAreEqual
from utils.GlobalFunctions.FileReader import FileReader
from utils.GlobalFunctions.SaveInTxtFileInPolarForm import SaveInTxtFileInPolarForm
from utils.GlobalFunctions.plotSignal import plotDiscreteSignal, plotSignal


class FourthTask:

    @staticmethod
    def testDFT(amplitudeList, phaseShiftList):
        noOfSample, outputAmplitudeList, outputPhaseShiftList = FileReader.browse_signal_file()
        for i in range(len(amplitudeList)):
            outputAmplitudeList[i] = round(outputAmplitudeList[i], 13)

        if SignalComapreAmplitude(amplitudeList, outputAmplitudeList) and SignalComaprePhaseShift(phaseShiftList,
                                                                                                  outputPhaseShiftList):
            print("DFT Test case passed successfully :)")
        else:
            print("DFT Test case failed !!!!!!!")

    @staticmethod
    def DisplayAmplitudePhaseGraphs(amplitudeList, phaseShiftList, SamplingFrequency):

        # Compute The Fundamental frequency = 2πFs/N
        fundamentalFrequency = ((2 * math.pi) * int(SamplingFrequency)) / len(amplitudeList)

        fundamentalFrequencyList = [fundamentalFrequency]
        for i in range(1, len(amplitudeList)):
            fundamentalFrequencyList.append(fundamentalFrequencyList[i - 1] + fundamentalFrequency)

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        plotDiscreteSignal(fundamentalFrequencyList, amplitudeList, ax1)
        plotDiscreteSignal(fundamentalFrequencyList, phaseShiftList, ax2)

        plt.show()

    @staticmethod
    # Allow modification of the amplitude and phase of the signal components.
    def EditAmplitudePhaseOfSignal(index, amplitude, phase, samplingFrequency):
        file_path = filedialog.askopenfilename(initialdir="/", title="Select a file",
                                               filetypes=(("Text files", "*.txt"), ("all files", "*.*")))

        noOfSamples, amplitudeList, phaseShiftList = FileReader.processing_signal(file_path)
        valueToEdit = amplitudeList[int(index)]
        j = 0

        for i in range(int(noOfSamples)):
            if amplitudeList[i] == valueToEdit:
                amplitudeList[i] = float(amplitude)
                phaseShiftList[i] = float(phase) if j == 0 else -float(phase)
                j = 1

        # Edit The file
        FourthTask.SaveInTxtFileInPolarForm(0, 1, noOfSamples, amplitudeList, phaseShiftList, file_path)

        # Plotting The graph
        if samplingFrequency != "":
            FourthTask.DisplayAmplitudePhaseGraphs(amplitudeList, phaseShiftList, samplingFrequency)
        else:
            FourthTask.DisplayAmplitudePhaseGraphs(amplitudeList, phaseShiftList, len(amplitudeList))

    @staticmethod
    def ComputeFrequencies(method, Samples):
        frequencies = []
        for i in range(len(Samples)):
            summation = 0

            for j in range(len(Samples)):
                angle = 2 * math.pi * i * j / len(Samples)
                cosValue = math.cos(angle)
                sinValue = -math.sin(angle) if method == 'DFT' else math.sin(angle)

                summation += Samples[j] * complex(cosValue, sinValue)

            frequencies.append(summation)

        return frequencies

    @staticmethod
    # Applying Fourier transform
    def DiscreteFourierTransform(SamplingFrequency):
        IsPeriodic, signalType, noOfSample, indices, listOfSamples = FileReader.browse_signal_file()
        amplitudeList = []
        phaseShiftList = []

        # Compute Sequence in frequency domain X(k)
        frequencies = FourthTask.ComputeFrequencies("DFT", listOfSamples)

        # Convert to Amplitude and Phase Shift
        for i in range(len(frequencies)):
            amplitudeList.append(round(math.sqrt(frequencies[i].real ** 2 + frequencies[i].imag ** 2), 13))
            phaseShiftList.append(math.atan2(frequencies[i].imag, frequencies[i].real))

        # Testing:
        FourthTask.testDFT(amplitudeList, phaseShiftList)

        # Save in the .txt file
        SaveInTxtFileInPolarForm(IsPeriodic, 1, noOfSample, amplitudeList, phaseShiftList,
                                            "DFT Output.txt")

        # Plotting
        FourthTask.DisplayAmplitudePhaseGraphs(amplitudeList, phaseShiftList, SamplingFrequency)

    @staticmethod
    # Signal reconstruction using IDFT
    def InverseDiscreteFourierTransform():
        noOfSample, amplitudeList, phaseShiftList = FileReader.browse_signal_file()
        indices = []
        Samples = []

        # computing the DFT component by (real = A*cos(Phase Shift)) and (imag = A*sin(Phase Shift))
        signalComponents = [complex(amp * math.cos(phase), amp * math.sin(phase))
                           for amp, phase in zip(amplitudeList, phaseShiftList)]

        # Compute Sequence in time domain X(n)
        frequencies = FourthTask.ComputeFrequencies("IDFT", signalComponents)

        for i in range(len(signalComponents)):
            frequencies[i] /= int(noOfSample)

            indices.append(i)
            Samples.append(round(frequencies[i].real))

        # Testing:
        SignalSamplesAreEqual("IDTF", "TestCases/Task4/IDFT/Output_Signal_IDFT.txt", indices, Samples)

        # Plot the Signal
        fig, (ax1) = plt.subplots(1, 1, figsize=(12, 5))
        plotSignal(indices, Samples, "IDFT", ax1)
        plt.xlim(0, 30)
        plt.show()
