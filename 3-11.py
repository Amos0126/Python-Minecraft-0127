from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getPos()

number = 1

for i in range(100):
    for j in range(number):
        mc.spawnEntity(x,y,z,11)
    number = number * 2
    mc.postToChat(str(number))