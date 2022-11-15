## Task 5 - Compressor Airfoil CFD 

This is a simple CFD simulation of a compressor airfoil. Readers will find the series of commands required to access the jp1 super cluster. 

## Getting Started

### MacOs Users

1. Download and install [XQuartz](https://www.xquartz.org/)

2. Make sure you are connected to the Texas A&M VPN

3. From the terminal, run the following command:

``` bash
ssh -X lastname@jp1.engr.tamu.edu
```
Where `lastname` is the last name of one of our team members.

4. Once logged in, you may change the password by running:

``` bash
passwd
```

5. From here log out and change directory to where you have the `i.n0006` file. Once you have located it, run the following command:

``` bash
scp i.n0006 lastname@jp1.engr.tamu.edu: 
```

6. Once the file has been copied, log back into jp1 and run the following command:

``` bash
fin i.n0006 output.whateveryouwanttocallit
```

7. From here you will see a list of options to choose from as far as figures go. You can choose to view the figures in the terminal.

### Windows Users

1. Download and install [MobaXterm](https://mobaxterm.mobatek.net/)

2. Make sure you are connected to the Texas A&M VPN

3. From the terminal, run the following command:

``` bash
ssh -X lastename@jp1.engr.tamu.edu
```
Where `lastname` is the last name of one of our team members.

4. Once logged in, you may change the password by running:

``` bash
passwd
```

5. From here log out and change directory to where you have the `i.n0006` file. Once you have located it, run the following command:

``` bash
scp i.n0006 lastname@jp1.engr.tamu.edu: 
```

6. Once the file has been copied, log back into jp1 via MobaXterm and run the following command:

``` bash
fin i.n0006 output.whateveryouwanttocallit
```

7. From here you will see a list of options to choose from as far as figures go. You can choose to view the figures in the terminal.

