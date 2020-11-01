library IEEE;
use IEEE.std_logic_1164.all;

entity ff_d is
    port(D: in std_logic;
         CLK: in std_logic;
         Q: out std_logic
        );
end ff_d;

architecture ff_d_arch of ff_d is
begin
    process(CLK)
    begin
        if(CLK'event and CLK = '1') then
            Q <= D;
        end if;
    end process;
end ff_d_arch;