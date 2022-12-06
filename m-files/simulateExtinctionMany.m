function [times, ys, dyn, t_end, pf] = simulateExtinctionMany(params, ic, maxSims)
    
    if nargin<3
        maxSims=1;
    end

    % Solver parameters
    %options = odeset('NonNegative', 1:length(ic));
    options.RelTol = 1e-12;
    options.AbsTol = 1e-12;   
    
    
    %Numerical simulation
    times=[];
    ys=[];
    t_end=-1;
    
    Ti=params.T;
    for i=1:maxSims
    
        [this_times, this_y] = ode15s(@(t,x)fMany(t,x, params),[0,1],ic, options);
        
        times=[times; (i-1)+this_times(2:end)];
        ys=[ys; this_y(2:end,:)];
        
        if params.numStrains>1
            Bpi=sum(this_y(:,2:params.numStrains+1),2);
            Bfi=sum(this_y(:,params.numStrains+2:end),2);
        else
            Bpi=this_y(:,2:params.numStrains+1);
            Bfi=this_y(:,params.numStrains+2:end);
        end
        
        a_p = (Bpi<params.epsilon)';
        iext_p = find([a_p(1) diff(a_p)]==1);
        if ~isempty(iext_p)
           t_end=params.T*((i-1)+this_times(iext_p)); 
           %disp(['Plasmid extinction @t=',num2str(round(t_end))]);
           pf=0;
           times=Ti.*times;
           dyn=-1;  %Plasmid extinct
           
           return 
        end
        
        %{
        a_f = (Bfi<params.epsilon)';
        iext_f = find([a_f(1) diff(a_f)]==1);
        if ~isempty(iext_f)
           t_end=params.T*((i-1)+this_times(iext_f)); 
           disp(['Plasmid fixation @t=',num2str(round(t_end))]);
           pf=0;
           times=params.T.*times;
           
           return 
        end
        %}
        if max(diff(Bpi(round(length(Bpi)/2):end)))<params.epsilon/100 && max(diff(Bfi(round(length(Bfi)/2):end)))<params.epsilon/100 && Bfi(end)<params.epsilon   %Plasmid stable
           t_end=params.T*((i-1)+this_times(end)); 
           if t_end>=24
               %disp(['Plasmid stable @t>',num2str(round(t_end))]);

                B=this_y(:,2:end);
                BpT=sum(B(end,1:params.numStrains),2);
                BfT=sum(B(end,params.numStrains+1:end),2);

                pf=BpT/(BpT+BfT);  %plasmid fraction
               times=params.T.*times;
               dyn=1;  %Plasmid stable

               return 
           end
        end
        
        ic=this_y(end,:);
        

        
    end
    
    times=params.T.*times;
    
    B=ys(:,2:end);
    
    BpT=sum(B(end,1:params.numStrains),2);
    BfT=sum(B(end,params.numStrains+1:end),2);
        
    pf=BpT/(BpT+BfT);  %plasmid fraction
    dyn=0; %Co-existence
    
   %disp(['Plasmid not extinct yet (T=',num2str(params.T*maxSims),', pf=',num2str(pf),')']);
    
end

