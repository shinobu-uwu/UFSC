library IEEE;
use IEEE.std_logic_1164.all;

entity registrador is
    port(EN: in std_logic;
         CLK: in std_logic;
         Q: out std_logic_vector(3 downto 0);
         SS: out std_logic
        );
end registrador;

architecture registrador_arch of registrador is
    signal S0, S1, S2, S3: std_logic;
    component ff_d is
        port(D: in std_logic;
             CLK: in std_logic;
             Q: out std_logic
            );
    end component;
begin
    F: ff_d port map(EN, CLK, S0);
    Q(0) <= S0;
    G: ff_d port map(S0, CLK, S1);
    Q(1) <= S1;
    H: ff_d port map(S1, CLK, S2);
    Q(2) <= S2;
    I: ff_d port map(S2, CLK, S3);
    Q(3) <= S3;
    SS <= S3;
end registrador_arch;