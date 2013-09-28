#include "Object.h"

Object::Object()
{
    setSize(OBJECT_SIZE);
    setPosition(70.0f, 70.0f);
    setColor(0.5f, 0.3f, 0.0f);
}

void Object::draw()
{
    
    glColor3f(getColor().red, getColor().green, getColor().blue);
    glBegin(GL_TRIANGLE_FAN);
    for( int i = 0; i < NUM_POINTS; i++ ){
        float Angle = i * (2.0 * PI / NUM_POINTS); // use 360 instead of 2.0*PI if
        float X = getPosition().x + cos(Angle) * getSize();  // you use d_cos and d_sin
        float Y = getPosition().y + sin(Angle) * getSize();
        glVertex2f(X, Y);
    }
    glEnd();
}



Color Object::getColor()
{
    return color;
}

float Object::getSize()
{
    return size;
}

Position Object::getPosition()
{
    return position;
}



void Object::setPosition(float x, float y)
{
    position.x = x;
    position.y = y;
}

void Object::setSize(float _size)
{
    size = _size;
}

void Object::setColor(float r, float g, float b)
{
    color.red = r;
    color.green = g;
    color.blue = b;
}

