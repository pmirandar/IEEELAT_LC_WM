set style fill solid
set boxwidth 18
set style line 1 lc rgb "#7500629B"
#set title "Casa 1"
set xlabel "Time (h)"
set ylabel "Consumption (l)"
set xr [0:1440]
set yr [0:1100]
#set xtics rotate by 45 offset -0.8,-1.1
set xtics 0, 200, 1200
set grid
set label "Starting app" at 820,660 tc rgb "#002855"
#set label "Starting app" at 820,900 tc rgb "blue"


set term png
v = "792"
set  arrow from v, graph 0 to v, graph 1 lw 1.5 lc "#002855" dt 2 nohead

set output "System-1-dc.png"
plot "System-1-Daily-Water_Consumtion.data" using 1:2 notitle with boxes ls 1


set yr [0:750]
set output "System-2-dc.png"
plot "System-2-Daily-Water_Consumtion.data" using 1:2 notitle with boxes ls 1
set output "System-3-dc.png"
plot "System-3-Daily-Water_Consumtion.data" using 1:2 notitle with boxes ls 1
