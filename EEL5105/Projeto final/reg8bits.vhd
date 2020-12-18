library IEEE;
use IEEE.std_logic_1164.all;


entity REG8BITS is
  port (CLK, E, R: in std_logic;
        D: in std_logic_vector(7 downto 0);
        Q: out std_logic_vector(7 downto 0)
        );
end REG8BITS;

architecture REG8BITS_arch of REG8BITS is
begin
  process(CLK, R)
  begin
    if R = '1' then
      Q <= "00000000";
    elsif (CLK'event and CLK = '1' and E = '1') then
      Q <= D;
    end if;
  end process;
end REG8BITS_arch;
