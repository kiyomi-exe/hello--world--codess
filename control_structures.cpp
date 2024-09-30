#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    int num;
    cout<<"Enter your number: ";
    cin>>num;

    switch(num%2){
        case 0:
            cout<<"Your number is even";
            break;

        case !0:
            cout<<"Your number is odd";
            break;

        default:
            cout<<"Enter a valid number"<<endl;
            break;
    }
    //FOR LOOP
    for (int i=1; i<=10; i++){
        cout<<i<<endl<<endl;
    }
    //WHILE LOOP
    int n=1;
    while (n<=10){
        cout<<n<<endl;
        n++;
    }
    //DO WHILE LOOPS
    int k =1;
    do{
        cout<<k<<endl;
        k++;
    }
    while(k<=25);

    return 0;
}
    
