/// Copyright [2021] Matheus Filipe dos Santos Reinert
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
    static const auto DEFAULT_MAX = 10u;

    T* contents;
    std::size_t size_;
    std::size_t max_size_;
};
}  // namespace structures

#endif

namespace structures {
    template<typename T>
    structures::ArrayList<T>::ArrayList() {
        size_ = 0;
        max_size_ = DEFAULT_MAX;
        contents = new T[max_size_];
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

#include <iostream>

namespace structures {
template<typename T>
class AVLTree {
public:
    AVLTree();

    ~AVLTree();

    void insert(const T& data);

    void remove(const T& data);

    bool contains(const T& data) const;

    bool empty() const;

    std::size_t size() const;

    int height() const;

    void print();

    ArrayList<T> pre_order();

    ArrayList<T> in_order();

    ArrayList<T> post_order();

private:
    struct Node {
        Node(const T& data_) {
            data = data_;
            left = nullptr;
            right = nullptr;
            height_ = 0;
        }
        T data;
        Node *left;
        Node *right;
        int height_;
    };

    int heightRecursive(Node* node) {
        if (node == nullptr)
            return -1;
        return node->height_;
    }

    Node *simpleLeft(Node *k2) {
        Node *k1;
        k1 = k2->left;
        k2->left = k1->right;
        k1->right = k2;

        k2->height_ = std::max(heightRecursive(k2->left), heightRecursive(k2->right)) + 1;
        k1->height_ = std::max(heightRecursive(k1->left), k2->height_) + 1;

        return k1;
    }

    Node *simpleRight(Node *k2) {
        Node *k1;
        k1 = k2->right;
        k2->right = k1->left;
        k1->left = k2;

        k2->height_ = std::max(heightRecursive(k2->right), heightRecursive(k2->left)) + 1;
        k1->height_ = std::max(heightRecursive(k1->right), k2->height_) + 1;

        return k1;
    }

    Node *doubleLeft(Node *k3) {
        k3->left = simpleRight(k3->left);

        return simpleLeft(k3);
    }

    Node *doubleRight(Node *k3) {
        k3->right = simpleLeft(k3->right);

        return simpleRight(k3);
    }

    Node *insertRecursive(const T& data, Node *node, Node *parent) {
        Node *rotated_tree;
        if (node == nullptr) {
            node = new Node(data);
        } else {
            if (data < node->data) {
                node->left = insertRecursive(data, node->left, node);
                if ((heightRecursive(node->left) - heightRecursive(node->right)) > 1) {
                    if (data < node->left->data)
                        rotated_tree = simpleLeft(node);
                    else
                        rotated_tree = doubleLeft(node);
                    if (parent->left == node)
                        parent->left = rotated_tree;
                    else
                        parent->right = rotated_tree;
                }
                node->height_ = std::max(heightRecursive(node->left), heightRecursive(node->right)) + 1;
            } else {
                if (data > node->data) {
                    node->right = insertRecursive(data, node->right, node);
                    if ((heightRecursive(node->right) - heightRecursive(node->left)) > 1) {
                        if (data < node->right->data)
                            rotated_tree = simpleRight(node);
                        else
                            rotated_tree = doubleRight(node);
                        if (parent->right == node)
                            parent->right =rotated_tree;
                        else
                            parent->left = rotated_tree;
                    }
                } else {
                    throw std::out_of_range("Element already in this tree");
                }
            }
        }
        return node;
    }

    Node *removeRecursive(T data, Node *node) {
        Node* tmp;
        Node* filho;

        if (node == nullptr) {
            return node;
        } else {
            if (data < node->data) {
                node->left = removeRecursive(data, node->right);
                update(node);
                return node;
            } else {
                if (data > node->data) {
                    node->right = removeRecursive(data, node->right);
                    update(node);
                    return node;
                } else {
                    if (node->right != nullptr && node->left != nullptr) {
                        tmp = min(node->right);
                        node->data = tmp->data;
                        node->right = removeRecursive(node->data, node->right);
                        update(node);
                        return node;
                    } else {
                        if (node->right == nullptr) {
                            filho = node->right;
                            return filho;
                        } else {
                            if (node->left != nullptr) {
                                filho = node->left;
                                return filho;
                            } else {
                                node->data.~T();
                                delete node;
                                return nullptr;
                            }
                        }
                    }
                }
            }
        }
    }

    Node *min(Node *node) {
        Node *aux = node;
        while (aux->left != nullptr)
            aux = aux->left;
        return aux;
    }

    void update(Node *node) {
        int balance = heightRecursive(node->left) - heightRecursive(node->right);
        if (balance > 1) {
            if (heightRecursive(node->left) > heightRecursive(node->right)) {
                simpleLeft(node);
            } else {
                doubleRight(node);
            }
        }
        else if (balance < -1) {
            if (heightRecursive(node->right) > heightRecursive(node->left)) {
                simpleRight(node);
            } else {
                doubleRight(node);
            }
        }
    }

    void preOrderRecursive(Node *node, ArrayList<T> *list) {
        if (node != nullptr) {
            list->push_back(node->data);
            preOrderRecursive(node->left, list);
            preOrderRecursive(node->right, list);
        }
    }

    void inOrderRecursive(Node *node, ArrayList<T> *list) {
        if (node == nullptr)
            return;
        inOrderRecursive(node->left, list);
        list->push_back(node->data);
        inOrderRecursive(node->right, list);
    }

    void postOrderRecursive(Node *node, ArrayList<T> *list) {
        if (node == nullptr)
            return;
        postOrderRecursive(node->left, list);
        postOrderRecursive(node->right, list);
        list->push_back(node->data);
    }

    Node *root;
    std::size_t size_;
};
}
