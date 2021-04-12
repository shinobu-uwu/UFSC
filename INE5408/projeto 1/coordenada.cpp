#include "coordenada.h"

structures::Coordenada::Coordenada() {
    i_ = 0;
    j_ = 0;
}

structures::Coordenada::Coordenada(int i, int j) {
    i_ = i;
    j_ = j;
}

structures::Coordenada::~Coordenada() {
    // Nada é alocado dinamicamente, então não precisamos fazer nada
}

int structures::Coordenada::i() {
    return i_;
}

int structures::Coordenada::j() {
    return j_;
}
