library IEEE;
use IEEE.std_logic_1164.all;


entity usertop is
  port(SW: in std_logic_vector(17 downto 0);
       CLK_1HZ: in std_logic;
       LEDR: out std_logic_vector(17 downto 0)
       );
end usertop;

architecture usertop_arch of usertop is
  component counter_time is
    port (R, E, CLK: in std_logic;
          S: out std_logic_vector(3 downto 0)
          );
  end component;
begin
  O: counter_time port map(sw(0), sw(1), clk_1hz, LEDR(3 downto 0));
end usertop_arch;
