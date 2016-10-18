
  # mapping.py
  # Mapping Generator

  # Created by Jorge Villamayor on 14/10/16.
  # Copyright © 2016 Jorge Villamayor. All rights reserved.

# Set total amount of ranks, sockets per node, and Cores (slots) per Socket.
totalRanks=128
totalSocketsPerNode=8
totalSlotPerSocket=8


fileName="hostfile"

with open(fileName) as f:
	data = f.read()

data = data.split('\n')

while '' in data:
    data.remove('')

totalNodes = len(data)

rankCount=0

totalProcessPerNode = totalRanks/totalNodes

if totalProcessPerNode>totalSocketsPerNode*totalSlotPerSocket:
	print "Not possible to map."
	exit(0)


print "Total processes per Node: " +str(totalProcessPerNode)

for host in data:

 	rankPerNodeCount=0
 	slotCount=0
 	# If we have more process than sockets, we fill using all slots, otherwise we jump slots to use only sockets

 	while totalProcessPerNode>rankPerNodeCount:

	 	print "rank "+str(rankCount)+"="+str(host)+" slot="+str(slotCount)
	 	if totalSocketsPerNode>=totalProcessPerNode:
	 		slotCount=slotCount+totalSlotPerSocket
	 	else:
	 		slotCount=slotCount+1

		rankCount=rankCount+1
		rankPerNodeCount=rankPerNodeCount+1

		
