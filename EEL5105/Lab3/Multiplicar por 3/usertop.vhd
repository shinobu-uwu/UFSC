library ieee;
use ieee.std_logic_1164.all;

entity usertop is
port(
	SW: in std_logic_vector(17 downto 0);
	LEDR: out std_logic_vector(17 downto 0)
	);
end usertop;

architecture soma of usertop is

    component somador is
    port    (A: in std_logic_vector(3 downto 0);
             S: out std_logic_vector(7 downto 0));
    end component;
    
begin
    SO: somador port map(SW(3 downto 0), LEDR(4 downto 0));
end soma;
