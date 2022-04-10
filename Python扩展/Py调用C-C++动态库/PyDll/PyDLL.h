#pragma once
#ifdef EXPORT_PRO_DLL
#define PRO_API __declspec(dllexport)
#else
#define PRO_API __declspec(dllimport)
#endif
extern "C"
{
    PRO_API int add(int a,int b);
}