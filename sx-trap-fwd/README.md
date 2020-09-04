# sx-trap-fwd
This script enables forwarding of Control Plane protocols instead of trapping them to CPU
on Spectrum-series switches.

# Requirements
Mellanox Spectrum Switches running NOS with SDK API access:
- Onyx
- Cumulus
- SONiC

## Install
Copy this `sx_trap_fwd.py` to Mellanox switch in an environment with SDK API access.

For example, a [docker container with SDK libs](https://community.mellanox.com/s/article/getting-started-with-docker-container-over-mlnx-os-sdk-interfaces) in Onyx.

# Usage
This script changes default CPU TRAP configuration in the ASIC to allow forwarding of
the following Control Plane protocols:
- STP/RPVST
- LACP
- EAPOL
- LLDP
- MMRP/MVRP
- IGMP
- DHCP
- UDLD
- ARP

## Docker build
You can also create a docker image with this script inside to be launched on container start.

To create a docker image run: `./build.sh <VERSION>`

Example:
```
$ git clone https://github.com/kvadrage/sx-sdk-examples/
$ cd sx-sdk-examples/sx-trap-fwd
$ ./build.sh 0.1
Sending build context to Docker daemon  56.32kB
Step 1/6 : FROM ubuntu:bionic
 ---> 72300a873c2c
Step 2/6 : RUN apt update && apt --no-install-recommends -y install python
 ---> Running in 30a514d9d07a
<...>
Successfully built dc4f5dd2ea05
Successfully tagged sx-trap-fwd:0.1
$ ls sx_trap_fwd_0.1.tar.gz 
sx_trap_fwd_0.1.tar.gz
```

## Running Docker container in Onyx
Example how to run a docker image with this script inside Mellanox Onyx:

```
sw1 [standalone: master] (config) # image fetch scp://user@x.x.x.x/home/user/sx_trap_fwd_0.1.tar.gz
Password (if required): *******
 100.0%  [#################################################################]  
sw1 [standalone: master] (config) # docker 
sw1 [standalone: master] (config docker) # no shutdown
sw1 [standalone: master] (config docker) # load sx_trap_fwd_0.1.tar.gz 
cc4590d6a718: Loading layer  65.58MB/65.58MB
8c98131d2d1d: Loading layer  991.2kB/991.2kB
03c9b9f537a4: Loading layer  15.87kB/15.87kB
1852b2300972: Loading layer  3.072kB/3.072kB
772ff43086fb: Loading layer  59.08MB/59.08MB
19be54c09e5f: Loading layer  14.85kB/14.85kB
acfe33f3edee: Loading layer  3.584kB/3.584kB
Loaded image: sx-trap-fwd:0.1

# run temporary container and copy SX SDK API libraries into it
sw1 [standalone: master] (config docker) # start sx-trap-fwd 0.1 sx-trap-fwd-temp now privileged sdk
Attempting to start docker container. Please wait (this can take a minute)...
sw1 [standalone: master] (config docker) # copy-sdk sx-trap-fwd-temp to /
Copying SDK files to docker container. Please wait (this can take a minute)...

# commit these changes and create final image with SX SDK libraries inside
sw1 [standalone: master] (config docker) # commit sx-trap-fwd-temp sx-trap-fwd-sdk 0.1
committing docker container. Please wait (this can take a minute)...

# run new container from the final image and enable autostart for it
sw1 [standalone: master] (config docker) # start sx-trap-fwd-sdk 0.1 sx-trap-fwd now-and-init privileged sdk
Attempting to start docker container. Please wait (this can take a minute)...

# remove the temporary container from configuration
sw1 [standalone: master] (config docker) # no start sx-trap-fwd-temp 
Stopping docker container. Please wait (this can take a minute)...
sw1 [standalone: master] (config docker) # exit
sw1 [standalone: master] (config) # wr mem
sw1 [standalone: master] (config) # 


# Verifying that container with sx-trap-fwd script correctly starts after switch boot
sw1 [standalone: master] (config) # reload
## Reconnect to switch after it's booted
sw1 [standalone: master] > en
sw1 [standalone: master] # conf t
sw1 [standalone: master] (config) # show docker ps
-------------------------------------------------------------------------------------------
Container           Image:Version           Created                Status                  
-------------------------------------------------------------------------------------------
sx-trap-fwd        sx-trap-fwd-sdk:0.1    8 minutes ago          Exited (0) 2 minutes ago
sw1 [standalone: master] (config) # 
```