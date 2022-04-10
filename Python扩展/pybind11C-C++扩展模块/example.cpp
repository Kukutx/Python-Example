#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <iostream>
#include <string>
// 这里应该是编译器认为用double类型给字符串赋值了，所以总是报错，搜了一下转字符串的宏：
// #define STR1(R) #R
// #define STR2(R) STR1(R) //然后调用STR2转换一下就行了
namespace py = pybind11;

int add(int i, int j=1)
{
  return i + j;
}

int add2(int i, int j)
{
 return i + j;
}

void inadd()
{
  int a, b;
  std::cin >> a >> b;
  std::cout << a + b;
}

// 绑定c++模板函数
// python是弱类型语言，而C++是强类型语言，如果要让python根据数据类型不同自动调用不同的C++函数，需要多次绑定
template <typename T>
T square(T x) {
    return x * x;
}

//绑定c++指针参数函数
void swap(int* a, int* b) {
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
}

//创建/导出模块
PYBIND11_MODULE(example, m)
{
  //绑定函数和设置函数信息
  m.doc() = "pybind11 example plugin"; // optional module docstring
  m.def("add", &add, "A function which adds two numbers");
  m.def("add2", &add2, "A function which adds two numbers", py::arg("i")=1, py::arg("j")=2);   //默认参数
  m.def("inadd", &inadd, "cin and count");
  m.def("square", &square<double>);
  m.def("square", &square<float>);
  m.def("square", &square<int>);
  m.def("swap", [](py::buffer a, py::buffer b) {\
        py::buffer_info a_info = a.request();
        py::buffer_info b_info = b.request();
        swap(static_cast<int*>(a_info.ptr), static_cast<int*>(b_info.ptr));
    });

  // 在python端使用库中的变量/导出变量
  // 在pybind11通过py::module::attr() 函数实现从C++中导出变量到Python中。内建的类型和泛型对象在被指定为属性（attribute）
  // 时将会被自动的转换，同事也可以使用函数py::module::cast进行显示的转换。 这里说下示例，编译的时候有一行会报语法错误
  m.attr("the_answer") = 42;
  py::object world = py::cast("World");
  m.attr("what") = world;
  m.attr("__version__") = "0.01";               //版本号
} 

// example：模型名，切记不需要引号
// m：可以理解成模块对象把
// m.doc()：help说明
// m.def：用来注册函数和python打通界限，用于绑定





