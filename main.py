import math
import tkinter as tk

import matplotlib.pyplot as plt
from decimal import Decimal

from Practical_Task.Ninth_task import NinthTask
from Task1.DiscreteContinuousSignalDisplayer import DiscreteContinuousSignalDisplayer
from Task1.SinCosSignalGenerator import SinCosSignalGenerator
# from Task2 import ArithmeticOperations

from Task2.ArithmeticOperations import ArithmeticOperations
from Task3.Quantization import Quantization
from Task4.FourthTask import FourthTask
from Task5.FifthTask import FifthTask
from Task6.SixthTask import SixthTask
from Task7.SeventhTask import SeventhTask
from Task8.EighthTask import EighthTask
from test import QuantizationTest1, QuantizationTest2
from utils.FileReader import FileReader


# Task 1.1 Read and display signal in continuous and discrete form
def display_signal():
    signalType, IsPeriodic, noOfSample, indices, listOfSamples = FileReader.browse_signal_file()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    DiscreteContinuousSignalDisplayer.display_continuous_signal(listOfSamples, ax1)
    DiscreteContinuousSignalDisplayer.display_discrete_signal(listOfSamples, ax2)

    plt.show()


# Task 1.2 Generate Sin & Cos Signals
def generate_signals(choice, amp_entry, freq_entry, sampling_entry, phase_entry):
    signal_generator = SinCosSignalGenerator(amp_entry, freq_entry, sampling_entry, phase_entry)
    signal_generator.generate_signal(choice)


# Task 2 Math Operations
def ArithmeticOperationsHandler(firstEntry, SecondEntry, choice):
    if choice == 0:
        ArithmeticOperations.Addition(firstEntry)
    elif choice == 1:
        ArithmeticOperations.subtraction(firstEntry)
    elif choice == 2:
        ArithmeticOperations.multiplication(firstEntry)
    elif choice == 3:
        ArithmeticOperations.squaring()
    elif choice == 4:
        ArithmeticOperations.shifting(firstEntry)
    elif choice == 5:
        ArithmeticOperations.normalization(firstEntry, SecondEntry)
    elif choice == 6:
        ArithmeticOperations.accumulation()


# Task 3 Quantization
def CheckParameters(numOfBits, numOfLevels):
    Quantization.handleQuantizationInput(numOfBits, numOfLevels)


# Task 4
def Task4(index, amplitude, phase, freq, command):
    if command == "DFT":
        FourthTask.DiscreteFourierTransform(freq.get())
    elif command == "Edit":
        FourthTask.EditAmplitudePhaseOfSignal(index.get(), amplitude.get(), phase.get(), freq.get())
    elif command == "IDFT":
        FourthTask.InverseDiscreteFourierTransform()


def Task5(command, coefficients):
    if command == "DCT":
        FifthTask.DCT(coefficients.get())
    elif command == "DCRemove":
        FifthTask.RemoveDcComponent()


def Task6(command, windowSizeEntry, ShiftingValueEntry):
    if command == "Smoothing":
        SixthTask.Smoothing(windowSizeEntry.get())
    elif command == "Sharpening":
        SixthTask.Sharpening()
    elif command == "ShiftingSignal":
        SixthTask.Shifting(ShiftingValueEntry)
    elif command == "FoldingSignal":
        SixthTask.FoldingSignal()
    elif command == "ShiftingFoldedSignal":
        SixthTask.ShiftingFoldedSignal(ShiftingValueEntry)
    elif command == "DCRemove":
        SixthTask.removeDcComponentFreqDomain()


def Task7(command):
    if command == "Convolution":
        SeventhTask.Convolution()


def Task8(command):
    if command == "Correlation":
        EighthTask.Correlation()


def Task9(command):
    if command == "Fast Auto Correlation":
        NinthTask.FastAutoCorrelation()
    elif command == "Fast Cross Correlation":
        NinthTask.FastCrossCorrelation()
    elif command == "Fast Convolution":
        NinthTask.FastConvolution()


class AppWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.phase_entry = None
        self.sampling_entry = None
        self.freq_entry = None
        self.amp_entry = None
        self.geometry('900x750')
        self.title("DSP")
        self.configure(bg='lightgrey')
        self.font_style = ("Arial", 12)
        self.create_ui_components()

    # Task 1 GUI
    def task_one_window(self):
        new_window = tk.Toplevel(self)
        new_window.title("Task 1")
        new_window.geometry("900x750")

        ### 1.1 Task GUI Components
        button = tk.Button(new_window, text="Read the file", command=display_signal, bg='lightblue', cursor="hand2",
                           font=self.font_style)
        button.place(x=0, y=0)

        ### 1.2 Task GUI Components
        tk.Label(new_window, text="Amplitude (A): ", font=self.font_style, bg='lightgrey').pack()
        new_window.amp_entry = tk.Entry(new_window, width=35)
        new_window.amp_entry.pack()

        tk.Label(new_window, text="Analog Frequency: ", font=self.font_style, bg='lightgrey').pack()
        new_window.freq_entry = tk.Entry(new_window, width=35)
        new_window.freq_entry.pack()

        tk.Label(new_window, text="Sampling Frequency: ", font=self.font_style, bg='lightgrey').pack()
        new_window.sampling_entry = tk.Entry(new_window, width=35)
        new_window.sampling_entry.pack()

        tk.Label(new_window, text="Phase Shift: ", font=self.font_style, bg='lightgrey').pack()
        new_window.phase_entry = tk.Entry(new_window, width=35)
        new_window.phase_entry.pack()

        menu = tk.Menu(new_window)
        new_window.config(menu=menu)

        signal_menu = tk.Menu(menu, tearoff=0, font=("Arial", 12))
        menu.add_cascade(label="Signal Generation", menu=signal_menu)

        signal_menu.add_command(label="Sine Wave",
                                command=lambda: generate_signals(0, new_window.amp_entry,
                                                                 new_window.freq_entry,
                                                                 new_window.sampling_entry,
                                                                 new_window.phase_entry))
        signal_menu.add_command(label="Cosine Wave",
                                command=lambda: generate_signals(1, new_window.amp_entry,
                                                                 new_window.freq_entry,
                                                                 new_window.sampling_entry,
                                                                 new_window.phase_entry))

    # Task 2 GUI
    def task_two_window(self):
        task2new_window = tk.Toplevel(self)
        task2new_window.title("Task 2")
        task2new_window.geometry("900x750")

        # Addition
        task2new_window.add_label = tk.Label(task2new_window, text="Number of signals:", font=('Arial', 12))
        task2new_window.add_label.place(x=190, y=35)
        task2new_window.signals_number_entry = tk.Entry(task2new_window, width=4)
        task2new_window.signals_number_entry.place(x=325, y=40)
        button = tk.Button(task2new_window, text="Addition",
                           command=lambda: ArithmeticOperationsHandler(task2new_window.signals_number_entry, "", 0),
                           width=20, height=3)
        button.pack(pady=20)

        # Subtraction
        task2new_window.subtract_label = tk.Label(task2new_window, text="Number of signals:", font=('Arial', 12))
        task2new_window.subtract_label.place(x=190, y=130)
        task2new_window.signals_num_entry = tk.Entry(task2new_window, width=4)
        task2new_window.signals_num_entry.place(x=325, y=135)
        button = tk.Button(task2new_window, text="Subtraction",
                           command=lambda: ArithmeticOperationsHandler(task2new_window.signals_num_entry, "", 1),
                           width=20, height=3)
        button.pack(pady=20)

        # Multiplication
        task2new_window.subtract_label = tk.Label(task2new_window, text="Constant:", font=('Arial', 12))
        task2new_window.subtract_label.place(x=255, y=225)
        task2new_window.const_entry = tk.Entry(task2new_window, width=4)
        task2new_window.const_entry.pack(pady=20)
        task2new_window.const_entry.place(x=325, y=230)
        button = tk.Button(task2new_window, text="Multiplication",
                           command=lambda: ArithmeticOperationsHandler(task2new_window.const_entry, "", 2), width=20,
                           height=3)
        button.pack(pady=20)

        # Squaring
        button = tk.Button(task2new_window, text="Squaring",
                           command=lambda: ArithmeticOperationsHandler("", "", 3), width=20,
                           height=3)
        button.pack(pady=20)

        # Shifting
        task2new_window.subtract_label = tk.Label(task2new_window, text="Constant:", font=('Arial', 12))
        task2new_window.subtract_label.place(x=240, y=415)
        task2new_window.Shifting_entry = tk.Entry(task2new_window, width=7)
        task2new_window.Shifting_entry.pack(pady=20)
        task2new_window.Shifting_entry.place(x=310, y=420)
        button = tk.Button(task2new_window, text="Shifting",
                           command=lambda: ArithmeticOperationsHandler(task2new_window.Shifting_entry, "", 4), width=20,
                           height=3)
        button.pack(pady=20)

        # Normalization
        task2new_window.min_label = tk.Label(task2new_window, text="Minimum Entry:", font=('Arial', 12))
        task2new_window.min_label.pack()
        task2new_window.min_label.place(x=205, y=495)
        task2new_window.min_entry = tk.Entry(task2new_window, width=5)
        task2new_window.min_entry.pack(pady=20)
        task2new_window.min_entry.place(x=320, y=500)

        task2new_window.max_label = tk.Label(task2new_window, text="Maximum Entry:", font=('Arial', 12))
        task2new_window.max_label.pack()
        task2new_window.max_label.place(x=205, y=535)
        task2new_window.max_entry = tk.Entry(task2new_window, width=5)
        task2new_window.max_entry.pack(pady=20)
        task2new_window.max_entry.place(x=320, y=540)

        button = tk.Button(task2new_window, text="Normalization",
                           command=lambda: ArithmeticOperationsHandler(task2new_window.max_entry,
                                                                       task2new_window.min_entry, 5),
                           width=20,
                           height=3)
        button.pack(pady=20)

        # Accumulation
        button = tk.Button(task2new_window, text="Accumulation",
                           command=lambda: ArithmeticOperationsHandler("", "", 6), width=20,
                           height=3)
        button.pack(pady=20)

    # Task 3 GUI
    def task_three_window(self):
        task3new_window = tk.Toplevel(self)
        task3new_window.title("Task 3")
        task3new_window.geometry("900x750")

        task3new_window.add_label = tk.Label(task3new_window, text="Enter number of bits or number of levels",
                                             font=('Arial', 12))
        task3new_window.add_label.place(x=(750 - 100) / 2, y=35)

        task3new_window.add_label = tk.Label(task3new_window, text="Number of bits:", font=('Arial', 12))
        task3new_window.add_label.place(x=(750 / 2) - 62, y=120)
        task3new_window.num_bits_entry = tk.Entry(task3new_window, width=20)
        task3new_window.num_bits_entry.place(x=(750 / 2) - 60, y=150)

        task3new_window.add_label = tk.Label(task3new_window, text="Number of levels:", font=('Arial', 12))
        task3new_window.add_label.place(x=(750 / 2) + 108, y=120)
        task3new_window.num_levels_entry = tk.Entry(task3new_window, width=20)
        task3new_window.num_levels_entry.place(x=(750 / 2) + 110, y=150)

        button = tk.Button(task3new_window, text="Compute",
                           command=lambda: CheckParameters(task3new_window.num_bits_entry,
                                                           task3new_window.num_levels_entry),
                           width=20, height=3)
        button.pack(pady=(200, 150))

    # Task 4 GUI
    def task_four_window(self):
        task4new_window = tk.Toplevel(self)
        task4new_window.title("Task 4")
        task4new_window.geometry("900x750")

        task4new_window.label = tk.Label(task4new_window, text="Sampling Frequency:", font=('Arial', 12))
        task4new_window.label.pack(pady=0)

        task4new_window.frequency_entry = tk.Entry(task4new_window, width=20)
        task4new_window.frequency_entry.pack()

        button = tk.Button(task4new_window, text="Apply Fourier transform",
                           command=lambda: Task4("", "", "", task4new_window.frequency_entry, "DFT"),
                           width=30, height=3)
        button.pack(pady=20)

        # The Edit Option
        task4new_window.label = tk.Label(task4new_window, text="Index:", font=('Arial', 12))
        task4new_window.label.place(x=(748 / 2), y=250)
        task4new_window.index_entry = tk.Entry(task4new_window, width=20)
        task4new_window.index_entry.place(x=(750 / 2), y=270)

        task4new_window.label = tk.Label(task4new_window, text="New Amplitude:", font=('Arial', 12))
        task4new_window.label.place(x=(748 / 2), y=290)
        task4new_window.amplitude_entry = tk.Entry(task4new_window, width=20)
        task4new_window.amplitude_entry.place(x=(750 / 2), y=310)

        task4new_window.label = tk.Label(task4new_window, text="New Phase Shift in rad:", font=('Arial', 12))
        task4new_window.label.place(x=(748 / 2), y=330)
        task4new_window.phase_shift_entry = tk.Entry(task4new_window, width=30)
        task4new_window.phase_shift_entry.place(x=(750 / 2), y=350)

        button = tk.Button(task4new_window, text="Edit Signal in the Polar From",
                           command=lambda: Task4(task4new_window.index_entry, task4new_window.amplitude_entry,
                                                 task4new_window.phase_shift_entry, task4new_window.frequency_entry,
                                                 "Edit"
                                                 ),
                           width=30, height=3)
        button.pack(pady=235)

        button = tk.Button(task4new_window, text="Apply Inverse Fourier transform",
                           command=lambda: Task4("", "", "", "", "IDFT"),
                           width=30, height=3)
        button.pack(pady=20)

    def task_five_window(self):
        task5new_window = tk.Toplevel(self)
        task5new_window.title("Task 5")
        task5new_window.geometry("900x750")

        task5new_window.label = tk.Label(task5new_window, text="m coefficients", font=('Arial', 12))
        task5new_window.label.pack(pady=0)

        task5new_window.coefficients_entry = tk.Entry(task5new_window, width=20)
        task5new_window.coefficients_entry.pack()

        button = tk.Button(task5new_window, text="Apply Discrete Cosine transform",
                           command=lambda: Task5("DCT", task5new_window.coefficients_entry),
                           width=30, height=3)
        button.pack(pady=20)
        button = tk.Button(task5new_window, text="Remove DC component",
                           command=lambda: Task5("DCRemove", ""),
                           width=30, height=3)
        button.pack(pady=20)

    def task_six_window(self):
        task_six_window = tk.Toplevel(self)
        task_six_window.title("Task 6")
        task_six_window.geometry("900x750")

        # 1) Smoothing
        task_six_window.label = tk.Label(task_six_window, text="Window size :", font=('Arial', 12))
        task_six_window.label.place(x=90, y=46)

        task_six_window.Window_size = tk.Entry(task_six_window, width=20)
        task_six_window.Window_size.place(x=200, y=50)
        button = tk.Button(task_six_window, text="Smoothing (moving average)",
                           command=lambda: Task6("Smoothing", task_six_window.Window_size, ""),
                           width=30, height=3)
        button.pack(pady=20)
        # 2) Sharpening
        button = tk.Button(task_six_window, text="Sharpening",
                           command=lambda: Task6("Sharpening", "", ""),
                           width=30, height=3)
        button.pack(pady=20)
        # 3) Shifting signal by K steps
        task_six_window.label = tk.Label(task_six_window, text="K Steps :", font=('Arial', 12))
        task_six_window.label.place(x=100, y=227)

        task_six_window.shift = tk.Entry(task_six_window, width=20)
        task_six_window.shift.place(x=200, y=230)
        button = tk.Button(task_six_window, text="Shifting Signal",
                           command=lambda: Task6("ShiftingSignal", "", task_six_window.shift),
                           width=30, height=3)
        button.pack(pady=20)
        # 4) Folding Signal
        button = tk.Button(task_six_window, text="Folding Signal",
                           command=lambda: Task6("FoldingSignal", "", ""),
                           width=30, height=3)
        button.pack(pady=20)
        # 5) Shifting Folded signal by K steps
        task_six_window.label = tk.Label(task_six_window, text="K Steps :", font=('Arial', 12))
        task_six_window.label.place(x=100, y=420)

        task_six_window.shiftFold = tk.Entry(task_six_window, width=20)
        task_six_window.shiftFold.place(x=200, y=420)
        button = tk.Button(task_six_window, text="Shifting Folded Signal",
                           command=lambda: Task6("ShiftingFoldedSignal", "", task_six_window.shiftFold),
                           width=30, height=3)
        button.pack(pady=20)
        # 6) Remove DC component
        button = tk.Button(task_six_window, text="Remove DC component Freq Domain",
                           command=lambda: Task6("DCRemove", "", ""),
                           width=30, height=3)
        button.pack(pady=20)

    def task_seven_window(self):
        task_seven_window = tk.Toplevel(self)
        task_seven_window.title("Task 7")
        task_seven_window.geometry("900x750")

        # 1) Convoluted Signal
        button = tk.Button(task_seven_window, text="Convolution",
                           command=lambda: Task7("Convolution"),
                           width=30, height=3)
        button.pack(pady=20)

    def task_eight_window(self):
        task_seven_window = tk.Toplevel(self)
        task_seven_window.title("Task 8")
        task_seven_window.geometry("900x750")

        # 1) Convoluted Signal
        button = tk.Button(task_seven_window, text="Correlation",
                           command=lambda: Task8("Correlation"),
                           width=30, height=3)
        button.pack(pady=20)

    def task_nine_window(self):
        task_nine_window = tk.Toplevel(self)
        task_nine_window.title("Task 8")
        task_nine_window.geometry("900x750")

        # 1) Fast Convolution Signal
        button = tk.Button(task_nine_window, text="Fast Convolution",
                           command=lambda: Task9("Fast Convolution"),
                           width=30, height=3)
        button.pack(pady=20)

        # 2) Fast Auto Correlation Signal
        button = tk.Button(task_nine_window, text="Fast Auto Correlation",
                           command=lambda: Task9("Fast Auto Correlation"),
                           width=30, height=3)
        button.pack(pady=20)

        # 3) Fast Cross Correlation Signal
        button = tk.Button(task_nine_window, text="Fast Cross Correlation",
                           command=lambda: Task9("Fast Cross Correlation"),
                           width=30, height=3)

        button.pack(pady=20)

    def create_ui_components(self):
        # A button To open Task 1 Window
        button = tk.Button(self, text="Task 1", command=self.task_one_window, width=20, height=3)
        button.pack(pady=15)
        button = tk.Button(self, text="Task 2", command=self.task_two_window, width=20, height=3)
        button.pack(pady=15)
        button = tk.Button(self, text="Task 3", command=self.task_three_window, width=20, height=3)
        button.pack(pady=15)
        button = tk.Button(self, text="Task 4", command=self.task_four_window, width=20, height=3)
        button.pack(pady=15)
        button = tk.Button(self, text="Task 5", command=self.task_five_window, width=20, height=3)
        button.pack(pady=15)
        button = tk.Button(self, text="Task 6", command=self.task_six_window, width=20, height=3)
        button.pack(pady=15)
        button = tk.Button(self, text="Task 7", command=self.task_seven_window, width=20, height=3)
        button.pack(pady=15)
        button = tk.Button(self, text="Task 8", command=self.task_eight_window, width=20, height=3)
        button.pack(pady=15)
        button = tk.Button(self, text="Task 9", command=self.task_nine_window, width=20, height=3)
        button.pack(pady=15)


if __name__ == '__main__':
    app = AppWindow()
    app.mainloop()
