import json

class AS_Connection:
    def __init__(self,
                 type: str, # 'Direct' / 'Indirect'
                 source: str,
                 target: list, # AS Set
                 weight: int
                ) -> None:
        self.type = type
        self.source = source
        self.target = target
        self.weight = weight
    def __dict__(self):
        return {
            'type': self.type,
            'source': self.source,
            'target': self.target,
            'weight': self.weight,
        }

ases_connections = []

as_data = open('cycle-asdata.txt', 'r', encoding='utf-8').readlines()
# print(as_data)

# D	10010	131915	0

connection_type = {
    'D': 'Direct',
    'I': 'Indirect',
}

for asn in as_data:
    if asn[0] in ('D', 'I'):
        asd = asn.split('\t')
        src = asd[1]
        tgt = asd[2]
        weight = int(asd[3])
        targets = tgt.split(',')
        target = []
        for i in targets:
            as_set = []
            for s in i.split('_'):
                as_set.append(s)
            target.append(as_set)
        ases_connections.append(AS_Connection(
            connection_type[asn[0]],
            src,
            target,
            weight,
        ).__dict__())

output_file = open('ASDATA.json', 'w', encoding='utf-8')

output_file.write(json.dumps(ases_connections))

output_file.close()
