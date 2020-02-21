#include <iostream>
#include "hello.h"

void hello(){
	std::cout << "Hello Hello" << std::endl;
    #ifdef NDEBUG
    std::cout << "Hello World Release!" <<std::endl;
    #else
    std::cout << "Hello World Debug!" <<std::endl;
    #endif
}
