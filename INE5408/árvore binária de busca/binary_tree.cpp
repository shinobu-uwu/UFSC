#include "binary_tree.h"
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <type_traits>
#include <typeinfo>
#include <vector>
#include <string>

template<typename T>
structures::BinaryTree<T>::BinaryTree() {
    root = nullptr;
    size_ = 0;
}

template<typename T>
structures::BinaryTree<T>::~BinaryTree() {
    while (!empty())
        remove(root->data);
}

template<typename T>
void structures::BinaryTree<T>::insert(const T &data) {
    Node *newNode = new Node(data);
    if (empty()) {
        root = newNode;
    } else {
        Node *aux = root;
        while (aux != nullptr) {
            if (data < aux->data) {
                if (aux->left == nullptr) {
                    aux->left = newNode;
                    break;
                } else {
                    aux = aux->left;
                }
            } else {
                if (aux->right == nullptr) {
                    aux->right = newNode;
                    break;
                }
                else {
                    aux = aux->right;
                }
            }
        }        
    }
    size_++;
}

template<typename T>
void structures::BinaryTree<T>::remove(const T &data) {
    if (empty())
        throw std::out_of_range("Árvore vazia");

    Node *aux = root;
    Node *anterior = root;
    // Encontrar o elemento que queremos deletar e o nodo anterior a ele
    while (aux->data != data) {
        if ((aux->left != nullptr && aux->left->data == data)
            || (aux->right != nullptr && aux->right->data == data))
            anterior = aux;
        if (aux->data > data)
            aux = aux->left;
        else
            aux = aux->right;
    }
    
    if (aux->right != nullptr && aux->left != nullptr) {
        Node *min = aux->right;
        // O menor da sub-árvore será o mais a esquerda
        while (min->left != nullptr)
            min = min->left;
        T value = min->data;
        remove(min->data);
        aux->data = value;
    } else {  // 1 filho
        if (aux->right != nullptr) {
            if (aux->data > anterior->data)
                anterior->right = aux->left;
            else
                anterior->left = aux->right;
        } else {
            if (aux->left != nullptr) {
                if (aux->data > anterior->data)
                    anterior->right = aux->left;
                else
                    anterior->left = aux->left;
                aux->data.~T();
                delete aux;
            } else {  // Nodo folha
                if (aux->data > anterior->data)
                    anterior->right = nullptr;
                else
                    anterior->left = nullptr;
                aux->data.~T();
                delete aux;
            }
        }
    }
    size_--;
}

template<typename T>
bool structures::BinaryTree<T>::contains(const T &data) const {
    Node *aux = root;
    while (aux != nullptr && aux->data != data)
        if (aux->data < data)
            aux = aux->right;
        else
            aux = aux->left;

    return aux != nullptr;
}

template<typename T>
bool structures::BinaryTree<T>::empty() const {
    return size_ == 0;
}

template<typename T>
std::size_t structures::BinaryTree<T>::size() const {
    return size_;
}

template<typename T>
structures::ArrayList<T> structures::BinaryTree<T>::pre_order() {
    ArrayList<T> *list = new ArrayList<T>(size() + 1);
    // raíz
    list->push_front(root->data);
    // sub-árvore da esquerda
    append_subtree(root->left, list);
    // sub-árvore da direita
    append_subtree(root->right, list);
    return *list;
}

template<typename T>
structures::ArrayList<T> structures::BinaryTree<T>::in_order() {
    ArrayList<T> *list = new ArrayList<T>(size() + 1);
    // sub-árvore da direita
    append_subtree(root->right, list);
    // sub-árvore da esquerda
    append_subtree(root->left, list);
    int meio = size_ % 2 == 0 ? size_ / 2 - 1: size_ / 2 + 1;
    list->insert(root->data, meio);
    return *list;
}

template<typename T>
structures::ArrayList<T> structures::BinaryTree<T>::post_order() {
    ArrayList<T> *list = new ArrayList<T>(size() + 1);
    // sub-árvore da esquerda
    append_subtree(root->left, list);
    // sub-árvore da direita
    append_subtree(root->right, list);
    // raíz
    list->push_back(root->data);
    return *list;
}

class Dummy {
public:
    Dummy() = default;
    explicit Dummy(double value):
        value_{value}
    {}

    /**
     * Valor encapsulado
     */
    double value() const {
        return value_;
    }

    bool operator<(const Dummy& other) const {
        return value() < other.value();
    }

    bool operator<=(const Dummy& other) const {
        return value() <= other.value();
    }

    bool operator>(const Dummy& other) const {
        return value() > other.value();
    }

    bool operator>=(const Dummy& other) const {
        return value() >= other.value();
    }

    bool operator==(const Dummy& other) const {
        return value() == other.value();
    }

    bool operator!=(const Dummy& other) const {
        return value() != other.value();
    }

private:
    /**
     * Valor encapsulado
     */
    double value_{0.};
};

int main() {
    structures::BinaryTree<Dummy> list{};
    const auto values = std::vector<Dummy>{
    Dummy{0.},
    Dummy{-5.},
    Dummy{10.},
    Dummy{7.5},
    Dummy{-5.5},
    Dummy{3.1415},
    Dummy{4.2},
    Dummy{-10.},
};
    for (auto& value : values) {
        list.insert(value);
    }
    auto output = list.pre_order();

        list.remove(Dummy{7.5});
}