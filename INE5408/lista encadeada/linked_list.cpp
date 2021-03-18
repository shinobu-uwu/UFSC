#include "linked_list.h"
#include <stdexcept>
#include <stdio.h>
#include <iostream>

namespace structures {
    template<typename T>
    structures::LinkedList<T>::LinkedList() {
        size_ = 0;
    }

    template<typename T>
    structures::LinkedList<T>::~LinkedList() {
        Node *aux = head;  // Percorrer a lista
        Node *aux2;  // Guardar referência para ser deletada
        while (aux != nullptr) {
            aux2 = aux;
            aux = aux->next();
            aux2->data().~T();
            delete aux2;
        }
    }

    template<typename T>
    void structures::LinkedList<T>::clear() {
        Node *aux = head;  // Percorrer a lista
        Node *aux2;  // Guardar referência para ser deletada
        while (aux != nullptr) {
            aux2 = aux;
            aux = aux->next();
            aux2->data().~T();
            delete aux2;
        }
        size_ = 0;
        head = nullptr;
    }

    template<typename T>
    void structures::LinkedList<T>::push_front(const T &data) {
        Node* newNode = new Node(data, head);
        head = newNode;
        size_++;
    }

    template<typename T>
    void structures::LinkedList<T>::push_back(const T &data) {
        insert(data, size_);
    }

    // TODO arrumar implementação para insert no index 0
    template<typename T>
    void structures::LinkedList<T>::insert(const T &data, std::size_t index) {
        if (index < 0 || index > size())
            throw std::out_of_range("Indice inválido");
        if (index == 0)
            push_front(data);
        else {
            Node* aux = head;
            Node* aux2; // node que está no index
            Node* newNode = new Node(data);
            for (int i = 0; i < index - 1; i++) {
                aux = aux->next();
            }
            aux2 = aux->next();
            newNode->next(aux2);
            aux->next(newNode);
            size_++;
        }
    }

    template<typename T>
    void structures::LinkedList<T>::insert_sorted(const T &data) {
        Node* aux = head;
        int i = 0 ; // Index para inserção
        while (aux != nullptr) {
            if (aux->data() >= data){
                insert(data, i);
                break;
            }
            aux = aux->next();
            i++;
        }
        if (aux == nullptr)
            push_back(data);
    }

    template<typename T>
    T& structures::LinkedList<T>::at(std::size_t index) {
        if (index < 0 || index >= size())
            throw std::out_of_range("Índice inválido");
        Node* aux = head;
        for (int i = 0; i < index; i++)
            aux = aux->next();
        return aux->data();
    }

    // TODO fix pop(0)
    template<typename T>
    T structures::LinkedList<T>::pop(std::size_t index) {
        if (empty())
            throw std::out_of_range("Lista vázia");
        if (index < 0 || index >= size())
            throw std::out_of_range("Indice inválido");
        Node* aux = head;
        Node* aux2;
        T value;
        for (int i = 0; i < index - 1; i++) {  // 1 posição antes do elemento que queremos deletar
            aux = aux->next();
        }
        aux2 = aux->next();
        aux->next(aux2->next());
        value = aux2->data();
        aux2->data().~T();
        delete aux2;
        size_--;
        return value;
    }

    template<typename T>
    T structures::LinkedList<T>::pop_back() {
        int i = size() - 1;
        if (i == 0)
            return pop_front();
        return pop(size() - 1);
    }

    template<typename T>
    T structures::LinkedList<T>::pop_front() {
        if (empty())
            throw std::out_of_range("Lista vazia");
        Node *aux = head;  // ponteiro para destruir a head atual
        T value = aux->data();  // variável para retornar o dado que estava na head
        head = head->next();
        aux->data().~T();
        delete aux;
        size_--;
        return value;
    }

    template<typename T>
    void structures::LinkedList<T>::remove(const T &data) {
        int i = find(data);
        if (i == 0)
            pop_front();
        else
            pop(i);
    }

    template<typename T>
    bool structures::LinkedList<T>::empty() const {
        return size_ == 0;
    }

    template<typename T>
    bool structures::LinkedList<T>::contains(const T &data) const {
        return find(data) != size();
    }

    // Retorna o size se o elemento não estiver na lista.
    template<typename T>
    std::size_t structures::LinkedList<T>::find(const T &data) const {
        Node* aux = head;
        std::size_t index = 0;
        for (int i = 0; i < size(); i++) {
            if (aux->data() == data)
                break;
            aux = aux->next();
            index++;
        }
        return index;
    }

    template<typename T>
    std::size_t structures::LinkedList<T>::size() const {
        return size_;
    }

   template<typename T>
    void structures::LinkedList<T>::print() {
        Node* aux = head;
        for (int i = 0; i < size(); i++) {
            std::cout << aux->data() << " @ " << aux << '\n';
            aux = aux->next();
        }
    }
}

int main() {
    structures::LinkedList<int> a{};
    for (auto i = 0; i < 10; ++i) {
        a.push_back(i);
    }
    a.pop(5);
    a.pop(5);
    a.size();
    a.pop(8);
}
