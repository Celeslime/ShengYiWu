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
int main(){
//	system("intiData.exe");
	double MINK,MAXK;
	freopen("DATA.TXT","r",stdin);
	setCol(White);
	scanf("%*s%lf~%lf",&MINK,&MAXK);
	cout<<"原神圣遗物计算器 by sth..\n\n";
	setCol(Green);
	cout<<"提示：开始计算之前要配置 <DATA.TXT> 文件.\n";
	setCol(White);
	cout<<"计算范围("<<MINK<<","<<MAXK<<"), ≈ "<<(int)(MAXK-MINK)*3<<"秒...\n";
	system("compute.exe");
	cout<<"计算完成.\n";
	system("print.exe");
	system("draw.exe");
	system("draw.py");
}
