def modifyip(ipfile):
    try:
        lines=open(ipfile,'r').readlines()
        for i in range(len(lines)):
            if 'NETMASK' in lines[i]:
                lines[i] ="NETMASK='255.255.254.0'\n"
            print lines[i]
        open(ipfile,'w').writelines(lines)
         
    except Exception,e:
        print e
         
modifyip('/etc/sysconfig/network-scripts/ifcfg-eth0')
