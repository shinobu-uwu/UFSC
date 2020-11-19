library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.std_logic_arith.all;
use IEEE.std_logic_unsigned.all;

entity circuito is
  port(clkin: in std_logic;
       enable: in std_logic;
       clkout1, clkout2: out std_logic);
end circuito;

architecture arch_circuito of circuito is
    signal contador1: std_logic_vector(3 downto 0) := "0000";
    signal contador2: std_logic_vector(1 downto 0) := "00";
begin
    --quando o contador é igual a 10 o primeiro clock de saída recebe 1
    --quando o contador é igual a 2 o segundo clock de saída recebe 1
    clkout1 <= '1' when contador1 = "1010" else '0';
    clkout2 <= '1' when contador2 = "10" else '0';
    process(clkin)
    begin
    if(enable = '0') then --o contador só contará se o enable for 0, se for 1
                          --as saídas ficam com nível lógico baixo
        if(clkin'event and clkin = '1') then
            contador1 <= contador1 + 1;
            contador2 <= contador2 + 1;
        end if;
        if(contador1 = "1010") then
            contador1 <= "0000";
        end if;
        if (contador2 = "10") then
            contador2 <= "00";
        end if;
    end if;
    end process;
end arch_circuito;
