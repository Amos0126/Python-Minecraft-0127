from mcpi.minecraft import Minecraft
import random,time
mc = Minecraft.create()

while True:
    x,y,z = mc.player.getPos()
    a = random.uniform(-20,20)
    b = random.uniform(-20,20)
    
    mc.spawnEntity(446,3,190,45)
    
    
    
    # /kill @e[type=chicken]
    # /time set day