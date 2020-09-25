library IEEE;
use IEEE.std_logic_1164.all;

entity halfadder is
port (A: in std_logic;
	  B: in std_logic;
	  S: out std_logic;
	  Cout: out std_logic);
end halfadder;

architecture arch_halfadder of halfadder is
begin
	S <= A xor B;
	Cout <= A and B;
end arch_halfadder;