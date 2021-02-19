#include "array_list.h"
#include <iostream>

#define TEMP template<typename T> // macro para template

namespace structures
{
    TEMP
    structures::ArrayList<T>::ArrayList()
    {
        ArrayList(DEFAULT_MAX);
    }

    TEMP
    structures::ArrayList<T>::ArrayList(std::size_t max_size)
    {
        size_ = 0;
        max_size_ = max_size;
        contents = new T[max_size_];
    }

    TEMP
    structures::ArrayList<T>::~ArrayList()
    {
        delete[] contents;
    }

    TEMP
    void structures::ArrayList<T>::push_back(const T& data)
    {
        insert(data, size_);
    }

    TEMP
    void structures::ArrayList<T>::push_front(const T& data)
    {
        insert(data, 0);
    }

    TEMP
    void structures::ArrayList<T>::insert(const T& data, std::size_t index)
    {
        if (full())
            throw std::out_of_range("Lista cheia");
        if (index > size_ || index < 0)
            throw std::out_of_range("Índice inválido");
        for (int i = size_; i > index; i--)
            contents[i] = contents[i - 1];
        contents[index] = data;
        size_++;
    }

    TEMP
    void structures::ArrayList<T>::insert_sorted(const T &data)
    {
        for (int i = 1; i < size_; i++)
            if (contents[i] >= data && contents[i - 1] <= data)
                insert(data, i);
    }

    TEMP
    void structures::ArrayList<T>::print()
    {
        for (int i = 0 ; i < size_; i++)
        {
            std::cout << contents[i] << ", ";
        }
    }

    TEMP
    bool structures::ArrayList<T>::full() const
    {
        return size_ == max_size_;
    }
}

using namespace structures;
using namespace std;

int main()
{
    ArrayList<int> a(30);
    a.push_back(1);
    a.push_back(3);
    a.push_back(4);
    a.insert_sorted(2);
    a.print();
}
