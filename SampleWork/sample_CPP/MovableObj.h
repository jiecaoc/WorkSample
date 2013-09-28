#ifndef _MOVABLEOBJ_H_
#define _MOVABLEOBJ_H_
#include "Object.h"
#include "const.h"
#include "Timer.h"
#include "Position.h"
#include "Vector.h"
#include <cmath>
const float OBJ_DERECTION = 0.0f;
const float OBJ_SIZE = 50.0f;
const float OBJ_SPEED = 0.0f;
const float unitDegree = 0.05f;
const float unitSpeed = 10.0f;

class MovableObj : public Object
{
public :
    MovableObj() : Object(), degree(OBJ_DERECTION), speed(OBJ_SPEED)
    {
        acceleration.setXY(0.0f, 0.0f);
    }
    
    MovableObj(float x, float y);

    virtual void draw();

    // speed *= times
    void timeSpeed(float times);
    
    // inverse object's dirction in the collision dirction,
    // follow the physical law
    // need a node as a parameter
    void invCollisionDir(Position);

    float getDirection();
    void printCurrentInfo();
    friend class RobotTests;
protected :
    VectorClass acceleration;
    float degree;
    float speed;
    Timer timer;
    void refreshObject();
    float getDegree(float cos, float sin);
};


#endif

