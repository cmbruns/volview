from OpenGL import GL
import glfw

from volview.actor import GLActor
from volview.window import GLWindow


class GlfwWindow(GLWindow):
    def __init__(self, renderer: GLActor):
        super().__init__()
        self.renderer = renderer
        glfw.init()
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
        self.window = glfw.create_window(640, 480, "Hello Triangle", None, None)
        glfw.make_context_current(self.window)
        glfw.set_framebuffer_size_callback(self.window, self.framebuffer_size_callback)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.renderer.dispose_gl()
        glfw.terminate()

    def framebuffer_size_callback(self, window, width: int, height: int):
        GL.glViewport(0, 0, width, height)
        # Update render while dragging window corner
        self.renderer.draw_gl()
        glfw.swap_buffers(window)  # session.end_frame()

    def render_loop(self):
        while True:  # Run render loop
            glfw.poll_events()
            if glfw.window_should_close(self.window):  # session.should_close()
                break
            if True:  # session.should_render()
                self.renderer.draw_gl()
                glfw.swap_buffers(self.window)  # session.end_frame()
