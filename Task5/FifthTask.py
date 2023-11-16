from utils.FileReader import FileReader


class FifthTask:
    @staticmethod
    def DCT():
        IsPeriodic, signalType, noOfSample, indices, listOfSamples = FileReader.browse_signal_file()

        print(listOfSamples)

