#include "linked_stack.h"
#include <iostream>

template<typename T>
structures::LinkedStack<T>::LinkedStack() {
    top_ = nullptr;
    size_ = 0 ;
}

template<typename T>
structures::LinkedStack<T>::~LinkedStack() {
    clear();
}

template<typename T>
void structures::LinkedStack<T>::clear() {
    while (!empty())
        pop();
}

template<typename T>
void structures::LinkedStack<T>::push(const T &data) {
    Node *newNode = new Node(data, top_);
    top_ = newNode;
    size_++;
}

template<typename T>
T structures::LinkedStack<T>::pop() {
    if (empty())
        throw std::out_of_range("Empty stack!");
    Node *aux = top_;
    T value = top();

    top_ = top_->next();
    aux->data().~T();
    size_--;

    delete aux;
    return value;
}

template<typename T>
T& structures::LinkedStack<T>::top() const {
    return top_->data();
}

template<typename T>
bool structures::LinkedStack<T>::empty() const {
    return size() == 0;
}

template<typename T>
std::size_t structures::LinkedStack<T>::size() const {
    return size_;
}
