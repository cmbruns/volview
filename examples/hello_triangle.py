"""
TODO:
  * abstract class for glfw vs Qt
  * abstract class for gl_renderer

  with windower, actor:

"""

import glfw
from OpenGL import GL

try:
    assert glfw.init()
    window = glfw.create_window(640, 480, "Hello Triangle", None, None)
    glfw.make_context_current(window)
    GL.glClearColor(0, 0.2, 0, 0)
    while True:
        glfw.poll_events()
        if glfw.window_should_close(window):  # session.should_close()
            break
        if True:  # session.should_render()
            # TODO: render
            GL.glClear(GL.GL_COLOR_BUFFER_BIT)
            #
            glfw.swap_buffers(window)  # session.end_frame()
finally:
    glfw.terminate()

print("Hello")
