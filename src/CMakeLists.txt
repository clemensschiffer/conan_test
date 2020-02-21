cmake_minimum_required(VERSION 2.8)
project(MyHello CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()
set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_CURRENT_SOURCE_DIR}/cmake/")
find_package(FMILib REQUIRED)
MESSAGE (STATUS "FMI library include = ${FMILIB_INCLUDE_DIR}")

MESSAGE (STATUS "FMI library include = ${FMILIB_INCLUDE_DIR}")
include_directories(${FMILIB_INCLUDE_DIR})

add_library(hello hello.cpp)
target_link_libraries(hello ${FMILIB_LIBRARY})   

