library IEEE;
use IEEE.std_logic_1164.all;


entity MUX10BITS is
  port (A, B: in std_logic_vector(9 downto 0);
        SEL: in std_logic;
        S: out std_logic_vector(9 downto 0)
        );
end MUX10BITS;

architecture MUX10BITS_arch of MUX10BITS is
begin
  S <= A when SEL = '0' else
       B;
end MUX10BITS_arch;
