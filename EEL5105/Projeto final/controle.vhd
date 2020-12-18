library IEEE;
use IEEE.std_logic_1164.all;

entity controle is
  port (clk, enter, reset, sw_erro, end_game, end_time, end_round: in std_logic;
        R1, R2, R3, R4, E1, E2, E3, E4, E5: out std_logic
        );
end controle;

architecture controle_arch of controle is
  -- para evitar conflitos com palavras reservadas da linguagem todos os
  -- estados começam com E
  type STATES is (EInit, ESetup, EPlay, EResult, ECountRound, EWait, ECheck);
  signal EAtual: STATES := EInit;
  signal PEstado: STATES;

begin
  process(clk, reset)
  begin
    if (reset = '1') then
      EAtual <= EInit;
    elsif (clk'event and clk = '1') then
      EAtual <= PEstado;
    end if;
  end process;

  process (EAtual, enter, sw_erro, end_game, end_time, end_round)
  begin
    case EAtual is
      when EInit =>
        E1 <= '0';
        E2 <= '0';
        E3 <= '0';
        E4 <= '0';
        E5 <= '0';
        R1 <= '1';
        R2 <= '1';
        R3 <= '1';
        R4 <= '1';
        if (enter = '1') then
          PEstado <= ESetup;
        else
          PEstado <= EInit;
        end if;
      when ESetup =>
        E5 <= '0';
        E2 <= '1';
        R1 <= '0';
        R2 <= '0';
        R3 <= '0';
        R4 <= '0';
        if (enter = '1') then
          PEstado <= EPlay;
        else
          PEstado <= ESetup;
        end if;
      when EPLay =>
        E2 <= '0';
        E1 <= '1';
        E3 <= '1';
        R1 <= '0';
        if (end_time = '1') then
          PEstado <= EResult;
        elsif (enter = '1') then
          PEstado <= ECountRound;
        else
          PEstado <= EPlay;
        end if;
      when ECountRound =>
        E1 <= '0';
        E4 <= '1';
        PEstado <= ECheck;
      when ECheck =>
        E4 <= '0';
        E3 <= '0';
        R2 <= '1';
        if(end_time = '1' or end_game = '1' or end_round = '1' or sw_erro = '1') then
          PEstado <= EResult;
        else
          PEstado <= EWait;
        end if;
      when EWait =>
        E3 <= '0';
        R1 <= '1';
        R2 <= '0';
        if(enter = '1') then
          PEstado <= EPlay;
        else
          PEstado <= EWait;
        end if;
      when EResult =>
        E5 <= '1';
        R1 <= '1';
        E1 <= '0';
        if (enter = '1') then
          PEstado <= EInit;
        else
          PEstado <= EResult;
        end if;
    end case;
  end process;
end controle_arch;
