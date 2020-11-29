import Q2_4
import CSV_read
import Stimulus_Mat_Read
import numpy as np
import Q3_1
import matplotlib.pyplot as plt
from scipy import stats
import Q2_3

def spike_projection(neuron, stimulus):
    #3.3
    project_vec = Q3_1.spike_triggered_neuron(neuron, stimulus, False)
    project_vec = project_vec.reshape(256)
    temp = []
    for i in range(len(neuron.events)):
        this = Q2_4.Func_StimuliExtraction(stimulus, neuron.events[i])
        for j in range(len(this)):
            if len(this[j]) < 16:
                this[j] = np.pad(this[j], ((0, 16 - len(this[j])), (0, 0)), mode='constant')
        temp.append(this)
    final = []
    random_sample = []
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            random_index = np.random.randint(15, len(stimulus))
            random_vector = np.array(stimulus[random_index-15:random_index+1]).reshape(256)

            x = temp[i][j].reshape(256)
            y = np.dot(x, project_vec)
            y = y / np.linalg.norm(project_vec)
            final.append(y)
            random_sample.append(np.dot(random_vector, project_vec) / np.linalg.norm(project_vec))

    plt.hist(final, bins=25, density = True)
    plt.hist(random_sample, bins=25, density=True)
    plt.title(neuron.name)
    plt.show()

    #3.4
    print(neuron.name, ":", stats.ttest_ind(final, random_sample))


    #3.5
    mine, random_samp = np.array(final), np.array(random_sample)
    mean_1, mean_2 = np.mean(mine), np.mean(random_samp)
    threshold = (mean_1 + mean_2) / 2
    counter , success = 0, 0
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            x = temp[i][j].reshape(256)
            y = np.dot(x, project_vec)
            y = y / np.linalg.norm(project_vec)
            counter += 1
            if y > threshold and mean_1 > threshold or y < threshold and mean_1 < threshold:
                success += 1
    print(neuron.name, "Success rate:", success/ counter)
    return final, random_sample


if __name__ == "__main__":
    stimulus = Stimulus_Mat_Read.main()
    neurons = CSV_read.main()
    to_be_deleted = Q2_3.main(False)
    my_temp = []
    for i in range(len(neurons)):
        if i not in to_be_deleted:
            my_temp.append(neurons[i])
    neurons = my_temp
    final, random_samp = spike_projection(neurons[8], stimulus)

