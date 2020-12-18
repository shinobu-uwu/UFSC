library IEEE;

use IEEE.std_logic_1164.all;
use IEEE.std_logic_arith.all;
use IEEE.std_logic_unsigned.all;


entity DATAPATH is
  port (SW: in std_logic_vector(9 downto 0);
        CLK_1HZ, CLK_500HZ, R1, R2, R3, R4, E1, E2, E3, E4, E5: in std_logic;
        sw_erro, end_game, end_time, end_round: out std_logic;
        LEDR: out std_logic_vector(9 downto 0);
        HEX0, HEX1, HEX2, HEX3, HEX4, HEX5: out std_logic_vector(6 downto 0)
        );
end DATAPATH;

architecture DATAPATH_arch of DATAPATH is
  signal SCOUNTER_TIME, SREG0, SMUXCOUNTER_TIME, SCOUNTER_ROUND, SSOMA0, SSOMA1: std_logic_vector(3 downto 0);
  signal SROM, SREG1, SCOMP: std_logic_vector(9 downto 0);
  signal SMUX2, SREG2, SCORE, ENTRADA_MUX2: std_logic_vector(7 downto 0);
  signal SEND_GAME: std_logic;
-----------------------------------------------------------
  component COMP is
    port (A, B: in std_logic_vector(9 downto 0);
          S: out std_logic_vector(9 downto 0)
          );
  end component;

  component COMP4 is
    port (A: in std_logic_vector (3 downto 0);
          S: out std_logic
          );
  end component;

  component COUNTER_ROUND is
    port (R, E, CLK: in std_logic;
          end_round: out std_logic := '0';
          S: out std_logic_vector(3 downto 0)
          );
  end component;

  component COUNTER_TIME is
    port (R, E, CLK: in std_logic;
          end_time: out std_logic;
          S: out std_logic_vector(3 downto 0)
          );
  end component;

  component DEC7SEG is
    port (A: in std_logic_vector(3 downto 0);
          S: out std_logic_vector(6 downto 0)
          );
  end component;

  component MUX10BITS is
    port (A, B: in std_logic_vector(9 downto 0);
          SEL: in std_logic;
          S: out std_logic_vector(9 downto 0)
          );
  end component;

  component MUX4BITS is
    port (A, B: in std_logic_vector(3 downto 0);
          SEL: in std_logic;
          S: out std_logic_vector(3 downto 0)
          );
  end component;

  component MUX8BITS is
    port (A, B: in std_logic_vector(7 downto 0);
         SEL: in std_logic;
         S: out std_logic_vector(7 downto 0)
         );
  end component;

  component REG10BITS is
    port (CLK, E, R: in std_logic;
          D: in std_logic_vector(9 downto 0);
          Q: out std_logic_vector(9 downto 0)
          );
  end component;

  component REG4BITS is
    port (CLK, E, R: in std_logic;
          D: in std_logic_vector(3 downto 0);
          Q: out std_logic_vector(3 downto 0)
          );
  end component;

  component REG8BITS is
    port (CLK, E, R: in std_logic;
          D: in std_logic_vector(7 downto 0);
          Q: out std_logic_vector(7 downto 0)
          );
  end component;

  component ROM is
    port (address : in std_logic_vector(3 downto 0);
          data : out std_logic_vector(9 downto 0)
          );
  end component;

  component SOMA10BITS is
    port (A: in std_logic_vector(9 downto 0);
          S: out std_logic_vector(3 downto 0)
          );
  end component;
-------------------------------------------------------------------
begin
  -- constantes, t e r dos displays HEX5 e HEX3
  HEX5 <= "0000111";
  HEX3 <= "0101111";
  -- -- Display HEX4
  COUNTER0: COUNTER_TIME port map(R1, E1, CLK_1HZ, end_time, SCOUNTER_TIME);
  REG0: REG4BITS port map(CLK_500HZ, E2, '0', SW(9 downto 6), SREG0);
  MUX0: MUX4BITS port map(SCOUNTER_TIME, SREG0, E2, SMUXCOUNTER_TIME);
  DEC7SEG0: DEC7SEG port map(SMUXCOUNTER_TIME, HEX4);
  -- -- Display HEX2
  COUNTER1: COUNTER_ROUND port map(R3, E4, CLK_500HZ, end_round, SCOUNTER_ROUND);
  DEC7SEG1: DEC7SEG port map(SCOUNTER_ROUND, HEX2);
  -- -- Pega o valor da ROM
  ROM0: ROM port map(SREG0, SROM);
  -- -- LED_OUT
  MUX1: MUX10BITS port map("0000000000", SROM, E5, LEDR(9 downto 0));
  -- -- Input do jogador no SW(9... 0)
  REG1: REG10BITS port map(CLK_500HZ, E1, R2, SW(9 downto 0), SREG1);
  -- -- Checa se o usuário inseriu 4 '1' lógicos
  SOMA0: SOMA10BITS port map(SREG1, SSOMA0);
  COMP40: COMP4 port map(SSOMA0, sw_erro);
  -- Compara com a ROM
  COMP0: comp port map(SREG1, SROM, SCOMP);
  SOMA1: SOMA10BITS port map(SCOMP, SSOMA1);
  -- Checa se o jogador acertou
  COMP41: COMP4 port map(SSOMA1, SEND_GAME);
  end_game <= not SEND_GAME;
  -- Score do jogador
  SCORE <= "000" & (not SEND_GAME) & ("1010" - SCOUNTER_ROUND);
  ENTRADA_MUX2 <= "0000" & SSOMA1;
  MUX2: MUX8BITS port map(ENTRADA_MUX2, SCORE, E5, SMUX2);
  REG2: REG8BITS port map(CLK_500HZ, R2, E3, SMUX2, SREG2);
  -- Display HEX0 e HEX1
  DEC7SEG2: DEC7SEG port map(SREG2(3 downto 0), HEX0);
  DEC7SEG3: DEC7SEG port map(SREG2(7 downto 4), HEX1);
end datapath_arch;
