#include "MovableObj.h"
#include <iostream>
using namespace std;

MovableObj::MovableObj(float x, float y)
{
    setSize(OBJ_SIZE);
    speed = OBJ_SPEED;
    degree = OBJ_DERECTION;
    setPosition(x,y);
    acceleration.setXY(0.0f, 0.0f);
}

void MovableObj::draw()
{
}

void MovableObj::timeSpeed(float times)
{
    speed *= times;
}

/*
  This function may be difficult to understand
  if you are not good at analytical geometry
*/
void MovableObj::invCollisionDir(Position node)
{
    /*
    degree += PI;
    if (degree > 2 * PI)
        degree -= 2 * PI;
    */
    
    //the collision direciton
    Position dir(node.x - getPosition().x,
                 node.y - getPosition().y);
    float length = sqrt(dir.x * dir.x + dir.y * dir.y);
    dir.x = dir.x / length;
    dir.y = dir.y / length;
    float alpha = getDegree(dir.x, dir.y);
    float delta = degree - alpha;
    
    
    dir.x = -cos(delta);
    dir.y = sin(delta);
    degree = getDegree(dir.x, dir.y) + alpha;
    if (degree > 2 * PI)
        degree -= 2 * PI;
    if (degree < 0)
        degree += 2 * PI;
    
}



float MovableObj::getDirection()
{
    return degree;
}


void MovableObj::refreshObject()
{
    float temp = timer.getElapsedTime();
    
    VectorClass tempVec(speed * cos(degree), speed * sin(degree));
    VectorClass deltaSpeed(acceleration.getX() * temp * 10, acceleration.getY() * temp * 10);
    tempVec = deltaSpeed + tempVec;
    speed = tempVec.getLength();
    if (speed > 0)
        degree = getDegree(tempVec.getX(), tempVec.getY());
    
    //set the unit diretion
    Position dir(cos(degree),sin(degree));
    
    setPosition(getPosition().x + speed * temp * dir.x,
                getPosition().y + speed * temp * dir.y);
 
    
}


void MovableObj::printCurrentInfo()
{
    VectorClass tempVec(speed * cos(degree), speed * sin(degree));
    cout << "\nSpeed vector : x = " << tempVec.getX() << ", y = " << tempVec.getY() << endl;
    cout << "Current Speed: " << speed << endl;
    cout << "Current Direction : " << degree << endl;
    cout << "Current Position : x = " << getPosition().x << ", y = " << getPosition().y << endl;
    cout << "Current Acceleration : " << acceleration.getX() << " " << acceleration.getY() << endl;

}



// get degree from the direction vector ( d * cos(deg), d * sin(deg) )
float MovableObj::getDegree(float c, float s)//not yet
{
    float len = sqrt( c * c + s * s );
    if (len == 0.0f)
        return 0;
    c = c / len;
    s = s / len;
    float deg = acos(c);
    if (s < 0.0f)
        deg = 2 * PI - deg;
    return deg;
}



