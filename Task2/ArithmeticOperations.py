from matplotlib import pyplot as plt

from utils.FileReader import FileReader
from test import AddSignalSamplesAreEqual, SubSignalSamplesAreEqual, MultiplySignalByConst, SignalSamplesAreEqual, \
    ShiftSignalByConst, NormalizeSignal
from utils.plotSignal import plotSignal


class ArithmeticOperations:
    @staticmethod
    def Addition(signals_number_entry):
        # read files for the given number of signals
        signals = []
        max_samples = 0
        for i in range(int(signals_number_entry.get())):
            signalType, IsPeriodic, noOfSample, indices, listOfSamples = FileReader.browse_signal_file()
            signals.append((signalType, IsPeriodic, noOfSample, indices, listOfSamples))
            # check the max size of the signals
            max_samples = max(max_samples, int(noOfSample))

        # adjust signal sizes
        for signal in signals:
            # check if the size of listOfSamples less than size max_samples put zeros to make the signals equal
            if len(signal[4]) < max_samples:
                signal[4].extend([0] * (max_samples - len(signal[4])))

        # perform addition
        resultSignal = [0] * max_samples
        for i in range(max_samples):
            for signal in signals:
                # adding index of i of listOfSamples from each signal from signals to the resultSignal
                resultSignal[i] += int(signal[4][i])

        # plotting
        fig, axs = plt.subplots(1, len(signals) + 1, figsize=(12, 5))
        x = list(range(max_samples))
        for i in range(len(signals)):
            plotSignal(x, signals[i][4], axs[i])
        plotSignal(x, resultSignal, axs[-1])
        # Testing
        # AddSignalSamplesAreEqual('Signal1.txt', 'Signal2.txt', x, resultSignal)
        AddSignalSamplesAreEqual('Signal1.txt', 'signal3.txt', x, resultSignal)
        # SignalSamplesAreEqual("test/Signal1+signal2.txt", x, resultSignal)
        plt.show()

    @staticmethod
    def subtraction(signals_num_entry):
        # read files for the given number of signals
        signals = []
        max_samples = 0
        for i in range(int(signals_num_entry.get())):
            signalType, IsPeriodic, noOfSample, indices, listOfSamples = FileReader.browse_signal_file()
            signals.append((signalType, IsPeriodic, noOfSample, indices, listOfSamples))
            # check the max size of the signals
            max_samples = max(max_samples, int(noOfSample))

        # adjust signal sizes
        for signal in signals:
            # check if the size of listOfSamples less than size max_samples put zeros to make the signals equal
            if len(signal[4]) < max_samples:
                signal[4].extend([0] * (max_samples - len(signal[4])))

        # perform subtraction
        resultSignal = [0] * max_samples
        for i in range(max_samples):
            for signal in signals:
                if signal == signals[0]:
                    resultSignal[i] += int(signal[4][i])
                else:
                    # adding index of i of listOfSamples from each signal from signals to the resultSignal
                    resultSignal[i] -= int(signal[4][i])

        for i in range(max_samples):
            resultSignal[i] = abs(resultSignal[i])

        # plotting
        fig, axs = plt.subplots(1, len(signals) + 1, figsize=(12, 5))
        x = list(range(max_samples))
        for i in range(len(signals)):
            plotSignal(x, signals[i][4], axs[i])
        plotSignal(x, resultSignal, axs[-1])
        # Testing
        # SubSignalSamplesAreEqual('Signal1.txt', 'Signal2.txt', x, resultSignal)
        SubSignalSamplesAreEqual('Signal1.txt', 'signal3.txt', x, resultSignal)
        plt.show()


    @staticmethod
    def multiplication(entry):
        # read one file
        signalType1, IsPeriodic1, noOfSample1, indices1, listOfSamples1 = FileReader.browse_signal_file()
        resultSignal = []
        for i in range(len(listOfSamples1)):
            resultSignal.append(int(listOfSamples1[i]) * int(entry.get()))

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

        plotSignal(indices1, listOfSamples1, ax1)
        plotSignal(indices1, resultSignal, ax2)
        # Testing
        MultiplySignalByConst(int(entry.get()), indices1, resultSignal)
        plt.show()

    @staticmethod
    def squaring():
        # read one file
        signalType1, IsPeriodic1, noOfSample1, indices1, listOfSamples1 = FileReader.browse_signal_file()
        resultSignal = []
        for i in range(len(listOfSamples1)):
            resultSignal.append(int(listOfSamples1[i]) * int(listOfSamples1[i]))

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

        plotSignal(indices1, listOfSamples1, ax1)
        plotSignal(indices1, resultSignal, ax2)
        # Testing
        SignalSamplesAreEqual("SQU", 'test/Output squaring signal 1.txt', indices1, resultSignal)
        plt.show()

    @staticmethod
    def shifting(entry):
        # read one file
        signalType1, IsPeriodic1, noOfSample1, indices1, listOfSamples1 = FileReader.browse_signal_file()
        resultSignal = []
        phaseShift = 0

        phaseShift = int(entry.get()) * -1

        print(phaseShift)
        for i in range(len(indices1)):
            resultSignal.append(indices1[i] + phaseShift)

        print(resultSignal)
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

        plotSignal(indices1, listOfSamples1, ax1)
        plotSignal(resultSignal, listOfSamples1, ax2)

        # Testing
        ShiftSignalByConst(int(entry.get()), resultSignal, listOfSamples1)

        plt.show()

    @staticmethod
    def normalization(maxEntry, minEntry):
        # read one file
        signalType1, IsPeriodic1, noOfSample1, indices1, listOfSamples1 = FileReader.browse_signal_file()
        resultSignal = []

        for i in range(len(listOfSamples1)):
            scaled_data = (int(listOfSamples1[i]) - int(min(listOfSamples1))) / (
                    int(max(listOfSamples1)) - int(min(listOfSamples1))) * (
                                  int(maxEntry.get()) - int(minEntry.get())) + int(minEntry.get())
            resultSignal.append(scaled_data)

        print(resultSignal)
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        plotSignal(indices1, listOfSamples1, ax1)
        plotSignal(indices1, resultSignal, ax2)
        # Testing (-1,1 Signal1) (0, 1 Signal2)
        NormalizeSignal(int(minEntry.get()), int(maxEntry.get()), indices1, resultSignal)
        plt.show()

    @staticmethod
    def accumulation():
        # read one file
        signalType1, IsPeriodic1, noOfSample1, indices1, listOfSamples1 = FileReader.browse_signal_file()
        resultSignal = []
        summation = 0

        for i in range(len(listOfSamples1)):
            resultSignal.append(int(listOfSamples1[i]) + summation)
            summation += int(listOfSamples1[i])

        print(resultSignal)
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

        plotSignal(indices1, listOfSamples1, ax1)
        plotSignal(indices1, resultSignal, ax2)
        # Testing
        SignalSamplesAreEqual("ACC", 'test/output accumulation for signal1.txt', indices1, resultSignal)
        plt.show()