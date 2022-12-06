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

%Define community composition
isub=[9 22 3 7 15 18]; 

sub_strains=model_params.strains(isub);
params=subParameters(model_params, sub_strains);
N=length(isub);
ic_TC=zeros(1,N);
ic_TC(1)=1; %Plamid invasion
ic_WT=B0*ones(1,N)/N;   
ic=[1 ic_TC ic_WT];

%Define environment
numDrugs=4;
numDays=12;

E=zeros(numDays, numDrugs);
E(4,1)=1;
%E(5,:)=0;

%Simulate experiment
[times, ys, t_end, pf] = simulateTransferMany(params, ic, E);
    
%Plot everything
plotManyGrowthCurves(times, ys, params, E, max_muKs, max_rhos);

%%


   