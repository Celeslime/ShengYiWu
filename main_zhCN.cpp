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
	cout<<"ԭ��ʥ��������� by sth..\n\n";
	setCol(Green);
	cout<<"��ʾ����ʼ����֮ǰҪ���� <DATA.TXT> �ļ�.\n";
	setCol(White);
	cout<<"���㷶Χ("<<MINK<<","<<MAXK<<"), �� "<<(int)(MAXK-MINK)*3<<"��...\n";
	system("compute.exe");
	cout<<"�������.\n";
	system("print.exe");
	system("draw.exe");
	system("draw.py");
}
