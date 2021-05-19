#ifndef TRIE_NODE_LINKED_LIST_H
#define TRIE_NODE_LINKED_LIST_H
#include <cstdint>
#include <iostream>

#define TEMP template<typename T>

namespace structures{
//! Lista encadeada especializada em ponteiros
TEMP
class TrieNodeLinkedList {
    class Node {
        T data_;
        Node *next_;

    public:
        explicit Node(T data) {
            data_ = data;
            next_ = nullptr;
        }

        Node(T data, Node *next) {
            data_ = data;
            next_ = next;
        }

        T& data() {
            return data_;
        }

        Node* next() {
            return next_;
        }

        void next(Node *next) {
            next_ = next;
        }
    };
    std::size_t size_;
    Node *head;

    Node* end() {
        Node *aux = head;
        while (aux != nullptr)
            aux = aux->next();
        return aux;
    }

    Node* get_index(std::size_t index) {
        Node *aux = head;
        for (int i = 0; i < index; i++)
            aux = aux->next();
        return aux;
    }

public:
    //! Construtor padrão, inicializa uma lista vazia
    TrieNodeLinkedList();
    //! Destrutor
    ~TrieNodeLinkedList();
    //! Deleta todos os elementos
    void clear();
    //! Insere no final
    void push_back(const T& data);
    //! Insere no inicio
    void push_front(const T& data);
    //! Insere no índice especificado
    void insert(const T& data, std::size_t index);
    //! Insere em ordem
    void insert_sorted(const T& data);
    //! Insere em ordem se o elemento não estiver na lista, considerando uma lista ordenada
    std::size_t insert_sorted_unique(const T& data);
    //! Acessa o elemento na posição, lançando exceções se necessário
    T& at(std::size_t index);
    //! Acessa o elemento na posição
    T& operator[](std::size_t index);
    //! Retirar da posição
    void pop(std::size_t index);
    //! Retirar do final
    void pop_back();
    //! Retirar do inicio
    void pop_front();
    //! Remover o elemento
    void remove(const T& data);
    //! Verifica se a lista está vazia
    bool empty() const;
    //! Verifica se o elemento está na lista
    bool contains(const T& data);
    //! A posição do elemento específico
    std::size_t find(const T& data) const;
    //! Tamanho da lista
    std::size_t size() const;
    //! Busca binária na lista, retorna size se o elemento não estiver presente
    std::size_t binary_search(const T& data);
    //! Busca binária na lista, dado um range
    std::size_t binary_search(const T& data, std::size_t left, std::size_t right);
};
}  // namespace structures

#endif

TEMP
structures::TrieNodeLinkedList<T>::TrieNodeLinkedList() {
    size_ = 0;
    head = nullptr;
}

TEMP
structures::TrieNodeLinkedList<T>::~TrieNodeLinkedList() {
    clear();
}

TEMP
void structures::TrieNodeLinkedList<T>::clear() {
    while (!empty())
        pop_front();
}

TEMP
void structures::TrieNodeLinkedList<T>::push_back(const T& data) {
    insert(data, size());
}

TEMP
void structures::TrieNodeLinkedList<T>::push_front(const T& data) {
    if (empty()) {
        head = new Node(data);
    } else {
        head  = new Node(data, head);
    }
    size_++;
}

TEMP
void structures::TrieNodeLinkedList<T>::insert(const T& data, std::size_t index) {
    if (index > size())
        throw std::out_of_range("Invalid index");

    if (index == 0) {
        push_front(data);
    } else {
        Node *aux = head;
        for (int i = 0; i < index - 1; i++)
            aux = aux->next();
        Node *newNode = new Node(data, aux->next());
        aux->next(newNode);
        size_++;
    }
}

TEMP
void structures::TrieNodeLinkedList<T>::insert_sorted(const T& data) {
    std::size_t index = 0;
    Node *aux = head;
    while (aux != nullptr && *data > *aux->data()) {
        index++;
        aux = aux->next();
    }

    insert(data, index);
}

TEMP
std::size_t structures::TrieNodeLinkedList<T>::insert_sorted_unique(const T& data) {
    auto index = binary_search(data);
    if (index == size()) {
        std::size_t index = 0;
        Node *aux = head;
        while (aux != nullptr && *data > *aux->data()) {
            index++;
            aux = aux->next();
        }

        insert(data, index);
        return index;
    }
    return index;
}

TEMP
T& structures::TrieNodeLinkedList<T>::at(std::size_t index) {
    if (index < 0 || index >= size())
        throw std::out_of_range("Not a valid index");

    Node *aux = head;
    for (int i = 0; i < index; i++)
        aux = aux->next();
    return aux->data();
}

TEMP
T& structures::TrieNodeLinkedList<T>::operator[](std::size_t index) {
    Node *aux = head;
    for (int i = 0; i < index; i++)
        aux = aux->next();
    return aux->data();
}

TEMP
void structures::TrieNodeLinkedList<T>::pop(std::size_t index) {
    if (empty())
        throw std::out_of_range("Empty list");
    
    if (index == 0) {
        return pop_front();
    } else {
        Node *aux = get_index(index - 1);
        aux->next(aux->next()->next());
        aux->next()->data().~T();
        delete aux->next();
        size_--;
    }
}

TEMP
void structures::TrieNodeLinkedList<T>::pop_back() {
    Node *aux = get_index(size() - 2);
    aux->next()->data().~T();
    delete aux->next();
    aux->next(nullptr);
    size_--;
}

TEMP
void structures::TrieNodeLinkedList<T>::pop_front() {
    T value = head->data();
    Node *aux = head;
    head = aux->next();
    aux->data().~T();
    delete aux;
    size_--;
}

TEMP
void structures::TrieNodeLinkedList<T>::remove(const T& data) {
    pop(find(data));
}

TEMP
bool structures::TrieNodeLinkedList<T>::empty() const {
    return size_ == 0;
}

TEMP
bool structures::TrieNodeLinkedList<T>::contains(const T& data) {
    return !find(data) == size();
}

TEMP
std::size_t structures::TrieNodeLinkedList<T>::find(const T& data) const {
    Node *aux = head;
    std::size_t index;
    while (aux != nullptr && *aux->data() != *data) {
        aux = aux->next();
        index++;
    }

    return index;
}

TEMP
std::size_t structures::TrieNodeLinkedList<T>::size() const {
    return size_;
}

TEMP
std::size_t structures::TrieNodeLinkedList<T>::binary_search(const T& data) {
    return binary_search(data, 0, size() - 1);
}

TEMP
std::size_t structures::TrieNodeLinkedList<T>::binary_search(const T& data, std::size_t left, std::size_t right) {
    if(!empty())
        if (right >= left) {
            std::size_t mid = left + (right - left) / 2;

            if (*at(mid) == *data)
                return mid;
            
            if (*at(mid) > *data)
                return binary_search(data, left, mid - 1);

            return binary_search(data, mid + 1, right);
        }
    // Elemento não presente
    return size();
}

