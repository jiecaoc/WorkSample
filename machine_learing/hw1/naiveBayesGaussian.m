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
    
    % given training data,
    % return w and w0 so that p(0 | x) = sigmoid(w'x + w0)
    function [w, w0] = naiveBayesG(data)
        % first, group the classes
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
        size(Sigma)
        size(mu1)
        size(mu2)
        w0 = -0.5 .* mu1' * (Sigma\ mu1) + 0.5 .* mu2' * (Sigma\ mu2) + log(n1 / n2);
    end
   
    [train, test] = dataSetRandomSplit(rawData, 0.8);
    [train, tmp] = dataSetRandomSplit(train, 0.5);
    [w, w0] = naiveBayesG(train);
    
    function p = f(x)
        p = sigmoid(w' * x + w0);
    end

    testN = length(test(:,1));
    errors = 0;
    for i = 1 : testN
        x = test(i, 2 : k);
        errors = errors + (abs( 2 - test(i, 1) - (f(x') > 0.5) ) > 0.1);
    end
    errors / testN
        
end