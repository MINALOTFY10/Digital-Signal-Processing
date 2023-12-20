import os

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
