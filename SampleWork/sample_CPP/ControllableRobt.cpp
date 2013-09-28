#include "ControllableRobt.h"
#include "Vector.h"
void ControllableRobt::draw()
{
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

float ControllableRobt::moveForward()
{
    float tmpTime = timer.getElapsedTime();
    VectorClass tempVec(speed * cos(degree), speed * sin(degree));
    float delta = tempVec.getLength() * tmpTime;
    if (delta > 5)
        return 0;
    setPosition(getPosition().x + tmpTime * tempVec.getX(),
                getPosition().y + tmpTime * tempVec.getY());
    return delta;
}

float ControllableRobt::moveBackward()
{
    return 1.0;
}

void ControllableRobt::stepSpeed(float signal)
{
    speed += signal * unitSpeed;
    if (speed < 0)
        speed = 0;
    if (speed > 100)
        speed = 100;
}

/* only the symbol of signal matter
   signal < 0 : clockwise
   signal > 0 : counter-clockwise
*/
float ControllableRobt::stepDirection(float signal)
{
    float flag = (signal > 0 ? 1 : -1);
    float delta;
    delta = flag * 0.05;
    degree += delta;
    if (degree > 2 * PI)
        degree -= 2 * PI;
    if (degree < 0)
        degree += 2 * PI;
    return delta;
}




    
