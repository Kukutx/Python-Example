from setuptools import setup, Extension
functions_module = Extension(
    name='example',
    sources=['example.cpp'],
    extra_compile_args=["-O3","-fPIC"],
    include_dirs=['C:\\Users\\liuzh\\AppData\\Local\\Programs\\Python\\Python39\\lib\\site-packages\\pybind11\\include\\'], #pybind11头文件路径
)
setup(ext_modules=[functions_module])
#运行方式
#python setup.py build
#cd build\lib.win-amd64-3.9\
#然后python进入交互模式
#>>import example
#>>example.inadd()
#1
#2
#3>>