cmake_minimum_required(VERSION 3.10)
project(imgui-glfw)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_library(imgui-glfw
  imconfig.h
  imgui.cpp
  imgui_demo.cpp
  imgui_draw.cpp
  imgui.h
  imgui_internal.h
  imgui_widgets.cpp
  imstb_rectpack.h
  imstb_textedit.h
  imstb_truetype.h
  examples/imgui_impl_glfw.cpp
  examples/imgui_impl_glfw.h
  examples/imgui_impl_opengl2.cpp
  examples/imgui_impl_opengl2.h
  )

target_include_directories(imgui-glfw SYSTEM PUBLIC .)
# target_link_libraries(imgui-glfw PUBLIC sfml-graphics sfml-window sfml-system sfml-network sfml-audio)
# target_link_libraries(imgui-glfw PUBLIC "-lGL")


# Rule to install the compiled library
install(TARGETS imgui-glfw DESTINATION lib)
# Rule to install the headers
install(FILES
  imconfig.h
  imgui.h
  imgui_internal.h
  imstb_rectpack.h
  imstb_textedit.h
  imstb_truetype.h
  examples/imgui_impl_glfw.h
  examples/imgui_impl_opengl2.h
  DESTINATION include
  )
# Rule to install the source -> Usually this is not necessary, but since imgui
# uses the source as documentation we also install the source in the conan cache
install(FILES
  imgui.cpp
  imgui_demo.cpp
  imgui_draw.cpp
  examples/imgui_impl_glfw.cpp
  examples/imgui_impl_opengl2.cpp
  imgui_widgets.cpp
  DESTINATION src
  )
