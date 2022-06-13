import jsonFileHandler
data = jsonFileHandler.readJsonFile('files/insulin.json')


if data != "":
    bInsulin = data['molecules']['bInsulin']
    aInsulin = data['molecules']['aInsulin']
    insulin = bInsulin + aInsulin
    molecularWeightInsulinActual = data['molecularWeightInsulinActual']
    print('bInsulin: ' + bInsulin)
    print('aInsulin: ' + aInsulin)
    print('molecularWeightInsulinActual: ' + str(molecularWeightInsulinActual))

    aaWeights = data['weights']
    aaCountInsulin = ({x: int(insulin.upper().count(x))
                      for x in aaWeights})
    print("aaCountInsulin is ")
    print(aaCountInsulin)
    molecularWeightInsulin = sum(
        {x: (aaCountInsulin[x]*aaWeights[x]) for x in aaWeights}.values())
    print("The rough molecular weight of insulin: " +
          str(molecularWeightInsulin))
    print("Percent error: " + str(((molecularWeightInsulin -
          molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))
else:
    print("Error. Exiting program")
