#include "World.h"
#include <cmath>
World::World()
{
    windowHeight = WIN_HEIGHT;
    windowWidth = WIN_WIDTH;
}


World::World(float w, float h)
{
    windowWidth = w;
    windowHeight = h;
}


void World::executeCommand(Command cmd)
{
    commandQueue.push_back(cmd);
    //cout << cmd.command << " will be executed." << endl;
}

void World::updateScreen()
{
    handleCollision();
    // excute the top command in the command queue
    //cout << "Number of CMD: " << commandQueue.size() << endl;
    fetchNextCmd();
    // show robots
    for (unsigned int i = 0; i < robotVector.size(); ++i){
        robotVector[i].draw();
    }
    // show RectObstacle
    for (unsigned int i = 0; i < rectObsVector.size(); ++i){
        rectObsVector[i].draw();
    }
    target.draw();
}

void World::addRobot(ControllableRobt robot)
{
    robotVector.push_back(robot);
}

void World::addRectObstacle(RectObstacle rectObs)
{
    rectObsVector.push_back(rectObs);
}


float World::getWindowWidth()
{
    return windowWidth;
}

float World::getWindowHeight()
{
    return windowHeight;
}


float World::string2float(string const& s)
{
    stringstream str(s);
    float f;
    str >> f;
    return f;
}

string World::float2string(float const& f)
{
    stringstream str;
    str << f;
    string s;
    str >> s;
    return s;
}

/*! fetch the top command of commandQueue,
  then execute it.
  All commands in commandQueue are atomic commands.
  Atomic commands :
      1. moveForward
      2. stepSpeed
      3. stepDirection
 */
void World::fetchNextCmd()
{
    if (commandQueue.size() == 0)
        return;
    ControllableRobt &robot = robotVector[0];
    Command currentCmd = commandQueue.front();
    commandQueue.pop_front();
    //cout << "Executing " << currentCmd.command << endl;

    // handle moveForward(x)
    if (currentCmd.command == "moveForward"){
        float dis = string2float( currentCmd.parametersVec[0] );
        float realMoveDis = robot.moveForward();
        //cout << "Move distance : " << realMoveDis << endl;
        dis -= realMoveDis;
        if (dis > 0){
            string strDis = float2string(dis);
            //      cout << "Dis left: " << strDis << endl;
            currentCmd.parametersVec[0] = strDis;
            commandQueue.push_front(currentCmd);
        }
    }
    else
    // handle stepSpeed(x)
    if (currentCmd.command == "stepSpeed"){
        float deltaSpeed = string2float( currentCmd.parametersVec[0] );
        robot.stepSpeed(deltaSpeed);
        //cout << "StepSpeed : " << deltaSpeed << endl;
    }
    else
    // handle stepDirection(x)
    if (currentCmd.command == "stepDirection"){
        float deg = string2float( currentCmd.parametersVec[0] );
        float flag = (deg > 0 ? 1 : -1);
        float realDegree = robot.stepDirection(flag);
        //cout << "Changed degree : " << realDegree << endl;
        deg -= realDegree;
        if (abs(deg * flag) > 0.04){
            string strDeg = float2string(deg);
            //  cout << "Deg left: " << strDeg << endl;
            currentCmd.parametersVec[0] = strDeg;
            commandQueue.push_front(currentCmd);
        }
    }
}



void World::setWindowSize(float w, float h)
{
    windowHeight = h;
    windowWidth = w;
}

void World::setTarget(Goal tar)
{
    target = tar;
}

void World::handleCollision()
{
    ControllableRobt &robot = robotVector[0];
    // handle collision between robot and RectObstacles
    for (unsigned int i = 0; i < rectObsVector.size(); ++i){
      RectObstacle &rectObs = rectObsVector[i];
        handleObjectCollision(robot, rectObs);
    }
    
    handleEdgeCollision(robot, windowWidth, windowHeight);
}

void World::handleEdgeCollision(MovableObj &mobj,
                                float width, float height)
{
    Position pos = mobj.getPosition();
    float degree = mobj.getDirection();
    Position dir(cos(degree), sin(degree));
    float size = mobj.getSize();
    if (pos.x + size > width && dir.x > 0)
        mobj.invCollisionDir( Position(width, pos.y) );
    if (pos.x - size < 0 && dir.x < 0)
        mobj.invCollisionDir( Position(0.0f, pos.y) );
    if (pos.y + size > height && dir.y > 0)
        mobj.invCollisionDir( Position(pos.x, height) );
    if (pos.y - size < 0 && dir.y < 0)
        mobj.invCollisionDir( Position(pos.x, 0.0f));
}

void World::handleObjectCollision(ControllableRobt &rbt, RectObstacle &rect)
{
    float wid = rect.getWidth();
    float hei = rect.getHeight();
    Position rectPos = rect.getPosition();
    Position rbtPos = rbt.getPosition();
    float size = rbt.getSize();
    float degree = rbt.getDirection();
    Position dir(cos(degree), sin(degree));
    // robot in left or right
    if (rbtPos.y < rectPos.y && rbtPos.y > rectPos.y - hei){
        // robot in left
        if (rbtPos.x + size > rectPos.x && dir.x > 0 && rbtPos.x < rectPos.x){
            rbt.invCollisionDir( Position(rectPos.x, rbtPos.y) );
        }else// robot in right
        if (rbtPos.x - size < rectPos.x + wid && dir.x < 0 && rbtPos.x > rectPos.x + wid ){
            rbt.invCollisionDir( Position(rectPos.x + wid, rbtPos.y) );
        }
    }  
    else
    // if robot in top or bottom
    if (rbtPos.x + size  > rectPos.x && rbtPos.x - size  < rectPos.x + wid){
        // robot in top
        if (rbtPos.y - size < rectPos.y && rbtPos.y > rectPos.y && dir.y < 0){
            rbt.invCollisionDir( Position(rbtPos.x, rbtPos.y - size) );
        }
        // robot in bottom
        if (rbtPos.y + size > rectPos.y - hei && rbtPos.y < rectPos.y - hei && dir.y > 0){
            rbt.invCollisionDir( Position(rbtPos.x, rbtPos.y + size) );
        }
    }
    
}


void World::monitorKeyPressUp(int key, int x, int y)
{
    
    if (robotVector.size() == 0){
        cerr << "Error: No Robot in the World!" << endl;
        return;
    }
    Command cmd;
    switch (key) {
    case GLUT_KEY_F1:
        cmd.command = "moveForward";
        cmd.parametersVec.push_back("5");
        this->executeCommand(cmd);
        cout << "moveForward(5)" << endl;
        break;
    case GLUT_KEY_LEFT:
        cmd.command = "stepDirection";
        cmd.parametersVec.push_back("0.05");
        executeCommand(cmd);
        cout << "stepDirection(0.05)" << endl;
        break;
    case GLUT_KEY_RIGHT:
        cmd.command = "stepDirection";
        cmd.parametersVec.push_back("-0.05");
        executeCommand(cmd);
        cout << "stepDirection(-0.05)" << endl;
        break;
    case GLUT_KEY_UP:
        cmd.command = "StepSpeed";
        cmd.parametersVec.push_back("5");
        executeCommand(cmd);
        cout << "stepSpeed(5)" << endl;
        break;
    case GLUT_KEY_DOWN:
        cmd.command = "StepSpeed";
        cmd.parametersVec.push_back("-5");
        executeCommand(cmd);
        cout << "stepSpeed(-5)" << endl;
        break;
    default:
        break;
    }  
}
