function vec = randomVect(n)
    vec = [];
    for index = 1 : n
        vec = [vec, rand];
    end
    vec = [(rand > 0.5) + 1, vec];
end