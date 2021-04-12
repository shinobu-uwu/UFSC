#include "linked_queue.h"
#include <stdexcept>

#define TEMP template<typename T>

TEMP
structures::LinkedQueue<T>::LinkedQueue() {
    head = nullptr;
    tail = nullptr;
    size_ = 0;
}

TEMP
structures::LinkedQueue<T>::~LinkedQueue() {
    clear();
}

TEMP
void structures::LinkedQueue<T>::clear() {
    while(!empty())
        dequeue();
}

TEMP
void structures::LinkedQueue<T>::enqueue(const T &data) {
    Node *newNode = new Node(data);

    if (empty()) {
        head = newNode;
        tail = newNode;
    } else {
        tail->next(newNode);
        tail = newNode;
    }
    size_++;
}

TEMP
T structures::LinkedQueue<T>::dequeue() {
    if (empty())
        throw std::out_of_range("Empty queue");
    Node *aux = head;
    T value = aux->data();
    head = aux->next();
    aux->data().~T();
    delete aux;
    size_--;
    return value;
}

TEMP
T& structures::LinkedQueue<T>::front() const {
    if (empty())
        throw std::out_of_range("Empty queue");
    return head->data();
}

TEMP
T& structures::LinkedQueue<T>::back() const {
    if (empty())
        throw std::out_of_range("Empty queue");
    return tail->data();
}

TEMP
bool structures::LinkedQueue<T>::empty() const {
    return size_ == 0;
}

TEMP
std::size_t structures::LinkedQueue<T>::size() {
    return size_;
}
