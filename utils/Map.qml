import QtQuick 2.0
import QtQuick.Window 2.2
import QtQuick.Controls 2.2
import QtLocation 5.6
import QtPositioning 5.6

Rectangle {    
    visible: true
    width: Screen.width/2
    height: Screen.height/2

    Plugin {
        id: mapPlugin
        name: "osm"
    }

    Map {
        anchors.fill: parent
        plugin: mapPlugin
        center: QtPositioning.coordinate(67.85, 20.24) // Kiruna
        zoomLevel: 10

        MapPolyline {
            id: pl
            line.width: 2
            line.color: 'red'
            path: p_manager.path
        }
    }
}