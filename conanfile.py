from conans import ConanFile, CMake, tools
import os
import shutil
import glob


class ImguisfmlConan(ConanFile):
    name = "imgui-glfw"
    version = "1.67"  # Version of the imgui-library
    license = "MIT"
    author = "Darlan Cavalcante Moreira (darcamo@gmail.com)"
    url = "https://github.com/darcamo/conan-imgui-glfw"
    description = (
        "Dear ImGui: Bloat-free Immediate Mode Graphical User "
        "interface for C++ with minimal dependencies. This conan "
        "package also depend on glfw.")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    exports_sources = "CMakeLists.txt"
    requires = "glfw/3.2.1@bincrafters/stable"

    def source(self):
        tools.get("https://github.com/ocornut/imgui/archive/v{}.zip".format(self.version))
        os.rename("imgui-{}".format(self.version), "sources")

        # Copy the CMakeLists.txt file to the sources folder
        shutil.move("CMakeLists.txt", "sources/")

    def build(self):
        os.mkdir("build")
        shutil.move("conanbuildinfo.cmake", "build/")
        cmake = CMake(self)
        cmake.configure(source_folder="sources", build_folder="build")
        cmake.build()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["imgui-glfw"]
