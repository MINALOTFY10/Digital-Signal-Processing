from utils.FileReader import FileReader


class SeventhTask:

    @staticmethod
    def Convolution():
        IsPeriodic, signalType, noOfSample, indices, listOfSamples = FileReader.browse_signal_file()
