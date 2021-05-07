#include "array_list.h"
#include <cstdint>
#include <limits.h>

namespace structures {

template <typename T> class BinaryTree {
  public:
    //! Inicializa árvore vazia
    BinaryTree();
    //! Destrutor da árvor
    ~BinaryTree();
    //! Insere um elemento na árvore, respeitando a ordem
    void insert(const T &data);
    //! Remove um elemento da árvore
    void remove(const T &data);
    //! Verifica se a árvore contém o elemento
    bool contains(const T &data) const;
    //! Verifica se a árvore está vazia
    bool empty() const;
    //! Tamanho da árvore
    std::size_t size() const;
    //! Notação pre order
    ArrayList<T> pre_order();
    //! Notação in order
    ArrayList<T> in_order();
    //! Notação post order
    ArrayList<T> post_order();

  private:
    struct Node {
        Node(const T &data_) {
            data = data_;
            left = nullptr;
            right = nullptr;
        }

        ~Node() {
            delete left;
            delete right;
        }

        T data;
        Node *left;
        Node *right;
    };

    // T find_min(Node *subTree) {
    //     // Retornar um número muito grande quando chegarmos no fim, assim não
    //     // altera o resultado
    //     if (subTree == nullptr) {
    //         T big;
    //         return big;
    //     }

    //     T min = subTree->data;
    //     T leftMin = find_min(subTree->left);
    //     T rightMin = find_min(subTree->right);

    //     if (leftMin < min)
    //         min = leftMin;
    //     if (rightMin < min)
    //         min = rightMin;
    //     return min;
    // }

        void append_subtree(Node *subtree, ArrayList<T> *list) {
            if (subtree == nullptr)
                return;

            list->push_back(subtree->data);
            append_subtree(subtree->left, list);
            append_subtree(subtree->right, list);
        }

    std::size_t size_;
    Node *root;
};

} // namespace structures
