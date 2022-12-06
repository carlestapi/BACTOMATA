

codes={ 'Ec01',  'Ec02',  'Ec03',  'Ec04',  'Ec05',  'Ec06',  'Ec07',  'Ec08',  'Ec09',  'Ec10',  'Ec11',  'Ec12',  'Ec13',  'Ec14',  'Ec15',  'Ec16',  'Ec17',  'Ec18',  'Ec19',  'Ec20',  'Ec21',  'Ec22',  'Ec23',  'Ec24',  'Ec25',  'Kpn01',  'Kpn02',  'Kpn03',  'Kpn04',  'Kpn05',  'Kpn06',  'Kpn07',  'Kpn08',  'Kpn09',  'Kpn10',  'Kpn11',  'Kpn12',  'Kpn13',  'Kpn14',  'Kpn15',  'Kpn16',  'Kpn17',  'Kpn18',  'Kpn19',  'Kpn20',  'Kpn21',  'Kpn22',  'Kpn23',  'Kpn24',  'Kpn25'};
strains={ 'C001',  'C002',  'C006',  'C011',  'C012',  'C021',  'C022',  'C031',  'C051',  'C063',  'C094',  'C107',  'C115',  'C131',  'C141',  'C201',  'C227',  'C232',  'C247',  'C261',  'C286',  'C290',  'C302',  'C309',  'C324',  'K037',  'K038',  'K087',  'K094',  'K112',  'K114',  'K125',  'K141',  'K168',  'K177',  'K200',  'K201',  'K209',  'K213',  'K216',  'K224',  'K225',  'K241',  'K248',  'K249',  'K253',  'K257',  'K275',  'K285',  'K300'};

plasmids={'WT','TC'};
load(dataPath);
%disp([num2str(length(MCMC_strains)),' MCMC output files loaded']);

max_muKs=10e-10;
max_rhos=12e8;

totStrains=length(strains);

cmap_brewer=cbrewer('qual', 'Paired', totStrains*2);
cmap=cmap_brewer([1:2:totStrains*2 2:2:totStrains*2], :);

model_params=dataParameters(dataPath, strains, cmap, T, d, S0, seg_rate, conj_rate, epsilon);

%% LOAD MIC / CONJ_RATE DATA

DATA_path='../../data/';

load([DATA_path,'DATA_params.mat'])


for istrain=1:totStrains
    this_strain=strains{istrain};
    
    idata=find(strcmp(DATA_params.strain,strains{istrain}));

    if ~isempty(idata)
        idata_TC=idata(2);
        idata_WT=idata(1);
        for imodel=1:length(model_params.strains)
           if strcmp(model_params.strains{imodel},  [DATA_params.strain{idata_TC},'_TC'])
               %disp(['Updating ',this_strain,'_TC'])
               
                model_params.MIC_AMC(imodel)=DATA_params.MIC_AMC(idata_TC);
                model_params.MIC_MER(imodel)=DATA_params.MIC_MER(idata_TC);
                model_params.MIC_IMP(imodel)=DATA_params.MIC_IMP(idata_TC);
                model_params.MIC_ERT(imodel)=DATA_params.MIC_ERT(idata_TC);
                model_params.conj_freq(imodel)=DATA_params.conj_freq(idata_TC);
               
           end
           
           if strcmp(model_params.strains{imodel},  [DATA_params.strain{idata_WT},'_WT'])
               %disp(['Updating ',this_strain,'_WT'])
               
                model_params.MIC_AMC(imodel)=DATA_params.MIC_AMC(idata_WT);
                model_params.MIC_MER(imodel)=DATA_params.MIC_MER(idata_WT);
                model_params.MIC_IMP(imodel)=DATA_params.MIC_IMP(idata_WT);
                model_params.MIC_ERT(imodel)=DATA_params.MIC_ERT(idata_WT);
                model_params.conj_freq(imodel)=DATA_params.conj_freq(idata_WT);
           end
        end
        
    end
    
    imodel_tc=find(strcmp(model_params.strains,[strains{istrain},'_TC']));
    imodel_wt=find(strcmp(model_params.strains,[strains{istrain},'_WT']));
   
    
end
