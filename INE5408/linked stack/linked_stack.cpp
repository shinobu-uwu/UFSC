#include "linked_stack.h"

namespace structures {

    template<typename T>
    structures::LinkedStack<T>::LinkedStack() {
        size_ = 0;
        top_ = nullptr;
    }
}
