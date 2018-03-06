cmake_minimum_required(VERSION 3.9)
project(BinaryNumber)

set(CMAKE_CXX_STANDARD 11)

add_executable(BinaryNumber
        binaryNumber.cpp
        binaryNumber_driver.cpp
        bit.cpp)
