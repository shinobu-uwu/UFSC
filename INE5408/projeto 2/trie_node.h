#ifndef TRIE_NODE_H
#define TRIE_NODE_H

#include "trie_node_linked_list.h"

namespace structures {
//! Nó da trie, armazena letra, os seus filhos, posição e comprimento se for palavra
struct TrieNode {
    //! Letra do nó
    char letter;
    //! Filhos do nó
    structures::TrieNodeLinkedList<structures::TrieNode*> *children;
    //! Posição de ínico da palavra, 0 se não for final de uma palavra
    unsigned long position;
    //! Tamanho da palavra, 0 se não for final de uma palavra
    unsigned long length;
    //! Construtor
    TrieNode(char letter);
    //! Destrutor
    ~TrieNode();
    //! Operador de igualdade, compara as letras de 2 nós
    bool operator==(const TrieNode& node);
    //! Operador maior, compara as letras de 2 nós
    bool operator>(const TrieNode& node);
    //! Operador diferente, compara as letras de 2 nós
    bool operator!=(const TrieNode& node);
};
}  // namespace structures

#endif

structures::TrieNode::TrieNode(char letter_) {
    letter = letter_;
    children = new TrieNodeLinkedList<TrieNode*>();
    length = 0;
    position = 0;
}

structures::TrieNode::~TrieNode() {
    children->clear();
}

bool structures::TrieNode::operator==(const TrieNode& node) {
    return letter == node.letter;
}

bool structures::TrieNode::operator>(const TrieNode& node) {
    return letter > node.letter;
}

bool structures::TrieNode::operator!=(const TrieNode& node) {
    return letter != node.letter;
}