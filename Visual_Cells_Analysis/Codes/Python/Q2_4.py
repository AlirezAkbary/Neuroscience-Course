import CSV_read
import Stimulus_Mat_Read
import math
import Q2_3
frequency =  59.721395


def Func_StimuliExtraction(stimulus, event):
    temp = []
    for i in range(len(event)):
        temp.append(math.floor(event[i] * frequency / 10000))
    #print(temp)
    answer = []
    #print(len(temp), "akbar")
    for i in range(len(temp)):

        if temp[i] < 15:
            answer.append(stimulus[0:temp[i]+1])
        else:
            answer.append(stimulus[temp[i]-15:temp[i]+1])
    return answer


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
    Func_StimuliExtraction(stimulus, neurons[1].events[0])

