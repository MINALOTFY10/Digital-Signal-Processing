import cmath
import math
from cmath import cos, sin

import mpmath

from utils.FileReader import FileReader
from decimal import Decimal


class FourthTask:
    @staticmethod
    def DiscreteFourierTransform():
        signalType, IsPeriodic, noOfSample, indices, listOfSamples = FileReader.browse_signal_file()

        # i = k
        # j = n
        frquencyies = []
        for i in range(len(listOfSamples)):
            realValue = 0
            imagValue = 0
            for j in range(len(listOfSamples)):
                cosValue = cos((2 * math.pi * i * j) / len(listOfSamples))
                if cosValue == 6.12323399573677e-17:
                    cosValue = 0

                sinValue = -sin((2 * math.pi * i * j) / len(listOfSamples))
                if sinValue == 1.22464679914735e-16:
                    sinValue = 0

                realValue += listOfSamples[j] * cosValue
                imagValue += listOfSamples[j] * sinValue

            print(complex(realValue, imagValue))
            frquencyies.append(complex(realValue, imagValue))

        amplitudeList = []
        phaseShiftList = []

        for i in range(len(frquencyies)):
            amplitudeList.append(math.sqrt(frquencyies[i].real ** 2 + frquencyies[i].imag ** 2))
            # print("----------------------------")
            # print(frquencyies[i].imag)
            # print(frquencyies[i].real)
            # print("----------------------------")

            phaseShiftList.append(math.atan(frquencyies[i].imag / frquencyies[i].real))

        print(amplitudeList)
        print(phaseShiftList)

    @staticmethod
    def InverseDiscreteFourierTransform():
        noOfSample, amplitudeList, phaseShiftList = FileReader.browse_signal_file()
