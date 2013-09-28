#include "Timer.h"

void Timer::initialize()
{
  elapsedTime = 0;
}

Timer::Timer()
{
  initialize();
}


float Timer::getElapsedTime()
{
  if (elapsedTime == 0)
    elapsedTime = glutGet(GLUT_ELAPSED_TIME);
  int now = glutGet(GLUT_ELAPSED_TIME);
  int elapsedMilliseconds = now - elapsedTime;
  elapsedTime = now;
  return elapsedMilliseconds / 1000.0f;
}

