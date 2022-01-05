#include<iostream>
void print();
double s=0.0005;
double S=0.01;
double max,x0,y0,z0,z,t;
double MINK,MAXK;
int main(){
	freopen("DATA.TXT","r",stdin);
	freopen("out.log","w",stdout);
	double A,B,C,E,D;
	scanf("%*s%lf~%lf%*s%lf%*s%lf%*s%lf%*s%lf%*s%lf",&MINK,&MAXK,&A,&B,&C,&E,&D);
	printf("%d\n",(int)((MAXK-MINK)/S));
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
		printf("%lf %lf %lf %lf\n",k,(A*(1+B+0.466*k*x0)+C),(D+0.622*k*y0),(E+0.311*k*(1-x0-y0)));
	}
}
