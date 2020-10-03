library IEEE;
use IEEE.std_logic_1164.all;

entity usertop is
port (SW: in std_logic_vector(17 downto 0);
      LEDR: out std_logic_vector(17 downto 0);
      HEX0: out std_logic_vector(6 downto 0);
      HEX1: out std_logic_vector(6 downto 0)
      );
end usertop;
      
architecture decod of usertop is
    component decodificador is
        port (A: in std_logic_vector(3 downto 0);
              S: out std_logic_vector(6 downto 0));
    end component;
begin
    S: decodificador port map(SW(3 downto 0), HEX0);
end decod; 
