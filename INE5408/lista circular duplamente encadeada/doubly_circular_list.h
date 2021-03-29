// Copyright [2021] Matheus Filipe dos Santos Reinert

#include <cstdint>

namespace structures {

template<typename T>
class DoublyCircularList {
 public:
    DoublyCircularList();
    ~DoublyCircularList();

    void clear();

    void push_back(const T& data);  // insere no fim
    void push_front(const T& data);  // insere no início
    void insert(const T& data, std::size_t index);  // insere na posição
    void insert_sorted(const T& data);  // insere em ordem

    T pop(std::size_t index);  // retira da posição
    T pop_back();   // retira do fim
    T pop_front();  // retira do início
    void remove(const T& data);  // retira específico

    bool empty() const;  // lista vazia
    bool contains(const T& data) const;  // contém

    T& at(std::size_t index);  // acesso a um elemento (checando limites)
    const T& at(std::size_t index) const;  // getter constante a um elemento

    std::size_t find(const T& data) const;  // posição de um dado
    std::size_t size() const;  // tamanho

 private:
    class Node {
     public:
        explicit Node(const T& data) {
            data_ = data;
            prev_ = nullptr;
            next_ = nullptr;
        }

        Node(const T& data, Node* next) {
            data_ = data;
            prev_ = nullptr;
            next_ = next;
        }

        Node(const T& data, Node* prev, Node* next) {
            data_ = data;
            prev_ = prev;
            next_ = next;
        }

        T& data() {
            return data_;
        }

        const T& data() const {
            return data_;
        }

        Node* prev() {
            return prev_;
        }

        const Node* prev() const {
            return prev_;
        }

        void prev(Node* node) {
            prev_ = node;
        }

        Node* next() {
            return next_;
        }

        const Node* next() const {
            return next_;
        }

        void next(Node* node) {
            next_ = node;
        }

     private:
        T data_;
        Node* prev_;
        Node* next_;
    };

    Node* head;
    Node* sentinel;
    std::size_t size_;
};

}  // namespace structures

namespace structures {
    template<typename T>
    structures::DoublyCircularList<T>::DoublyCircularList() {
        sentinel = new Node(1, sentinel, sentinel);
        head = nullptr;
        size_ = 0;
    }

    template<typename T>
    structures::DoublyCircularList<T>::~DoublyCircularList() {
        clear();
        delete sentinel;
    }

    template<typename T>
    void structures::DoublyCircularList<T>::clear() {
        while (!empty())
            pop_back();
    }

    template<typename T>
    void structures::DoublyCircularList<T>::push_back(const T &data) {
       if (empty()) {
            Node *newNode = new Node(data, sentinel, sentinel);
            sentinel->next(newNode);
            sentinel->prev(newNode);
            size_++;
        } else {
            Node *newNode = new Node(data, sentinel->prev(), sentinel);
            sentinel->prev()->next(newNode);
            sentinel->prev(newNode);
            size_++;
        }
    }

    template<typename T>
    void structures::DoublyCircularList<T>::push_front(const T &data) {
        if (empty()) {
            Node *newNode = new Node(data, sentinel, sentinel);
            sentinel->next(newNode);
            sentinel->prev(newNode);
            size_++;
        } else {
            Node *newNode = new Node(data, sentinel, sentinel->next());
            sentinel->next()->prev(newNode);
            sentinel->next(newNode);
            size_++;
        }
    }

    template<typename T>
    void structures::DoublyCircularList<T>::insert(const T &data,
    std::size_t index) {
        if (index < 0 || index > size())
            throw std::out_of_range("Índice inválido");
        if (index == 0) {
            push_front(data);
        } else if (index == size()) {
            push_back(data);
        } else {
            Node *aux = sentinel->next();
            for (int i = 0; i < static_cast<int>(index); i++) {
                aux = aux->next();
            }
            Node *newNode = new Node(data, aux->prev(), aux);
            aux->prev()->next(newNode);
            aux->prev(newNode);
            size_++;
        }
    }

    template<typename T>
    void structures::DoublyCircularList<T>::insert_sorted(const T& data) {
        auto count = 0u;
        for (auto i = 0u; i < size(); i++) {
            if (at(i) >= data)
                break;
            count++;
        }
        insert(data, count);
    }

    template<typename T>
    T structures::DoublyCircularList<T>::pop(std::size_t index) {
        if (empty())
            throw std::out_of_range("Lista vázia!");
        if (index >= size())
            throw std::out_of_range("Índice inválido!");

        if (index == 0)
            return pop_front();

        Node *aux = sentinel->next();
        for (int i = 0; i < static_cast<int>(index); i++)
            aux = aux->next();
        T value = aux->data();

        aux->prev()->next(aux->next());
        aux->next()->prev(aux->prev());

        aux->data().~T();
        size_--;

        delete aux;
        return value;
    }

    template <typename T>
    T structures::DoublyCircularList<T>::pop_back() {
        return pop(size() - 1);
    }

    template<typename T>
    T structures::DoublyCircularList<T>::pop_front() {
        if (empty())
            throw std::out_of_range("Lista vázia");

        Node *aux = sentinel->next();
        T value = aux->data();

        sentinel->next(aux->next());
        aux->prev()->next(aux->next());
        aux->next()->prev(aux->prev());

        aux->data().~T();
        size_--;

        delete aux;
        return value;
    }

    template<typename T>
    void structures::DoublyCircularList<T>::remove(const T &data) {
        auto i = find(data);
        pop(i);
    }

    template<typename T>
    bool structures::DoublyCircularList<T>::empty() const {
        return size_ == 0;
    }

    template<typename T>
    bool structures::DoublyCircularList<T>::contains(const T &data) const {
        return find(data) != size();
    }

    template<typename T>
    T& structures::DoublyCircularList<T>::at(std::size_t index) {
        if (index < 0 || index >= size())
            throw std::out_of_range("Índice inválido!");
        Node *aux = sentinel->next();
        for (int i = 0; i < static_cast<int>(index); i++)
            aux = aux->next();
        return aux->data();
    }

    template<typename T>
    const T& structures::DoublyCircularList<T>::at(std::size_t index) const {
        if (index < 0 || index >= size())
            throw std::out_of_range("Índice inválido!");
        Node *aux = sentinel->next();
        for (int i = 0; i < index; i++)
            aux = aux->next();
        return aux->data();
    }

    template<typename T>
    std::size_t structures::DoublyCircularList<T>::find(const T &data) const {
        Node *aux = sentinel->next();
        for (auto i = 0u; i < size(); i++) {
            if (aux->data() == data)
                return i;
            aux = aux->next();
        }
        return size();
    }

    template<typename T>
    std::size_t structures::DoublyCircularList<T>::size() const {
        return size_;
    }
}  // namespace structures
