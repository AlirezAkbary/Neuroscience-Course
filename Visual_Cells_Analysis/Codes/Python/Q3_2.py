import Q2_4
import CSV_read
import Stimulus_Mat_Read
import numpy as np
from scipy import stats
from PIL import Image
import matplotlib.pyplot as plt
import Q2_3


def t_test_matrix(neuron, stimulus):
    p_value = np.zeros((16,16))
    for i in range(16):
        for j in range(16):
            the = t_test_element(neuron, i, j, stimulus)
            #print(the)
            p_value[i][j] = the[1]
    #print(p_value)
    plt.imshow(p_value, cmap="gray")
    plt.title(neuron.name)
    plt.show()



def t_test_element(neuron, m, n, stimulus):
    temp = []
    for i in range(len(neuron.events)):
        this = Q2_4.Func_StimuliExtraction(stimulus, neuron.events[i])
        for j in range(len(this)):
            if len(this[j]) < 16:
                this[j] = np.pad(this[j], ((0, 16-len(this[j])), (0, 0)), mode='constant')
        temp.append(this)
    datas = []
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            datas.append(temp[i][j][m][n])
    return stats.ttest_1samp(datas, 0)
    #print(stats.ttest_1samp(datas, 0))
    pass


if __name__ == "__main__":
    stimulus = Stimulus_Mat_Read.main()
    neurons = CSV_read.main()

    to_be_deleted = Q2_3.main(False)
    my_temp = []
    for i in range(len(neurons)):
        if i not in to_be_deleted:
            my_temp.append(neurons[i])
    neurons = my_temp
    for i in range(len(neurons)):
        print(i, neurons[i].name)
    t_test_matrix(neurons[1], stimulus)