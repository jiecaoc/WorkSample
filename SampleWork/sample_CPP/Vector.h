/*
  This class provides vector support for the project
*/

#ifndef _VECTOR_H_
#define _VECTOR_H_

class VectorClass
{
public :
    VectorClass() : x(1.0f), y(0.0f)
    {}
    VectorClass(float _x, float _y) : x(_x), y(_y)
    {}
    float getLength();
    VectorClass operator + (const VectorClass & v) const;
    VectorClass operator - (const VectorClass & v) const;
    float operator * (const VectorClass & v) const;
    float getX() 
    {
        return x;
    }
    float getY()
    {
        return y;
    }
    void setXY(float _x, float _y)
    {
        x = _x;
        y = _y;
    }
    
private :
    float x;
    float y;
};

#endif
