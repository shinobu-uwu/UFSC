namespace structures {
    // Coordenada i, j de uma matriz
    class Coordenada {
     public:
        //! Construtor sem argumentos, padrão (0, 0)
        Coordenada();
        //! Construtor com as coordenada (i, j)
        Coordenada(int i, int j);
        //! Destrutor
        ~Coordenada();
        //! Coordenada i
        int i();
        //! Coordenada j
        int j();
     private:
        int i_;
        int j_;
    };
}  // namespace structures