transcript on
if {[file exists rtl_work]} {
	vdel -lib rtl_work -all
}
vlib rtl_work
vmap work rtl_work

vcom -93 -work work {/home/matheus/Documents/UFSC/EEL5105/EX1/ex1.vhd}

