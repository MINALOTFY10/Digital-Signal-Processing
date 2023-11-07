from utils.FileReader import FileReader


#
# def SignalSamplesAreEqual(file_name, indices, samples):
#     expected_indices = []
#     expected_samples = []
#     with open(file_name, 'r') as f:
#         line = f.readline()
#         line = f.readline()
#         line = f.readline()
#         line = f.readline()
#         while line:
#             # process line
#             L = line.strip()
#             if len(L.split(' ')) == 2:
#                 L = line.split(' ')
#                 V1 = int(L[0])
#                 V2 = float(L[1])
#                 expected_indices.append(V1)
#                 expected_samples.append(V2)
#                 line = f.readline()
#             else:
#                 break
#
#     if len(expected_samples) != len(samples):
#         print("Test case failed, your signal have different length from the expected one")
#         return
#     for i in range(len(expected_samples)):
#         if abs(samples[i] - expected_samples[i]) < 0.01:
#             continue
#         else:
#             print("Test case failed, your signal have different values from the expected one")
#             return
#     print("Test case passed successfully")
#

# In[6]:


def AddSignalSamplesAreEqual(userFirstSignal, userSecondSignal, Your_indices, Your_samples):
    fileName = ''
    if userFirstSignal == 'Signal1.txt' and userSecondSignal == 'Signal2.txt':
        fileName = "test/Signal1+signal2.txt"  # write here path of signal1+signal2
    elif userFirstSignal == 'Signal1.txt' and userSecondSignal == 'signal3.txt':
        fileName = "test/signal1+signal3.txt"  # write here path of signal1+signal3
    x, y, z, expected_indices, expected_samples = FileReader.processing_signal(fileName)
    if (len(expected_samples) != len(Your_samples)) and (len(expected_indices) != len(Your_indices)):
        print("Addition Test case failed, your signal have different length from the expected one")
        return
    for i in range(len(Your_indices)):
        if Your_indices[i] != expected_indices[i]:
            print("Addition Test case failed, your signal have different indicies from the expected one")
            return
    for i in range(len(expected_samples)):
        if abs(Your_samples[i] - expected_samples[i]) < 0.01:
            continue
        else:
            print("Addition Test case failed, your signal have different values from the expected one")
            return
    print("Addition Test case passed successfully")


# In[ ]:


def SubSignalSamplesAreEqual(userFirstSignal, userSecondSignal, Your_indices, Your_samples):
    fileName = ''
    if userFirstSignal == 'Signal1.txt' and userSecondSignal == 'Signal2.txt':
        fileName = "test/signal1-signal2.txt"  # write here path of signal1-signal2
    elif userFirstSignal == 'Signal1.txt' and userSecondSignal == 'signal3.txt':
        fileName = "test/signal1-signal3.txt"  # write here path of signal1-signal3

    x, y, z, expected_indices, expected_samples = FileReader.processing_signal(fileName)

    if (len(expected_samples) != len(Your_samples)) and (len(expected_indices) != len(Your_indices)):
        print("Subtraction Test case failed, your signal have different length from the expected one")
        return
    for i in range(len(Your_indices)):
        if Your_indices[i] != expected_indices[i]:
            print("Subtraction Test case failed, your signal have different indicies from the expected one")
            return
    for i in range(len(expected_samples)):
        if abs(Your_samples[i] - expected_samples[i]) < 0.01:
            continue
        else:
            print("Subtraction Test case failed, your signal have different values from the expected one")
            return
    print("Subtraction Test case passed successfully")


# In[ ]:


