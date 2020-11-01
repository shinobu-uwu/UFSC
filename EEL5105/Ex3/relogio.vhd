library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.std_logic_arith.all; 
use IEEE.std_logic_unsigned.all;

entity relogio is
    port(CLK: in std_logic;
         EN: in std_logic;
         --CLR: in std_logic;
         S0: out std_logic_vector(6 downto 0);
         S1: out std_logic_vector(6 downto 0);
         S2: out std_logic_vector(6 downto 0);
         S3: out std_logic_vector(6 downto 0)
        );
end relogio;

architecture behav of relogio is
    signal M0, M1, M2, M3, MAX0, MAX1, MAX2: std_logic;
    component contador_ate_9 is
        port(CLK: in std_logic;
             EN: in std_logic;
             --CLR: in std_logic;
             S: out std_logic_vector(6 downto 0);
             MAX: out std_logic
            );
    end component;

    component contador_ate_5 is
        port(CLK: in std_logic;
         EN: in std_logic;
         --CLR: in std_logic;
         S: out std_logic_vector(6 downto 0);
         MAX: out std_logic
        );
    end component;
begin
    F: contador_ate_9 port map(CLK, EN, S0, M0);
    MAX0 <= M0;
    G: contador_ate_5 port map(CLK, MAX0, S1, M1);
    MAX1 <= MAX0 AND M1;
    H: contador_ate_9 port map(CLK, MAX1, S2, M2);
    MAX2 <= M0 AND M1 AND M2;
    I: contador_ate_5 port map(CLK, MAX2, S3, M3);
end architecture;