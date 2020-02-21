from conans import ConanFile, CMake, tools


class HelloConan(ConanFile):
    name = "Hello_next"
    version = "0.1"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Hello here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    exports_sources = "src/*"
    #requires = "FMILibrary/2.0.3@aev25/stable"
    requires = "AEV_CMAKE/2.0.0@aev25/stable"
    

    #def source(self):
        #self.run("git clone https://github.com/conan-io/hello.git")

    def build(self):
        cmake = CMake(self)
        #cmake.configure(source_folder="hello")
        cmake.configure(source_folder="src")
        cmake.build()

        # Explicit way:
        # self.run('cmake %s/hello %s'
        #          % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)
    def requirements(self):
        self.requires("AEV_CMAKE/2.0.0@aev25/stable")

    def package(self):
        self.copy("*.h", dst="include", src="src")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.exe", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["hello"]
