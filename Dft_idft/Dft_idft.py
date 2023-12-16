
import math

class DftIdft:
    @staticmethod
    def Dft(listOfSamples):
        frequencies = []
        for i in range(len(listOfSamples)):
            summation = 0

            for j in range(len(listOfSamples)):
                angle = 2 * math.pi * i * j / len(listOfSamples)
                cosValue = math.cos(angle)
                sinValue = -math.sin(angle)

                summation += listOfSamples[j] * complex(cosValue, sinValue)

            frequencies.append(summation)

        return  frequencies


    @staticmethod
    def Idft(amplitudeList, phaseShiftList):
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

        return  indices, Samples