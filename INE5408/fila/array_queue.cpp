#include "array_queue.h"
#include <iostream>

namespace structures{

    template<typename T>
    structures::ArrayQueue<T>::ArrayQueue(std::size_t max) {
        max_size_ = max;
        contents = new T[max_size_];
        begin_ = 0;
        end_ = -1;
    }

    template<typename T>
    structures::ArrayQueue<T>::ArrayQueue() {
        ArrayQueue DEFAULT_SIZE;
    }

    template<typename T>
    structures::ArrayQueue<T>::~ArrayQueue() {
        delete [] contents;
    }

    template<typename T>
    void structures::ArrayQueue<T>::enqueue(const T &data) {
        if (full())
            throw std::out_of_range("Fila cheia");
        end_++;
        contents[end_] = data;
    }

    template<typename T>
    T structures::ArrayQueue<T>::dequeue() {
        if (empty())
            throw std::out_of_range("Fila vazia");
        T elemento = contents[0];
        for (int i = 0; i < static_cast<int>(size()); i++) {
            contents[i] = contents[i + 1];
        }
        end_--;
        return elemento;
    }

    template<typename T>
    T& structures::ArrayQueue<T>::back() {
        return contents[end_];
    }

    template<typename T>
    bool structures::ArrayQueue<T>::empty() {
        return end_ == -1;
    }

    template<typename T>
    bool structures::ArrayQueue<T>::full() {
        return end_ == max_size() - 1;
    }

    template<typename T>
    std::size_t structures::ArrayQueue<T>::size() {
        return end_ + 1;
    }

    template<typename T>
    std::size_t structures::ArrayQueue<T>::max_size() {
        return max_size_;
    }

    template<typename T>
    void structures::ArrayQueue<T>::print() {
        for (int i = 0; i < size(); i++)
            std::cout << i + 1 << ": " << contents[i] << std::endl;
    }

    template<typename T>
    void structures::ArrayQueue<T>::clear() {
        end_ = -1;
    }

}

using namespace structures;
int main() {
    ArrayQueue<int> a(2);
    a.enqueue(3);
    a.enqueue(2);
    a.print();
    a.clear();
    std::cout << a.empty() << std::endl;
    std::cout << a.full() << "\n";
    // a.dequeue();
    // a.print();
}