def NormalizeSignal(MinRange, MaxRange, Your_indices, Your_samples):
    fileName = ''
    if MinRange == -1 and MaxRange == 1:
        fileName = "test/normalize of signal 1 -- output.txt"  # write here path of normalize signal 1 output.txt
    elif MinRange == 0 and MaxRange == 1:
        fileName = "test/normlize signal 2 -- output.txt"  # write here path of normalize signal 2 output.txt

    x, y, z, expected_indices, expected_samples = FileReader.processing_signal(fileName)

    if (len(expected_samples) != len(Your_samples)) and (len(expected_indices) != len(Your_indices)):
        print("Normalization Test case failed, your signal have different length from the expected one")
        return
    for i in range(len(Your_indices)):
        if Your_indices[i] != expected_indices[i]:
            print("Normalization Test case failed, your signal have different indicies from the expected one")
            return
    for i in range(len(expected_samples)):
        if abs(Your_samples[i] - expected_samples[i]) < 0.01:
            continue
        else:
            print("Normalization Test case failed, your signal have different values from the expected one")
            return
    print("Normalization Test case passed successfully")


# In[ ]:


def MultiplySignalByConst(User_Const, Your_indices, Your_samples):
    fileName = ''
    if User_Const == 5:
        fileName = "test/MultiplySignalByConstant-Signal1 - by 5.txt"  # write here path of MultiplySignalByConstant-Signal1 - by 5.txt
    elif User_Const == 10:
        fileName = "test/MultiplySignalByConstant-signal2 - by 10.txt"  # write here path of MultiplySignalByConstant-Signal2 - by 10.txt

    x, y, z, expected_indices, expected_samples = FileReader.processing_signal(fileName)
    if (len(expected_samples) != len(Your_samples)) and (len(expected_indices) != len(Your_indices)):
        print(
            "Multiply by " + str(
                User_Const) + " Test case failed, your signal have different length from the expected one")
        return
    for i in range(len(Your_indices)):
        if Your_indices[i] != expected_indices[i]:
            print(
                "Multiply by " + str(
                    User_Const) + " Test case failed, your signal have different indicies from the expected one")
            return
    for i in range(len(expected_samples)):
        if abs(Your_samples[i] - expected_samples[i]) < 0.01:
            continue
        else:
            print(
                "Multiply by " + str(
                    User_Const) + " Test case failed, your signal have different values from the expected one")
            return
    print("Multiply by " + str(User_Const) + " Test case passed successfully")


# In[ ]:

def ShiftSignalByConst(Shift_value, Your_indices, Your_samples):
    global file_name
    if Shift_value == 500:
        file_name = "test/output shifting by add 500.txt"  # write here path of output shifting by add 500.txt
    elif Shift_value == -500:
        file_name = "test/output shifting by minus 500.txt"  # write here path of output shifting by minus 500.txt

    x, y, z, expected_indices, expected_samples = FileReader.processing_signal(file_name)
    if (len(expected_samples) != len(Your_samples)) and (len(expected_indices) != len(Your_indices)):
        print(
            "Shift by " + str(
                Shift_value) + " Test case failed, your signal have different length from the expected one")
        return
    for i in range(len(Your_indices)):
        if Your_indices[i] != expected_indices[i]:
            print(
                "Shift by " + str(
                    Shift_value) + " Test case failed, your signal have different indicies from the expected one")
            return
    for i in range(len(expected_samples)):
        if abs(Your_samples[i] - expected_samples[i]) < 0.01:
            continue
        else:
            print(
                "Shift by " + Shift_value.str() + " Test case failed, your signal have different values from the expected one")
            return
    print("Shift by " + str(Shift_value) + " Test case passed successfully")


# In[ ]:


# use this twice one for Accumlation and one for Squaring
# Task name when call ACC or SQU
def SignalSamplesAreEqual(TaskName, file_name, Your_indices, Your_samples):
    expected_indices = []
    expected_samples = []
    with open(file_name, 'r') as f:
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        while line:
            # process line
            L = line.strip()
            if len(L.split(' ')) == 2:
                L = line.split(' ')
                V1 = int(L[0])
                V2 = float(L[1])
                expected_indices.append(V1)
                expected_samples.append(V2)
                line = f.readline()
            else:
                break
    if (len(expected_samples) != len(Your_samples)) and (len(expected_indices) != len(Your_indices)):
        print(TaskName + " Test case failed, your signal have different length from the expected one")
        return

    for i in range(len(Your_indices)):
        if Your_indices[i] != expected_indices[i]:
            print(TaskName + " Test case failed, your signal have different indicies from the expected one")
            return
    for i in range(len(expected_samples)):
        if abs(Your_samples[i] - expected_samples[i]) < 0.01:
            continue
        else:
            print(TaskName + " Test case failed, your signal have different values from the expected one")
            return
    print(TaskName + " Test case passed successfully")


