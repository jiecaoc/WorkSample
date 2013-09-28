#ifndef __ROBOT_H__
#define __ROBOT_H__
#include "MovableObj.h"

class Robot : public MovableObj
{
public :
    Robot() : MovableObj(), sensorClosed(false)
    {
        acceleration.setXY(0.0f, 0.0f);
    }
    
    Robot(float x, float y) : MovableObj(x, y)
    {
        sensorClosed = false;
        acceleration.setXY(0.0f, 0.0f);
    }

    void draw();
    
    //use int to modify the Direction
    void stepDirection(int);
    //use int to modify the speed
    void stepSpeed(int);

        
    friend class RobotTests;
    friend class EnvironmentTests;

    //following methods introduce automation
    
    //detect potential fields and then change acceleration
    void detectPFields(VectorClass fields);

    /*
      once the field sensor is closed, the acceleration
      will not change anymore
    */
    void closeFieldSensor();
    


    
private :
    void refreshRobot();
    

    /*
      closed : true
      open : flase
    */
    bool sensorClosed;
    
    
};


#endif
