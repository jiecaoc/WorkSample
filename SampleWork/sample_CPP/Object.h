#ifndef _OBJECT_H_
#define _OBJECT_H_
#include "Position.h"
#include "Color.h"
#include "const.h"
#include <GL/glut.h>
#include <cmath>

const float OBJECT_SIZE = 50.0f;

class Object
{
public :
    Object();
    virtual void draw();
    Position getPosition();
    float getSize();
    Color getColor();
    void setPosition(float, float);
    virtual void setSize(float);
    void setColor(float, float, float);

    //set friend class to test
    friend class ObjectTests;
private:
    Position position;
    Color color;
    float size;
};

#endif
