library IEEE;
use IEEE.std_logic_1164.all;


entity MUX4BITS is
  port (A, B: in std_logic_vector(3 downto 0);
        SEL: in std_logic;
        S: out std_logic_vector(3 downto 0)
        );
end MUX4BITS;

architecture MUX4BITS_arch of MUX4BITS is
begin
  S <= A when SEL = '0' else
       B;
end MUX4BITS_arch;
