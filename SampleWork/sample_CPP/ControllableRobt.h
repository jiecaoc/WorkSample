#ifndef _CONTROLLABLEROBOT_H_
#define _CONTROLLABLEROBOT_H_
#include "MovableObj.h"
class ControllableRobt  : public MovableObj
{
public:
    /*! Move forward,
     return how far actually move*/
    float moveForward();
    
    /*! Move backward,
     return how far actually move*/
    float moveBackward();
    
    /*! Change direction,
     return degree that actually change,
     signal > 0 : counter-clockwise
     signal < 0 : clockwise
    */
    float stepDirection(float signal);
    
    /*! Change Max speed,
     signal > 0 : counter-clockwise,
     signal < 0 : clockwise
    */
    void stepSpeed(float signal);

    /*! draw the robot*/
    void draw();
    
};



#endif
