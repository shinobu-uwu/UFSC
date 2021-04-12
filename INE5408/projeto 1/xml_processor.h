#include <string>
#include <fstream>

namespace parser {
   class XMLProcessor {
    public:
        // Construtor com o path do arquivo
        XMLProcessor(std::string filename);
        // Destrutor
        ~XMLProcessor();
        // Verifica se o árquivo XML é válido
        bool parse();
        // Processa a imagem na tag <data> do arquivo XML validado
        void process();

    private:
      // std::ifstream file;
      std::string filename;
    };
}  // namespace structures