#ifndef _COMMAND_H_
#define _COMMAND_H_
#include <string>
#include <vector>
using namespace std;

class Command
{
public:
    //Command();
    //Command(string &cmdName, string &para);
    //Command(string cmdName, vector<string> & paraVec);
    string command;
    vector<string> parametersVec;
};



#endif
