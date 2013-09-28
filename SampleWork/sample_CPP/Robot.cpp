#include "Robot.h"
#include <iostream>
using namespace std;

/*
Robot::Robot()
{
    Object::Object();
    degree = 0.0f;
    speed = 0.0f;
}
*/



void Robot::draw()
{
    //update parameters before drawing
    refreshRobot();
    //base class will draw a circle
    Object::draw();
    //------draw the line, as the direction------ 
    glBegin(GL_LINES);
    {
        float X = getPosition().x + 2 * cos( degree ) * getSize();
        float Y = getPosition().y + 2 * sin( degree ) * getSize();
        glVertex2f( getPosition().x, getPosition().y ); 
        glVertex2f(X, Y);
    }
    glEnd();

}

// change the direction by a int ctr
void Robot::stepDirection(int ctr)
{
    degree += ctr * unitDegree;
    if (degree > 2 * PI)
        degree -= 2 * PI;
    if (degree < 0)
        degree += 2 * PI;
    refreshRobot();
}


//control the speed, but will no less than 0
void Robot::stepSpeed(int ctr)
{
    speed += ctr * unitSpeed;
    if (speed < 0.0f)
        speed = 0.0f;
    refreshRobot();
}

void Robot::refreshRobot()
{
    if (! sensorClosed)
        refreshObject();
    printCurrentInfo();
}


/*
  Potential field could be consider as
  acceleration of the robot, thus it will affect
  the speed and dirction of the robot
*/

void Robot::detectPFields(VectorClass field)
{
    acceleration = field;
}

void Robot::closeFieldSensor()
{
    sensorClosed = true;
}
