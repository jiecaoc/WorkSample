#ifndef _CLOCK_H_
#define _CLOCK_H_
#include "Object.h"
#include "Timer.h"
#include "const.h"
class ClockClass : public Object
{
public :
    ClockClass() : Object(), totalTime(TOT_TIME), leftTime(TOT_TIME)
    {}
    void draw();
    bool isTimeOver();
    void setTimeOver();
    friend class ClockTests;
private :
    Timer timer;
    float totalTime;
    float leftTime;
};




#endif
