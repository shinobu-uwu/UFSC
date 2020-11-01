library IEEE;
use IEEE.std_logic_1164.all;

entity usertop is
    port(SW: in std_logic_vector(17 downto 0);
         LEDR: out std_logic_vector(17 downto 0)
        );
end usertop;

architecture arch_usertop of usertop is
    component registrador is
        port(EN: in std_logic;
             CLK: in std_logic;
             Q: out std_logic_vector(3 downto 0);
             SS: out std_logic
            );
    end component;
begin
    A: registrador port map(SW(0), SW(1), LEDR(3 downto 0), LEDR(4));
end arch_usertop;