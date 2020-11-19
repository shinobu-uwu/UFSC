library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.std_logic_arith.all; 
use IEEE.std_logic_unsigned.all;

entity contador_ate_5 is
    port(CLK: in std_logic;
         EN: in std_logic;
         --CLR: in std_logic;
         S: out std_logic_vector(6 downto 0);
         MAX: out std_logic
        );
end contador_ate_5;

architecture behv of contador_ate_5 is
    signal cnt: std_logic_vector(3 downto 0) := "0000";
    signal A: std_logic_vector (6 downto 0);
    signal CLR, M: std_logic := '0';

    component bcd7seg is
      port(bcd_in:  in std_logic_vector(3 downto 0);
          out_7seg:  out std_logic_vector(6 downto 0)
          );
    end component;

  begin
    process(CLK)
    begin
      if (CLR = '1') then
        if(EN = '1') then
        cnt <= "0000";
        CLR <= '0';
        M <= '0';
        end if;
      elsif (CLK'event and CLK = '1') then 
      if(EN = '1') then
        if(cnt = "1001") then
            CLR <= '1';
            M <= '1';
        else
            cnt <= cnt + "0001";
        end if;
      end if;
      end if;
    end process;
    P: bcd7seg port map(cnt, A);
    S <= A;
    MAX <= M;
  end behv;