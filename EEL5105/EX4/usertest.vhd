library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.std_logic_arith.all;
use IEEE.std_logic_unsigned.all;

entity usertest is
end usertest;

architecture tb of usertest is
  signal clk, enable, clkout1, clkout2: std_logic := '0';
  signal contador: std_logic_vector(3 downto 0):= "0000";
  component circuito is
    port(clkin: in std_logic;
         enable: in std_logic;
         clkout1, clkout2: out std_logic);
  end component;
begin
  DUT: circuito port map(clkin => clk,
                         enable => enable,
                         clkout1 => clkout1,
                         clkout2 => clkout2);
  clk <= not clk after 5 ns; --período de 10ns, cada subida de borda leva 10ns
  process
  begin
    --valores altos para conseguir visualizar bem o enable e clkout1
    enable <= '1';
    wait for 100 ns;
    enable <= '0';
    wait for 100 ns;
  end process;
end tb;
