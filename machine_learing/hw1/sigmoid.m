function y = sigmoid(x)
    if x > 20
        x = 20;
    elseif x < -20
        x = -20;
    end
    y = 1 / (1 + exp(-x));
end