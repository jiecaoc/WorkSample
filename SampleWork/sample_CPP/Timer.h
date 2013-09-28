/*
  this class is used to get elapsed time.
*/

#ifndef _TIMER_H
#define _TIMER_H

#include <GL/glut.h>
class Timer
{
 public:
  //return the elapsed time, second
  float getElapsedTime();
  Timer();
  friend class TimerTest;
 private:
  void initialize();
  int elapsedTime;
  
};

#endif

