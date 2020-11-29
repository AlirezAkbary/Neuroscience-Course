function answer=Func_ReadData(neuron_name)
neuron_dir = dir(['/Users/alireza/Desktop/University/97-98\ Spring/Neuroscience/Bonus_Project/Bonus_Project/Data/Spike_and_Log_Files ' neuron_name]);
answer=[];
for i=3:length(neuron_dir)    
    if contains(upper(neuron_dir(i).name),'MSQ1D.SA0')&& ~contains(upper(neuron_dir(i).name),'.SA0.SUB') && ~contains(upper(neuron_dir(i).name),'.SA0.VECS')
      [c,b]= fget_spk([['/Users/alireza/Desktop/University/97-98\ Spring/Neuroscience/Bonus_Project/Bonus_Project/Data/Spike_and_Log_Files ' neuron_name] '\' neuron_dir(i).name],'header');
      struct.events=c;
      struct.hdr=b;
      answer=[answer;struct];
    end
end
