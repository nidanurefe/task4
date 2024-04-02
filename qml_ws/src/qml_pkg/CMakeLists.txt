cmake_minimum_required(VERSION 3.8)
project(qml_pkg)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

set(Qt6_DIR "/home/nida/Qt/6.6.3/gcc_64/lib/cmake/Qt6")      
set(QML_FILE_PATH ${CMAKE_CURRENT_SOURCE_DIR}/src/main.qml)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(example_interfaces REQUIRED)
find_package(std_msgs REQUIRED)
find_package(Qt6 REQUIRED COMPONENTS Quick Core Widgets Gui Qml)

find_package(Qt6 COMPONENTS Quick QuickControls2 REQUIRED)


add_executable(main src/main.cpp)
add_executable(deneme src/deneme.cpp)

ament_target_dependencies(main rclcpp Qt6 std_msgs)
ament_target_dependencies(deneme rclcpp Qt6 std_msgs)

# set(ENV{LD_LIBRARY_PATH} "/home/nida/Qt/6.6.3/gcc_64/lib:${LD_LIBRARY_PATH}")
target_link_directories(main PRIVATE /home/nida/Qt/6.6.3/gcc_64/lib)
target_link_directories(deneme PRIVATE /home/nida/Qt/6.6.3/gcc_64/lib)


install(TARGETS
  main
  deneme
  DESTINATION lib/${PROJECT_NAME}
)

target_link_libraries(main
  Qt6::Core
  Qt6::Widgets
  Qt6::Gui
  Qt6::Qml
  Qt6::Quick
)

ament_package()