// 7.在python端使用自定义结构体 
// 7.1绑定函数
// //结构体定义
// struct Pet {
//     Pet(const string &name) : name(name) { }
//     void setName(const string &name_) { name = name_; }
//     const string& getName() const { return name; }
//     //此处name变量是public的
//     string name;
// };
// py::class_<T>是模板类，py::init是注册构造函数 
// //注册结构体
// #include <pybind11/pybind11.h>
// namespace py = pybind11;
// PYBIND11_MODULE(example, m) {//这几行代码只使用了一个m，说明这几个函数都是绑在一起
//         py::class_<Pet>(m, "Pet")
//         .def(py::init<const std::string &>())
//         .def("setName", &Pet::setName)
//         .def("getName", &Pet::getName);
// }
// >>> import example
// >>> p = example.Pet('Molly')
// >>> print(p)
// <example.Pet object at 0x10cd98060>
// >>> p.getName()
// u'Molly'
// >>> p.setName('Charly')
// >>> p.getName()
// u'Charly'
// 静态成员函数可以使用class_::def_static()绑定。
// 7.2改进print信息
// 示例程序中print(p)是生成一个无用的数据结构摘要信息，可以绑定一个名为__repr__的函数增加摘要信息。
// py::class_<Pet>(m, "Pet")
//     .def(py::init<const std::string &>())
//     .def("setName", &Pet::setName)
//     .def("getName", &Pet::getName)
//     .def("__repr__",
//         [](const Pet &a) {
//             return "<example.Pet named '" + a.name + "'>";
//         });
// 再执行print(p)得到的结果如下：
// >>> print(p)
// <example.Pet named 'Molly'>
// 7.3绑定变量
// 可以使用class::def_readwrite()来直接注册变量，class::def_readonly注册const变量（常量）。
// py::class_<Pet>(m, "Pet")
//     .def(py::init<const std::string &>())
//     .def_readwrite("name", &Pet::name)
//     // ... remainder …
// >>> p = example.Pet('Molly')
// >>> p.name
// u'Molly'
// >>> p.name = 'Charly'
// >>> p.name
// u'Charly'
// 7.4绑定私有变量
// 私有变量是不能直接访问的，但是可以通过class_::def_property()（class_::defproperty_readonly()用于只读数据）绑定访问私有变量的setter和getter函数。
// class Pet {
// public:
//     Pet(const std::string &name) : name(name) { }
//     void setName(const std::string &name_) { name = name_; }
//     const std::string &getName() const { return name; }
// private:
//     std::string name;
// };
// py::class_<Pet>(m, "Pet")
//     .def(py::init<const std::string &>())
//     .def_property("name", &Pet::getName, &Pet::setName)
//     // ... remainder ...
// 只读变量可以将第三个参数设为nullptr，只写变量可以将第二个参数设为nullptr。
// class_::def_readwrite_static()，class_::def_readonly_static()，class_::def_property_static()，以及class_::def_property_readonly_static()用于绑定静态变量。
// 8.python端为类绑定动态属性
// >>> class Pet:
// ...     name = 'Molly'
// ...
// >>> p = Pet()
// >>> p.name = 'Charly'  # 赋值
// >>> p.age = 2  # 动态增加属性
// C++类要支持动态属性，必须将py::dynamic_attr这个标记添加到py::class_构造函数中:
// py::class_<Pet>(m, "Pet", py::dynamic_attr())
//     .def(py::init<>())
//     .def_readwrite("name", &Pet::name);
// 9.python端实现继承
// 9.1非虚函数的继承
// struct Pet {
//     Pet(const string &name) : name(name) { }
//     string name;
// };
// struct Dog : Pet {
//     Dog(const string &name) : Pet(name) { }
//     string bark() const { return "woof!"; }
// };
// 有两种方式可以实现python端的继承关系，第一种将父类作为子类额外的模板参数。
// py::class_<Pet>(m, "Pet")
//    .def(py::init<const std::string &>())
//    .def_readwrite("name", &Pet::name);
// // Method 1: template parameter:
// py::class_<Dog, Pet /* <- specify C++ parent type */>(m, "Dog")
//     .def(py::init<const std::string &>())
//     .def("bark", &Dog::bark);
// 第二种先创建一个父类对象pet，在子类定义中传入pet，推荐第一种。
// py::class_<Pet> pet(m, "Pet");
// pet.def(py::init<const std::string &>())
//    .def_readwrite("name", &Pet::name);
// // Method 2: pass parent class_ object:
// py::class_<Dog>(m, "Dog", pet /* <- specify Python parent type */)
//     .def(py::init<const std::string &>())
//     .def("bark", &Dog::bark);
// >>> p = example.Dog('Molly')
// >>> p.name
// u'Molly'
// >>> p.bark()
// u'woof!'
// 但是由于子类的bark是非虚函数，并且父类中没有任何虚函数，不能通过父类指针调用子类的bark函数。
// // 在模块中添加这个函数用于测试
// m.def("pet_store", []() { return unique_ptr<Pet>(new Dog("Molly")); });
// >>> p = example.pet_store()
// >>> type(p)  # `Dog` instance behind `Pet` pointer
// Pet          # no pointer downcasting for regular non-polymorphic types
// >>> p.bark()
// AttributeError: 'Pet' object has no attribute 'bark'
// 9.2虚函数的继承
// struct Pet {
//     virtual ~Pet() = default;
// };
// struct Dog : Pet {
//     string bark() const { return "woof!"; }
// };
// // Same binding code
// py::class_<Pet>(m, "Pet");
// py::class_<Dog, Pet>(m, "Dog")
//     .def(py::init<>())
//     .def("bark", &Dog::bark);
// // Again, return a base pointer to a derived instance
// m.def("pet_store2", []() { return unique_ptr<Pet>(new Dog); });
// >>> p = example.pet_store2()
// >>> type(p)
// Dog  # automatically downcast
// >>> p.bark()
// u'woof!'
// 10.绑定重载函数
// struct Pet {
//     Pet(const string &name, int age) : name(name), age(age) { }
//     //重载函数
//     void set(int age_) { age = age_; }
//     void set(const string &name_) { name = name_; }
//     string name;
//     int age;
// };
// 如果直接绑定Pet::set将导致错误，因为编译器不知道是哪种方法。可以将它们转换为函数指针来消除歧义。多个函数绑定相同的名称会自动创建一系列重载函数。
// py::class_<Pet>(m, "Pet")
//    .def(py::init<const std::string &, int>())
//    .def("set", (void (Pet::*)(int)) &Pet::set, "Set the pet's age")
//    .def("set", (void (Pet::*)(const std::string &)) &Pet::set, "Set the pet's name");
// 11.返回值策略
// Python和C ++使用根本不同的方式来管理对象的内存和生命周期，当绑定返回较复杂类型的函数时，可能会导致问题。仅通过查看类型信息，尚不清楚Python是否应该掌管返回的值并负责释放其资源，还是在C ++端进行处理。所以pybind11提供了一些返回值参数，可以将其传递给module::def()and class_::def()函数，默认策略是 return_value_policy::automatic。
//                    返回值策略	                                               描述
// return_value_policy::take_ownership	管理现有对象（但不创建新副本）并获得所有权。当对象的引用计数达到零时，Python将调用析构函数和delete运算符。当C++端执行相同操作或未动态分配数据时，就会发生未定义的行为。
// return_value_policy::copy	创建返回对象的新副本，该副本将归Python所有。此策略相对比较安全，因为这两个实例的生命周期是分离的。
// return_value_policy::move	使用std::move将返回值内容移动到将由Python拥有的一个新的实例中。此策略相对比较安全，因为两个实例（移动源和目标）的生存期已分离。
// return_value_policy::reference	引用现有对象，但不拥有所有权。C ++端负责管理对象的生存期，并在不再使用该对象时对其进行分配。警告：当C ++端删除仍由Python引用和使用的对象时，将会发生未定义的行为。
// return_value_policy::reference_internal	指示返回值的生存期与父对象的生存期相关联，该父对象即被调用方法或属性的隐式this或自self变量。在内部，此策略的工作原理与之类似，return_value_policy::reference但是另外还应用了 调用策略（在下一节中进行描述），只要返回值被Python引用，该策略就 可以防止父对象被垃圾回收。这是通过创建属性获取默认的策略，等等。keep_alive<0, 1> def_propertydef_readwrite
// return_value_policy::automatic	默认策略。return_value_policy::take_ownership当返回值是一个指针时，此策略将回退到该策略 。否则，它分别将return_value_policy::move或 return_value_policy::copy用于rvalue和lvalue引用。有关所有这些不同策略的作用的说明，请参见上文。
// return_value_policy::automatic_reference	如上所述，但是return_value_policy::reference当返回值是指针时使用策略。当从C ++代码手动调用Python函数时（即通过handle :: operator（）），这是函数参数的默认转换策略。您可能不需要使用它。
