import curses
import curses.wrapper
import curses.ascii
import time


def init_colors():
  curses.start_color()
  curses.use_default_colors()
  
  curses.init_pair(1, curses.COLOR_WHITE, -1)
  curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE)
  curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_CYAN)
  curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_GREEN)

test = """[   28.689906] ADDRCONF(NETDEV_UP): eth0: link is not ready
[   28.695415] [drm] radeon defaulting to kernel modesetting.
[   28.695422] [drm] radeon kernel modesetting enabled.
[   28.695597] radeon 0000:01:00.0: power state changed by ACPI to D0
[   28.695645] radeon 0000:01:00.0: power state changed by ACPI to D0
[   28.695658] radeon 0000:01:00.0: PCI INT A -> Link[LNKA] -> GSI 11 (level, low) -> IRQ 11
[   28.728391] [drm] initializing kernel modesetting (RV100 0x1002:0x4C59).
[   28.731068] [drm] register mmio base: 0xC0100000
[   28.731073] [drm] register mmio size: 65536
[   28.731378] agpgart-intel 0000:00:00.0: AGP 2.0 bridge
[   28.731399] agpgart-intel 0000:00:00.0: putting AGP V2 device into 1x mode
[   28.731443] radeon 0000:01:00.0: putting AGP V2 device into 1x mode
[   28.731477] radeon 0000:01:00.0: GTT: 256M 0xD0000000 - 0xDFFFFFFF
[   28.731488] radeon 0000:01:00.0: VRAM: 64M 0xE0000000 - 0xE3FFFFFF (16M used)
[   28.787137] type=1400 audit(1295537995.655:9): apparmor="STATUS" operation="profile_load" name="/usr/bin/evince" pid=776 comm="apparmor_parser"
[   28.806305] type=1400 audit(1295537995.675:10): apparmor="STATUS" operation="profile_load" name="/usr/bin/evince-previewer" pid=776 comm="apparmor_parser"
[   28.819691] type=1400 audit(1295537995.687:11): apparmor="STATUS" operation="profile_load" name="/usr/bin/evince-thumbnailer" pid=776 comm="apparmor_parser"
[   28.824092] [drm] radeon: irq initialized.
[   28.824461] [drm] Detected VRAM RAM=64M, BAR=128M
[   28.824467] [drm] RAM width 32bits DDR
[   28.828414] [TTM] Zone  kernel: Available graphics memory: 253952 kiB.
[   28.828418] [TTM] Initializing pool allocator.
[   28.828450] [drm] radeon: 16M of VRAM memory ready
[   28.828454] [drm] radeon: 256M of GTT memory ready.
[   28.864202] [drm] Loading R100 Microcode
[   28.869299] [drm] radeon: ring at 0x00000000D0000000
[   28.869327] [drm] ring test succeeded in 1 usecs
[   28.869679] [drm] radeon: ib pool ready.
[   28.869816] [drm] ib test succeeded in 0 usecs
[   28.871360] [drm] Panel ID String: 1024x768                
[   28.871364] [drm] Panel Size 1024x768
[   28.879105] [drm] Radeon Display Connectors
[   28.879110] [drm] Connector 0:
[   28.879114] [drm]   VGA
[   28.879119] [drm]   DDC: 0x60 0x60 0x60 0x60 0x60 0x60 0x60 0x60
[   28.879121] [drm]   Encoders:
[   28.879124] [drm]     CRT1: INTERNAL_DAC1
[   28.879127] [drm] Connector 1:
[   28.879129] [drm]   LVDS
[   28.879131] [drm]   Encoders:
[   28.879133] [drm]     LCD1: INTERNAL_LVDS
[   28.883802] [drm] radeon: power management initialized
[   28.965654] [drm] fb mappable at 0xE0040000
[   28.965659] [drm] vram apper at 0xE0000000
[   28.965661] [drm] size 786432
[   28.965664] [drm] fb depth is 8
[   28.965666] [drm]    pitch is 1024
[   29.065615] Console: switching to colour frame buffer device 128x48
[   29.070358] fb0: radeondrmfb frame buffer device
[   29.070361] drm: registered panic notifier
[   29.073335] Slow work thread pool: Starting up
[   29.075649] Slow work thread pool: Ready
[   29.075666] [drm] Initialized radeon 2.5.0 20080528 for 0000:01:00.0 on minor 0
"""


