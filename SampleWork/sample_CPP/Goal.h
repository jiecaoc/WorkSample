#ifndef _GOAL_H_
#define _GOAL_H_
#include "MovableObj.h"
#include <time.h>
#include <stdlib.h>

const int RAND_SPEED = 80;

class Goal : public MovableObj
{
public:
    Goal() : MovableObj()
    {
        srand ( time(NULL) );
        flagStopMove = false;
    }
    void draw();
    // randomly move with a constant speed
    void randomlyMove();
    void stopRandlyMove();
    
private:
    //if true : stop move
    bool flagStopMove;
};


#endif
