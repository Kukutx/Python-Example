#define EXPORT_PRO_DLL
#include "PyDLL.h"
#include <string>
PRO_API int add(int a,int b)
{
    return a + b;
}