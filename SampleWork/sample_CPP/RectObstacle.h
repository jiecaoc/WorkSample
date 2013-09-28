#ifndef _RECTOBSTACLE_H_
#define _RECTOBSTACLE_H_
#include "Obstacle.h"
#include "Position.h"

const float WIDTH = 20.0f;
const float HEIGHT = 100.0f;

class RectObstacle: public Obstacle
{
public:
    RectObstacle() : Obstacle(), width(WIDTH), height(HEIGHT)
    {};
    void setSize(float wd, float ht);
    float getWidth();
    float getHeight();
    void draw();
private:
    float width;
    float height;
};



#endif
