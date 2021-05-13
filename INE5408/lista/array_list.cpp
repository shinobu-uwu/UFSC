#include "array_list.h"
#include <iostream>

#define TEMP template<typename T> // macro para template

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
    void structures::ArrayList<T>::insert_sorted(const T &data) {
        for (int i = 1; i < static_cast<int>(size()); i++) {
            if (contents[i - 1] <= data && contents[i] >= data) {
                insert(data, i);
                break;
            }
        }
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

    // Remove r elementos de cada extremidade da lista e
    // depois espelha a lista, assumindo que a lista tenha tamanho
    // suficiente para isso.
    template<typename T>
    void structures::ArrayList<T>::peel_mirror(int r) {
        // Parte 1:
        // Processo iterativo para remover da lista os elementos desejados,
        // sempre retiramos o primeiro e o úlimo elemento r vezes.
        for (int i = 0; i < r; i++) {
            pop_front();
            pop_back();
        }

        // Parte 2:
        std::size_t initial_size = size();  // Como o size se altera durante o processo vamos salvá-lo primeiro

        // Processo iterativo para percorrer a lista e inserí-los na última posição initial
        for (int i = 0; i < initial_size; i++)
            insert(contents[i], initial_size);
    }

    template<typename T>
    void structures::ArrayList<T>::reposicionaSubLista(int p, int k) {
        // Lista para armazenar os elementos selecionados
        ArrayList<T> *elementosSelecionados = new ArrayList<T>(k);

        // Adicionamos os elementos desejados na nova lista e retiramos da atual
        for (int i = p; i < p + k; i++) { // temos que selecionar k elementos da lista atual a partir de p
            elementosSelecionados->push_back(pop(i));  // Se o indice for invalido uma excecao sera lancada
        }

        // Adicionamos a nova lista no final da que já temos
        for (int i = 0; i < elementosSelecionados->size(); i++)
            push_back(elementosSelecionados->at(i));
    }

    template<typename T>
    void structures::ArrayList<T>::print() {
        for (int i = 0; i < size(); i++) {
            std::cout << contents[i] << '\n';
        }
    }
}  // namespace structures
