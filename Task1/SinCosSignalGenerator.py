# generate sinusoidal and cosinusoidal signals
import numpy as np
from matplotlib import pyplot as plt

from test import SignalSamplesAreEqual1
from utils.GlobalFunctions.plotSignal import plotSignal


class SinCosSignalGenerator:
    def __init__(self, amp_entry, freq_entry, sampling_entry, phase_entry):
        self.A = float(amp_entry.get())
        self.analog_frequency = float(freq_entry.get())
        self.sampling_frequency = float(sampling_entry.get())
        self.phase_shift = float(phase_entry.get())

    def generate_signal(self, choice):
        indices = []
        y = []
        if choice == 0:
            for i in range(int(self.sampling_frequency)):
                indices.append(i)
                y.append(self.A * np.sin(
                    2 * np.pi * self.analog_frequency * (i / int(self.sampling_frequency)) + self.phase_shift))
            # Test the signal values
            SignalSamplesAreEqual1("TestCases/Task1/Signals/Sin_Cos/SinOutput.txt", indices, y)
        else:
            for i in range(int(self.sampling_frequency)):
                indices.append(i)
                y.append(self.A * np.cos(
                    2 * np.pi * self.analog_frequency * (i / int(self.sampling_frequency)) + self.phase_shift))
            # Test the signal values
            SignalSamplesAreEqual1("TestCases/Task1/Signals/Sin_Cos/CosOutput.txt", indices, y)


        # Plot the Signal
        plotSignal(indices, y, "Sine Wave Signal" if choice == 0 else "Cosine Wave Signal", plt)
        plt.xlim(0, 30)
        plt.show()
