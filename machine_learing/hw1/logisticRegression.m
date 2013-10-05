function [] = logisticRegression(filename, num_splits, train_percent)
    % import the data
    rawData = csvread(filename);
    [N, k] = size(rawData);
    % pre-process the rawData
    n = 1;
    for i = 2 : k
        if norm(rawData(:,i) - rawData(1,i) * ones(N,1)) > 0.001
            n = n + 1;
            rawData(:, n) = rawData(:, i);
        end
    end
    rawData = rawData(:, 1 : n);
    [N, k] = size(rawData);
    
    
    
    
    
    
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % given trainingData and testData
    % return the errorRate
    function [errorRate] = calcErrorRate(trainingData, testData)
        % train and get the optimal para vector w
        w = logReg(trainingData);
        [n1, n2] = size(testData);
        errorRate = 0;
        for index = 1 : n1
            x = testData(index, :);
            if abs( x(1) - 1 - (sigmoid(x(2:k) * w) > 0.5) ) > 0.01
                errorRate = errorRate + 1.;
            end
        end
        errorRate = errorRate / length(testData);
    end
    


     %%%%%%%
    % given a percentage of training data
    % let's compute the errors
    %%%%%%%
    [train, test] = dataSetRandomSplit(rawData, 0.8);
    
    function [meanError, varError] = calcError(train, test, percent)
        Errors = [];
        for i = 1 : num_splits
            [trainData, tmp] = dataSetRandomSplit(train, percent/100.);
            errors = calcErrorRate(trainData, test);
            Errors = [Errors, errors];             
        end
        meanError = mean(Errors);
        varError = sqrt(var(Errors)) / meanError;
    end


    % OK, let's show our result
    %%%%
    meanErrors = [];
    stdVarErrors = [];
    for i = 1 : length(train_percent) 
        [a, b] =  calcError(train, test, train_percent(i));
        meanErrors = [meanErrors, a];
        stdVarErrors = [stdVarErrors, b];
    end
    train_percent
    meanErrors
    stdVarErrors
%     plot(train_percent, meanErrors);
%     xlabel('Percentage of used trainning data');
%     ylabel('Mean of Error Rates');
%     plot(train_percent, stdVarErrors);
%     xlabel('Percentage of used trainning data');
%     ylabel('Std var of Error Rates')
    %plot(train_percent, stdVarErrors);
    
    
end