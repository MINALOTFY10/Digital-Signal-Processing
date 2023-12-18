import math

from test import QuantizationTest1, QuantizationTest2
from utils.FileReader import FileReader
from decimal import Decimal


class Quantization:
    @staticmethod
    def handleQuantizationInput(numOfBits, numOfLevels):
        numOfBits = numOfBits.get()
        numOfLevels = numOfLevels.get()

        if numOfBits != "" and numOfLevels == "":
            numOfLevels = pow(2, int(numOfBits))
            Quantization.quantize(numOfLevels)

        elif numOfLevels != "" and numOfBits == "":
            Quantization.quantize(numOfLevels)

        else:
            print("Enter single value (bits or number of levels)")


    @staticmethod
    def quantize(numOfLevels):
        signalType, IsPeriodic, noOfSample, indices, listOfSamples = FileReader.browse_signal_file()

        # Step 1
        minValue = min(listOfSamples)
        maxvalue = max(listOfSamples)

        # Step 2
        resolution = (Decimal(str(maxvalue)) - Decimal(str(minValue))) / Decimal(numOfLevels)

        # Step 3
        # Creating the intervals
        intervals = []
        current = Decimal(str(minValue))
        while current < maxvalue:
            temp = [float(current)]
            newCurrent = current + resolution

            temp.append(float(newCurrent))
            current = newCurrent

            intervals.append(temp)

        # Creating the Midpoints Array
        midpoints = []
        for i in range(int(numOfLevels)):
            point = (Decimal(str(intervals[i][0])) + Decimal(str(intervals[i][1]))) / 2
            midpoints.append(float(point))

        interval_index = []
        quantized = []
        encoding = []
        error = []

        # finding the quantized value by getting it from the midpoint index of the interval
        for sample in listOfSamples:
            for i in range(len(intervals)):
                if intervals[i][0] <= sample <= intervals[i][1]:
                    interval_index.append(i + 1)
                    encoding.append(format(i, f'0{int(math.log(int(numOfLevels), 2))}b'))
                    quantized.append(midpoints[i])
                    error.append(float(Decimal(str(midpoints[i])) - Decimal(str(sample))))  # error = quantized-sample
                    break

        # printing Output Results
        print("midpoints: ")
        print(midpoints)
        print("intervals: ")
        print(intervals)
        print("interval_index: ")
        print(interval_index)
        print("encoding: ")
        print(encoding)
        print("quantized: ")
        print(quantized)
        print("error: ")
        print(error)

        # Testing
        QuantizationTest1("test/Test_Task3/Test 1/Quan1_Out.txt", encoding, quantized)
        # QuantizationTest2("test/Test_Task3/Test 2/Quan2_Out.txt", interval_index, encoding, quantized, error)