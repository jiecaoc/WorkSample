function naiveBayesGaussian(filename, num_splits, train_percent)
    % import the data %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    rawData = csvread(filename);
    [N, k] = size(rawData);
    % pre-process the rawData %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    n = 1;
    for i = 2 : k
        if norm(rawData(:,i) - rawData(1,i) * ones(N,1)) > 0.001
            n = n + 1;
            rawData(:, n) = rawData(:, i);
        end
    end
    rawData = rawData(:, 1 : n);
    [N, k] = size(rawData);
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    function vec = randomVect(n)
        vec = [];
        for index = 1 : n
            vec = [vec, rand];
        end
        vec = [(rand > 0.5) + 1, vec];
    end
    % given training data,
    % return w and w0 so that p(0 | x) = sigmoid(w'x + w0)
    function [w, w0] = naiveBayesG(data)
        % first, group the classes
        [Ndata, Kdata] = size(data);
        % pre-processing
        % when the size of training data is smaller than 
        % dim of feature, add some noise
        if Ndata <= Kdata
            for i = 1 : (25 + Kdata - Ndata)
                vec = randomVect(Kdata - 1);
                data = [data; vec];
            end
        end
        [Ndata, Kdata] = size(data);
        class1 = data(:, 2 : Kdata);
        class2 = class1;
        n1 = 0;
        n2 = 0;
        for i = 1 : Ndata
            if abs(1 - data(i, 1)) < 0.1
                % belong to class 1
                n1 = n1 + 1;
                class1(n1, :) = data(i, 2 : Kdata);
            else
                n2 = n2 + 1;
                class2(n2, :) = data(i, 2 : Kdata);
            end
        end
        class1 = class1(1 : n1, :);
        class2 = class2(1 : n2, :);
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%
        % let's compute mu
        mu1 = mean(class1)';
        mu2 = mean(class2)';
        % now, let's compute Sigma
        S = zeros(Kdata - 1, Kdata - 1);
        for i = 1 : n1
            S = S + (class1(i, :)' - mu1) * (class1(i, :)' - mu1)';
        end
        for i = 1 : n2
            S = S + (class2(i, :)' - mu2) * (class2(i, :)' - mu2)';
        end
        S = S ./ Ndata;
        Sigma = S;
        %%%% now compute w and w0
        w = Sigma\(mu1 - mu2); 
        w0 = -0.5 .* mu1' * (Sigma\ mu1) + 0.5 .* mu2' * (Sigma\ mu2) + log(n1 / n2);
    end
   

    %%%%%%%
    % given a percentage of training data
    % let's compute the errors
    %%%%%%%
    [train, test] = dataSetRandomSplit(rawData, 0.8);
    
    function [meanError, varError] = calcError(train, test, percent)
        [testN, testM] = size(test);
        Errors = [];
        for i = 1 : num_splits
            [trainData, tmp] = dataSetRandomSplit(train, percent/100.);
            [w, w0] = naiveBayesG(trainData);
            
            errors = 0;
            for j = 1 : testN
                x = test(j, 2 : k);
                errors = errors + (abs( 2 - test(j, 1) - (sigmoid(w' * x' + w0) > 0.5) ) > 0.1);
            end
            Errors = [Errors, errors / testN];             
        end
        meanError = mean(Errors);
        varError = sqrt(var(Errors)) / meanError;
    end

    
    %%%%
    meanErrors = [];
    stdVarErrors = [];
    for i = 1 : length(train_percent) 
        [a, b] =  calcError(train, test, train_percent(i));
        meanErrors = [meanErrors, a];
        stdVarErrors = [stdVarErrors, b];
    end
    
    plot(train_percent, meanErrors);
    xlabel('Percentage of used trainning data');
    ylabel('Mean of Error Rates');
%     plot(train_percent, stdVarErrors);
%     xlabel('Percentage of used trainning data');
%     ylabel('Std var of Error Rates')
           
end