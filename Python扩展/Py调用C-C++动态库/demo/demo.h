#pragma once
#ifdef EXPORT_PRO_DLL
#define PRO_API __declspec(dllexport)
#else
#define PRO_API __declspec(dllimport)
#endif
    PRO_API long my_app(long a);