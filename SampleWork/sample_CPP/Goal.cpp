#include "Goal.h"

void Goal::draw()
{
    //randomlyMove();
    glColor3f(getColor().red, getColor().green, getColor().blue);

    glBegin(GL_TRIANGLES);
    for (int i = 0; i < 3; i++){
        float Angle = PI / 2 + i * 2 * PI / 3;
        float X = getPosition().x + cos(Angle) * getSize();  // you use d_cos and d_sin
        float Y = getPosition().y + sin(Angle) * getSize();
        glVertex2f(X, Y);
    }
    glEnd();
}

void Goal::randomlyMove()
{
    if (flagStopMove)
        return;
    float dx = rand() % RAND_SPEED * (0.5 - rand() % 2);
    float dy = rand() % RAND_SPEED * (0.5 - rand() % 2);
    acceleration.setXY(dx, dy);
    refreshObject();
}

void Goal::stopRandlyMove()
{
    flagStopMove = true;
}

    
