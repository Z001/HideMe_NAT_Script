#############################################
#        HideMe NAT script | by Z001        #
#############################################

import mechanize
from mechanize import ParseResponse, urlopen
from mechanize import Browser

br = Browser()

br.open('http://10.117.0.1/')
br.form = list(br.forms())[0]
control = br.form.find_control("c")

br["c"] = str(raw_input("Input your access code: "))
br.submit()

response = br.open('http://10.117.0.1/?division=dnat')
iplist = []
protlist = []

br.form = list(br.forms())[0]
#for form in br.forms(): #form debug if something goes wrong
#    print "Form name:", form.name
#    print form
ipselector = br.form.find_control("dst_ip")
protsel = br.form.find_control("prot")

if ipselector.type == "select":  
	for item in ipselector.items:
		iplist.append(item.name)
print '\n'.join(iplist)
ipsel = int(raw_input("Select desired IP (0-n): "))

if protsel.type == "select":  
	for item in protsel.items:
		protlist.append(item.name)
print '\n'.join(protlist)
protsel = int(raw_input("Select protocol (0-n): "))
print "Enter desired port range. (1000-65535)"

dsr_from = int(raw_input("FROM: ")) - 1
dsr_to = int(raw_input("TO: "))
counterx = dsr_to - dsr_from
countery = 0

while countery < counterx:
	br.form = list(br.forms())[0]
	ip = br.form.find_control("dst_ip")
	dst_port = br.form.find_control("dst_port")
	to_port = br.form.find_control("to_port")
	port = br.form.find_control("prot")
	port.value = [protlist[protsel]]
	ip.value = [iplist[ipsel]]
	dsr_from += 1
	dst_port.value = str(dsr_from)
	to_port.value = str(dsr_from)
	response = br.submit()
	print dst_port.value + " OPEN"
	countery += 1 
	br.open('http://10.117.0.1/?division=dnat')

print str(protlist[protsel]) + " port range " + str(dsr_from - countery + 1) + " " + "to " + str(dsr_to) + " " + "is open."