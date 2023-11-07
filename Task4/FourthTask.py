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
    def DiscreteFourierTransformTest(amplitudeList, phaseShiftList):
        noOfSample, outputAmplitudeList, outputPhaseShiftList = FileReader.browse_signal_file()
        print("My Samples: ")
        print(amplitudeList)
        print(phaseShiftList)
        print("Test Samples")
        print(outputAmplitudeList)
        print(outputPhaseShiftList)

        for i in range(len(amplitudeList)):
            amplitudeList[i] = round(amplitudeList[i], 13)
            outputAmplitudeList[i] = round(outputAmplitudeList[i], 13)

        if SignalComapreAmplitude(amplitudeList, outputAmplitudeList) and SignalComaprePhaseShift(phaseShiftList,
                                                                                                  outputPhaseShiftList):
            print("DFT Test case passed successfully")

    @staticmethod
    def DisplayAmplitudePhaseGraphs(amplitudeList, phaseShiftList, SamplingFrequency, listOfSamples):

        fundamentalFrequency = ((2 * math.pi) * int(SamplingFrequency)) / len(listOfSamples)

        fundamentalFrequencyList = [fundamentalFrequency]
        for i in range(1, len(listOfSamples)):
            fundamentalFrequencyList.append(fundamentalFrequencyList[i - 1] + fundamentalFrequency)

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

        plotDiscreteSignal(fundamentalFrequencyList, amplitudeList, ax1)
        plotDiscreteSignal(fundamentalFrequencyList, phaseShiftList, ax2)

        plt.show()

    @staticmethod
    def SaveInTxtFileInPolarForm(IsPeriodic, signalType, noOfSample, amplitudeList, phaseShiftList, file_path):
        # Specify the filename
        filename = file_path

        # Check if the file already exists
        if os.path.exists(filename):
            # If the file exists, delete it
            os.remove(filename)

        # Create and open the new file in write mode
        with open(filename, "w") as file:
            # Write the contents of list1 to the file
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
    def EditAmplitudePhaseOfSignal(index, amplitude, phase):
        file_path = filedialog.askopenfilename(initialdir="/", title="Select a file",
                                               filetypes=(("Text files", "*.txt"), ("all files", "*.*")))

        noOfSamples, amplitudeList, phaseShiftList = FileReader.processing_signal(file_path)

        amplitudeList[int(index)] = amplitude
        phaseShiftList[int(index)] = phase

        # Edit The file
        FourthTask.SaveInTxtFileInPolarForm(0, 1, noOfSamples, amplitudeList, phaseShiftList, file_path)

    @staticmethod
    def DiscreteFourierTransform(SamplingFrequency):
        IsPeriodic, signalType, noOfSample, indices, listOfSamples = FileReader.browse_signal_file()

        frquencyies = []
        for i in range(len(listOfSamples)):
            realValue = 0
            imagValue = 0

            for j in range(len(listOfSamples)):
                angle = 2 * math.pi * i * j / len(listOfSamples)
                cosValue = math.cos(angle)
                sinValue = -math.sin(angle)

                realValue += listOfSamples[j] * cosValue
                imagValue += listOfSamples[j] * sinValue

            frquencyies.append(complex(round(realValue, 14), round(imagValue, 14)))

        amplitudeList = []
        phaseShiftList = []

        for i in range(len(frquencyies)):
            amplitudeList.append(round(math.sqrt(frquencyies[i].real ** 2 + frquencyies[i].imag ** 2), 14))
            phaseShiftList.append(round(math.atan2(frquencyies[i].imag, frquencyies[i].real), 14))

        # Testing:
        # FourthTask.DiscreteFourierTransformTest(amplitudeList, phaseShiftList)

        # Save in the .txt file
        FourthTask.SaveInTxtFileInPolarForm(IsPeriodic, 1, noOfSample, amplitudeList, phaseShiftList,
                                            "DFT Output.txt")

        # Plotting
        FourthTask.DisplayAmplitudePhaseGraphs(amplitudeList, phaseShiftList, SamplingFrequency, listOfSamples)

    @staticmethod
    def InverseDiscreteFourierTransform():
        noOfSample, amplitudeList, phaseShiftList = FileReader.browse_signal_file()

        indices=[]
        Samples = []
        for i in range(len(amplitudeList)):
            summation = 0

            for j in range(len(amplitudeList)):
                # computing the DFT component by (real = A*cos(Phase Shift)) and (imag = A*sin(Phase Shift))
                dftComponent = complex(amplitudeList[j] * math.cos(phaseShiftList[j]), amplitudeList[j] * math.sin(phaseShiftList[j]))

                angle = 2 * math.pi * i * j / len(amplitudeList)
                cosValue = math.cos(angle)
                sinValue = math.sin(angle)

                exponentialTerm = complex(cosValue, sinValue)

                xnTerm =  dftComponent * exponentialTerm

                summation += xnTerm

            summation /= len(amplitudeList)

            indices.append(i)
            Samples.append(round(summation.real))

        # Testing:
        print(indices)
        print(Samples)
        SignalSamplesAreEqual("IDTF", "utils/IDFT/Output_Signal_IDFT.txt", indices, Samples)
