#include <cstdint>

namespace structures {
    template<typename T>
    class LinkedStack {
        public:
            LinkedStack();

            ~LinkedStack();

            void clear(); // limpa pilha

            void push(const T& data); // empilha

            T pop(); // desempilha

            T& top() const; // dado no topo

            bool empty() const; // pilha vazia

            std::size_t size() const; // tamanho da pilha

        private:
            class Node {
                public:
                    Node(const T& data){
                        data_ = data;
                    }

                    Node(const T& data, Node* next) {
                        data_ = data;
                        next_ = next;
                    }

                    T& data() {  // getter: info
                        return data_;  
                    } 

                    const T& data() const { // getter-constante: info
                        return data_;
                    }
                    Node* next() { // getter: próximo
                        return next_;
                    }
                    const Node* next() const{ // getter-constante: próximo
                        return next_;
                    }

                    void next(Node* next){ // setter: próximo
                        next_ = next;
                    }
                private:
                    T data_;
                    Node* next_;
            };

            Node* top_; // nodo-topo
            std::size_t size_; // tamanho
    };
}  // namespace structures
