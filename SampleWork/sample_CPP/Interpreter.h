/*
  Class Interpretor will be use in
  the main.cpp.
*/

#ifndef _INTERPRETER_H_
#define _INTERPRETER_H_
//#include "Environment.h"
#include "Command.h"
#include <string>
#include <queue>
#include <sstream>
#include <iostream>
#include "World.h"
using namespace std;

class Interpreter
{
public:
    Interpreter(World * worldP);
    /*! interpret cmd as Command type */
    void interpretCmd(string cmd);
private:
    string deleteBlank(string cmd);
    /*! convert cmd with the format "xxxxx(xx)" to
      Command form
     */
    Command interpCommonCmd(string cmd);
    queue<Command> cmdQueue;
    /*! forFlag < 0 means we are
      handling for-routine
    */
    int forFlag;
    World * worldPtr;
    
};


#endif
