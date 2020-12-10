library IEEE;
use IEEE.std_logic_1164.all;


entity REG10BITS is
  port (CLK, E, R: in std_logic;
        D: in std_logic_vector(9 downto 0);
        Q: out std_logic_vector(9 downto 0)
        );
end REG10BITS;

architecture REG10BITS_arch of REG10BITS is
begin
  process(CLK, R)
  begin
    if R = '1' then
      Q <= "0000000000";
    elsif (CLK'event and CLK = '1' and E = '1') then
      Q <= D;
    end if;
  end process;
end REG10BITS_arch;
