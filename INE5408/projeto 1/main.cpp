#include <iostream>
#include "xml_processor.cpp"

int main() {

    char xmlfilename[100];

    std::cin >> xmlfilename;  // entrada
    
    auto processor = new parser::XMLProcessor(xmlfilename);

    if (processor->parse())
        processor->process();
    else
        std::cout << "error\n";

    return 0;
}