import re

#data = 'NNCB'
data = 'PSVVKKCNBPNBBHNSFKBO'

#rules = [['CH','B'],['HH','N'],['CB','H'],['NH','C'],['HB','C'],['HC','B'],['HN','C'],['NN','C'],['BH','H'],['NC','B'],['NB','B'],['BN','B'],['BB','N'],['BC','B'],['CC','N'],['CN','C']]
rules = [['CF','H'],['PP','H'],['SP','V'],['NO','C'],['SF','F'],['FS','H'],['OF','P'],['PN','B'],['SH','V'],['BO','K'],['ON','V'],['VP','S'],['HN','B'],['PS','P'],['FV','H'],['NC','N'],['FN','S'],['PF','F'],['BF','F'],['NB','O'],['HS','C'],['SC','V'],['PC','K'],['KF','K'],['HC','C'],['OK','H'],['KS','P'],['VF','C'],['NV','S'],['KK','F'],['HV','H'],['SV','V'],['KC','N'],['HF','P'],['SN','F'],['VS','P'],['VN','F'],['VH','C'],['OB','K'],['VV','O'],['VC','O'],['KP','V'],['OP','C'],['HO','S'],['NP','K'],['HB','C'],['CS','S'],['OO','S'],['CV','K'],['BS','F'],['BH','P'],['HP','P'],['PK','B'],['BB','H'],['PV','N'],['VO','P'],['SS','B'],['CC','F'],['BC','V'],['FF','S'],['HK','V'],['OH','N'],['BV','C'],['CP','F'],['KN','K'],['NN','S'],['FB','F'],['PH','O'],['FH','N'],['FK','P'],['CK','V'],['CN','S'],['BP','K'],['CH','F'],['FP','K'],['HH','N'],['NF','C'],['VB','B'],['FO','N'],['PB','C'],['KH','K'],['PO','K'],['OV','F'],['NH','H'],['KV','B'],['OS','K'],['OC','K'],['FC','H'],['SO','H'],['KO','P'],['NS','F'],['CB','C'],['CO','F'],['KB','V'],['BK','K'],['NK','O'],['SK','C'],['SB','B'],['VK','O'],['BN','H']]

def generateRuleMap(rules):
	ruleMap = {}
	for pair in rules:
		ruleMap[pair[0]] = pair[1]

	return ruleMap

def getValidRules(ruleMap, data):
	validRules = []
	for rule in ruleMap.keys():
		if(re.search(rule, data)):
			validRules.append(rule)
	return validRules

# def performInsert(ruleMap,data):
# 	validRules = getValidRules(ruleMap, data)
# 	print("Identifying indices...")
# 	insertions = {}
# 	for rule in validRules:
# 		for i in range(len(data)):
# 			if(i < len(data) -1 and data[i] == rule[0] and data[i+1] == rule[1]):
# 				insertions[i+1] = ruleMap[rule]
# 	print("done")
# 	return insert(insertions, data)

def performInsert(ruleMap,data):
	validRules = getValidRules(ruleMap, data)
	insertions = {}
	for rule in validRules:
		for match in re.finditer(rule, data):
			print("found "+rule+" at "+str(match.start()+1)+", inserting "+ruleMap[rule])
			insertions[match.start()+1] = ruleMap[rule]
	return insert(insertions, data)



def sort(i, insertions):
	newDict = {}
	ls = insertions.keys()
	ls.sort(reverse=True)
	for n in ls:
		if(n >= i):
			newDict[n+1] = insertions[n]
		else:
			newDict[n] = insertions[n]
	# print(newDict)
	return newDict

def insert(insertions, data):
	#print("sorting...")
	ls = insertions.keys()
	ls.sort(reverse=True)
	# print(len(ls))
	# print(len(data))
	#print("inserting")
	for key in ls:
		data = data[:key] + insertions[key] + data[key:]
	#print("done")
	return data

ruleMap = generateRuleMap(rules)
assert len(rules) == len(ruleMap.keys())

for n in range(1):
	#print('iteration')
	#print(n)
	print(len(data))
	data = performInsert(ruleMap,data)

print(data)
countMap = {}

for s in data:
	if(s not in countMap.keys()):
		countMap[s] = 0 
	countMap[s] += 1

for key in countMap.keys():
	print(key +": "+str(countMap[key]))


