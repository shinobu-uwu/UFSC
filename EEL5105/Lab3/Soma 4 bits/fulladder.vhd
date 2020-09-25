library IEEE;
use IEEE.std_logic_1164.all;

entity fulladder is
port (A: in std_logic;
	  B: in std_logic;
	  Cin: in std_logic;
	  S: out std_logic;
	  Cout: out std_logic);
end fulladder;

architecture arch_fulladder of fulladder is
begin
	S <= (not A and not B and Cin) or (A and not B and not Cin) or (A and B and Cin);
	
	Cout <= (B or Cin) and (A or Cin) and (A or B);
end arch_fulladder;