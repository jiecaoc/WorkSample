#include "Obstacle.h"
#include <iostream>
using namespace std;



Obstacle::Obstacle(Position pos, Color cl, float sz)
{
    setPosition(pos.x, pos.y);
    setColor(cl.red, cl.green, cl.blue);
    setSize(sz);
}



void Obstacle::draw()
{
    Object::draw();
}

