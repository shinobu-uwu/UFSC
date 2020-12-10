library IEEE;
use IEEE.std_logic_1164.all;


entity REG4BITS is
  port (CLK, E, R: in std_logic;
        D: in std_logic_vector(3 downto 0);
        Q: out std_logic_vector(3 downto 0)
        );
end REG4BITS;

architecture REG4BITS_arch of REG4BITS is
begin
  process(CLK)
  begin
    if R = '1' then
      Q <= "0000";
    elsif (CLK'event and CLK = '1' and E = '1') then
      Q <= D;
    end if;
  end process;
end REG4BITS_arch;
