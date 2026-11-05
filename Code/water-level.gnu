set style fill solid
#set boxwidth 18
set style line 1 lc rgb "#00629B"
#set title "Casa 1"
set xlabel "Time (h)"
set ylabel "Height (m)"
set xr [0:1380]
set yr [0:1.5]
set grid

set term png

set output "System-1.png"
plot "System-1-Water_Level_per_hour.data" using 1:2 notitle with lines ls 1
set output "System-2.png"
plot "System-2-Water_Level_per_hour.data" using 1:2 notitle with lines ls 1
set output "System-3.png"
plot "System-3-Water_Level_per_hour.data" using 1:2 notitle with lines ls 1

