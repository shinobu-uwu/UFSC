#include <cstdint>

namespace structures {
    template<typename T>
    class LinkedQueue {
        public:
            LinkedQueue();      // Construtor

            ~LinkedQueue();     // Destrutor

            void clear();       // Limpa a fila

            void enqueue(const T& data);  // Adiciona no final da fila

            T dequeue();      // Retira do ínicio da fila

            T& front() const;  // Primeiro dado na fila

            T& back() const;  // Último dado na fila

            bool empty() const;  // Verifica se a fila está vazia

            std::size_t size();  // Tamanho da fila

        private:
            class Node {
                public:
                    explicit Node(const T& data) {
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

            Node *head;
            Node *tail;
            std::size_t size_;
    };
}  // namespace structures
