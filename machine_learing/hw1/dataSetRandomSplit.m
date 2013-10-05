
function [set1, set2] = dataSetRandomSplit(dataSet, percent)
    [N, K] = size(dataSet);
    % num of data should be used
    n = int64(N .* percent);
    % random choose from dataSet
    pos = randperm(N);
    set1 = dataSet(pos(1, 1:n), :);
    set2 = dataSet(pos(1, n + 1 : N), :);  
end