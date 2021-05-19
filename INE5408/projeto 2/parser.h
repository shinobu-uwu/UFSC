#ifndef PARSER_H
#define PARSER_H

#include "linked_list.h"
#include "trie_node.h"

#include <iostream>
#include <iostream>
#include <fstream>
#include <sstream>


namespace parser {
//! Percorre o arquivo identificando prefixos e indexando as palavras
class Parser {
    std::string filename;
    structures::TrieNode *letters;

    std::string read_file() {
        std::ifstream file;

        file.open(filename, std::ios::in);
        std::string text, line;
        while (getline(file, line)) {
            text += line;
        }
        
        file.close();
        return text;
    }

    std::size_t count_leaves(structures::TrieNode *node) {
        std::size_t total = 0;
        // Caso nó folha ou é uma palavra completa
        if (node->children->size() == 0 || node->length != 0) {
            total++;
        }
        // Recursividade para cada nó
        for (int i = 0; i < node->children->size(); i++) {
            total += count_leaves(node->children->at(i));
        }

        return total;
    }

public:
    //! Construtor com o nome do arquivo
    Parser(std::string path);
    //! Identifica as palavras e adiciona na árvore Trie
    void identify();
    //! Verifica se as palavras são prefixos
    void verify(std::string words);
};
}  // namespace parser
#endif

using namespace structures;

parser::Parser::Parser(std::string path) {
    filename = path;
    letters = new structures::TrieNode(' ');
}

void parser::Parser::identify() {
    // Ler os arquivo e separá-lo por linha
    std::ifstream file;
    auto lines = new structures::LinkedList<std::string>();
    file.open(filename, std::ios::in);
    std::string read_line, text;
    while (getline(file, read_line)) {
        lines->push_back(read_line);
        text += read_line + '\n';
    }
    file.close();

    for (int i = 0; i < lines->size(); i++) {
        std::string line = lines->at(i);
        std::string word = line.substr(line.find('[') + 1, line.find(']') - 1);

        auto aux = letters;
        for (int j = 0; j < word.length() - 1; j++) {
            auto newNode = new TrieNode(word[j]);
            auto index = aux->children->insert_sorted_unique(newNode);
            aux = aux->children->at(index);
        }
        // Última iteração para adicionar a posição e o comprimento
        auto newNode = new TrieNode(word[word.length() - 1]);
        newNode->length = line.length();
        newNode->position = text.find('[' + word + ']');
        auto index = aux->children->insert_sorted_unique(newNode);
        aux = aux->children->at(index);
    }
}

void parser::Parser::verify(std::string word) {
    auto aux = letters;

    for (int i = 0; i < word.length(); i++) {
        auto letter = new TrieNode(word[i]);
        auto index = aux->children->binary_search(letter);
        // Char não está na árvore, logo a palavra não é prefixo
        if (index == aux->children->size()) {
            std::cout << word << " is not prefix\n";
            return;
        }
        aux = aux->children->at(index);
        delete letter;
    }
    std::size_t n = count_leaves(aux);
    std::cout << word << " is prefix of " << n << " words\n";
    if (aux->length != 0) {
        std::cout << word << " is at (" << aux->position << "," << aux->length << ")\n";
    }
}
