import CSV_read
import Stimulus_Mat_Read
import Q2_4
import numpy as np
import time
import matplotlib.pyplot as plt
import Q2_3
from scipy import stats
#def spike_triggered_correlation(neuron, stimulus):

stimulus = Stimulus_Mat_Read.main()
neurons = CSV_read.main()
to_be_deleted = Q2_3.main(False)
my_temp = []
for i in range(len(neurons)):
    if i not in to_be_deleted:
        my_temp.append(neurons[i])
neurons = my_temp
neuron = neurons[42]
temp = []
for i in range(len(neuron.events)):
    #print(neuron.events[i])
    this = Q2_4.Func_StimuliExtraction(stimulus, neuron.events[i])
    for j in range(len(this)):
        if len(this[j]) < 16:
            this[j] = np.pad(this[j], ((0, 16 - len(this[j])), (0,0)), mode='constant')
    temp.append(this)
correlation_matrix = np.zeros((256, 256))
start = time.time()
for i in range(1):
    for j in range(len(temp[i])):
        new = temp[i][j].reshape(256)
        for m in range(256):
            for n in range(256):
                correlation_matrix[m][n] += new[m]* new[n]
N = 0
for i in range(len(temp)):
    N += len(temp[i])
correlation_matrix /= N
end = time.time()
#%%
w, v = np.linalg.eig(correlation_matrix)

max_eig = sorted(np.absolute(w), reverse=True)[:3]
max_eig_index = []
for i in range(len(w)):
    if len(max_eig_index) == 3:
        break
    if w[i] in max_eig or -w[i] in max_eig:
        max_eig_index.append(i)
eig_one = v[max_eig_index[0]].reshape((16,16))
eig_two = v[max_eig_index[1]].reshape((16,16))
eig_three = v[max_eig_index[2]].reshape((16,16))

plt.imshow(eig_one, cmap='gray')
plt.show()
plt.imshow(eig_two, cmap='gray')
plt.show()
plt.imshow(eig_three, cmap='gray')
plt.show()



#part 4.3
#%%
max_eig_3 = sorted(np.absolute(w), reverse=True)[:2]
max_eig_index_3 = []
for i in range(len(w)):
    if len(max_eig_index_3) == 2:
        break
    if w[i] in max_eig_3 or -w[i] in max_eig_3:
        max_eig_index_3.append(i)
eig_one_3 = v[max_eig_index_3[0]]
eig_two_3 = v[max_eig_index_3[1]]
final_eig_one = []
final_eig_two = []
random_eig_one , random_eig_two = [], []
for i in range(len(temp)):
    for j in range(len(temp[i])):
        final_eig_one.append(np.dot(temp[i][j].reshape(256), eig_one_3) / np.linalg.norm(eig_one_3))
        final_eig_two.append(np.dot(temp[i][j].reshape(256), eig_two_3) / np.linalg.norm(eig_two_3))
        random_index = np.random.randint(15, len(stimulus))
        random_vector = np.array(stimulus[random_index - 15:random_index + 1]).reshape(256)
        random_eig_one.append(np.dot(random_vector, eig_one_3) / np.linalg.norm(eig_one_3))
        random_eig_two.append(np.dot(random_vector, eig_two_3) / np.linalg.norm(eig_two_3))

plt.hist(final_eig_one, bins=25, density = True)
plt.hist(random_eig_one, bins=25, density=True)
plt.show()
plt.hist(final_eig_two, bins=25, density = True)
plt.hist(random_eig_two, bins=25, density=True)
plt.show()
print(stats.ttest_ind(final_eig_one, random_eig_one))






# if __name__ == "__main__":
#     stimulus = Stimulus_Mat_Read.main()
#     neurons = CSV_read.main()
#     spike_triggered_correlation(neurons[24], stimulus)