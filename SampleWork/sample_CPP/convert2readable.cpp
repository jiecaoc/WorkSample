#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <sstream>
#include <string>
#include <iostream>
#include "Command.h"
#include <string.h>
using namespace std;

string deleteBlank(string cmd)
{
    //cout << "Before Del : " << cmd << endl;
    stringstream str(cmd);
    string s;
    str >> s;
    //cout << "After Del : " << s << endl;
    return s;
}



Command interpCommonCmd(string cmd)
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

float string2float(string const& s)
{
    stringstream str(s);
    float f;
    str >> f;
    return f;
}

string float2string(float const& f)
{
    stringstream str;
    str << f;
    string s;
    str >> s;
    return s;
}

int main(int argc, char **argv)
{
    string cmdline;
    Command preCommand;
    if (argc != 2){
        cerr << "Error command, please type again!" << endl;
        return 1;
    }
    ifstream fin(argv[1]);
    ofstream fout("tmpoutput");
    if (!getline(fin, cmdline)){
        cerr << "File is empty!" << endl;
        return 1;
    }
    preCommand = interpCommonCmd(cmdline);
    while (getline(fin, cmdline)){
        Command curCmd = interpCommonCmd(cmdline);
        //if same as previous command
        if (preCommand.command == curCmd.command){
            float a = string2float(preCommand.parametersVec[0]);
            float b = string2float(curCmd.parametersVec[0]);
            preCommand.parametersVec[0] = float2string(a+b);
        }
        else{
            fout << preCommand.command << "(" << preCommand.parametersVec[0]
                 << ")" << endl;
            preCommand = curCmd;
        }
    }
    fout << preCommand.command << "(" << preCommand.parametersVec[0] << ")" << endl;
    fin.close();
    fout.close();
    string linuxCmd(argv[1]);
    linuxCmd = "mv tmpoutput " + linuxCmd;
    system(linuxCmd.c_str());
    system("rm -f tmpoutput");
    return 0;
}

