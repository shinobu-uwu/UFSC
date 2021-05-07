// Copyright [2021] Matheus Filipe dos Santos Reinert
#ifndef STRUCTURES_ARRAY_LIST_H
#define STRUCTURES_ARRAY_LIST_H

#include <cstdint>
#include <stdexcept>


namespace structures {

template<typename T>
class ArrayList {
 public:
    ArrayList();
    explicit ArrayList(std::size_t max_size);
    ~ArrayList();

    void clear();
    void push_back(const T& data);
    void push_front(const T& data);
    void insert(const T& data, std::size_t index);
    T pop(std::size_t index);
    T pop_back();
    T pop_front();
    void remove(const T& data);
    bool full() const;
    bool empty() const;
    bool contains(const T& data) const;
    std::size_t find(const T& data) const;
    std::size_t size() const;
    std::size_t max_size() const;
    T& at(std::size_t index);
    T& operator[](std::size_t index);
    const T& at(std::size_t index) const;
    const T& operator[](std::size_t index) const;

 private:
    const static auto DEFAULT_MAX = 10u;

    T* contents;
    std::size_t size_;
    std::size_t max_size_;
};
}  // namespace structures

#endif

namespace structures {
    template<typename T>
    structures::ArrayList<T>::ArrayList() {
        ArrayList DEFAULT_MAX;
    }

    template<typename T>
    structures::ArrayList<T>::ArrayList(std::size_t max_size) {
        size_ = 0;
        max_size_ = max_size;
        contents = new T[max_size_];
    }

    template<typename T>
    structures::ArrayList<T>::~ArrayList() {
        delete[] contents;
    }

    template<typename T>
    void structures::ArrayList<T>::clear() {
        size_ = 0;
    }

    template<typename T>
    void structures::ArrayList<T>::push_back(const T& data) {
        insert(data, size_);
    }

    template<typename T>
    void structures::ArrayList<T>::push_front(const T& data) {
        insert(data, 0);
    }

    template<typename T>
    void structures::ArrayList<T>::insert(const T& data, std::size_t index) {
        if (full())
            throw std::out_of_range("Lista cheia");
        if (index > size_ || index < 0)
            throw std::out_of_range("Índice inválido");
        for (std::size_t i = size(); i > index; i--)
            contents[i] = contents[i - 1];
        contents[index] = data;
        size_++;
    }

    template<typename T>
    T structures::ArrayList<T>::pop(std::size_t index) {
        if (empty())
            throw std::out_of_range("Lista vazia");
        if (index >= size() || index < 0)
            throw std::out_of_range("Índice inválido");
        T aux = contents[index];
        for (int i = index + 1; i < static_cast<int>(size()); i++)
            contents[i - 1] = contents[i];
        size_--;
        return aux;
    }

    template<typename T>
    T structures::ArrayList<T>::pop_back() {
        return pop(size() - 1);
    }

    template<typename T>
    T structures::ArrayList<T>::pop_front() {
        return pop(0);
    }

    template<typename T>
    void structures::ArrayList<T>::remove(const T& data) {
        if (empty())
            throw std::out_of_range("Lista vazia");
        for (int i = 0; i < static_cast<int>(size()); i++)
            if (contents[i] == data)
                pop(i);
    }

    template<typename T>
    bool structures::ArrayList<T>::full() const {
        return size() == max_size();
    }

    template<typename T>
    bool structures::ArrayList<T>::empty() const {
        return size() == 0;
    }

    template<typename T>
    bool structures::ArrayList<T>::contains(const T &data) const {
        return static_cast<int>(find(data)) != static_cast<int>(size());
    }

    // Retorna size() se o elemento não estiver na lista,
    // se estiver retorna o index
    template<typename T>
    std::size_t structures::ArrayList<T>::find(const T &data) const {
        for (int i = 0; i < static_cast<int>(size()); i++)
            if (contents[i] == data)
                return i;
        return size();
    }

    template<typename T>
    std::size_t structures::ArrayList<T>::size() const {
        return size_;
    }

    template<typename T>
    std::size_t structures::ArrayList<T>::max_size() const {
        return max_size_;
    }

    template<typename T>
    T& structures::ArrayList<T>::at(std::size_t index) {
        if (index >= size() || index < 0)
            throw std::out_of_range("Índice inválido");
        return contents[index];
    }

    template<typename T>
    T& structures::ArrayList<T>::operator[](std::size_t index) {
        return contents[index];
}
}  // namespace structures
