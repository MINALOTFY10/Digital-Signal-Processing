import math

from matplotlib import pyplot as plt

from Task2.ArithmeticOperations import ArithmeticOperations
from test import SignalSamplesAreEqual, Shift_Fold_Signal, SharpeningTest
from utils.GlobalFunctions.FileReader import FileReader
from utils.GlobalFunctions.plotSignal import plotSignal


class SixthTask:

    @staticmethod
    def Smoothing(window_size_entry):
        IsPeriodic, signalType, noOfSample, indices, listOfSamples = FileReader.browse_signal_file()
        new_signal = []
        new_indices = []

        for i in range(len(listOfSamples) - int(window_size_entry) + 1):
            # summation of samples from i to i + w
            summation = sum(listOfSamples[i:i + int(window_size_entry)])
            new_signal.append(summation / int(window_size_entry))
            new_indices.append(i)


        # Testing
        SignalSamplesAreEqual("Smoothing", "TestCases/Task6/Moving Average/OutMovAvgTest1.txt", new_indices, new_signal)
        # SignalSamplesAreEqual("Smoothing", "TestCases/Task6/Moving Average/OutMovAvgTest2.txt", new_indices, new_signal)

        # Plotting
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        plotSignal(indices, listOfSamples, "Before Smoothing", ax1)
        plotSignal(new_indices, new_signal, "After Smoothing", ax2)
        plt.show()

    @staticmethod
    def Sharpening():
        InputSignal = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0,
                       18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0, 25.0, 26.0, 27.0, 28.0, 29.0, 30.0, 31.0, 32.0, 33.0,
                       34.0, 35.0, 36.0, 37.0, 38.0, 39.0, 40.0, 41.0, 42.0, 43.0, 44.0, 45.0, 46.0, 47.0, 48.0, 49.0,
                       50.0, 51.0, 52.0, 53.0, 54.0, 55.0, 56.0, 57.0, 58.0, 59.0, 60.0, 61.0, 62.0, 63.0, 64.0, 65.0,
                       66.0, 67.0, 68.0, 69.0, 70.0, 71.0, 72.0, 73.0, 74.0, 75.0, 76.0, 77.0, 78.0, 79.0, 80.0, 81.0,
                       82.0, 83.0, 84.0, 85.0, 86.0, 87.0, 88.0, 89.0, 90.0, 91.0, 92.0, 93.0, 94.0, 95.0, 96.0, 97.0,
                       98.0, 99.0, 100.0]

        FirstDrev = []
        firstDevInd = []
        secondDevInd = []
        SecondDrev = []
        # First Derivative X(n) - X(n-1)
        for i in range(1, len(InputSignal)):
            FirstDrev.append(InputSignal[i] - InputSignal[i - 1])
            firstDevInd.append(i)

        # Second Derivative X(n+1) - 2 * X(n) + X(n-1)
        for i in range(1, len(InputSignal) - 1):
            SecondDrev.append(InputSignal[i + 1] - (2 * InputSignal[i]) + InputSignal[i - 1])
            secondDevInd.append(i)

        print("First Derivative, ", FirstDrev)
        print("Second Derivative, ", SecondDrev)
        # Plotting
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        plotSignal(firstDevInd, FirstDrev, "First Derivative", ax1)
        plotSignal(secondDevInd, SecondDrev, "Second Derivative", ax2)
        # Testing
        SharpeningTest(FirstDrev, SecondDrev)
        plt.show()

    @staticmethod
    def Shifting(shiftingValue):
        ArithmeticOperations.shifting(shiftingValue)

    @staticmethod
    def FoldingSignal():
        IsPeriodic, signalType, noOfSample, indices, listOfSamples = FileReader.browse_signal_file()

        # Invert the signal
        FoldedList = listOfSamples[::-1]

        # Plotting
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        plotSignal(indices, listOfSamples, "Original Signal", ax1)
        plotSignal(indices, FoldedList, "Folded Signal", ax2)

        # Testing
        SignalSamplesAreEqual("Folding Signal", "TestCases/Task6/Shifting and Folding/Output_fold.txt", indices, FoldedList)
        plt.show()

    @staticmethod
    def ShiftingFoldedSignal(ShiftingValueEntry):
        IsPeriodic, signalType, noOfSample, indices, listOfSamples = FileReader.browse_signal_file()
        newIndices = []

        # Folding the Signal
        FoldedList = listOfSamples[::-1]

        # Shifting the Signal
        phaseShift = int(ShiftingValueEntry.get())
        for i in range(len(indices)):
            newIndices.append(indices[i] + phaseShift)

        # Plotting
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        plotSignal(indices, FoldedList, "Original Signal", ax1)
        plotSignal(newIndices, FoldedList, "Result", ax2)

        # Testing
        Shift_Fold_Signal("TestCases/Task6/Shifting and Folding/Output_ShifFoldedby500.txt", newIndices, FoldedList)
        # Shift_Fold_Signal("TestCases/Task6/Shifting and Folding/Output_ShiftFoldedby-500.txt", newIndices, FoldedList)
        plt.show()

    @staticmethod
    def removeDcComponentFreqDomain():
        IsPeriodic, signalType, noOfSample, indices, listOfSamples = FileReader.browse_signal_file()

        # Preforming DFT
        frequencies = []
        for i in range(len(listOfSamples)):
            summation = 0

            for j in range(len(listOfSamples)):
                angle = 2 * math.pi * i * j / len(listOfSamples)
                cosValue = math.cos(angle)
                sinValue = -math.sin(angle)

                summation += listOfSamples[j] * complex(cosValue, sinValue)

            frequencies.append(summation)

        # Make the first sample = 0
        frequencies[0] = complex(0, 0)

        # Converting the Signal from time domain to frequency domain
        amplitudeList = []
        phaseShiftList = []
        for i in range(len(frequencies)):
            amplitudeList.append(round(math.sqrt(frequencies[i].real ** 2 + frequencies[i].imag ** 2), 13))
            phaseShiftList.append(math.atan2(frequencies[i].imag, frequencies[i].real))

        # Preforming IDFT
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
            Samples.append(round(summation.real, 3))

        print("indices: ", indices)
        print("Samples: ", Samples)

        # Plot the Signal
        plt.scatter(indices, Samples, label='Data Points', color='b', marker='o')
        plt.title("DC Removed")
        plt.plot(indices, Samples, marker='o', color='b', linestyle='-')
        plt.legend()
        plt.xlim(0, 30)
        SignalSamplesAreEqual("DC Remover", "TestCases/Task6/Remove DC component/DC_component_output.txt", indices, Samples)
        plt.show()
