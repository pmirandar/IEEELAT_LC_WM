set style fill solid
set boxwidth 18
set style line 1 lc rgb "#5000629B"
set xlabel "Time (h)"
set ylabel "Consumption (l)"
set yr [0:10300]
set xr [0:1420]
set xtics 0, 200, 1200

set grid

set term png
v = "792"
set  arrow from v, graph 0 to v, graph 1 lw 1.5 lc "#002855" dt 2 nohead

set label "Starting app" at 420,7500 tc rgb "#002855"
set output "System-1-ac.png"
set yr [0:10100]
plot "System-1-Accumulated_Water_Consumption.data" using 1:2 notitle with boxes ls 1

set output "System-3-ac.png"
set yr [0:8000]
set label "Starting app" at 420,7500 tc rgb "#002855"
plot "System-3-Accumulated_Water_Consumption.data" using 1:2 notitle with boxes ls 1

set output "System-2-ac.png"
set yr [0:4900]
set label "Starting app" at 420,3200 tc rgb "#002855"
plot "System-2-Accumulated_Water_Consumption.data" using 1:2 notitle with boxes ls 1

