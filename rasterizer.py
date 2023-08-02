from gl import Renderer
import shaders


width = 1000
height = 500

rend = Renderer(width, height)
rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.fragmentShader

rend.glLoadModel(filename = "model.obj", texName = "model.bmp", translate=(250, 250, 0), rotate=(0, 2, 0), scale=(300, 300, 300))
rend.glLoadModel(filename = "model.obj", texName = "model.bmp", translate=(750, 250, 0), rotate=(0, 3, 0), scale=(300, 300, 300))


rend.glRender()

rend.glFinish("output1.bmp")
