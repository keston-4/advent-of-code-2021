import re

data_example = 'NNCB'
data_puzzle = 'PSVVKKCNBPNBBHNSFKBO'

rules_example = [['CH','B'],['HH','N'],['CB','H'],['NH','C'],['HB','C'],['HC','B'],['HN','C'],['NN','C'],['BH','H'],['NC','B'],['NB','B'],['BN','B'],['BB','N'],['BC','B'],['CC','N'],['CN','C']]
rules_puzzle = [['CF','H'],['PP','H'],['SP','V'],['NO','C'],['SF','F'],['FS','H'],['OF','P'],['PN','B'],['SH','V'],['BO','K'],['ON','V'],['VP','S'],['HN','B'],['PS','P'],['FV','H'],['NC','N'],['FN','S'],['PF','F'],['BF','F'],['NB','O'],['HS','C'],['SC','V'],['PC','K'],['KF','K'],['HC','C'],['OK','H'],['KS','P'],['VF','C'],['NV','S'],['KK','F'],['HV','H'],['SV','V'],['KC','N'],['HF','P'],['SN','F'],['VS','P'],['VN','F'],['VH','C'],['OB','K'],['VV','O'],['VC','O'],['KP','V'],['OP','C'],['HO','S'],['NP','K'],['HB','C'],['CS','S'],['OO','S'],['CV','K'],['BS','F'],['BH','P'],['HP','P'],['PK','B'],['BB','H'],['PV','N'],['VO','P'],['SS','B'],['CC','F'],['BC','V'],['FF','S'],['HK','V'],['OH','N'],['BV','C'],['CP','F'],['KN','K'],['NN','S'],['FB','F'],['PH','O'],['FH','N'],['FK','P'],['CK','V'],['CN','S'],['BP','K'],['CH','F'],['FP','K'],['HH','N'],['NF','C'],['VB','B'],['FO','N'],['PB','C'],['KH','K'],['PO','K'],['OV','F'],['NH','H'],['KV','B'],['OS','K'],['OC','K'],['FC','H'],['SO','H'],['KO','P'],['NS','F'],['CB','C'],['CO','F'],['KB','V'],['BK','K'],['NK','O'],['SK','C'],['SB','B'],['VK','O'],['BN','H']]

def generateRuleMap(rules):
	ruleMap = {}
	for pair in rules:
		ruleMap[pair[0]] = pair[1]
	return ruleMap

def generateDataMap(data, characterMap):
	dataMap = {}
	for i in range(len(data)):
		addToDict(data[i], 1, characterMap)
		if(i < len(data) -1):
			addToDict(data[i]+data[i+1], 1, dataMap)
	return dataMap

def performInsert(ruleMap,dataMap,characterMap):
	newPairs = {} #newPairs
	matchedPairs = {} #matchedPairs
	for rule in ruleMap:
		if(rule in dataMap and dataMap[rule] > 0):
			addToDict(ruleMap[rule], dataMap[rule], characterMap)
			addToDict(rule[0]+ruleMap[rule], dataMap[rule], newPairs)
			addToDict(ruleMap[rule]+rule[1], dataMap[rule], newPairs)
			addToDict(rule, - (dataMap[rule]), matchedPairs)

	for k in matchedPairs.keys():
		addToDict(k, matchedPairs[k], dataMap)

	for k in newPairs.keys():
		addToDict(k, newPairs[k], dataMap)

	return dataMap

def addToDict(k, v, mDict):
	mDict[k] = (mDict[k] if k in mDict.keys() else 0) + v

def printPairs(dataMap):
	for k in dataMap.keys():	
		print(str(k)+":"+str(dataMap[k]))

def calculateCharacters(dataMap):
	outputMap = {}
	for k in dataMap.keys():
		addToDict(k[0], dataMap[k], outputMap)
		addToDict(k[1], dataMap[k], outputMap)

	for k in outputMap.keys():
		outputMap[k] = (outputMap[k] / 2) + (outputMap[k] % 2)
	return outputMap

def start(rules, data, steps):	
	characterMap = {}
	ruleMap = generateRuleMap(rules)
	dataMap = generateDataMap(data, characterMap)
	for iteration in range(steps):
		performInsert(ruleMap, dataMap, characterMap)
	return max(characterMap.values()) - min(characterMap.values())

print("Part 1 (Example): "+ str(start(rules_example, data_example, 10)))
print("Part 2 (Example): "+ str(start(rules_example, data_example, 40)))

print("Part 1 (Puzzle): "+ str(start(rules_puzzle, data_puzzle, 10)))
print("Part 2 (Puzzle): "+ str(start(rules_puzzle, data_puzzle, 40)))


	
