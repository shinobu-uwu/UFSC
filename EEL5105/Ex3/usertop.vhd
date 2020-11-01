library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.std_logic_arith.all; 
use IEEE.std_logic_unsigned.all;

entity usertop is
    port(SW: in std_logic_vector(17 downto 0);
         LEDR: out std_logic_vector(17 downto 0);
         HEX0: out std_logic_vector(6 downto 0);
         HEX1: out std_logic_vector(6 downto 0);
         HEX2: out std_logic_vector(6 downto 0);
         HEX3: out std_logic_vector(6 downto 0);
         CLK_1HZ: in std_logic
        );
end usertop;

architecture arch_usertop of usertop is
    component relogio is
        port(CLK: in std_logic;
        EN: in std_logic;
        --CLR: in std_logic;
        S0: out std_logic_vector(6 downto 0);
        S1: out std_logic_vector(6 downto 0);
        S2: out std_logic_vector(6 downto 0);
        S3: out std_logic_vector(6 downto 0)
       );
    end component;
begin
    S: relogio port map(CLK_1HZ, SW(0), HEX0, HEX1, HEX2, HEX3);
end arch_usertop;