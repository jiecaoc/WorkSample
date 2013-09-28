#ifndef _BOSTABLE_H_
#define _BOSTABLE_H_
#include "Object.h"
#include <cmath>

class Obstacle : public Object
{
public:
    Obstacle() : Object()
    {}
    Obstacle(Position, Color, float);

    //draw the Obstable itself
    void draw();
};

#endif
