import numpy as np
import Q2_4
import CSV_read
import Stimulus_Mat_Read
import matplotlib.pyplot as plt
import Q2_3


def spike_triggered_neuron(neuron, stimulus, plot):#for a neuron
    temp = []
    for i in range(len(neuron.events)):
        temp.append(Spike_triggered_average(Q2_4.Func_StimuliExtraction(stimulus, neuron.events[i])))
    #print(temp)
    answer = np.mean(temp, axis=0)
    if plot:
        plt.imshow(answer, cmap="gray")
        plt.title(neuron.name)
        plt.show()
    return answer
    #print(answer)

    pass


def Spike_triggered_average(spike_stimulus):#just for one experiment
    for i in range(len(spike_stimulus)):
        if len(spike_stimulus[i]) < 16:
            #print(len(spike_stimulus[i]), i)
            spike_stimulus[i] = np.pad(spike_stimulus[i], ((0, 16 - len(spike_stimulus[i])),(0, 0)), mode="constant")
    #print(np.mean(spike_stimulus, axis=0))
    return np.mean(spike_stimulus, axis=0)


if __name__ == "__main__":
    stimulus = Stimulus_Mat_Read.main()
    #print(len(stimulus))
    neurons = CSV_read.main()
    to_be_deleted = Q2_3.main(False)
    my_temp = []
    for i in range(len(neurons)):
        if i not in to_be_deleted:
            my_temp.append(neurons[i])
    neurons = my_temp
    #spike_stimulus = Q2_4.Func_StimuliExtraction(stimulus, neurons[1].events[0])
    # for i in range(len(neurons)):
    #     if neurons[i].name == "000412":
    #         print(i)
    #         break
    #print(spike_stimulus[3])
    #Spike_triggered_average(spike_stimulus)
    spike_triggered_neuron(neurons[42], stimulus, True)