test2 = """Jan 19 23:04:31 arwen wpa_supplicant[818]: Trying to associate with 00:14:6c:5a:7e:43 (SSID='vonthron' freq=2462 MHz)
Jan 19 23:04:31 arwen NetworkManager[788]: <info> (wlan0): supplicant connection state:  scanning -> associating
Jan 19 23:04:31 arwen kernel: [   43.569104] wlan0: authenticate with 00:14:6c:5a:7e:43 (try 1)
Jan 19 23:04:31 arwen kernel: [   43.586192] wlan0: authenticated
Jan 19 23:04:31 arwen kernel: [   43.586229] wlan0: associate with 00:14:6c:5a:7e:43 (try 1)
Jan 19 23:04:31 arwen wpa_supplicant[818]: Associated with 00:14:6c:5a:7e:43
Jan 19 23:04:31 arwen kernel: [   43.593915] wlan0: RX AssocResp from 00:14:6c:5a:7e:43 (capab=0x411 status=0 aid=4)
Jan 19 23:04:31 arwen kernel: [   43.593921] wlan0: associated
Jan 19 23:04:31 arwen kernel: [   43.594668] ADDRCONF(NETDEV_CHANGE): wlan0: link becomes ready
Jan 19 23:04:31 arwen NetworkManager[788]: <info> (wlan0): supplicant connection state:  associating -> associated
Jan 19 23:04:31 arwen NetworkManager[788]: <info> (wlan0): supplicant connection state:  associated -> 4-way handshake
Jan 19 23:04:31 arwen kernel: [   43.621571] padlock: VIA PadLock not detected.
Jan 19 23:04:31 arwen wpa_supplicant[818]: WPA: Key negotiation completed with 00:14:6c:5a:7e:43 [PTK=CCMP GTK=TKIP]
Jan 19 23:04:31 arwen wpa_supplicant[818]: CTRL-EVENT-CONNECTED - Connection to 00:14:6c:5a:7e:43 completed (auth) [id=0 id_str=]
Jan 19 23:04:31 arwen NetworkManager[788]: <info> (wlan0): supplicant connection state:  4-way handshake -> group handshake
Jan 19 23:04:31 arwen NetworkManager[788]: <info> (wlan0): supplicant connection state:  group handshake -> completed
Jan 19 23:04:31 arwen NetworkManager[788]: <info> Activation (wlan0/wireless) Stage 2 of 5 (Device Configure) successful.  Connected to wireless network 'vonthron'.
Jan 19 23:04:31 arwen NetworkManager[788]: <info> Activation (wlan0) Stage 3 of 5 (IP Configure Start) scheduled.
Jan 19 23:04:31 arwen NetworkManager[788]: <info> Activation (wlan0) Stage 3 of 5 (IP Configure Start) started...
Jan 19 23:04:31 arwen NetworkManager[788]: <info> (wlan0): device state change: 5 -> 7 (reason 0)
Jan 19 23:04:31 arwen NetworkManager[788]: <info> Activation (wlan0) Beginning DHCPv4 transaction (timeout in 45 seconds)
Jan 19 23:04:31 arwen NetworkManager[788]: <info> dhclient started with pid 1426
Jan 19 23:04:31 arwen NetworkManager[788]: <info> Activation (wlan0) Stage 3 of 5 (IP Configure Start) complete.
Jan 19 23:04:31 arwen dhclient: Internet Systems Consortium DHCP Client V3.1.3
Jan 19 23:04:31 arwen dhclient: Copyright 2004-2009 Internet Systems Consortium.
Jan 19 23:04:31 arwen dhclient: All rights reserved.
Jan 19 23:04:31 arwen dhclient: For info, please visit https://www.isc.org/software/dhcp/
Jan 19 23:04:31 arwen dhclient: 
Jan 19 23:04:31 arwen NetworkManager[788]: <info> (wlan0): DHCPv4 state changed nbi -> preinit
Jan 19 23:04:31 arwen dhclient: Listening on LPF/wlan0/00:21:27:c2:54:d9
Jan 19 23:04:31 arwen dhclient: Sending on   LPF/wlan0/00:21:27:c2:54:d9
Jan 19 23:04:31 arwen dhclient: Sending on   Socket/fallback
Jan 19 23:04:31 arwen dhclient: DHCPDISCOVER on wlan0 to 255.255.255.255 port 67 interval 3
Jan 19 23:04:33 arwen avahi-daemon[792]: Joining mDNS multicast group on interface wlan0.IPv6 with address fe80::221:27ff:fec2:54d9.
Jan 19 23:04:33 arwen avahi-daemon[792]: New relevant interface wlan0.IPv6 for mDNS.
Jan 19 23:04:33 arwen avahi-daemon[792]: Registering new address record for fe80::221:27ff:fec2:54d9 on wlan0.*.
Jan 19 23:04:33 arwen dhclient: DHCPOFFER of 192.168.1.106 from 192.168.1.254
Jan 19 23:04:33 arwen dhclient: DHCPREQUEST of 192.168.1.106 on wlan0 to 255.255.255.255 port 67
Jan 19 23:04:33 arwen dhclient: DHCPACK of 192.168.1.106 from 192.168.1.254
Jan 19 23:04:33 arwen NetworkManager[788]: <info> (wlan0): DHCPv4 state changed preinit -> bound
Jan 19 23:04:33 arwen NetworkManager[788]: <info> Activation (wlan0) Stage 4 of 5 (IP4 Configure Get) scheduled...
Jan 19 23:04:33 arwen NetworkManager[788]: <info> Activation (wlan0) Stage 4 of 5 (IP4 Configure Get) started...
Jan 19 23:04:33 arwen NetworkManager[788]: <info>   address 192.168.1.106
Jan 19 23:04:33 arwen NetworkManager[788]: <info>   prefix 24 (255.255.255.0)
Jan 19 23:04:33 arwen NetworkManager[788]: <info>   gateway 192.168.1.254
Jan 19 23:04:33 arwen NetworkManager[788]: <info>   nameserver '192.168.1.254'
Jan 19 23:04:33 arwen NetworkManager[788]: <info>   domain name 'lan'
Jan 19 23:04:33 arwen NetworkManager[788]: <info> Activation (wlan0) Stage 5 of 5 (IP Configure Commit) scheduled...
Jan 19 23:04:33 arwen NetworkManager[788]: <info> Activation (wlan0) Stage 4 of 5 (IP4 Configure Get) complete.
Jan 19 23:04:33 arwen NetworkManager[788]: <info> Activation (wlan0) Stage 5 of 5 (IP Configure Commit) started...
Jan 19 23:04:33 arwen avahi-daemon[792]: Joining mDNS multicast group on interface wlan0.IPv4 with address 192.168.1.106.
Jan 19 23:04:33 arwen avahi-daemon[792]: New relevant interface wlan0.IPv4 for mDNS.
Jan 19 23:04:33 arwen avahi-daemon[792]: Registering new address record for 192.168.1.106 on wlan0.IPv4.
Jan 19 23:04:33 arwen dhclient: bound to 192.168.1.106 -- renewal in 32685 seconds.
Jan 19 23:04:34 arwen NetworkManager[788]: <info> (wlan0): device state change: 7 -> 8 (reason 0)
Jan 19 23:04:34 arwen NetworkManager[788]: <info> Policy set 'Auto vonthron' (wlan0) as default for IPv4 routing and DNS.
Jan 19 23:04:34 arwen NetworkManager[788]: <info> Updating /etc/hosts with new system hostname
Jan 19 23:04:34 arwen NetworkManager[788]: <info> Activation (wlan0) successful, device activated.
Jan 19 23:04:34 arwen NetworkManager[788]: <info> Activation (wlan0) Stage 5 of 5 (IP Configure Commit) complete.
Jan 19 23:04:34 arwen nm-dispatcher.action: nm_dispatcher_action: Invalid connection: '(null)' / 'connection setting not found' invalid: 1
Jan 19 23:04:34 arwen nm-dispatcher.action: Script '/etc/NetworkManager/dispatcher.d/01ifupdown' exited with error status 1.
Jan 19 23:04:34 arwen ntpdate[1479]: step time server 91.189.94.4 offset -0.937153 sec
Jan 19 23:04:41 arwen kernel: [   54.208030] wlan0: no IPv6 routers present
Jan 19 23:05:17 arwen anacron[1556]: Anacron 2.3 started on 2011-01-19
Jan 19 23:05:17 arwen anacron[1556]: Normal exit (0 jobs run)
Jan 19 23:05:17 arwen kernel: [   90.940159] EXT4-fs (sda1): re-mounted. Opts: errors=remount-ro,commit=0
"""

