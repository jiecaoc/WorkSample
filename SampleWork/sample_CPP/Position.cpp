#include "Position.h"
/* --------- implementation of class Positon -------------- */


float Position::getPositionX()
{
  return x;
}  
float Position::getPositionY()
{
  return y;
}

void Position::setPosition(float _x, float _y)
{
    x = _x;
    y = _y;
}