####################################################################################################################
def QuantizationTest1(file_name, Your_EncodedValues, Your_QuantizedValues):
    expectedEncodedValues = []
    expectedQuantizedValues = []
    with open(file_name, 'r') as f:
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        while line:
            # process line
            L = line.strip()
            if len(L.split(' ')) == 2:
                L = line.split(' ')
                V2 = str(L[0])
                V3 = float(L[1])
                expectedEncodedValues.append(V2)
                expectedQuantizedValues.append(V3)
                line = f.readline()
            else:
                break
    if ((len(Your_EncodedValues) != len(expectedEncodedValues)) or (
            len(Your_QuantizedValues) != len(expectedQuantizedValues))):
        print("QuantizationTest1 Test case failed, your signal have different length from the expected one")
        return
    for i in range(len(Your_EncodedValues)):
        if (Your_EncodedValues[i] != expectedEncodedValues[i]):
            print(
                "QuantizationTest1 Test case failed, your EncodedValues have different EncodedValues from the expected one")
            return
    for i in range(len(expectedQuantizedValues)):
        if abs(Your_QuantizedValues[i] - expectedQuantizedValues[i]) < 0.01:
            continue
        else:
            print(
                "QuantizationTest1 Test case failed, your QuantizedValues have different values from the expected one")
            return
    print("QuantizationTest1 Test case passed successfully")


def QuantizationTest2(file_name, Your_IntervalIndices, Your_EncodedValues, Your_QuantizedValues, Your_SampledError):
    expectedIntervalIndices = []
    expectedEncodedValues = []
    expectedQuantizedValues = []
    expectedSampledError = []
    with open(file_name, 'r') as f:
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        while line:
            # process line
            L = line.strip()
            if len(L.split(' ')) == 4:
                L = line.split(' ')
                V1 = int(L[0])
                V2 = str(L[1])
                V3 = float(L[2])
                V4 = float(L[3])
                expectedIntervalIndices.append(V1)
                expectedEncodedValues.append(V2)
                expectedQuantizedValues.append(V3)
                expectedSampledError.append(V4)
                line = f.readline()
            else:
                break
    if (len(Your_IntervalIndices) != len(expectedIntervalIndices)
            or len(Your_EncodedValues) != len(expectedEncodedValues)
            or len(Your_QuantizedValues) != len(expectedQuantizedValues)
            or len(Your_SampledError) != len(expectedSampledError)):
        print("QuantizationTest2 Test case failed, your signal have different length from the expected one")
        return
    for i in range(len(Your_IntervalIndices)):
        if (Your_IntervalIndices[i] != expectedIntervalIndices[i]):
            print("QuantizationTest2 Test case failed, your signal have different indicies from the expected one")
            return
    for i in range(len(Your_EncodedValues)):
        if (Your_EncodedValues[i] != expectedEncodedValues[i]):
            print(
                "QuantizationTest2 Test case failed, your EncodedValues have different EncodedValues from the expected one")
            return

    for i in range(len(expectedQuantizedValues)):
        if abs(Your_QuantizedValues[i] - expectedQuantizedValues[i]) < 0.01:
            continue
        else:
            print(
                "QuantizationTest2 Test case failed, your QuantizedValues have different values from the expected one")
            return
    for i in range(len(expectedSampledError)):
        if abs(Your_SampledError[i] - expectedSampledError[i]) < 0.01:
            continue
        else:
            print("QuantizationTest2 Test case failed, your SampledError have different values from the expected one")
            return
    print("QuantizationTest2 Test case passed successfully")



