#include "Clock.h"

void ClockClass::draw()
{
    Object::draw();

    //update leftTime
    leftTime -= timer.getElapsedTime();
    if (leftTime < 0.0f)
        leftTime = 0.0f;

    //draw circular arc based on leftTime/totalTime
    glColor3f(0.2f, 0.2f, 0.2f);
    glBegin(GL_TRIANGLE_FAN);
    int passedPoints = (int) (leftTime / totalTime * NUM_POINTS + 1.5f);
    float x = getPosition().x;
    float y = getPosition().y;
    glVertex2f(x, y);
    for( int i = 0; i < passedPoints; i++ ){
        float Angle = i * (2.0 * PI / NUM_POINTS); // use 360 instead of 2.0*PI if
        float X = x + cos(Angle) * getSize();  // you use d_cos and d_sin
        float Y = y + sin(Angle) * getSize();
        glVertex2f(X, Y);
    }
    glEnd();
}


bool ClockClass::isTimeOver()
{
    if (leftTime <= 0.0f)
        return true;
    return false;
}

void ClockClass::setTimeOver()
{
    leftTime = 0.0f;
}
