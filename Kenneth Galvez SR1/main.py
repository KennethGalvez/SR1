from gl import Render, color

width = 100
height = 100


rend = Render()
rend.glCreateWindow(width, height)

rend.glViewport(int(width / 4),
                int(height / 4), 
                int(width / 2), 
                int(height / 2))

rend.glClearColor(0,0,0.82)
rend.glClear()
rend.glClearViewport(color(1,0.54,0))

rend.glPoint_vp(0,0)
#rend.glPoint_vp(1,1)
rend.glPoint_vp(0.999,0.999)
rend.glPoint_vp(-1,-1)

#for i in range(width):
#    rend.glPoint(i, i)


rend.glFinish('output.bmp')