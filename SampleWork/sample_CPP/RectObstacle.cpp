#include "RectObstacle.h"



float RectObstacle::getHeight()
{
    return height;
}

float RectObstacle::getWidth()
{
    return width;
}


void RectObstacle::draw()
{
    glColor3f(getColor().red, getColor().green, getColor().blue);
    Position pos = getPosition();
    glRectf(pos.x, pos.y, pos.x + width, pos.y - height);
}

void RectObstacle::setSize(float wd, float ht)
{
    width = wd;
    height = ht;
}

