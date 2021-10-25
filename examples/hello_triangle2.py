"""
TODO:
  * abstract class for glfw vs Qt
  * abstract class for gl_renderer

  with windower, actor:

"""

import glfw
from OpenGL import GL
from volview.actor.hello_triangle import HelloTriangle

triangle = HelloTriangle()
try:
    assert glfw.init()
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    window = glfw.create_window(640, 480, "Hello Triangle", None, None)
    glfw.make_context_current(window)
    while True:
        glfw.poll_events()
        if glfw.window_should_close(window):  # session.should_close()
            break
        if True:  # session.should_render()
            # TODO: render
            triangle.draw_gl()
            #
            glfw.swap_buffers(window)  # session.end_frame()
finally:
    glfw.terminate()

print("Hello")
