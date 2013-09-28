#include "Interpreter.h"
#include <iostream>
#include <sstream>
using namespace std;

Interpreter::Interpreter(World *worldP)
{
    // forFlag < 0
    forFlag = -1;
    worldPtr = worldP;
}

string Interpreter::deleteBlank(string cmd)
{
    //cout << "Before Del : " << cmd << endl;
    stringstream str(cmd);
    string s;
    str >> s;
    //cout << "After Del : " << s << endl;
    return s;
}



Command Interpreter::interpCommonCmd(string cmd)
{
    cmd = deleteBlank(cmd);
    Command tmp;
    size_t left_n = cmd.find("(");
    size_t right_n = cmd.find(")");
    //cout << left_n << " " << right_n << endl;
    tmp.command = cmd.substr(0, left_n);
    tmp.parametersVec.push_back( cmd.substr(left_n + 1, right_n - left_n - 1) );
    return tmp;
}



/*!
  convert cmd to the form of Command
*/
void Interpreter::interpretCmd(string cmd)
{
    //cmd =  deleteBlank(cmd);
    Command tmp;
    //cout << cmd << " will be interpreted" << endl;
    // if is a one line command : XXXXX(xx) 
    if (cmd.find("for") == string::npos && forFlag < 0){
        // if it is a moveBackward command
        if (cmd.find("moveBackward") != string::npos){
            /* moveBackward(xx) =
                  stepDirection(PI)
                  moveForward(xx)
            */
            tmp.command = "stepDirection";
            tmp.parametersVec.push_back("3.2");
            worldPtr->executeCommand(tmp);
            tmp = interpCommonCmd(cmd);
            tmp.command = "moveForward";
            worldPtr->executeCommand(tmp);
        }
        
        
        tmp = interpCommonCmd(cmd);
        worldPtr->executeCommand(tmp);
        //cout << tmp.command << tmp.parametersVec[0];
    }
    
    else  // handle with for-routine
    {
        // if cmd is of the format "xxxxx(xx)"
        if (cmd.find("for") == string::npos){
            cmdQueue.push(interpCommonCmd(cmd));
        }
        /* if cmd == "endfor;"
           for i = 1 to forFlag do
              move cmds in cmdQueue to commandQueue
           endfor;
         */
        if (cmd.find("endfor") != string::npos){
            for (int i = 0; i < forFlag; ++i){
                for (unsigned int j = 0; j < cmdQueue.size(); ++j){
                    worldPtr->executeCommand(cmdQueue.front());
                    cmdQueue.push(cmdQueue.front());
                    cmdQueue.pop();
                }
                
            }
            forFlag = -1;
        }
        // cmd is "for a to b do", calculate forFlag as (b-a)
        if (cmd.find("for") != string::npos){
            stringstream str(cmd);
            string tmp;
            str >> tmp;
            int a;
            str >> a;
            str >> tmp;
            int b;
            str >> b;
            forFlag = b - a;
            if (forFlag < 0)
                forFlag = 0;
            //cout << "forFlag : " << forFlag << endl;
        }
            //tmp.parametersVec.push_back("1.2");
    }
}

