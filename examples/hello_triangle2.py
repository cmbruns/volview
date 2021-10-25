"""
TODO:
  * abstract class for glfw vs Qt
  * abstract class for gl_renderer

  with windower, actor:

"""

import glfw
from OpenGL import GL
from volview.actor.hello_triangle import HelloTriangle
from volview.window.glfw_window import GlfwWindow


def framebuffer_size_callback(window, width: int, height: int):
    print(width, height)
    GL.glViewport(0, 0, width, height)


try:
    assert glfw.init()
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 1)
    window = glfw.create_window(640, 480, "Hello Triangle", None, None)
    glfw.make_context_current(window)
    glfw.set_framebuffer_size_callback(window, framebuffer_size_callback)
    with HelloTriangle() as triangle:
        while True:  # Run render loop
            glfw.poll_events()
            if glfw.window_should_close(window):  # session.should_close()
                break
            if True:  # session.should_render()
                # TODO: render
                triangle.draw_gl()
                #
                glfw.swap_buffers(window)  # session.end_frame()
finally:
    glfw.terminate()  # dispose context AFTER disposing actors...
