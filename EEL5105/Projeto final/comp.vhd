library IEEE;

use IEEE.std_logic_1164.all;
use IEEE.std_logic_arith.all;
use IEEE.std_logic_unsigned.all;


entity COMP is
  port (A, B: in std_logic_vector(9 downto 0);
        S: out std_logic_vector(9 downto 0)
        );
end COMP;

architecture COMP_arch of COMP is
  signal POSICOESCERTAS: std_logic_vector(9 downto 0) := "0000000000";
begin
  process(A)
  begin
    for i in 0 to 9 loop
      if((A(i) = B(i)) and (A(i) = '1')) then
        POSICOESCERTAS(i) <= '1';
      end if;
    end loop;
  end process;
    S <= POSICOESCERTAS;
end COMP_arch;
