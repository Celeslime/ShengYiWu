#include<iostream>
//0沙、杯、冠
#define ATK_RATE   0.466
#define DEF_RATE   0.583
#define HP_NUM      4780
//1花
#define HP_NUM      4780
//2羽
#define ATK_NUM      311
//3沙
#define RECHARGE   0.578
//4杯 
#define ELEM_DMG   0.466
#define PHY_DMG    0.583 
//5冠 
#define CRIT_RATE  0.311
#define CRIT_DMG   0.622
using namespace std;



struct crit{
	double DMG;
	double RATE;
	crit(double D=0.50,double R=0.05){
		this->DMG=D;
		this->RATE=R;
	}
};

struct atk{
	double BASE;
	double RATE;
	double UP;
	atk(double B=750,double R=0,double U=0){
		this->BASE=B;
		this->RATE=R;
		this->UP=U;
	}
};

struct charactor{
public:
	atk ATK;
	crit CRIT;
	double MST;
	double ELEM;
	double STEP;
	double HP;
	charactor(){
		this->MST=0; 
		this->STEP=2;
	}
	double getAtk(void){
		return ATK.BASE + ATK.BASE*ATK.RATE/100 + ATK.UP;
	}
//	double getATK2(void){
//		return (ATK.BASE+ATK.UP)*(1+ATK.RATE/100);
//	}
	double getHit(void){
		return getAtk()*STEP;//*0.428  *0.43
	}
	double getElem(void){
		return getHit()*(1+ELEM);
	}
	double getElemCrit(void){
		return getHit()*(1+CRIT.DMG)*(1+ELEM);
	}
}; 
main(){//683 1024
	charactor dan;
	
	dan.ATK.BASE = 335 + 510;
	dan.ATK.RATE = 41.3;//36-72
	dan.ATK.UP   = 0;
	
	
	dan.CRIT.DMG = 0.884;
	dan.ELEM     = 0;
	
	dan.HP       += HP_NUM;
	dan.ATK.UP   += ATK_NUM;
	dan.ATK.RATE += ATK_RATE;
	dan.ELEM     += ELEM_DMG;
	dan.CRIT.DMG += CRIT_DMG;
	for(int x=0;x<5;x++){
		for(int y=0;y<5;y++){
			for(int z=0;z<5;z++){
				int w=4-x-y-z;
				if(w<0 || x+y+z!=3)continue;
				//dan.HP       += HP_NUM;
				dan.ATK.UP   += 0.5*x*ATK_NUM;
				dan.ATK.RATE += 0.5*y*ATK_RATE;
				dan.CRIT.DMG += 0.5*z*CRIT_DMG;
				printf("%d %d %d--- %lf %lf\n",x,y,z,dan.getElem(),dan.getElemCrit());
			}
		}
	}
	//printf("%lf %lf\n",dan.getElem(),dan.getElemCrit());//*1.24*1.736
} 

//845  
//x+y+z=k

// max((845)*(1.413+0.466*x)+343)*((0.844+0.622*y)*(0.25+0.311*z)+1)
// (845*(1.413+0.466*x)+343)*((0.844+0.622*y)*(0.25+0.311*(k-x-y))+1)
//---x/k---(x+y)/k

//(A(1+46.6%x)+B)((D+62.2%y)(E+31.1%z)+1)
//(750(1.377+0.466x)+311)((0.844+0.622*0)(0.25+0.311*0)+1) 
//(750(1.377+0.466*0)+311)((0.844+0.622*x)(0.25+0.311*0)+1)
//(750(1.377+0.466*0)+311)((0.844+0.622*0)(0.25+0.311*x)+1) 
//A为角色+武器攻击(A>666) 
//B为圣遗物小攻击 (B>311)
//D为暴击伤害加成 (D>50%)
//E为暴击率       (E>5%) 

//(A(1+46.6%x)+B)(2(D+31.1%y)(E+31.1%z)+1)
//A为角色+武器攻击(A>666) 
//B为圣遗物小攻击 (B>311)
//D为暴击伤害加成 (D>25%)
//E为暴击率       (E>5%) 


//ln(A(1+0.466k(1-y-z))+B)+ln((D+0.622ky)(E+0.311kz)+1)
//采用主元y
//([A(1+0.466k(1-z))+B] - 0.466Aky)([1+D(E+0.311kz)] + 0.622(E+0.311kz)ky)=0
//a= -0.466Ak*0.622(E+0.311kz)k
//b= [A(1+0.466k(1-z))+B]0.622(E+0.311kz)k - [1+D(E+0.311kz)]0.466Ak
//c= [A(1+0.466k(1-z))+B][1+D(E+0.311kz)]
//max = c - b2/4a
//max = (A(1+0.466k(1-z))+B)(1+D(E+0.311kz)) + (((A(1+0.466k(1-z))+B)0.622(E+0.311kz)k - (1+D(E+0.311kz))0.466Ak)^2)/(4*0.466Ak*0.622(E+0.311kz)k)












//454 55.1     510  41.3
//(845*(1.413+0.466+0.72)+343)/((845-56)*(1.551+0.466)+343)/(1.48)
      
