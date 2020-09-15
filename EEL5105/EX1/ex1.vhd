library IEEE;
use IEEE.std_logic_1164.all;

entity ex1 is
port (A1: in std_logic;
		A0: in std_logic;
		B1: in std_logic;
		B0: in std_logic;
		R3: out std_logic;
		R2: out std_logic;
		R1: out std_logic;
		R0: out std_logic);
end ex1;
		
architecture arch_ex1 of ex1 is
begin
	R0 <= A0 and B0;
	R1 <= (not A1 and not A0) or (not A0 and B0) or (not A1 and B1) or (A0 and not B0) or (A1 and not B1);
	R2 <= (A1 and B1 and not B0) or (A1 and not A0 and B1);
	R3 <= (not A1 and not A0) or (not B1 and not B0) or (A1 and A0 and B1 and B0);
end arch_ex1;