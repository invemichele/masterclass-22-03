#!/bin/bash

# phi3-phi2-phi1 state
# 000  1
# 001  2
# 010  3
# 011  4
# 100  5
# 101  6
# 110  7
# 111  8

#bck="bck.0."
bck=""
bck.meup.sh -i states.data
awk 'BEGIN{phi1=0;phi2=0;phi3=0;state=1;counter=0;print "#time state counter"}
     NR>20{
       if(phi1==1){if($2>-2.2 && $2<-1.8) phi1=0;}
       else {if($2>0.8 && $2<1.2) phi1=1;}

       if(phi2==1){if($3>-2.2 && $3<-1.8) phi2=0;}
       else {if($3>0.8 && $3<1.2) phi2=1;}

       if(phi3==1){if($4>-2.2 && $4<-1.8) phi3=0;}
       else {if($4>0.8 && $4<1.2) phi3=1;}

       state=phi1+2*phi2+4*phi3+1;
       if(count[state]==0){count[state]++;counter++;}
       print $1,state,counter;}' ${bck}COLVAR > states.data
