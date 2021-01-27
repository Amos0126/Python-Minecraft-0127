from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
    hits = mc.events.pollBlockHits()
    if len(hits)>0:
        a = hits[0]
        x,y,z = a.pos.x,a.pos.y,a.pos.z
        block = mc.getBlock(x,y,z)
        mc.postToChat("You hit: "+str(block))
        if block == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
            mc.setBlock(x,y,z,14)
            mc.postToChat("That Block trun to 14!")
            