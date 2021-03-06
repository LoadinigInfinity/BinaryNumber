/*-------------------------------------------------------------------------------
# Name:        binaryNumber_driver.cpp
# Purpose:
#
# Authors:      nakazawam & pearecej
#
# Created:     21/09/2014
#------------------------------------------------------------------------------*/

#include "binaryNumber.cpp"
#include <iostream> // has cout and cin defined therein
using namespace std;

int main() {

    BinaryNumber testing = BinaryNumber();
    cout<< "instantiation of testing list.\n" << endl;

    testing.convert_decimal_to_binary(10);
    cout << testing.to_string() << endl;
    cout <<"converted ten to binary.\n" << endl;

    testing.increment();
    cout << testing.to_string() << endl;
    cout <<"after incrementing (needs to be implemented.)\n" << endl;

    testing.remove_all();
    cout << testing.to_string() << endl;

    return 0;
}

