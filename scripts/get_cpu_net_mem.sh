#!/bin/bash
Time=1
#CPU0
CPULOG_1=`cat /proc/stat | head -n1 | awk '{print $2" "$3" "$4" "$5" "$6" "$7" "$8}'`
SYS_IDLE_1=`echo $CPULOG_1 | awk '{print $4}'`
Total_1=`echo $CPULOG_1 | awk '{print $1+$2+$3+$4+$5+$6+$7}'`

#NET0
TE1=`date --utc`
RX1=`cat /proc/net/dev | grep eth0 |awk '{print $2}'`
TX1=`cat /proc/net/dev | grep eth0 |awk '{print $10}'`

sleep $Time

#CPU1
CPULOG_2=`cat /proc/stat | head -n1 | awk '{print $2" "$3" "$4" "$5" "$6" "$7" "$8}'`
SYS_IDLE_2=`echo $CPULOG_2 | awk '{print $4}'`
Total_2=`echo $CPULOG_2 | awk '{print $1+$2+$3+$4+$5+$6+$7}'`
Total=`expr $Total_2 - $Total_1`
SYS_IDLE=`expr $SYS_IDLE_2 - $SYS_IDLE_1`
SYS_USAGE=`echo $SYS_IDLE/$Total*100 |bc -l`
SYS_Rate=`echo 100-$SYS_USAGE |bc -l`
Disp_SYS_Rate=`expr "scale=2; $SYS_Rate/1" |bc`

printf "%4.2f\n" ${Disp_SYS_Rate}

#NET1
DATE2=`date --utc`
RX2=`cat /proc/net/dev | grep eth0 |awk '{print $2}'`
TX2=`cat /proc/net/dev | grep eth0 |awk '{print $10}'`
RX=$(( $RX2-$RX1 ))
TX=$(( $TX2-$TX1 ))
RXBAND=$(($RX*8/$Time))
TXBAND=$(($TX*8/$Time)) 
printf  "%.0f\n" ${TXBAND}
printf  "%.0f\n" ${RXBAND}

#MEM
LoadMemory=$(cat /proc/meminfo | awk '{print $2}')
Total=$(echo $LoadMemory | awk '{print $1}')
Free1=$(echo $LoadMemory | awk '{print $2}')
Free2=$(echo $LoadMemory | awk '{print $3}')
Free3=$(echo $LoadMemory | awk '{print $4}')
 
Used=`expr $Total - $Free1 - $Free2 - $Free3`
Used_Rate=`expr  $Used/$Total*100 | bc -l`
Memory_Used_Rate=`expr  $Used_Rate/1 | bc`
echo $Memory_Used_Rate%
