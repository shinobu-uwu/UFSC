library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.std_logic_arith.all;
use IEEE.std_logic_unsigned.all;


entity counter_time is
  port(R, E, CLK: in std_logic;
       end_time: out std_logic;
       S: out std_logic_vector(3 downto 0)
       );
end counter_time;

architecture counter_time_arch of counter_time is
  signal cnt: std_logic_vector(3 downto 0) := "0000";
begin
  process(CLK, R)
  begin
    if (R = '1') then
      cnt <= "0000";
      end_time <= '0';
    end if;
    if(E = '1') then
      if (CLK'event and CLK = '1') then
        cnt <= cnt + 1;
      elsif (cnt = "0101") then
        cnt <= "0000";
        end_time <= '1';
      end if;
    end if;
    S <= cnt;
  end process;
end counter_time_arch;
