library IEEE;
use IEEE.std_logic_1164.all;


entity MUX8BITS is
  port (A, B: in std_logic_vector(7 downto 0);
        SEL: in std_logic;
        S: out std_logic_vector(7 downto 0)
        );
end MUX8BITS;

architecture MUX8BITS_arch of MUX8BITS is
begin
  S <= A when SEL = '0' else
       B;
end MUX8BITS_arch;
