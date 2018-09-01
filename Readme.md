### Fatek PLC Communication Protocol Using Python 3 ###
#### MF Alfafa ###
#### miftahf77@gmail.com ####
#### 1 September 2018 ####

> Introduction

This Python program is used to get data from Fatek PLC using Fatek standard protocol in Port 0. This program is using Fatek standard command to get response from Fatek PLC in order to receive data. And then the received data from Fatek PLC is displayed to HMI (Human Machine Interface) using Raspi 3, Intel NUC, etc. 

> Note 

Command format (from Python script)	: STX + SlaveStationNo + CommandNo + Data + LRCChecksum + ETX.
LRC_checksum_calculator Python file is used to calculate LRC (Longitudinal Redundancy Check) of the command.

> Refference

1. Ascii Code
https://www.rapidtables.com/convert/number/ascii-to-hex.html