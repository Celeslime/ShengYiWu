#include<iostream>
using namespace std;
int n;
double K[2000],X[2000],Y[2000],Z[2000];
void draw();
int main(){
	freopen("out.log","r",stdin);
	freopen("draw.py","w",stdout);
	cin>>n;
	for(int i=0;i<n;i++){
		scanf("%lf%lf%lf%lf",&K[i],&X[i],&Y[i],&Z[i]);
	}
	draw();
}
void draw(){
	printf("from matplotlib import pyplot as plt\nimport numpy as np\n");
	/* K arr */
	printf("K= np.array([");
	for(int i=0;i<n;i++){
		printf("%lf,",K[i]);
	}
	printf("])\n\n");
	/* X arr */
	printf("X= np.array([");
	for(int i=0;i<n;i++){
		printf("%lf,",X[i]);
	}
	printf("])\nplt.plot(K,X,color=\'green\')\n");
	/* Y arr */
	printf("Y= np.array([");
	for(int i=0;i<n;i++){
		printf("%lf,",Y[i]);
	}
	printf("])\nplt.plot(K,1000*Y,color=\'red\')\n");
	/* Z arr */
	printf("Z= np.array([");
	for(int i=0;i<n;i++){
		printf("%lf,",Z[i]);
	}
	printf("])\nplt.plot(K,1000*Z,color=\'blue\')\n");
	
	printf("plt.ylim(0,)\nplt.show()\n");
}
