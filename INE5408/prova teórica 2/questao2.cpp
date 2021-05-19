#include <iostream>

template <class T, int M>
class BTreeNode {
public:
    BTreeNode() {
        leaf = true;
        size = 0;
    }
    BTreeNode(const T&);
    // private:
    bool leaf;
    // verdadeiro se for folha
    int size;
    // no chaves inseridas
    T keys[M-1]; // vetor de chaves
    BTreeNode *pointers[M];
    int conta_nos_cheios(BTreeNode<T, M> *node);
};

//! Quantos nós da árvore estão cheios
template <class T, int M>
int BTreeNode<T, M>::conta_nos_cheios(BTreeNode<T, M> *node) {
    // Caso específico para ponteiro nulo
    if (node == nullptr)
        return 0;

    int total = 0;  // total de nós cheios
    bool full = true;  // se o nó está cheio
    // Verifica se o nó está cheio, se estiver soma 1 ao
    // total se não ignora
    for (int i = 0; i < M - 1; i++)
        if (node->keys[i] == NULL)
            full = false;
    if (full)
        total++;
    // Repetimos isso recursivamente para todos os nós
    for (int i = 0; i < M; i++)
        total += conta_nos_cheios(node->pointers[i]);

    return total;
}
