#include "array_stack.h"
#include <iostream>

namespace structures {

    template<typename T>
    structures::ArrayStack<T>::ArrayStack() {
        ArrayStack((std::size_t)DEFAULT_SIZE);
    }

    template<typename T>
    structures::ArrayStack<T>::ArrayStack(std::size_t max) {
        max_size_ = max;
        contents = new T[max_size_];
        top_ = -1;
    }

    template<typename T>
    structures::ArrayStack<T>::~ArrayStack<T>() {
        delete [] contents;
    }

    template<typename T>
    bool structures::ArrayStack<T>::empty() {
        return top_ == -1;
    }

    template<typename T>
    bool structures::ArrayStack<T>::full() {
        return top_ == static_cast<int>(max_size()) - 1;
    }

    template<typename T>
    std::size_t structures::ArrayStack<T>::max_size() {
        return max_size_;
    }

    template<typename T>
    void structures::ArrayStack<T>::clear() {
        top_ = -1;
    }

    template<typename T>
    T& structures::ArrayStack<T>::top() {
        if (empty())
            throw std::out_of_range("Pilha vazia");
        return contents[top_];
    }

    template<typename T>
    std::size_t structures::ArrayStack<T>::size() {
        return top_ + 1;
    }

    template<typename T>
    T structures::ArrayStack<T>::pop() {
        if (empty())
            throw std::out_of_range("Pilha vazia");
        T aux = contents[top_];
        top_--;
        return aux;
    }

    template<typename T>
    void structures::ArrayStack<T>::push(const T &data) {
        if (full())
            throw std::out_of_range("Pilha cheia");
        top_++;
        contents[top_] = data;
    }

    template<typename T>
    void structures::ArrayStack<T>::print() {
        for (int i = 0; i < size(); i ++)
            std::cout << contents[i] << std::endl;
    }
}

int main() {
    structures::ArrayStack<int> a(20);
    a.push(3);
    a.push(2);
    a.push(1);
    a.print();
}
