clc
clear all
close all

run('lib/addpath_recurse');
addpath_recurse('lib/');
addpath_recurse('src/');

%% LOAD MODELING PARAMETERS

B0=1e5;
T=24;   %Length of experiment
S0=1;    %Resource concentration
x0=1e6;  %Initial bacterial density
d=0.02;  %dilution rate
seg_rate=1e-8;  %Segregation rate
conj_rate=0e-12;  %Conjugation rate
epsilon=1e-6; %extinction threshold

%% LOAD DATA

dataPath='../../data/MCMC_params.mat';
loadData();

%% SIMULATE COMMUNITY

num_randperms=100;

other_nodes=model_params.numStrains;
score_nodes=zeros(1,other_nodes);

nr=1;
while nr<num_randperms

    %Define community composition
    %isub=[9 22 3 7 15 18]; 
    isub=randperm(50,4);
    
    %isub=[23    27    15    36]
    %isub=[18 26]

    sub_strains=model_params.strains(isub);
    params=subParameters(model_params, sub_strains);
    N=length(isub);
    ic_TC=zeros(1,N);
    ic_TC(1)=1; %Plamid invasion
    ic_WT=B0*ones(1,N)/N;   
    ic=[1 ic_TC ic_WT];

    %Define environment
    numDrugs=1;
    numDays=1e3;

    E=zeros(numDays, numDrugs);

    %Simulate experiment
    [times, ys, dyn, t_end, pf] = simulateExtinctionMany(params, ic, numDays);

    if dyn<0
        disp([num2str(nr),'*** Random community: ',num2str(isub),' --> plasmid unstable']);
    else
        disp([num2str(nr),'*** Random community: ',num2str(isub),' --> plasmid stable']);
    end
    
    
    if dyn==-1  %Only if plasmid extinction
        nr=nr+1;
        %Add new node
        for inode=1:other_nodes

            if sum(ismember(isub, inode))==0  %Not in original community

                isub_node=[isub inode];

                node_strains=model_params.strains(isub_node);
                params_node=subParameters(model_params, node_strains);
                N_node=length(isub_node);
                ic_TC_node=zeros(1,N_node);
                ic_TC_node(1)=1; %Plamid invasion experiment
                ic_WT_node=B0*ones(1,N_node)/N_node;   
                ic_node=[1 ic_TC_node ic_WT_node];

                %Simulate experiment
                [times_node, ys_node, dyn_node, t_end_node, pf_node] = simulateExtinctionMany(params_node, ic_node, numDays);

                if dyn_node>=0  %Plasmid not extinct yet
                    score_nodes(inode)=score_nodes(inode)+1;
                    disp(['     +',num2str(inode),' --> plasmid stabilized'])
                %else
                %    disp(['     +',num2str(inode)])
                end

            end
        end
    end
end
score_nodes


%%

istable=find(score_nodes>10);
istable
model_params.strains(istable)
model_params.conj_freq(istable)
model_params.species(istable)

C=model_params.cs(istable);
meanC=mean(model_params.cs(istable));
VK=model_params.Vs(istable)./model_params.Ks(istable);
meanVK=mean(model_params.Vs(1:25)./model_params.Ks(1:25));

plot(VK,C,'ok','MarkerFaceColor','k'); hold on;
plot(meanVK,meanC,'or','MarkerFaceColor','r'); hold on;



