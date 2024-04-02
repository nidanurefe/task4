#include <QGuiApplication>
#include <QQmlApplicationEngine>
#include <QQmlContext>
#include <QObject>
#include <QTimer>
#include <thread>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/int32.hpp"

# ifndef APP_QML_PATH
# define APP_QML_PATH "/home/nida/Desktop/qml_ws/src/qml_pkg/src/main.qml"
# endif


//export LD_LIBRARY_PATH=/home/nida/Qt/6.6.3/gcc_64/lib:$LD_LIBRARY_PATH 


std_msgs::msg::Int32 SLIDER; 

void update_slider(QObject *object) { 

    QObject *obj = object->findChild<QObject*>("slider");

    if (obj) { 
        obj->setProperty("value", QVariant(QString::number(SLIDER.data)));

        
    } else {
        std::cerr << "Failed to find slider object in QML." << std::endl;
    }
}


void manage_slider(const std_msgs::msg::Int32::SharedPtr msg) {
    SLIDER.data = msg->data;     
}

int main(int argc, char *argv[]) {
    rclcpp::init(argc, argv); 


    auto node = std::make_shared<rclcpp::Node>("subscriber_node"); 
    auto subscriber = node->create_subscription<std_msgs::msg::Int32>(
        "slider_topic", 10, manage_slider);


    std::thread rosSpinner([&node]() {
        rclcpp::spin(node);
    });


    QGuiApplication app(argc, argv); 

    QQmlApplicationEngine engine; 
    engine.load(QUrl::fromLocalFile(APP_QML_PATH));
    
    if (engine.rootObjects().isEmpty()){
        std::cerr << "Failed to load QML file." << std::endl;
        return -1;
    }

    QTimer timer;
    QObject::connect(&timer,&QTimer::timeout, [&engine](){
        std::cout << "Value: " << SLIDER.data << '\n';
        QObject *qmlRoot = engine.rootObjects().first(); 

        update_slider(qmlRoot);

    });

    
    timer.start(1000);
    int result = app.exec();
    rosSpinner.join();
    rclcpp::shutdown();
    

    return result;
}
