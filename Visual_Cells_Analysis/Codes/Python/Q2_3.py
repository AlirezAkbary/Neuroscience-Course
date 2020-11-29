import numpy as np
import CSV_read
import Stimulus_Mat_Read
import matplotlib.pyplot as plt
frequency =  59.721395


def main(plot):#plot is a boolean determines to plot the histogram
    stimulus = Stimulus_Mat_Read.main()
    neurons = CSV_read.main()
    for i in range(len(neurons)):
        neurons[i].calc_spike_count_rate(frequency, len(stimulus))
    if plot:
        print("Neuron with spike count rate less than 2:")
    to_be_deleted = []
    for i in range(len(neurons)):
        if neurons[i].spike_count_rate < 2:
            to_be_deleted.append(i)
            if plot:
                print(neurons[i].name)
    x = [i.name for i in neurons]
    y = [i.spike_count_rate for i in neurons]
    if plot:
        plt.bar(x, height=y)
        plt.show()
    return to_be_deleted


if __name__ == "__main__":
    main(True)

