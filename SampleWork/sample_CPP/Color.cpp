#include "Color.h"

// ---- Implementation for class Color
void Color::setColor(GLfloat _r, GLfloat _g, GLfloat _b)
{
  red = _r;
  green =  _g;
  blue = _b;
}

Color::Color(GLfloat _r, GLfloat _g, GLfloat _b)
{
  setColor(_r, _g, _b);
}

Color::Color()
{
  setColor(0.9f, 0.0f, 0.0f);
}

