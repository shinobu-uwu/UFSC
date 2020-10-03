library IEEE;
use std_logic_1164.all;

entity c2to7seg is
    port (C2: in std_logic_vector(3 downto 0);
          F: in std_logic;
          S: in std_logic_vector(6 downto 0)
         );
end c2to7seg;

architecture arch_c2to7seg of c2to7seg is
    signal S0, S1: std_logic_vector(3 downto 0)
    component mux2x1 is
        port(A, B: in std_logic_vector(3 downto 0);
             C: in std_logic;
             S: out std_logic_vector(3 downto 0)
            );
    end component;

    component compl2 is
        port(X: in std_logic_vector(3 downto 0);
             Y: out std_logic_vector(3 downto 0)
            );
    end component;

    component decodificador is
        port(A: in std_logic_vector(3 downto 0);
             S: out std_logic_vector(6 downto 0)
            );
    end component;

begin
    F <= C2(3);
    Compl2: compl2(C2, S0);
    MUX: mux2x1(C2, S0, C2(3), S1);
    Decod: decodificador(S1, S);
end arch_c2to7seg;
    