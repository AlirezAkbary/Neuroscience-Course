import CSV_read
import Stimulus_Mat_Read
import Q2_3
import Q3_1
import Q3_2
import Q3_3_4

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
        Q3_1.spike_triggered_neuron(neurons[i], stimulus, True)
        Q3_2.t_test_matrix(neurons[i], stimulus)
        Q3_3_4.spike_projection(neurons[i], stimulus)

