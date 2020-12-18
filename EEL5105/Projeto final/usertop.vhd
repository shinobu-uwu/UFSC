library IEEE;
use IEEE.std_logic_1164.all;


entity usertop is
  port(SW: in std_logic_vector(17 downto 0);
       CLK_1HZ: in std_logic;
       CLK_500HZ: in std_logic;
       KEY: in std_logic_vector(3 downto 0);
       LEDR: out std_logic_vector(17 downto 0);
       HEX0, HEX1, HEX2, HEX3, HEX4, HEX5: out std_logic_vector(6 downto 0)
       );
end usertop;

architecture usertop_arch of usertop is
  signal enter, reset,
    R1, R2, R3, R4, E1, E2, E3, E4, E5,
    sw_erro, end_game, end_time, end_round: std_logic := '0';
  component DATAPATH is
    port (SW: in std_logic_vector(9 downto 0);
          CLK_1HZ, CLK_500HZ, R1, R2, R3, R4, E1, E2, E3, E4, E5: in std_logic;
          sw_erro, end_game, end_time, end_round: out std_logic;
          LEDR: out std_logic_vector(9 downto 0);
          HEX0, HEX1, HEX2, HEX3, HEX4, HEX5: out std_logic_vector(6 downto 0)
          );
  end component;

  component CONTROLE is
    port (clk, enter, reset, sw_erro, end_game, end_time, end_round: in std_logic;
          R1, R2, R3, R4, E1, E2, E3, E4, E5: out std_logic
          );
  end component;

  component BUTTONSYNC is
    port (KEY0, KEY1, CLK: in std_logic;
          BTN0, BTN1: out std_logic
          );
  end component;

begin
  BUTTON0: BUTTONSYNC port map(KEY(0), KEY(1), CLK_500HZ, reset, enter);
  CONTROLE0: CONTROLE port map(CLK_500HZ, enter, reset, sw_erro, end_game, end_time, end_round,
                                R1, R2, R3, R4, E1, E2, E3, E4, E5);
    DATAPATH0: DATAPATH port map(SW(9 downto 0), CLK_1HZ, CLK_500HZ, R1, R2, R3, R4, E1, E2, E3, E4, E5,
                                 sw_erro, end_game, end_time, end_round,
                                 LEDR(9 downto 0), HEX0, HEX1, HEX2, HEX3, HEX4, HEX5);
end usertop_arch;
