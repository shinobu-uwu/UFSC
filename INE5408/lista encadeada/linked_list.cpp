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
    structures::LinkedList<T>::~LinkedList<T>() {
        
    }

    template<typename T>
    void structures::LinkedList<T>::clear() {
        
    }

    template<typename T>
    void structures::LinkedList<T>::push_back(const T &data) {
        Node* newNode = new Node(data, head);
        head = newNode;
        size_++;
    }

    template<typename T>
    void structures::LinkedList<T>::push_front(const T &data) {
        insert(data, size_);
    }

    // TODO arrumar implementação para insert no index 0
    template<typename T>
    void structures::LinkedList<T>::insert(const T &data, std::size_t index) {
        if (index == 0)
            push_back(data);
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
            printf("%p", newNode->next());
            size_++;
        }
    }

//     template<typename T>
//     void structures::LinkedList<T>::insert_sorted(const T &data) {

//     }

    template<typename T>
    T& structures::LinkedList<T>::at(std::size_t index) {
        if (index < 0 || index >= size())
            throw std::out_of_range("Índice inválido");
        Node* aux = head;
        for (int i = 0; i < index; i++)
            aux = aux->next();
        return aux->data();
    }

    template<typename T>
    T structures::LinkedList<T>::pop(std::size_t index) {
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
         
    }

//     template<typename T>
//     T structures::LinkedList<T>::pop_front() {
        
//     }

//     template<typename T>
//     void structures::LinkedList<T>::remove(const T &data) {

//     }

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
        int index = 0;
        while (aux->data() != data || index != size()) {
            index++;
            aux = aux->next();
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
    structures::LinkedList<int> a;
    a.push_back(3);
    a.push_back(2);
    a.push_back(1);
    a.pop(2);
    // a.push_front(500);
    // a.insert(20, 4);
    a.print();
    // std::cout << a.size() << '\n';
    // auto b = a.at(2);
    // printf("%i", b);
    // printf("%p", nullptr);
    // a.~LinkedList();
    // printf("%p", &a);
}