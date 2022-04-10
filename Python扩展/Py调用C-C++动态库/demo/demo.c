#define EXPORT_PRO_DLL
#include "demo.h"
#include<stdio.h>
long my_app(long a){
    long ret = 0;
    for(long i=0; i<a; i++){
        ret += 2;
    }
    return(ret);
}