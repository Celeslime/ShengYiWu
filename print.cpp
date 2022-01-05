#include<iostream>
#include<windows.h>
#define Blue   1
#define Green  2
#define Red    4
#define White  7
using namespace std;
void setCol(char col){
	SetConsoleTextAttribute(
		GetStdHandle(STD_OUTPUT_HANDLE), 
		FOREGROUND_INTENSITY|col);
}
void printHead(){
	setCol(Green);
	cout<<"ATK    ";
	setCol(Red);	
	cout<<"CRIT-DMG   ";
	setCol(Blue);
	cout<<"CRIT-RATE\n";
} 
int main(){
	freopen("out.log","r",stdin);
	printHead();
	int n;
	double K,X,Y,Z;
	cin>>n;
	for(int i=0;i<n;i++){
		scanf("%*lf%lf%lf%lf",&X,&Y,&Z);
		setCol(Green);
		printf("%.0lf\t",X);
		setCol(Red);
		printf("%5.1lf%\t",100*Y);
		setCol(Blue);
		printf("%7.1lf%\n",100*Z);
	}
	printHead();
}
