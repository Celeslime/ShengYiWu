#include<iostream>
void print();
double s=0.0005;
double S=0.01;
double max,x0,y0,z0,z,t;
double X[2000];int px=0;
double Y[2000];int py=0;
double Z[2000];int pz=0;
double MINK,MAXK;
int main(){
	freopen("DATA.TXT","r",stdin);
	freopen("out.log","w",stdout);
	double A,B,C,E,D;
	scanf("%*s%lf~%lf%*s%lf%*s%lf%*s%lf%*s%lf%*s%lf",&MINK,&MAXK,&A,&B,&C,&E,&D);
	for(double k=MINK;k<MAXK;k+=S){
		max=0;
		for(double x=0;x<1;x+=s){
			for(double y=0;y<1;y+=s){
				//Ô¼ÊøÌõ¼þ 
				z=1-x-y;
				if(z<-0.01)continue;
				if((E+0.311*k*z)>1)continue; 
				
				t=(A*(1+B+0.466*k*x)+C)*((D+0.622*k*y)*(E+0.311*k*z)+1);
				
				if(max<t){
					max=t;
					x0=x;
					y0=y;
				}
			}
		}
		X[px++]=(D+0.622*k*y0);
		Y[py++]=(E+0.311*k*(1-x0-y0));
		Z[pz++]=(A*(1+B+0.466*k*x0)+C);
	}
	print();
}
void print(){
	double j=MINK;
	for(int i=0;i<px;i++,j+=S){
		printf("%lf %lf %lf %lf\n",j,Z[i],X[i],Y[i]);
	}
}
