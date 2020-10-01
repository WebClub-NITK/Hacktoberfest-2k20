#include <iostream>
using namespace std;
int stack[100000];
int top=-1;
void push(int x)
{
    stack[++top]=x;
}
void pop()
{
    if(top<0)
    printf("empty");
    else
    --top;


}



int main() {

int t=1,y,x,k;
printf("enter 1 to push\n");
printf("enter 2 to pop\n");
printf("enter 3 to getmaxelement\n");
printf("enter 4 to exit\n");
while(t-->0)
{
scanf("%d",&x);
if(x==1)
{
    scanf("%d",&y);
    push(max(y,stack[top]));

}
else if(x==2)
{
    pop();
}
else if(x==3)  {
printf("%d\n",stack[top]);    
}
else
t=0;
}
    
    return 0;
}
