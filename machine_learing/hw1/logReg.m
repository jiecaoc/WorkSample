function [w] = logReg(rawData)
    [Ndata, Kdata] = size(rawData);
    % pre-processing
    % when the size of training data is smaller than 
    % dim of feature, add some noise
    if Ndata <= Kdata
        for i = 1 : (Kdata - Ndata)
            vec = randomVect(Kdata - 1);
            rawData = [rawData; vec];
        end
    end
    [N, k] = size(rawData);
    y = rawData(:,1) - 1;
    phi = rawData(:,2:k);  
    [N, k] = size(phi);

    

    
    function y = calcPi(w, phi)
        tmp = phi * w;
        y = rand * ones(k, 1);
        for j = 1 : length(tmp)
            y(j) = sigmoid(tmp(j));
        end 
    end

    function y = calcR(pi)
        y = pi;
        for j = 1 : length(pi)
            y(j) = pi(j) * (1 - pi(j));
            if abs(y(j)) < 0.01
                y(j) = 0.01;
            end
        end  
        y = diag(y);
    end


    
    w1 = 0.001 * rand * ones(k, 1);
    delta = 1;
    ct = 0;
    while delta > 0.001
        ct = ct + 1;
        w0 = w1;
        pi = calcPi(w0, phi);
        R = calcR(pi);
        % z = phi * w0 - R \ (pi - y);
        w1 = w0 - (phi' * R * phi) \ phi' * (pi - y);
        % w1 = (phi' * R * phi) \ (phi' * R * z);
        if ct > 400
            break;
        end
        delta = norm(phi' * (y - pi));
    end
    w = w1;
end
