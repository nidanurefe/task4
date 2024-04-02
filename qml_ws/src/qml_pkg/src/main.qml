import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

ApplicationWindow {
    visible: true
    width: 400
    height: 400
    title: "Slider"

  
    Slider {
        id: slider
        objectName: "slider"
        anchors.centerIn: parent
        from: 0
        to: 100
        value: 20 // Initial value
        onValueChanged: {
            sliderValue.text = "Slider Value: " + slider.value.toFixed(2);
        }
    }

    Text {
        id: sliderValue
        anchors.top: slider.bottom
        anchors.horizontalCenter: parent.horizontalCenter
        text: "Slider Value: " + slider.value.toFixed(2)
    }

    Button {
        anchors.bottom: parent.bottom
        anchors.horizontalCenter: parent.horizontalCenter
        text: "Play/Pause"
        checkable: true
        onClicked: Qt.quit()
    }
}

