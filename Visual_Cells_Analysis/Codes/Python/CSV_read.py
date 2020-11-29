import numpy as np
import os


class Neuron:
    def __init__(self, name, files):
        self.name = name
        self.events = []
        self.files = files
        self.spike_count_rate = 0

    def add_events(self):
        for i in range(len(self.files)):
            self.events.append(np.genfromtxt("Data/"+self.files[i], delimiter=','))
        #print(self.events)

    def calc_spike_count_rate(self, frequency, stimulus_len):
        temp = 0
        for i in range(len(self.events)):
            temp += len(self.events[i])
        temp2 = 1 / frequency * stimulus_len * len(self.events)
        self.spike_count_rate = temp / temp2
        return self.spike_count_rate



def main():
    files = os.listdir("Data/")
    data = [i for i in files if ".csv" in i]
    seen = []
    neurons = []
    for i in range(len(data)):
        if data[i][0:12].count('.') == 2:
            if data[i][0:12] not in seen:
                seen.append(data[i][0:12])
                files = [data[i]]
                for j in range(i+1, len(data)):
                    if data[i][0:12] == data[j][0:12]:
                        files.append(data[j])
                neuron = Neuron(data[i][0:12], files)
                neurons.append(neuron)
        else:
            if data[i][0:10] not in seen:
                seen.append(data[i][0:10])
                files = [data[i]]
                for j in range(i+1, len(data)):
                    if data[i][0:10] == data[j][0:10]:
                        files.append(data[j])
                neuron = Neuron(data[i][0:10], files)
                neurons.append(neuron)
    for i in range(len(neurons)):
        neurons[i].add_events()
    return neurons




