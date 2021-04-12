#include "xml_processor.h"
#include "linked_stack.cpp"
#include "linked_queue.cpp"
#include "coordenada.cpp"
#include <algorithm>
#include <cstdlib>
#include <fstream>
#include <limits>
#include <string>
#include <iostream>

parser::XMLProcessor::XMLProcessor(std::string name) {
    // file.open(filename, std::ios::in);
    filename = name;
}

parser::XMLProcessor::~XMLProcessor() {
    // file.close();
}

bool parser::XMLProcessor::parse() {
    // Abrir e ler o texto do arquivo
    std::ifstream file;
    file.open(filename, std::ios::in);
    std::string text, line;
    while (getline(file, line)) {
        text += line;
    }

    structures::LinkedStack<std::string> *pilha
        = new structures::LinkedStack<std::string>();

    // Checa o arquivo de texto
    for (int i = 0; i <= text.length(); i++) {
        if (text[i] == '<' && text[i + 1] != '/') {
            std::string tag;
            
            for (int n = i + 1; text[n] != '>'; n++) {  // Percorremos até o fechamento da tag
                tag += text[n];
            } 
            pilha->push(tag);
        }
        else if(text[i] == '<' && text[i + 1] == '/') {
            std::string tag;
            for (int n = i + 2; text[n] != '>'; n++)  // Não precisamos incluir '/'
                tag += text[n];

            if (pilha->empty()) {
                return false;
            } else {
                std::string top = pilha->pop();

                if (tag != top) {
                    return false;
                }
            }
        }
   }

   if (!pilha->empty()) {
       return false;
    }
    delete pilha;
    file.close();
    return true;
}

void parser::XMLProcessor::process() {
    // Abrir e ler o arquivo de texto
    std::ifstream file;
    file.open(filename, std::ios::in);
    std::string text, line;
    while (getline(file, line))
        text += line;

    int count = 0;
    std::size_t pos = text.find("<img>", 0); // Primeira ocorrência
    while (pos != std::string::npos)
    {
        count++;
        pos = text.find("<img>", pos + 1);
    }

    for (int iteration = 0; iteration < count; iteration++) {
        // Achamos o nome do arquivo
        std::string name;
        for (int i = text.find("<name>") + 6; i < text.find("</name>"); i++)
            name += text[i];

        // Achamos a altura e largura da matriz
        int height, width;
        std::string h, w;
        for (int i = text.find("<height>") + 8; i < text.find("</height>"); i++)
            h += text[i];
        for (int i = text.find("<width>") + 7; i < text.find("</width>"); i++)
            w += text[i];
        height = std::stoi(h);
        width = std::stoi(w);

        // Agora criamos a matriz de dados com base no texto.
        // Ela será um array de string, que por si só é um array de caracter.
        std::string data_text;
        std::string E[height]; // Matriz de entrada E
        for (int i = text.find("<data>") + 6; i < text.find("</data>"); i++)
            data_text += text[i];
        // Popula o array de string com os dados
        for (int i = 0; i < height; i++)
            E[i] = data_text.substr(
                i * width,
                (i + 1) * width);

        // Rotulação utilizando uma fila encadeada
        int rotulo = 1;
        auto fila = new structures::LinkedQueue<structures::Coordenada*>();
        int R[height][width];  // Matriz populada com 0s R
        for (int i = 0; i < height; i++) {
            for (int j = 0; j < width; j++) {
                R[i][j] = 0;
            }
        }
        for (int i = 0; i < height; i++) {
            for (int j = 0; j < width; j++) {
                if (E[i][j] == '1' && R[i][j] == 0) {
                    fila->enqueue(new structures::Coordenada(i, j));
                    R[i][j] = rotulo;
                    while (!fila->empty()) {
                        auto coord = fila->dequeue();
                        int cima = coord->i() - 1;
                        int baixo = coord->i() + 1;
                        int esquerda = coord->j() - 1;
                        int direita = coord->j() + 1;

                        if (cima >= 0 && E[cima][coord->j()] == '1' && R[cima][coord->j()] == 0) {
                            fila->enqueue(new structures::Coordenada(cima, coord->j()));
                            R[cima][coord->j()] = rotulo;
                        }
                        if (baixo < height && E[baixo][coord->j()] == '1' && R[baixo][coord->j()] == 0) {
                            fila->enqueue(new structures::Coordenada(baixo, coord->j()));
                            R[baixo][coord->j()] = rotulo;
                        }
                        if (esquerda >= 0 && E[coord->i()][esquerda] == '1' && R[coord->i()][esquerda] == 0) {
                            fila->enqueue(new structures::Coordenada(coord->i(), esquerda));
                            R[coord->i()][esquerda] = rotulo;
                        }
                        if (direita < width && E[coord->i()][direita] == '1' && R[coord->i()][direita] == 0) {
                            fila->enqueue(new structures::Coordenada(coord->i(), direita));
                            R[coord->i()][direita] = rotulo;
                        }
                        delete coord;
                    }
                    rotulo++;
                }
            }
        }
        delete fila;
        // Resultado
        int max = -1;
        for (int i = 0; i < height; i++)
            for (int j = 0; j < width; j++)
                if (R[i][j] > max)
                    max = R[i][j];
        std::cout << name << ' ' << max << '\n';
        // Tiramos a parte do texto já processada
        text = text.substr(text.find("</img>") + 6, text.length());
    }
    file.close();
} 
