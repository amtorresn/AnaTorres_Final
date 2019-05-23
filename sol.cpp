#include <iostream>
#include <fstream>
#include <cstdlib>
#include <ctime>
#include <cmath>

using namespace std;
using std::cout;
using std::endl;


void solve(string filename);
void leap_frog(int ti, int tf, double dt, string filename);

int main(){
    leap_frog(0, 10, 0.1, "data.dat");
    return 0;
}


void leap_frog(int ti, int tf, double dt, string filename){
    
    float y = 0;
    float x = 1;
    float t = ti;
    float vx = 0;
    float vy = 1;
    
    float q = 2;
    float m = 7294.29;
    
    float w2 = (q*q)/(m*m);
    ofstream outfile;
    outfile.open(filename);
    
    //Inicializa E
    float E[100][2];
    
    for (int j = 0; j < 101; j++ ){
        if(j<30 || j>70){
            E[j][0] = 0;
            E[j][1] = 0;
        }
        else if(30<j<70){
            E[j][0]= 0;
            E[j][0]= 3;
        }
        
    }
    
    while(t<tf){
        
//         cout << t << " " << t*10 << " " << dt<< endl;
//         outfile << t << " " << E[t*10][0]*x << " " << E[t*10][1]*y << endl;}
        outfile << t << " " << x << " " << y << endl;
        x += vx*dt/2;
        vx += (-w2*x)*dt;
        x += vx*dt/2;
        
        y += vy*dt/2;
        vy += (-w2*y)*dt;
        y += vy*dt/2;
        
        t += dt;
        
    }
    outfile.close();
    
}



