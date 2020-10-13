library IEEE;
use IEEE.Std_Logic_1164.all;
use IEEE.std_logic_arith.all; 
use IEEE.std_logic_unsigned.all;

entity usertop is
    port (SW: in std_logic_vector(17 downto 0);
          LEDR: out std_logic_vector(17 downto 0);
          HEX0: out std_logic_vector(6 downto 0);
          HEX1: out std_logic_vector(6 downto 0);
          HEX2: out std_logic_vector(6 downto 0)
          );
end usertop;

architecture arch_usertop of usertop is
    signal D, E, F: std_logic_vector(7 downto 0);
    signal G: std_logic_vector(11 downto 0);
    component soma8 is
        port(A:  in std_logic_vector(7 downto 0);
             B:  in std_logic_vector(7 downto 0);
             S:  out std_logic_vector(7 downto 0)
            );
    end component;

    component binbcd is
        port(bin_in: in std_logic_vector(7 downto 0);
             bcd_out: out std_logic_vector(11 downto 0)
            );
    end component;

    component bcd7seg is
        port(bcd_in:  in std_logic_vector(3 downto 0);
             out_7seg:  out std_logic_vector(6 downto 0)
            );
    end component;

    component mux2x1 is
        port(A, B: in std_logic_vector(7 downto 0);
             C: in std_logic;
             S: out std_logic_vector(7 downto 0)
            );
    end component;

    begin
        S1: soma8 port map(SW(7 downto 0), SW(7 downto 0), D);
        S2: soma8 port map(D, "00100000", E);
        A1: mux2x1 port map(E, SW(7 downto 0), SW(17), F);
        S3: binbcd port map(F, G);
        S4: bcd7seg port map(G(3 downto 0), HEX0);
        S5: bcd7seg port map(G(7 downto 4), HEX1);
        S6: bcd7seg port map(G(11 downto 8), HEX2);
    end arch_usertop;