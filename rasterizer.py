from gl import Renderer
import shaders


width = 2048
height = 2048

rend = Renderer(width, height)
rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.fragmentShader

scaleDim = 30

rend.glLoadModel(filename = "cap.obj", texName = "captex.bmp", translate=(512, 512, 0), rotate=(-1.5, 0, -1.5), scale=(scaleDim, scaleDim, scaleDim))
rend.glLoadModel(filename = "cap.obj", texName = "captex.bmp", translate=(1536, 512, 0), rotate=(-2, 0, 0), scale=(scaleDim, scaleDim, scaleDim))
rend.glLoadModel(filename = "cap.obj", texName = "captex.bmp", translate=(512, 1536, 0), rotate=(-1.5, 0, 0.5), scale=(scaleDim, scaleDim, scaleDim))
rend.glLoadModel(filename = "cap.obj", texName = "captex.bmp", translate=(1536, 1536, 0), rotate=(-1.5, 0, 3.15), scale=(scaleDim, scaleDim, scaleDim))


rend.glRender()

rend.glFinish("Cap.bmp")
