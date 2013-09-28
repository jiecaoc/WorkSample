#include"Vector.h"
#include<cmath>

float VectorClass::getLength()
{
    return sqrt( x * x + y * y );
}

VectorClass VectorClass::operator + (const VectorClass & v) const
{
    VectorClass result;
    result.x = x + v.x;
    result.y = y + v.y;
    return result;
}

VectorClass VectorClass::operator - (const VectorClass & v) const
{
    VectorClass result;
    result.x = x - v.x;
    result.y = y - v.y;
    return result;
}

float VectorClass::operator * (const VectorClass & v) const
{
    return x * v.x + y * v.y;
}

