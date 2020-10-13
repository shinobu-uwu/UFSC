library IEEE;
use IEEE.Std_Logic_1164.all;

entity mux2x1 is
    port (A, B: in std_logic_vector(7 downto 0);
          C: in std_logic;
          S: out std_logic_vector(7 downto 0)
         );
end mux2x1;

architecture arch_mux2x1 of mux2x1 is
begin
    S <= A when C = '0' else
         B when C = '1';
end arch_mux2x1;
