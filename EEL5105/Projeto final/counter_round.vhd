library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.std_logic_arith.all;
use IEEE.std_logic_unsigned.all;


entity counter_round is
  port(R, E, CLK: in std_logic;
       S: out std_logic_vector(3 downto 0)
       );
end counter_round;

architecture counter_round_arch of counter_round is
  signal cnt: std_logic_vector(3 downto 0) := "0000";
begin
  process(CLK) -- Reset será síncrono, quando atingir 10 ou R = 1
  begin
    if(E = '1') then
      if (R = '1' or cnt = "1010") then
        cnt <= "0000";
      elsif (CLK'event and CLK = '1') then
        cnt <= cnt + '1';
      end if;
    end if;
    S <= cnt;
  end process;
end counter_round_arch;
