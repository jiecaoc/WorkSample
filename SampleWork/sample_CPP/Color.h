#ifndef _COLOR_H_
#define _COLOR_H_

#include <GL/glut.h>
class Color
{
 public:
  GLfloat red;
  GLfloat green;
  GLfloat blue;
  Color();
  Color(GLfloat, GLfloat, GLfloat);
  void setColor(GLfloat, GLfloat, GLfloat);

};

#endif
