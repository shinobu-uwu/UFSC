#include "array_queue.h"
#include <cstdlib>
#include <stdexcept>
#include <iostream>

namespace structures
{
    template<typename T>
    structures::ArrayQueue<T>::ArrayQueue()
    {
        ArrayQueue(DEFAULT_SIZE);
    }

    template<typename T>
    structures::ArrayQueue<T>::ArrayQueue(std::size_t max)
    {
        max_size_ = max;
        contents = new T[max_size_];
        begin_ = 0;
        end_ = -1;
        size_ = 0;
    }

    template<typename T>
    structures::ArrayQueue<T>::~ArrayQueue<T>()
    {
        delete[] contents;
    }

    template<typename T>
    T structures::ArrayQueue<T>::enqueue(const T &data)
    {
        if (full())
            throw std::out_of_range("Fila cheia");
        end_ = (end_ + 1) % size_;
        contents[end_] = data;
        size_++;
        return contents[end_];
    }

    template<typename T>
    T structures::ArrayQueue<T>::dequeue()
    {
        if (empty())
            throw std::out_of_range("Fila vazia");
        T data = contents[begin_];
        begin_ = (begin_ + 1) % size_;
        size_--;
        return data;
    }

    template<typename T>
    T& structures::ArrayQueue<T>::back()
    {
        return contents[begin_ + size_ - 1];
    }

    template<typename T>
    void structures::ArrayQueue<T>::clear()
    {
        delete this;
        ArrayQueue(max_size());
    }

    template<typename T>
    std::size_t structures::ArrayQueue<T>::size()
    {
        return size_;
    }

    template<typename T>
    std::size_t structures::ArrayQueue<T>::max_size()
    {
        return max_size_;
    }

    template<typename T>
    bool structures::ArrayQueue<T>::empty()
    {
        return size_ == 0;

    }

    template<typename T>
    bool structures::ArrayQueue<T>::full()
    {
        return size_ == max_size();
        
    }

    template<typename T>
    T& structures::ArrayQueue<T>::front()
    {
        return contents[begin_];
    }
}

using namespace structures;

int main()
{
    ArrayQueue<int> a(5);
    for (int i = 0; i < 5; i++)
    {
        std::cout << a.enqueue(i) << ", ";
    }
    std::cout << std::endl << a.back() << std::endl << a.front() << std::endl;
}