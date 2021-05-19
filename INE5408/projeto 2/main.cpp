#include "parser.h"

using namespace structures;

int main() {
    using namespace std;

    string filename;

    string word;

    cin >> filename;  // entrada
    auto parser = new parser::Parser(filename);
    parser->identify();
    
    while (1) {  // leitura das palavras ate' encontrar "0"
        cin >> word;
        if (word.compare("0") == 0) {
            break;
        }
        parser->verify(word);
    }

    return 0;
}