def main(stdscr):
  init_colors()
  
  lines = 2*curses.LINES
  cols  = 5*curses.COLS
  
  pad = curses.newpad(lines, cols)
  pad.addstr(3, 3, "this is a string: pad border [%d, %d] screen: [%d, %d]" % (lines, cols, curses.LINES, curses.COLS))
  pad.addstr(0, 0, test)
  
  i=0
  for line in test2.split('\n'):
    pad.addstr(i, curses.COLS, line)
    i += 1
    
#~ 
  #~ pad.refresh( 0,0, 0,0, curses.LINES-1,curses.COLS-1 )
  #~ 
  #~ time.sleep(3)
  #~ 
  #~ for i in range(20):
    #~ pad.refresh( i,0, 0,0, curses.LINES-1,curses.COLS-1 )
    #~ time.sleep(0.1)
  #~ 
  pad.refresh( 0,0, 0,0, curses.LINES-1,curses.COLS-1 )
  time.sleep(2)
  pad.refresh( 0,curses.COLS, 0,0, curses.LINES-1,curses.COLS-1 )
  time.sleep(2)
  pad.refresh( 0,0, 0,0, curses.LINES-1,curses.COLS-1 )
  
  time.sleep(5)




if __name__ == '__main__':
  curses.wrapper(main)
