#include "avl_tree.h"
#include <iostream>

template<typename T>
structures::AVLTree<T>::AVLTree() {
    root = nullptr;
    size_ = 0;
}

template<typename T>
structures::AVLTree<T>::~AVLTree<T>() {
    while (!empty())
        remove(root);
}

template<typename T>
void structures::AVLTree<T>::insert(const T& data) {
    insertRecursive(data, root, nullptr);
    size_++;
}

template<typename T>
void structures::AVLTree<T>::remove(const T &data) {
    removeRecursive(data, root);
    size_--;
}

template<typename T>
bool structures::AVLTree<T>::contains(const T& data) const {
    Node *aux = root;
    while (aux != nullptr && aux->data != data)
        if (aux->data < data)
            aux = aux->right;
        else
            aux = aux->left;

    return aux != nullptr;
}

template<typename T>
bool structures::AVLTree<T>::empty() const {
    return size_ == 0;
}

template<typename T>
std::size_t structures::AVLTree<T>::size() const {
    return size_;
}

template<typename T>
structures::ArrayList<T> structures::AVLTree<T>::pre_order() {
    auto list = new ArrayList<T>();
    preOrderRecursive(root, list);
    return *list;
}

template<typename T>
structures::ArrayList<T> structures::AVLTree<T>::in_order() {
    structures::ArrayList<T> list;
    inOrderRecursive(root, &list);
    return list;
}

template<typename T>
structures::ArrayList<T> structures::AVLTree<T>::post_order() {
    auto list = new ArrayList<T>();
    postOrderRecursive(root, list);
    return *list;
}

int main() {
    auto a = new structures::AVLTree<int>();
    a->insert(3);
    printf("%i\n",a->in_order().size());
}
