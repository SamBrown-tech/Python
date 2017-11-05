import xmltodict

with open('stations.xml') as xml:
    xmldct = xmltodict.parse(xml.read())


def code_type(xmldict):
    print('Dit zijn de codes en types van de 4 stations:')
    for d in xmldict['Stations']['Station']:
        print('{:4} - {}'.format(d['Code'], d['Type']))
    print()

def code_synoniemen(xmldict):
    print('Dit zijn alle stations met één of meer synoniemen:')
    for d in xmldict['Stations']['Station']:
        if d['Synoniemen'] is not None:
            print('{:4} - {}'.format(d['Code'], d['Synoniemen']['Synoniem']))
    print()


def code_langenaam(xmldict):
    print('Dit is de lange naam van elk station:')
    for d in xmldict['Stations']['Station']:
        print('{:4} - {}'.format(d['Code'] ,d['Namen']['Lang']))
    print()


code_type(xmldct)
code_synoniemen(xmldct)
code_langenaam(xmldct)

