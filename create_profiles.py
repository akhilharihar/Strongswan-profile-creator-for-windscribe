import os
import argparse
import json
from uuid import uuid4


parser = argparse.ArgumentParser(description="strongswan profile creator for windscribe vpn", allow_abbrev=False)
parser.add_argument('-u', '--username', default=None, help="windscribe ikev2 username")

args = parser.parse_args()

servers = {
	"us_central": "us-central.windscribe.com",
	"us_east": "us-east.windscribe.com",
	"us_west": "us-west.windscribe.com",
	"windflix_us": "wf-us.windscribe.com",
	"canada_east": "ca.windscribe.com",
	"canada_west": "ca-west.windscribe.com",
	"windflix_ca": "wf-ca.windscribe.com",
	"austria": "at.windscribe.com",
	"belgium": "be.windscribe.com",
	"bulgaria": "bg.windscribe.com",
	"croatia": "hr.windscribe.com",
	"czech_republic": "cz.windscribe.com",
	"denmark": "dk.windscribe.com",
	"estonia": "ee.windscribe.com",
	"finland": "fi.windscribe.com",
	"france": "fr.windscribe.com",
	"germany": "de.windscribe.com",
	"greece": "gr.windscribe.com",
	"hungary": "hu.windscribe.com",
	"iceland": "is.windscribe.com",
	"ireland": "ie.windscribe.com",
	"israel": "il.windscribe.com",
	"italy": "it.windscribe.com",
	"latvia": "lv.windscribe.com",
	"lithuania": "lt.windscribe.com",
	"moldova": "md.windscribe.com",
	"netherlands": "nl.windscribe.com",
	"norway": "no.windscribe.com",
	"poland": "pl.windscribe.com",
	"portugal": "pt.windscribe.com",
	"romania": "ro.windscribe.com",
	"slovakia": "sk.windscribe.com",
	"spain": "es.windscribe.com",
	"sweden": "se.windscribe.com",
	"switzerland": "ch.windscribe.com",
	"tunisia": "tn.windscribe.com",
	"united_kingdom": "uk.windscribe.com",
	"windflix_uk": "wf-uk.windscribe.com",
	"albania": "al.windscribe.com",
	"azerbaijan": "az.windscribe.com",
	"bosnia": "ba.windscribe.com",
	"india": "in.windscribe.com",
	"russia": "ru.windscribe.com",
	"serbia": "rs.windscribe.com",
	"slovenia": "si.windscribe.com",
	"south_africa": "za.windscribe.com",
	"turkey": "tr.windscribe.com",
	"ukraine": "ua.windscribe.com",
	"australia": "au.windscribe.com",
	"new_zealand": "nz.windscribe.com",
	"hong_kong": "hk.windscribe.com",
	"indonesia": "id.windscribe.com",
	"japan": "jp.windscribe.com",
	"malaysia": "my.windscribe.com",
	"philippines": "ph.windscribe.com",
	"singapore": "sg.windscribe.com",
	"south_korea": "kr.windscribe.com",
	"taiwan": "tw.windscribe.com",
	"thailand": "th.windscribe.com",
	"vietnam": "vn.windscribe.com",
	"windflix_jp": "wf-jp.windscribe.com",
	"argentina": "ar.windscribe.com",
	"brazil": "br.windscribe.com",
	"colombia": "co.windscribe.com",
	"mexico": "mx.windscribe.com"
}

format = {
	"uuid": None,
	"name": None,
	"type": "ikev2-eap",
	"remote": {
		"addr": None
	},
	"local": {
		"eap_id": args.username
	},
	"split-tunneling": {
		"block-ipv4": True,
		"block-ipv6": True
	}
}

dir_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'profiles')

if not os.path.isdir(dir_path):
	try:
		os.mkdir(dir_path)
	except OSError as e:
		print(e)
		exit()

for index, value in servers.items():
	with open(os.path.join(dir_path, index + '.sswan'), "w+") as f:
		profile = format.copy()
		profile['uuid'] = str(uuid4())
		profile['name'] = ' '.join(list(map(lambda x: x[0].upper() + x[1:], index.split('_'))))
		profile['remote']['addr'] = value
		f.write(json.dumps(profile))
	print('created ', index, ' profile')
