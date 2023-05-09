import os
import json

from qtpy.QtCore import *
from qtpy.QtGui import *

def loadJsonStyle(self, ui, **jsonFiles):

    self.customWidgetsThreadpool = QThreadPool()
    self.ui = ui

    file = open('style.json',)
    data = json.load(file)
    applyJsonStyle(self, ui, data)

def applyJsonStyle(self, ui, data):
    if "AnalogGaugeWidget" in data:
        for AnalogGaugeWidget in data['AnalogGaugeWidget']:
            if "name" in AnalogGaugeWidget and len(str(AnalogGaugeWidget["name"])) > 0:
                if hasattr(self.ui, str(AnalogGaugeWidget["name"])):
                    gaugeWidget = getattr(self.ui, str(AnalogGaugeWidget["name"]))

                    if not gaugeWidget.metaObject().className() == "AnalogGaugeWidget":
                        raise Exception(
                            "Error: " + str(AnalogGaugeWidget["name"]) + " is not a AnalogGaugeWidget object")
                        return

                    if "units" in AnalogGaugeWidget and len(str(AnalogGaugeWidget["units"])) > 0:
                        # Set gauge units
                        gaugeWidget.units = str(AnalogGaugeWidget["units"])

                    if "scaleFontSize" in AnalogGaugeWidget:
                        # Set scale font size
                        gaugeWidget.initial_scale_fontsize = int(AnalogGaugeWidget["scaleFontSize"])

                    if "valueFontSize" in AnalogGaugeWidget:
                        # Set value font size
                        gaugeWidget.initial_value_fontsize = int(AnalogGaugeWidget["valueFontSize"])

                    if "minValue" in AnalogGaugeWidget:
                        # Set gauge min value
                        gaugeWidget.minValue = int(AnalogGaugeWidget["minValue"])

                    if "maxValue" in AnalogGaugeWidget:
                        # Set gauge max value
                        gaugeWidget.maxValue = int(AnalogGaugeWidget["maxValue"])

                    if "scalaCount" in AnalogGaugeWidget:
                        # Set scala count
                        gaugeWidget.scalaCount = int(AnalogGaugeWidget["scalaCount"])

                    if "scalaSubDivCount" in AnalogGaugeWidget:
                        # Set scala count
                        gaugeWidget.scala_subdiv_count = int(AnalogGaugeWidget["scalaSubDivCount"])

                    if "startValue" in AnalogGaugeWidget:
                        # Set start value
                        gaugeWidget.updateValue(int(AnalogGaugeWidget["startValue"]))

                    if "gaugeTheme" in AnalogGaugeWidget:
                        # Set gauge theme
                        gaugeWidget.setGaugeTheme(int(AnalogGaugeWidget["gaugeTheme"]))

                    if "offsetAngle" in AnalogGaugeWidget:
                        # Set offset angle
                        gaugeWidget.updateAngleOffset(int(AnalogGaugeWidget["offsetAngle"]))

                    if "innerRadius" in AnalogGaugeWidget:
                        # Set inner radius
                        gaugeWidget.setGaugeColorInnerRadiusFactor(int(AnalogGaugeWidget["innerRadius"]))

                    if "outerRadius" in AnalogGaugeWidget:
                        # Set outer radius
                        gaugeWidget.setGaugeColorOuterRadiusFactor(int(AnalogGaugeWidget["outerRadius"]))

                    if "scaleStartAngle" in AnalogGaugeWidget:
                        # Set start angle
                        gaugeWidget.setScaleStartAngle(int(AnalogGaugeWidget["scaleStartAngle"]))

                    if "totalScaleAngle" in AnalogGaugeWidget:
                        # Set total scale angle
                        gaugeWidget.setTotalScaleAngleSize(int(AnalogGaugeWidget["totalScaleAngle"]))

                    if "enableOuterCircle" in AnalogGaugeWidget:
                        # Set enable outer circle
                        gaugeWidget.setEnableOuterCircle(bool(AnalogGaugeWidget["enableOuterCircle"]))

                    if "enableOuterHalfCircle" in AnalogGaugeWidget:

                        gaugeWidget.setEnableOuterHalfCircle(bool(AnalogGaugeWidget["enableOuterHalfCircle"]))

                    if "enableBarGraph" in AnalogGaugeWidget:
                        # Set enable bar graph
                        gaugeWidget.setEnableBarGraph(bool(AnalogGaugeWidget["enableBarGraph"]))

                    if "enableValueText" in AnalogGaugeWidget:
                        # Set enable text value
                        gaugeWidget.setEnableValueText(bool(AnalogGaugeWidget["enableValueText"]))

                    if "enableNeedlePolygon" in AnalogGaugeWidget:
                        # Set enable needle polygon
                        gaugeWidget.setEnableNeedlePolygon(bool(AnalogGaugeWidget["enableNeedlePolygon"]))

                    if "enableCenterPoint" in AnalogGaugeWidget:
                        # Set enable needle center
                        gaugeWidget.setEnableCenterPoint(bool(AnalogGaugeWidget["enableCenterPoint"]))

                    if "enableScalePolygon" in AnalogGaugeWidget:
                        if AnalogGaugeWidget["enableScalePolygon"]:
                            gaugeWidget.setEnableScalePolygon(True)
                        else:
                            gaugeWidget.setEnableScalePolygon(False)

                    if "enableScaleText" in AnalogGaugeWidget:
                        # Set enable scale text
                        gaugeWidget.setEnableScaleText(bool(AnalogGaugeWidget["enableScaleText"]))

                    if "enableScaleBigGrid" in AnalogGaugeWidget:
                        # Set enable big scale grid
                        gaugeWidget.setEnableBigScaleGrid(bool(AnalogGaugeWidget["enableScaleBigGrid"]))

                    if "enableScaleFineGrid" in AnalogGaugeWidget:
                        # Set enable big scale grid
                        gaugeWidget.setEnableFineScaleGrid(bool(AnalogGaugeWidget["enableScaleFineGrid"]))

                    if "needleLength" in AnalogGaugeWidget :
                        gaugeWidget.needle_scale_factor = float(AnalogGaugeWidget["needleLength"])

                    if "needleColor" in AnalogGaugeWidget and len(str(AnalogGaugeWidget["needleColor"])) > 0:
                        # Set needle color
                        gaugeWidget.NeedleColor = QColor(str(AnalogGaugeWidget["needleColor"]))
                        gaugeWidget.NeedleColorReleased = QColor(str(AnalogGaugeWidget["needleColor"]))

                    if "needleColorOnDrag" in AnalogGaugeWidget and len(
                            str(AnalogGaugeWidget["needleColorOnDrag"])) > 0:
                        # Set needle color on drag
                        gaugeWidget.NeedleColorDrag = QColor(str(AnalogGaugeWidget["needleColorOnDrag"]))

                    if "scaleValueColor" in AnalogGaugeWidget and len(str(AnalogGaugeWidget["scaleValueColor"])) > 0:
                        # Set value color
                        gaugeWidget.ScaleValueColor = QColor(str(AnalogGaugeWidget["scaleValueColor"]))

                    if "displayValueColor" in AnalogGaugeWidget and len(
                            str(AnalogGaugeWidget["displayValueColor"])) > 0:
                        # Set display value color
                        gaugeWidget.DisplayValueColor = QColor(str(AnalogGaugeWidget["displayValueColor"]))

                    if "bigScaleColor" in AnalogGaugeWidget and len(str(AnalogGaugeWidget["bigScaleColor"])) > 0:
                        # Set big scale color
                        gaugeWidget.setBigScaleColor(QColor(str(AnalogGaugeWidget["bigScaleColor"])))

                    if "fineScaleColor" in AnalogGaugeWidget and len(str(AnalogGaugeWidget["fineScaleColor"])) > 0:
                        # Set fine scale color
                        gaugeWidget.setFineScaleColor(QColor(str(AnalogGaugeWidget["fineScaleColor"])))

                    if "customGaugeTheme" in AnalogGaugeWidget:
                        # Set custom gauge theme
                        colors = AnalogGaugeWidget['customGaugeTheme']

                        for x in colors:

                            if "color1" in x and len(str(x['color1'])) > 0:
                                if "color2" in x and len(str(x['color2'])) > 0:
                                    if "color3" in x and len(str(x['color3'])) > 0:

                                        gaugeWidget.setCustomGaugeTheme(
                                            color1=str(x['color1']),
                                            color2=str(x['color2']),
                                            color3=str(x['color3'])
                                        )

                                    else:

                                        gaugeWidget.setCustomGaugeTheme(
                                            color1=str(x['color1']),
                                            color2=str(x['color2']),
                                        )

                                else:

                                    gaugeWidget.setCustomGaugeTheme(
                                        color1=str(x['color1']),
                                    )

                    if "scalePolygonColor" in AnalogGaugeWidget:
                        # Set scale polygon color
                        colors = AnalogGaugeWidget['scalePolygonColor']

                        for x in colors:

                            if "color1" in x and len(str(x['color1'])) > 0:
                                if "color2" in x and len(str(x['color2'])) > 0:
                                    if "color3" in x and len(str(x['color3'])) > 0:

                                        gaugeWidget.setScalePolygonColor(
                                            color1=str(x['color1']),
                                            color2=str(x['color2']),
                                            color3=str(x['color3'])
                                        )

                                    else:

                                        gaugeWidget.setScalePolygonColor(
                                            color1=str(x['color1']),
                                            color2=str(x['color2']),
                                        )

                                else:

                                    gaugeWidget.setScalePolygonColor(
                                        color1=str(x['color1']),
                                    )

                    if "setScalePolygonColorInverse" in AnalogGaugeWidget:
                        if AnalogGaugeWidget["setScalePolygonColorInverse"] :
                            gaugeWidget.set_scale_polygon_colors([
                                                      [.05, Qt.green],
                                                      [.15, Qt.yellow],
                                                      [.25, Qt.red],
                                                      [1, Qt.transparent]])

                    if "setScalePolygonColorHalf" in AnalogGaugeWidget:
                        if AnalogGaugeWidget["setScalePolygonColorHalf"]:
                            gaugeWidget.set_scale_polygon_colors([
                                                    [.25, Qt.green],
                                                    [.5, Qt.red],
                                                    [1, Qt.transparent]])

                    if "needleCenterColor" in AnalogGaugeWidget:
                        # Set needle center color
                        colors = AnalogGaugeWidget['needleCenterColor']

                        for x in colors:

                            if "color1" in x and len(str(x['color1'])) > 0:
                                if "color2" in x and len(str(x['color2'])) > 0:
                                    if "color3" in x and len(str(x['color3'])) > 0:

                                        gaugeWidget.setNeedleCenterColor(
                                            color1=str(x['color1']),
                                            color2=str(x['color2']),
                                            color3=str(x['color3'])
                                        )

                                    else:

                                        gaugeWidget.setNeedleCenterColor(
                                            color1=str(x['color1']),
                                            color2=str(x['color2']),
                                        )

                                else:

                                    gaugeWidget.setNeedleCenterColor(
                                        color1=str(x['color1']),
                                    )

                    if "outerCircleColor" in AnalogGaugeWidget:
                        # Set outer circle color
                        colors = AnalogGaugeWidget['outerCircleColor']

                        for x in colors:

                            if "color1" in x and len(str(x['color1'])) > 0:
                                if "color2" in x and len(str(x['color2'])) > 0:
                                    if "color3" in x and len(str(x['color3'])) > 0:

                                        gaugeWidget.setOuterCircleColor(
                                            color1=str(x['color1']),
                                            color2=str(x['color2']),
                                            color3=str(x['color3'])
                                        )

                                    else:

                                        gaugeWidget.setOuterCircleColor(
                                            color1=str(x['color1']),
                                            color2=str(x['color2']),
                                        )

                                else:

                                    gaugeWidget.setOuterCircleColor(
                                        color1=str(x['color1']),
                                    )

                    if "valueFontFamily" in AnalogGaugeWidget:
                        # Set value font family
                        font = AnalogGaugeWidget['valueFontFamily']

                        for x in font:
                            if "path" in x and len(str(x['path'])) > 0:
                                QFontDatabase.addApplicationFont(
                                    os.path.join(os.path.dirname(__file__), str(x['path'])))

                            if "name" in x and len(str(x['name'])) > 0:
                                gaugeWidget.setValueFontFamily(str(x['name']))

                    if "scaleFontFamily" in AnalogGaugeWidget:
                        # Set scale font family
                        font = AnalogGaugeWidget['scaleFontFamily']
                        for x in font:
                            if "path" in x and len(str(x['path'])) > 0:
                                QFontDatabase.addApplicationFont(
                                    os.path.join(os.path.dirname(__file__), str(x['path'])))

                            if "name" in x and len(str(x['name'])) > 0:
                                gaugeWidget.setScaleFontFamily(str(x['name']))


                else:
                    raise Exception(str(AnalogGaugeWidget["name"]) + " is not a AnalogGaugeWidget, no widget found")