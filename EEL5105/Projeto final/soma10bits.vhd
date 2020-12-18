library IEEE;

use IEEE.std_logic_1164.all;
use IEEE.std_logic_arith.all;
use iEEE.std_logic_unsigned.all;


entity SOMA10BITS is
  port (A: in std_logic_vector(9 downto 0);
        S: out std_logic_vector(3 downto 0)
        );
end SOMA10BITS;

architecture SOMA10BITS_arch of SOMA10BITS is
  signal cnt: std_logic_vector (3 downto 0) := "0000";
begin
  process(A)
  begin
    for i in 0 to 9 loop
      if(A(i) = '1') then
        cnt <= cnt + 1;
      end if;
    end loop;
  end process;
  S <= cnt;
end SOMA10BITS_arch;
