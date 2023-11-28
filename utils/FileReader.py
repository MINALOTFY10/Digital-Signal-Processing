from tkinter import filedialog


class FileReader:
    @staticmethod
    def clean_and_convert(value, dataType):
        if 'f' in value:
            value = value.replace('f', '')

        if dataType == "float":
            return float(value)
        elif dataType == "int":
            return int(value)


    @staticmethod
    def processing_signal(file_path):
        with open(file_path, 'r') as file:
            arrayOfData = file.read().split('\n')

            # Time Domain
            if arrayOfData[1] == '0':
                Samples = arrayOfData[3:]
                split_list = [item.split() for item in Samples]

                sampleList = []
                indicesList = []

                for i in range(int(arrayOfData[2])):
                    indices = FileReader.clean_and_convert(split_list[i][0], "float")
                    samples = FileReader.clean_and_convert(split_list[i][1], "float")

                    indicesList.append(indices)
                    sampleList.append(samples)

                return arrayOfData[0], arrayOfData[1], arrayOfData[2], indicesList, sampleList

            # Frequency Domain
            elif arrayOfData[1] == '1':
                Samples = arrayOfData[3:]
                if ',' in arrayOfData[4]:
                    split_list = [item.split(',') for item in Samples]
                else:
                    split_list = [item.split() for item in Samples]


                amplitudeList = []
                phaseList = []

                for i in range(int(arrayOfData[2])):
                    amplitude = FileReader.clean_and_convert(split_list[i][0], "float")
                    phaseShift = FileReader.clean_and_convert(split_list[i][1], "float")

                    amplitudeList.append(amplitude)
                    phaseList.append(phaseShift)


                return arrayOfData[2], amplitudeList, phaseList


    @staticmethod
    def browse_signal_file():
        file_path = filedialog.askopenfilename(initialdir="/", title="Select a file",
                                               filetypes=(("Text files", "*.txt"), ("all files", "*.*")))

        return FileReader.processing_signal(file_path)

    @staticmethod
    def readTestFile():
        return FileReader.processing_signal("DFT/Output_Signal_DFT_A,Phase.txt")

    @staticmethod
    def readTask5TestFile():
        return FileReader.processing_signal("test/DCT_output.txt")