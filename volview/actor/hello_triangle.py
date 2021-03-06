import inspect
import numpy
from OpenGL import GL
from OpenGL.GL import shaders

from volview.actor import GLActor


class HelloTriangle(GLActor):
    def __init__(self):
        super().__init__()
        self._is_initialized = False
        self.vao = None
        self.position_buffer_object = None
        self.vertex_positions = None
        self.vertex_shader = None
        self.fragment_shader = None
        self.program = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.dispose_gl()

    def init_gl(self) -> None:
        self.vao = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao)
        self.position_buffer_object = GL.glGenBuffers(1)
        GL.glBindBuffer(GL.GL_ARRAY_BUFFER, self.position_buffer_object)
        self.vertex_positions = numpy.array([
            0.75, 0.75, 0.0, 1.0,
            0.75, -0.75, 0.0, 1.0,
            -0.75, -0.75, 0.0, 1.0,
        ], dtype=numpy.float32)
        GL.glBufferData(GL.GL_ARRAY_BUFFER, self.vertex_positions, GL.GL_STATIC_DRAW)
        GL.glClearColor(0.0, 0.0, 0.2, 0)
        self.vertex_shader = shaders.compileShader(inspect.cleandoc("""
            #version 410
            layout(location = 0) in vec4 position;
            void main()
            {
               gl_Position = position;
            }
        """), GL.GL_VERTEX_SHADER)
        self.fragment_shader = shaders.compileShader(inspect.cleandoc("""
            #version 410
            out vec4 outputColor;
            void main()
            {
               outputColor = vec4(0.9f, 1.0f, 1.0f, 1.0f);
            }
        """), GL.GL_FRAGMENT_SHADER)
        self.program = shaders.compileProgram(
            self.vertex_shader,
            self.fragment_shader,
        )
        GL.glUseProgram(self.program)
        GL.glEnableVertexAttribArray(0)
        GL.glVertexAttribPointer(0, 4, GL.GL_FLOAT, False, 0, None)
        self._is_initialized = True

    def draw_gl(self) -> None:
        if not self._is_initialized:
            self.init_gl()
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)
        GL.glDrawArrays(GL.GL_TRIANGLES, 0, 3)

    def dispose_gl(self) -> None:
        if self.position_buffer_object is not None:
            GL.glDeleteBuffers(1, [self.position_buffer_object, ])
            self.position_buffer_object = None
        if self.program is not None:
            GL.glDeleteProgram(self.program)
            self.program = None
        if self.vao is not None:
            GL.glDeleteVertexArrays(1, [self.vao])
            self.vao = None
