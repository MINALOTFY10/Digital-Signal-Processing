import math
import os
from tkinter import filedialog

from matplotlib import pyplot as plt

from test import SignalComapreAmplitude, SignalComaprePhaseShift, SignalSamplesAreEqual
from utils.FileReader import FileReader
from decimal import Decimal

from utils.plotSignal import plotSignal, plotDiscreteSignal


class FourthTask:

    @staticmethod
    def testDiscreteFourierTransform(amplitudeList, phaseShiftList):
        noOfSample, outputAmplitudeList, outputPhaseShiftList = FileReader.browse_signal_file()
        for i in range(len(amplitudeList)):
            outputAmplitudeList[i] = round(outputAmplitudeList[i], 13)
        print("My Samples: ")
        print(amplitudeList)
        print(phaseShiftList)
        print("Test Samples")
        print(outputAmplitudeList)
        print(outputPhaseShiftList)

        if SignalComapreAmplitude(amplitudeList, outputAmplitudeList) and SignalComaprePhaseShift(phaseShiftList,
                                                                                                  outputPhaseShiftList):
            print("DFT Test case passed successfully :)")
        else:
            print("DFT Test case failed !!!!!!!")

    @staticmethod
    def DisplayAmplitudePhaseGraphs(amplitudeList, phaseShiftList, SamplingFrequency):

        fundamentalFrequency = ((2 * math.pi) * int(SamplingFrequency)) / len(amplitudeList)

        fundamentalFrequencyList = [fundamentalFrequency]
        for i in range(1, len(amplitudeList)):
            fundamentalFrequencyList.append(fundamentalFrequencyList[i - 1] + fundamentalFrequency)

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

        plotDiscreteSignal(fundamentalFrequencyList, amplitudeList, ax1)
        plotDiscreteSignal(fundamentalFrequencyList, phaseShiftList, ax2)

        plt.show()

    @staticmethod
    # Frequency components saved in txt file in polar form (amplitude and phase)
    def SaveInTxtFileInPolarForm(IsPeriodic, signalType, noOfSample, amplitudeList, phaseShiftList, file_path):
        # Specify the filename
        filename = file_path

        # Check if the file already exists
        if os.path.exists(filename):
            os.remove(filename)

        with open(filename, "w") as file:
            file.write(str(IsPeriodic))
            file.write("\n")
            file.write(str(signalType))
            file.write("\n")
            file.write(str(noOfSample))
            file.write("\n")

            for i in range(int(noOfSample)):
                file.write(str(amplitudeList[i]))
                file.write(" ")
                file.write(str(phaseShiftList[i]))
                file.write("\n")

    @staticmethod
    # Allow modification of the amplitude and phase of the signal components.
    def EditAmplitudePhaseOfSignal(index, amplitude, phase, samplingFrequency):
        file_path = filedialog.askopenfilename(initialdir="/", title="Select a file",
                                               filetypes=(("Text files", "*.txt"), ("all files", "*.*")))

        noOfSamples, amplitudeList, phaseShiftList = FileReader.processing_signal(file_path)
        wantToEdit = amplitudeList[int(index)]
        j = 0

        for i in range(int(noOfSamples)):
            if amplitudeList[i] == wantToEdit and j == 0:
                j += 1
                amplitudeList[i] = float(amplitude)
                phaseShiftList[i] = float(phase)
            elif amplitudeList[i] == wantToEdit:
                amplitudeList[i] = float(amplitude)
                phaseShiftList[i] = -float(phase)
        amplitudeList[int(index)] = float(amplitude)
        phaseShiftList[int(index)] = float(phase)

        # Edit The file
        FourthTask.SaveInTxtFileInPolarForm(0, 1, noOfSamples, amplitudeList, phaseShiftList, file_path)

        # Plotting The graph
        if samplingFrequency != "":
            FourthTask.DisplayAmplitudePhaseGraphs(amplitudeList, phaseShiftList, samplingFrequency)
        else:
            FourthTask.DisplayAmplitudePhaseGraphs(amplitudeList, phaseShiftList, len(amplitudeList))

    @staticmethod
    # Applying Fourier transform
    def DiscreteFourierTransform(SamplingFrequency):
        IsPeriodic, signalType, noOfSample, indices, listOfSamples = FileReader.browse_signal_file()

        frequencies = []
        for i in range(len(listOfSamples)):
            summation = 0

            for j in range(len(listOfSamples)):
                angle = 2 * math.pi * i * j / len(listOfSamples)
                cosValue = math.cos(angle)
                sinValue = -math.sin(angle)

                summation += listOfSamples[j] * complex(cosValue, sinValue)

            frequencies.append(summation)

        amplitudeList = []
        phaseShiftList = []

        for i in range(len(frequencies)):
            amplitudeList.append(round(math.sqrt(frequencies[i].real ** 2 + frequencies[i].imag ** 2), 13))
            phaseShiftList.append(math.atan2(frequencies[i].imag, frequencies[i].real))

        # Testing:
        FourthTask.testDiscreteFourierTransform(amplitudeList, phaseShiftList)

        # Save in the .txt file
        FourthTask.SaveInTxtFileInPolarForm(IsPeriodic, 1, noOfSample, amplitudeList, phaseShiftList,
                                            "DFT Output.txt")

        # Plotting
        FourthTask.DisplayAmplitudePhaseGraphs(amplitudeList, phaseShiftList, SamplingFrequency)

    @staticmethod
    # Signal reconstruction using IDFT
    def InverseDiscreteFourierTransform():
        noOfSample, amplitudeList, phaseShiftList = FileReader.browse_signal_file()

        indices = []
        Samples = []
        for i in range(len(amplitudeList)):
            summation = 0

            for j in range(len(amplitudeList)):
                # computing the DFT component by (real = A*cos(Phase Shift)) and (imag = A*sin(Phase Shift))
                signalComponent = complex(amplitudeList[j] * math.cos(phaseShiftList[j]),
                                          amplitudeList[j] * math.sin(phaseShiftList[j]))

                angle = 2 * math.pi * i * j / len(amplitudeList)
                cosValue = math.cos(angle)
                sinValue = math.sin(angle)

                summation += signalComponent * complex(cosValue, sinValue)

            summation /= len(amplitudeList)

            indices.append(i)
            Samples.append(round(summation.real))

        # Testing:
        print(indices)
        print(Samples)
        SignalSamplesAreEqual("IDTF", "utils/IDFT/Output_Signal_IDFT.txt", indices, Samples)

        # Plot the Signal
        plt.scatter(indices, Samples, label='Data Points', color='b', marker='o')
        plt.title("IDFT")
        plt.plot(indices, Samples, marker='o', color='b', linestyle='-')
        plt.legend()
        plt.xlim(0, 30)
        plt.show()
