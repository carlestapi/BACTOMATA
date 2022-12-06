clc
clear all
close all

run('lib/addpath_recurse');
addpath_recurse('lib/');
addpath_recurse('src/');

figPath='figures/';

%% LOAD MODELING PARAMETERS

B0=1e3;
%ic=[1 B0 0];
ic=[1 B0/2 B0/2];

seg_rate=.1;
Vmax=6e-10;
cost=0.6;

MIC=1.1;

%%

params.conj_rate= 0;
params.S0= 1;
params.T= 24;
params.d= 0.1;
params.cs= [877563800 984410100];
params.Ks= [1 1];
params.species={'E'  'E'};
params.plasmids= {'TC'  'WT'};
params.strains={'X1'  'X1'};
params.colors= [[0.6510    0.8078    0.8902], [0.6510    0.8078    0.8902]];
params.numStrains= 1;
params.MIC_AMC= [32768 32];
params.MIC_MER= [4 1];
params.MIC_IMP= [16 0.5000];
params.MIC_ERT= [16 0.5000];
params.conj_freq= [0 0];


dose_max=32768; 
params.MIC_AMC=[dose_max*MIC, 32]; 

params.seg_rate=seg_rate;

params.Vs= [cost*Vmax Vmax];
params.extinction_threshold=1e1;
     
%% LOAD CA
CA=importdata('rule30_50.txt');
[num_rows, num_cols]=size(CA);

BTs=zeros(size(CA));
Pfs=zeros(size(CA));


for icol=1:num_cols

    E=CA(:,icol);
    disp([num2str(icol),' E=',num2str(E')]);
    
    %Simulate experiment
    [times, ys, t_end, ~] = simulateTransferMany(params, ic, E);
    
    %Estimate plasmid fraction in each transfer
    B=ys(:,2:end);
    
    Ti=find(mod(times,params.T)==0);
   
    daily_BpT=sum(B(Ti,1:params.numStrains),2);
    daily_BfT=sum(B(Ti,params.numStrains+1:end),2);
        
    Pfs(:, icol)=daily_BpT./(daily_BpT+daily_BfT);  %plasmid fraction
    
    BTs(:, icol)=log10(daily_BpT(:)+daily_BfT(:));  %Final bacterial density
    
    
%     %     %Cross-correlation plasmid fraction y E / Final bacterial density y E 
%     
%     cEPTs(:, icol) = xcorr(E,Pfs(:, icol),'normalized');
%     cEBfs(:, icol) = xcorr(E,BTs(:, icol),'normalized');
%     cEBpT(:, icol) = xcorr(E,daily_BpT,'normalized');

%     %     %Auto-correlation plasmid fraction, Final bacterial density, E 
     
    cPTs(:, icol) = autocorr(daily_BpT,'NumLags',49);
    cBfs(:, icol) = autocorr(daily_BfT,'NumLags',49);
    cE(:, icol) = autocorr(E,'NumLags',40);
    
    
%         [acfBpT,lags] = autocorr(daily_BpT,'NumLags',1000,'NumSTD',2);
%         [acfBfT,lags] = autocorr(daily_BfT,'NumLags',1000,'NumSTD',2);
%         [acfE,lags] = autocorr(E,'NumLags',1000,'NumSTD',2);
%     
    %Plot everything
    
%    plotManyGrowthCurves(times, ys, params, E); %, max_muKs, max_rhos   
%    export_fig([figPath,'rule30/rule30_col',num2str(icol),'.png']);
%    export_fig([figPath,'contCA/contCA_col',num2str(icol),'.png']);
%    pause
%    close();
    
end
%%
figure();
clf('reset');set(gcf,'DefaultLineLineWidth',4); set(gcf, 'color', 'white'); hold all
set(gcf, 'Position', [1 1 2000 800])

subaxis(2, 3, 1,'spacinghoriz',0.1,'paddingbottom',0.1);
heatmap(CA)
title('Environments');
ylabel('Seasons');
xlabel('Treatments');
set(gca,'FontSize', 16);
colormap('turbo');

subaxis(2, 3, 2,'spacinghoriz',0.1,'paddingbottom',0.1);
heatmap(BTs);
title('Bacterial density');
ylabel('Seasons');
xlabel('Treatments');
set(gca,'FontSize', 16);
colormap('turbo');

subaxis(2, 3, 3,'spacinghoriz',0.1,'paddingbottom',0.1);
h=heatmap(Pfs);
title('Plasmid frequency');
ylabel('Seasons');
xlabel('Treatments');
set(gca,'FontSize', 16)
colormap('turbo');

subaxis(2, 3, 4,'spacinghoriz',0.1,'paddingbottom',0.1);
h=heatmap(cPTs);
title('AutoCorrelation Bp');
ylabel('lag');
xlabel('Treatments');
set(gca,'FontSize', 16)
colormap('turbo');

subaxis(2, 3, 5,'spacinghoriz',0.1,'paddingbottom',0.1);
h=heatmap(cBfs);
title('AutoCorrelation B0');
ylabel('lag');
xlabel('Treatments');
set(gca,'FontSize', 16)
colormap('turbo');

subaxis(2, 3, 6,'spacinghoriz',0.1,'paddingbottom',0.1);
h=heatmap(cE);
title('AutoCorrelation Environment');
ylabel('lag');
xlabel('Treatments');
set(gca,'FontSize', 16)
colormap('turbo');
