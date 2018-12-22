# RaspberryPi
<h1> Communication protocol client -> server</h1><br>
Client------------------------->Server--------------------------------------------->Client------------------------------------>Server
 1s   req=post(outputpinstatus)        response=json(outputpins changed) 
 60s  req=post(pinstatus)              response=json(ouptutpinschanged+inputpinsdata)       request=post(json(inputpinsvalues))   