import inspect
import numpy
from OpenGL import GL
from OpenGL.GL import shaders


class HelloTriangle(object):
    def __init__(self):
        super().__init__()
        self._is_initialized = False
        self.position_buffer_object = None
        self.vertex_positions = None
        self.program = None

    def init_gl(self):
        self.position_buffer_object = GL.glGenBuffers(1)
        GL.glBindBuffer(GL.GL_ARRAY_BUFFER, self.position_buffer_object)
        self.vertex_positions = numpy.array([
            0.75, 0.75, 0.0, 1.0,
            0.75, -0.75, 0.0, 1.0,
            -0.75, -0.75, 0.0, 1.0,
        ], dtype=numpy.float32)
        GL.glBufferData(GL.GL_ARRAY_BUFFER, self.vertex_positions, GL.GL_STATIC_DRAW)
        GL.glBindBuffer(GL.GL_ARRAY_BUFFER, 0)
        GL.glClearColor(0.0, 0.0, 0.2, 0)
        self.program = shaders.compileProgram(
            shaders.compileShader(inspect.cleandoc("""
                #version 330
                layout(location = 0) in vec4 position;
                void main()
                {
                   gl_Position = position;
                }
            """), GL.GL_VERTEX_SHADER),
            shaders.compileShader(inspect.cleandoc("""
                #version 330
                out vec4 outputColor;
                void main()
                {
                   outputColor = vec4(1.0f, 1.0f, 1.0f, 1.0f);
                }
        """), GL.GL_FRAGMENT_SHADER),
        )
        # GL.glUseProgram(self.program)
        self._is_initialized = True

    def draw_gl(self):
        if not self._is_initialized:
            self.init_gl()
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)
        GL.glUseProgram(self.program)
        GL.glBindBuffer(GL.GL_ARRAY_BUFFER, self.position_buffer_object)
        GL.glEnableVertexAttribArray(0)
        GL.glVertexAttribPointer(0, 4, GL.GL_FLOAT, False, 0, None)
        GL.glDrawArrays(GL.GL_TRIANGLES, 0, 3)
        GL.glDisableVertexAttribArray(0)
        GL.glUseProgram(0)

    def dispose_gl(self):
        pass
