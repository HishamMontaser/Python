import os 
import subprocess

# f1 = open("Assignment.cpp","x")
f1 = open("Assignment.cpp" , "w")
f1.write('''#include<iostream>\n
            using namespace std ; \n
            int main(){ \n
            string variable; \n
            cout<<"Please enter your string"<<endl;
            getline(cin,variable); \n
            cout<<"Here's your string"<<variable<<endl; \n
            return 0 ;\n
            } '''   )

f1.close()

subprocess.call("g++ Assignment.cpp -o out.exe")
subprocess.call("out.exe")