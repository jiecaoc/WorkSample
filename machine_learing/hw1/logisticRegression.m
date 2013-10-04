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
    


    % now let's calculate the error
    error_means = ones(length(train_percent) , 1);
    error_var = ones(length(train_percent) , 1);
    
    for pct = 1 : length(train_percent)
        percent = train_percent(pct);
        errorRates = ones(num_splits, 1);
        for i = 1 : num_splits
            % num of data should be used
            n = int64(N * percent / 100.);
            % random choose from rawData
            pos = randperm(N);
            randomData = rawData(pos(1:n), :);
            % split data and calc errorRate
            tmp = int64(n * 0.8);
            errorRates(i) = calcErrorRate(randomData(1:tmp, :), rawData(1 : int64(N * 0.2), :));%randomData((tmp + 1) : n, :));
        end
        error_means(pct) = mean(errorRates);
        error_var(pct) = var(errorRates);
    end
 
    % OK, let's show our result
    for i = 1 : length(train_percent)   
        fprintf('Percentage of used training data: %f \n', train_percent(i));
        fprintf('Mean of error rate: %f\n', error_means(i));
        fprintf('Var of error rate: %f\n', error_var(i));
    end
end