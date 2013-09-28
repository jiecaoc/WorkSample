#include<stdlib.h>
#include<stdio.h>
#include<time.h>
double P[2][16];

int Hash(int list[])
{
    int len = 4;
    int sum = 0;
    while (len--)
    {
        sum = sum * 2 + list[len];
    }
    return sum;
}


double getProb(int z, int bn[])
{
    return P[z][Hash(bn)];
}

int sampling(double p)
{
    int M = 10000;
    printf("p = %lf\n",p);
    if (rand() % M < p * M)
        return 1;
    else
        return 0;
}

double Gibbs_ask(int N)
{
    int bn[] = {0, 1, 1, 1};
    int n = 0;
    int j;
    for (j = 0; j < N; ++j)
    {
        int z = rand() % 2;
        bn[z] = sampling(getProb(z, bn));
        if (bn[1])
            ++n;
    }
    return (n + 0.0) / N;    
}


int main()
{
    srand(time(NULL));
    int key[] = {1, 1, 1, 1};
    P[0][Hash(key)] = 0.444444;
    P[1][Hash(key)] = 0.814815;
    key[0] = 0;
    P[0][Hash(key)] = 0.555556;
    P[1][Hash(key)] = 0.215686;
    key[0] = 1;
    key[1] = 0;
    P[0][Hash(key)] = 0.047619;
    P[1][Hash(key)] = 0.185185;
    key[0] = 0;
    P[0][Hash(key)] = 0.952381;
    P[1][Hash(key)] = 0.784314;

    
    int N = 1000;
    double ans = Gibbs_ask(N);
    printf("%lf\n",ans);
    return 0;
}
