#ifndef _POSITION_H_
#define _POSITION_H_

class Position
{
 public:
  float x;
  float y;
  Position(){}
  Position(float _x, float _y)
  {
    x = _x;
    y = _y;
  }  
  float getPositionX();
  float getPositionY();
  void setPosition(float, float);

};

#endif
