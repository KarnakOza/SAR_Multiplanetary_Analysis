## Apply Orbit File

##Applying Orbit File 
 
parameters = HashMap()
GPF.getDefaultInstance().getOperatorSpiRegistry().loadOperatorSpis()
parameters.put('orbitType', 'Sentinel Precise (Auto Download)')
parameters.put('polyDegree', '3')
parameters.put('continueOnFail', 'false')
apply_orbit_file = GPF.createProduct('Apply-Orbit-File', parameters, product)
return imgplot
