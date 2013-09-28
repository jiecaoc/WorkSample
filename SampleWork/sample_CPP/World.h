#ifndef _WORLD_H_
#define _WORLD_H_
#include "Command.h"
#include <deque>
#include <vector>
#include "Robot.h"
#include "RectObstacle.h"
#include "ControllableRobt.h"
#include "Goal.h"
#include <string>
#include <iostream>
#include <sstream>
#include "MovableObj.h"
#include "Position.h"
#include "Vector.h"
#include <cmath>

using namespace std;

const float WIN_WIDTH = 800.0f;
const float WIN_HEIGHT = 400.0f;


using namespace std;


class World
{
public:
    World();
    World(float width, float height);
    void monitorKeyPressUp(int key, int x, int y);
    void setWindowSize(float width, float height);
    float getWindowWidth();
    float getWindowHeight();
    
    /*! refresh and update objects on screen */
    void updateScreen();
    void addRobot(ControllableRobt robot);
    void addRectObstacle(RectObstacle rectObs);
    void setTarget(Goal tar);
    /*! get command from interpretor,
      store it into commandQueue,
      fetchNextCmd will excute the commandQueue
    */
    void executeCommand(Command cmd);

private:
    void handleCollision();
    void handleEdgeCollision(MovableObj &mobj, float wid, float hei);
    void handleObjectCollision(ControllableRobt &rbt, RectObstacle &rect);
    float string2float(string const& s);
    string float2string(float const& f);
    /*! store commands  */
    deque<Command> commandQueue;
    /*! fetch and excute the top of commandQueue */
    void fetchNextCmd();
    vector<ControllableRobt> robotVector;
    vector<RectObstacle> rectObsVector;
    float windowWidth;
    float windowHeight;
    Goal target;
};

#endif
