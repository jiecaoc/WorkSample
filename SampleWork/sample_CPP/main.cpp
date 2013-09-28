#include "const.h"
#include "Robot.h"
#include "Obstacle.h"
#include "Clock.h"
#include "Goal.h"
//#include "Environment.h"        
#include "Interpreter.h"
#include "World.h"
#include "ControllableRobt.h"
#include <fstream>
#include <iostream>
#include <GL/glut.h>
#include <string>

using namespace std;
/*! keyPressMode
  true : robot can be controled by keypress
  false: robot can be controled by commands
*/
bool keyPressMode;
// initial width and heigh of the window

//Environment environment;
World world;
Interpreter interpreter(& world);
void processMouse (int, int, int, int);
void display(void)
{
    //Always have this line at the top
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    world.updateScreen();
    glutSwapBuffers();
}

void processKeySpecialUp (int key, int x, int y) {
    if (keyPressMode){
        world.monitorKeyPressUp(key, x, y);
    }
    else{        
        //execute command, 1 line per time
        if (key == GLUT_KEY_F1){
            string cmd;
            getline(cin, cmd);
            interpreter.interpretCmd(cmd);
        }
        //execute all commands
        if (key == GLUT_KEY_F2){
            string cmd;
            while (getline(cin, cmd))
                interpreter.interpretCmd(cmd);
        }
    }
    
    
}

void reshape(int width, int height)
{
    glViewport(0, 0, width, height);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(0, width, 0, height);
    glMatrixMode(GL_MODELVIEW);
}

void idle(void)
{
    glutPostRedisplay();
}

void initializeWorld()
{
    ifstream fin("environment.txt");
    float win_wid;
    float win_hei;
    fin >> win_wid >> win_hei;
    //environment.setWindowSize(win_wid, win_hei);
    world.setWindowSize(win_wid, win_hei);
    float radius;
    float x, y;
    for (int i = 0; i < 1; ++i){
        ControllableRobt robot;
        fin >> radius >> x >> y;
        robot.setSize(radius);
        robot.setPosition(x, y);
        robot.setColor(1 - i, 1 - i, i);
        robot.stepSpeed(10);
        //environment.addRobot(robot);
        world.addRobot(robot);
        Goal goal;
        fin >> radius >> x >> y;
        goal.setSize(radius);
        goal.setColor(1 - i, 1 - i, i);
        goal.setPosition(x, y);
        //environment.addGoal(goal);
        world.setTarget(goal);

        // add RectObstacles
        int n;
        fin >> n;
        for (int i = 0; i < n; i++){
            RectObstacle rect;
            float w, h, x, y;
            fin >> w >> h >> x >> y;
            rect.setSize(w, h);
            rect.setPosition(x, y);
            rect.setColor(0.1, 0.5, 1.0);
            world.addRectObstacle(rect);
        }
        
    }
    fin.close();
    
    ClockClass theClock;
    theClock.setColor(0.9f, 0.3f, 0.2f);
    theClock.setPosition(theClock.getSize(),
                         WIN_HEIGHT - theClock.getSize());
    //environment.setClock(theClock);
    
}





int main(int argc, char** argv)
{
    keyPressMode = false;
    if (argc == 2){
        string para(argv[1]);
        if (para.find("k") != string::npos)
            keyPressMode = true;
    }
    
    initializeWorld();
    glutInit(&argc, argv);
    
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH);
    //glutInitWindowSize(environment.getWinWidth(), environment.getWinHeight());
    glutInitWindowSize(world.getWindowWidth(), world.getWindowHeight());
    glutCreateWindow("Robot");
    // Tell GLUT which function will manage keyboard input
    glutSpecialUpFunc(processKeySpecialUp);
    //glutMouseFunc(processMouse);
    glutDisplayFunc(display);
    glutReshapeFunc(reshape);
    glutIdleFunc(idle);
    // You can use cout up to this point, but once control flow moves to glutMainLoop()
    // control will not come back here until the graphics window is closed.
    glutMainLoop();
    return EXIT_SUCCESS;
}


