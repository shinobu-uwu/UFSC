library IEEE;

use IEEE.std_logic_1164.all;


entity COMP4 is
  port (A: in std_logic_vector(3 downto 0);
        S: out std_logic
        );
end COMP4;

architecture COMP4_arch of COMP4 is
begin
  S <= '0' when A = "0100" else
       '1';
end COMP4_arch;
