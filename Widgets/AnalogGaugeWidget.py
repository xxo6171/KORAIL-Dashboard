import math
from PySide2.QtWidgets import QMainWindow, QWidget
from PySide2.QtGui import QPolygon, QPolygonF, QColor, QPen, QFont, QPainter, QFontMetrics, QConicalGradient, \
    QRadialGradient, QFontDatabase
from PySide2.QtCore import Qt, QTime, QTimer, QPoint, QPointF, QRect, QSize, QObject, Signal

class AnalogGaugeWidget(QWidget):
    valueChanged = Signal(int)

    def __init__(self, parent=None):
        super(AnalogGaugeWidget, self).__init__(parent)
        # print(self.width(), self.height())
        
        # DEFAULT TIMER VALUE
        self.use_timer_event = False

        # DEFAULT NEEDLE COLOR
        self.setNeedleColor(0, 0, 0, 255)

        # DEFAULT NEEDLE WHEN RELEASED
        self.NeedleColorReleased = self.NeedleColor

        # DEFAULT SCALE TEXT COLOR
        self.setScaleValueColor(0, 0, 0, 255)

        # DEFAULT VALUE COLOR
        self.setDisplayValueColor(0, 0, 0, 255)

        # DEFAULT CENTER POINTER COLOR
        # self.CenterPointColor = QColor(50, 50, 50, 255)
        self.set_CenterPointColor(0, 0, 0, 255)

        # DEFAULT NEEDLE COUNT
        self.value_needle_count = 1
        self.value_needle = QObject

        # DEFAULT MINIMUM AND MAXIMUM VALUE
        self.minValue = 0
        self.maxValue = 1000
        
        # DEFAULT START VALUE
        self.value = self.minValue

        # DEFAULT OFFSET
        self.value_offset = 0
        self.valueNeedleSnapzone = 0.05
        self.last_value = 0

        # DEFAULT RADIUS
        self.gauge_color_outer_radius_factor = 1
        self.gauge_color_inner_radius_factor = 0.9

        self.center_horizontal_value = 0
        self.center_vertical_value = 0

        # DEFAULT SCALE VALUE
        self.scale_angle_start_value = 135
        self.scale_angle_size = 270

        self.scale_length = -1

        self.angle_offset = 0

        self.setScalaCount(10)
        self.scala_subdiv_count = 5

        self.pen = QPen(QColor(0, 0, 0))

        # DEFAULT OUTER CIRCLE ADDED RADIUS LENGTH
        self.outer_circle_radius = 3

        self.circle_padding = 13

        # DEFAULT POLYGON COLOR
        self.scale_polygon_colors = []

        # BIG SCALE COLOR
        self.bigScaleMarker = Qt.black

        # FINE SCALE COLOR
        self.fineScaleColor = Qt.black

        # DEFAULT SCALE TEXT STATUS
        self.setEnableScaleText(True)
        self.scale_fontname = "Orbitron"
        self.initial_scale_fontsize = 14
        self.scale_fontsize = self.initial_scale_fontsize

        # DEFAULT VALUE TEXT STATUS
        self.enable_value_text = True
        self.value_fontname = "Orbitron"
        self.initial_value_fontsize = 40
        self.value_fontsize = self.initial_value_fontsize
        self.text_radius_factor = 0.5

        # ENABLE BAR GRAPH BY DEFAULT
        self.setEnableBarGraph(True)
        
        # FILL POLYGON COLOR BY DEFAULT
        self.setEnableScalePolygon(True)

        # ENABLE OUTER CIRCLE BY DEFAULT
        self.enable_outer_circle = True

        self.enable_outer_half_circle = False
        
        # ENABLE CENTER POINTER BY DEFAULT
        self.enable_CenterPoint = True
        
        # ENABLE FINE SCALE BY DEFAULT
        self.enable_fine_scaled_marker = True
        
        # ENABLE BIG SCALE BY DEFAULT
        self.enable_big_scaled_marker = True

        # ENABLE INNER VALUE TEXT BY DEFAULT
        self.enable_inner_value_text = True

        # NEEDLE SCALE FACTOR/LENGTH
        self.needle_scale_factor = 0.8
        
        # ENABLE NEEDLE POLYGON BY DEFAULT
        self.enable_Needle_Polygon = True

        # ENABLE NEEDLE MOUSE TRACKING BY DEFAULT
        self.setMouseTracking(True)

        # SET GAUGE UNITS
        self.units = "℃"

        self.timer = QTimer(self)
        if self.use_timer_event:
            self.timer.timeout.connect(self.update)
            self.timer.start(10)
        else:
            self.update()

        # SET DEFAULT THEME
        self.setGaugeTheme(0)

        # RESIZE GAUGE
        self.rescale_method()

    # SET SCALE FONT FAMILY
    def setScaleFontFamily(self, font):
        self.scale_fontname = str(font)

    # SET VALUE FONT FAMILY
    def setValueFontFamily(self, font):
        self.value_fontname = str(font)
    
    # SET BIG SCALE COLOR
    def setBigScaleColor(self, color):
        self.bigScaleMarker = QColor(color)

    # SET FINE SCALE COLOR
    def setFineScaleColor(self, color):
        self.fineScaleColor = QColor(color)

    # GAUGE THEMES
    def setGaugeTheme(self, Theme=1):
        if Theme == 0 or Theme is None:
            self.set_scale_polygon_colors([[.00, Qt.red],
                                           [.1, Qt.yellow],
                                           [.15, Qt.green],
                                           [1, Qt.transparent]])

            self.needle_center_bg = [
                                    [0, QColor(35, 40, 3, 255)],
                                    [0.16, QColor(30, 36, 45, 255)],
                                    [0.225, QColor(36, 42, 54, 255)],
                                    [0.423963, QColor(19, 23, 29, 255)],
                                    [0.580645, QColor(45, 53, 68, 255)],
                                    [0.792627, QColor(59, 70, 88, 255)],
                                    [0.935, QColor(30, 35, 45, 255)],
                                    [1, QColor(35, 40, 3, 255)]
            ]

            self.outer_circle_bg = [
                [0.0645161, QColor(30, 35, 45, 255)],
                [0.37788, QColor(57, 67, 86, 255)],
                [1, QColor(30, 36, 45, 255)]
            ]

        if Theme == 1:
            self.set_scale_polygon_colors([[.75, Qt.red],
                                           [.5, Qt.yellow],
                                           [.25, Qt.green]])

            self.needle_center_bg = [
                                    [0, QColor(35, 40, 3, 255)],
                                    [0.16, QColor(30, 36, 45, 255)],
                                    [0.225, QColor(36, 42, 54, 255)],
                                    [0.423963, QColor(19, 23, 29, 255)],
                                    [0.580645, QColor(45, 53, 68, 255)],
                                    [0.792627, QColor(59, 70, 88, 255)],
                                    [0.935, QColor(30, 35, 45, 255)],
                                    [1, QColor(35, 40, 3, 255)]
            ]

            self.outer_circle_bg = [
                [0.0645161, QColor(30, 35, 45, 255)],
                [0.37788, QColor(57, 67, 86, 255)],
                [1, QColor(30, 36, 45, 255)]
            ]

        if Theme == 2:
            self.set_scale_polygon_colors([[.25, Qt.red],
                                           [.5, Qt.yellow],
                                           [.75, Qt.green]])

            self.needle_center_bg = [
                                    [0, QColor(35, 40, 3, 255)],
                                    [0.16, QColor(30, 36, 45, 255)],
                                    [0.225, QColor(36, 42, 54, 255)],
                                    [0.423963, QColor(19, 23, 29, 255)],
                                    [0.580645, QColor(45, 53, 68, 255)],
                                    [0.792627, QColor(59, 70, 88, 255)],
                                    [0.935, QColor(30, 35, 45, 255)],
                                    [1, QColor(35, 40, 3, 255)]
            ]

            self.outer_circle_bg = [
                [0.0645161, QColor(30, 35, 45, 255)],
                [0.37788, QColor(57, 67, 86, 255)],
                [1, QColor(30, 36, 45, 255)]
            ]

        elif Theme == 3:
            self.set_scale_polygon_colors([[.00, Qt.white]])

            self.needle_center_bg = [
                                    [0, Qt.white],
            ]

            self.outer_circle_bg = [
                [0, Qt.white],
            ]

            self.bigScaleMarker = Qt.black
            self.fineScaleColor = Qt.black

        elif Theme == 4:
            self.set_scale_polygon_colors([[1, Qt.black]])

            self.needle_center_bg = [
                                    [0, Qt.black],
            ]

            self.outer_circle_bg = [
                [0, Qt.black],
            ]

            self.bigScaleMarker = Qt.white
            self.fineScaleColor = Qt.white

        elif Theme == 5:
            self.set_scale_polygon_colors([[1, QColor("#029CDE")]])

            self.needle_center_bg = [
                                    [0, QColor("#029CDE")],
            ]

            self.outer_circle_bg = [
                [0, QColor("#029CDE")],
            ]

        elif Theme == 6:
            self.set_scale_polygon_colors([[.75, QColor("#01ADEF")],
                                           [.5, QColor("#0086BF")],
                                           [.25, QColor("#005275")]])

            self.needle_center_bg = [
                                    [0, QColor(0, 46, 61, 255)],
                                    [0.322581, QColor(1, 173, 239, 255)],
                                    [0.571429, QColor(0, 73, 99, 255)],
                                    [1, QColor(0, 46, 61, 255)]
            ]

            self.outer_circle_bg = [
                [0.0645161, QColor(0, 85, 116, 255)],
                [0.37788, QColor(1, 173, 239, 255)],
                [1, QColor(0, 69, 94, 255)]
            ]

            self.bigScaleMarker = Qt.black
            self.fineScaleColor = Qt.black

        elif Theme == 7:
            self.set_scale_polygon_colors([[.25, QColor("#01ADEF")],
                                           [.5, QColor("#0086BF")],
                                           [.75, QColor("#005275")]])

            self.needle_center_bg = [
                                    [0, QColor(0, 46, 61, 255)],
                                    [0.322581, QColor(1, 173, 239, 255)],
                                    [0.571429, QColor(0, 73, 99, 255)],
                                    [1, QColor(0, 46, 61, 255)]
            ]

            self.outer_circle_bg = [
                [0.0645161, QColor(0, 85, 116, 255)],
                [0.37788, QColor(1, 173, 239, 255)],
                [1, QColor(0, 69, 94, 255)]
            ]

            self.bigScaleMarker = Qt.black
            self.fineScaleColor = Qt.black

        elif Theme == 8:
            self.setCustomGaugeTheme(
                color1="#ffaa00",
                color2="#7d5300",
                color3="#3e2900"
            )

            self.bigScaleMarker = Qt.black
            self.fineScaleColor = Qt.black

        elif Theme == 9:
            self.setCustomGaugeTheme(
                color1="#3e2900",
                color2="#7d5300",
                color3="#ffaa00"
            )

            self.bigScaleMarker = Qt.white
            self.fineScaleColor = Qt.white

        elif Theme == 10:
            self.setCustomGaugeTheme(
                color1="#ff007f",
                color2="#aa0055",
                color3="#830042"
            )

            self.bigScaleMarker = Qt.black
            self.fineScaleColor = Qt.black

        elif Theme == 11:
            self.setCustomGaugeTheme(
                color1="#830042",
                color2="#aa0055",
                color3="#ff007f"
            )

            self.bigScaleMarker = Qt.white
            self.fineScaleColor = Qt.white

        elif Theme == 12:
            self.setCustomGaugeTheme(
                color1="#ffe75d",
                color2="#896c1a",
                color3="#232803"
            )

            self.bigScaleMarker = Qt.black
            self.fineScaleColor = Qt.black

        elif Theme == 13:
            self.setCustomGaugeTheme(
                color1="#ffe75d",
                color2="#896c1a",
                color3="#232803"
            )

            self.bigScaleMarker = Qt.black
            self.fineScaleColor = Qt.black

        elif Theme == 14:
            self.setCustomGaugeTheme(
                color1="#232803",
                color2="#821600",
                color3="#ffe75d"
            )

            self.bigScaleMarker = Qt.white
            self.fineScaleColor = Qt.white

        elif Theme == 15:
            self.setCustomGaugeTheme(
                color1="#00FF11",
                color2="#00990A",
                color3="#002603"
            )

            self.bigScaleMarker = Qt.black
            self.fineScaleColor = Qt.black

        elif Theme == 16:
            self.setCustomGaugeTheme(
                color1="#002603",
                color2="#00990A",
                color3="#00FF11"
            )

            self.bigScaleMarker = Qt.white
            self.fineScaleColor = Qt.white

        elif Theme == 17:
            self.setCustomGaugeTheme(
                color1="#00FFCC",
                color2="#00876C",
                color3="#00211B"
            )

            self.bigScaleMarker = Qt.black
            self.fineScaleColor = Qt.black

        elif Theme == 18:
            self.setCustomGaugeTheme(
                color1="#00211B",
                color2="#00876C",
                color3="#00FFCC"
            )

            self.bigScaleMarker = Qt.white
            self.fineScaleColor = Qt.white

        elif Theme == 19:
            self.setCustomGaugeTheme(
                color1="#001EFF",
                color2="#001299",
                color3="#000426"
            )

            self.bigScaleMarker = Qt.black
            self.fineScaleColor = Qt.black

        elif Theme == 20:
            self.setCustomGaugeTheme(
                color1="#000426",
                color2="#001299",
                color3="#001EFF"
            )

            self.bigScaleMarker = Qt.white
            self.fineScaleColor = Qt.white

        elif Theme == 21:
            self.setCustomGaugeTheme(
                color1="#F200FF",
                color2="#85008C",
                color3="#240026"
            )

            self.bigScaleMarker = Qt.black
            self.fineScaleColor = Qt.black

        elif Theme == 22:
            self.setCustomGaugeTheme(
                color1="#240026",
                color2="#85008C",
                color3="#F200FF"
            )

            self.bigScaleMarker = Qt.white
            self.fineScaleColor = Qt.white

        elif Theme == 23:
            self.setCustomGaugeTheme(
                color1="#FF0022",
                color2="#080001",
                color3="#009991"
            )

            self.bigScaleMarker = Qt.white
            self.fineScaleColor = Qt.white

        elif Theme == 24:
            self.setCustomGaugeTheme(
                color1="#009991",
                color2="#080001",
                color3="#FF0022"
            )

            self.bigScaleMarker = Qt.white
            self.fineScaleColor = Qt.white

    # SET CUSTOM GAUGE THEME
    def setCustomGaugeTheme(self, **colors):
        if "color1" in colors and len(str(colors['color1'])) > 0:
            if "color2" in colors and len(str(colors['color2'])) > 0:
                if "color3" in colors and len(str(colors['color3'])) > 0:

                    self.set_scale_polygon_colors([[.25, QColor(str(colors['color1']))],
                                                   [.5, QColor(
                                                       str(colors['color2']))],
                                                   [.75, QColor(str(colors['color3']))]])

                    self.needle_center_bg = [
                                            [0, QColor(str(colors['color3']))],
                                            [0.322581, QColor(
                                                str(colors['color1']))],
                                            [0.571429, QColor(
                                                str(colors['color2']))],
                                            [1, QColor(str(colors['color3']))]
                    ]

                    self.outer_circle_bg = [
                        [0.0645161, QColor(str(colors['color3']))],
                        [0.36, QColor(
                            str(colors['color1']))],
                        [1, QColor(str(colors['color2']))]
                    ]

                else:

                    self.set_scale_polygon_colors([[.5, QColor(str(colors['color1']))],
                                                   [1, QColor(str(colors['color2']))]])

                    self.needle_center_bg = [
                                            [0, QColor(str(colors['color2']))],
                                            [1, QColor(str(colors['color1']))]
                    ]

                    self.outer_circle_bg = [
                        [0, QColor(str(colors['color2']))],
                        [1, QColor(str(colors['color2']))]
                    ]

            else:

                self.set_scale_polygon_colors(
                    [[1, QColor(str(colors['color1']))]])

                self.needle_center_bg = [
                                        [1, QColor(str(colors['color1']))]
                ]

                self.outer_circle_bg = [
                    [1, QColor(str(colors['color1']))]
                ]

        else:

            self.setGaugeTheme(0)
            print("color1 is not defined")

    # SET SCALE POLYGON COLOR
    def setScalePolygonColor(self, **colors):
        if "color1" in colors and len(str(colors['color1'])) > 0:
            if "color2" in colors and len(str(colors['color2'])) > 0:
                if "color3" in colors and len(str(colors['color3'])) > 0:

                    self.set_scale_polygon_colors([[.25, QColor(str(colors['color1']))],
                                                   [.5, QColor(
                                                       str(colors['color2']))],
                                                   [.75, QColor(str(colors['color3']))]])

                else:

                    self.set_scale_polygon_colors([[.5, QColor(str(colors['color1']))],
                                                   [1, QColor(str(colors['color2']))]])

            else:

                self.set_scale_polygon_colors(
                    [[1, QColor(str(colors['color1']))]])

        else:
            print("color1 is not defined")

    # SET NEEDLE CENTER COLOR
    def setNeedleCenterColor(self, **colors):
        if "color1" in colors and len(str(colors['color1'])) > 0:
            if "color2" in colors and len(str(colors['color2'])) > 0:
                if "color3" in colors and len(str(colors['color3'])) > 0:

                    self.needle_center_bg = [
                                            [0, QColor(str(colors['color3']))],
                                            [0.322581, QColor(
                                                str(colors['color1']))],
                                            [0.571429, QColor(
                                                str(colors['color2']))],
                                            [1, QColor(str(colors['color3']))]
                    ]

                else:

                    self.needle_center_bg = [
                                            [0, QColor(str(colors['color2']))],
                                            [1, QColor(str(colors['color1']))]
                    ]

            else:

                self.needle_center_bg = [
                                        [1, QColor(str(colors['color1']))]
                ]
        else:
            print("color1 is not defined")

    # SET OUTER CIRCLE COLOR
    def setOuterCircleColor(self, **colors):
        if "color1" in colors and len(str(colors['color1'])) > 0:
            if "color2" in colors and len(str(colors['color2'])) > 0:
                if "color3" in colors and len(str(colors['color3'])) > 0:

                    self.outer_circle_bg = [
                        [0.0645161, QColor(str(colors['color3']))],
                        [0.37788, QColor(
                            str(colors['color1']))],
                        [1, QColor(str(colors['color2']))]
                    ]

                else:

                    self.outer_circle_bg = [
                        [0, QColor(str(colors['color2']))],
                        [1, QColor(str(colors['color2']))]
                    ]

            else:

                self.outer_circle_bg = [
                    [1, QColor(str(colors['color1']))]
                ]

        else:
            print("color1 is not defined")

    # RESCALE
    def rescale_method(self):
        # SET WIDTH AND HEIGHT
        if self.width() <= self.height():
            self.widget_diameter = self.width() - self.circle_padding
        else:
            self.widget_diameter = self.height() - self.circle_padding

        y_length = 30
        if self.scale_angle_size == 90:
            y_length = 0
        if self.scale_angle_size == 180:
            y_length = 0

        # SET NEEDLE SIZE
        self.change_value_needle_style([QPolygon([
            # QPoint(4, 30),
            # QPoint(-4, 30),
            QPoint(3, y_length),
            QPoint(-3, y_length),
            QPoint(-2, int(- self.widget_diameter / 2 * self.needle_scale_factor)),
            QPoint(0, int(- self.widget_diameter /
                   2 * self.needle_scale_factor - 6)),
            QPoint(2, int(- self.widget_diameter / 2 * self.needle_scale_factor))
        ])])

        # SET FONT SIZE
        self.scale_fontsize = int(
            self.initial_scale_fontsize * self.widget_diameter / 400)
        self.value_fontsize = int(
            self.initial_value_fontsize * self.widget_diameter / 400)

    def change_value_needle_style(self, design):
        # prepared for multiple needle instrument
        self.value_needle = []
        for i in design:
            self.value_needle.append(i)
        if not self.use_timer_event:
            self.update()

    # UPDATE VALUE
    def updateValue(self, value, inv=False):
        mnewvalue, mmaxval, mminval = value, self.maxValue, self.minValue

        # swap
        if inv:
            mmaxval, mminval = mminval, mmaxval

        if mnewvalue <= mminval:
            self.value = mminval
        elif mnewvalue >= mmaxval:
            self.value = mmaxval
        else:
            self.value = mnewvalue

        self.valueChanged.emit(self.value)

        if not self.use_timer_event:
            self.timer.start(100000)
            self.update()

    def updateAngleOffset(self, offset):
        self.angle_offset = offset
        if not self.use_timer_event:
            self.update()

    def center_horizontal(self, value):
        self.center_horizontal_value = value

    def center_vertical(self, value):
        self.center_vertical_value = value

    def setEnableOuterCircle(self, enable=True):
        self.enable_outer_circle = enable

        if not self.use_timer_event:
            self.update()

    def setEnableOuterHalfCircle(self, enable=False):
        self.enable_outer_half_circle = enable

        if not self.use_timer_event:
            self.update()

    # SET NEEDLE COLOR
    def setNeedleColor(self, R=50, G=50, B=50, Transparency=255):
        self.NeedleColor = QColor(R, G, B, Transparency)
        self.NeedleColorReleased = self.NeedleColor

        if not self.use_timer_event:
            self.update()
    
    # SET NEEDLE COLOR ON DRAG
    def setNeedleColorOnDrag(self, R=50, G=50, B=50, Transparency=255):
        self.NeedleColorDrag = QColor(R, G, B, Transparency)

        if not self.use_timer_event:
            self.update()

    # SET SCALE VALUE COLOR
    def setScaleValueColor(self, R=50, G=50, B=50, Transparency=255):
        self.ScaleValueColor = QColor(R, G, B, Transparency)

        if not self.use_timer_event:
            self.update()

    # SET DISPLAY VALUE COLOR
    def setDisplayValueColor(self, R=50, G=50, B=50, Transparency=255):
        self.DisplayValueColor = QColor(R, G, B, Transparency)

        if not self.use_timer_event:
            self.update()

    # SET CENTER POINTER COLOR
    def set_CenterPointColor(self, R=50, G=50, B=50, Transparency=255):
        self.CenterPointColor = QColor(R, G, B, Transparency)

        if not self.use_timer_event:
            self.update()

    # SHOW HIDE NEEDLE POLYGON
    def setEnableNeedlePolygon(self, enable=True):
        self.enable_Needle_Polygon = enable

        if not self.use_timer_event:
            self.update()

    # SHOW HIDE SCALE TEXT
    def setEnableScaleText(self, enable=True):
        self.enable_scale_text = enable

        if not self.use_timer_event:
            self.update()

    # SHOW HIDE BAR GRAPH
    def setEnableBarGraph(self, enable=True):
        self.enableBarGraph = enable

        if not self.use_timer_event:
            self.update()

    # SHOW HIDE VALUE TEXT
    def setEnableValueText(self, enable=True):
        self.enable_value_text = enable

        if not self.use_timer_event:
            self.update()

    # SHOW HIDE CENTER POINTER
    def setEnableCenterPoint(self, enable=True):
        self.enable_CenterPoint = enable

        if not self.use_timer_event:
            self.update()

    # SHOW HIDE FILLED POLYGON
    def setEnableScalePolygon(self, enable=True):
        self.enable_filled_Polygon = enable

        if not self.use_timer_event:
            self.update()

    # SHOW HIDE BIG SCALE
    def setEnableBigScaleGrid(self, enable=True):
        self.enable_big_scaled_marker = enable

        if not self.use_timer_event:
            self.update()

    # SHOW HIDE FINE SCALE
    def setEnableFineScaleGrid(self, enable=True):
        self.enable_fine_scaled_marker = enable

        if not self.use_timer_event:
            self.update()

    # SHOW INNER VALUE TEXT
    def setEnableInnerValueText(self, enable=True):
        self.enable_inner_value_text = enable

        if not self.use_timer_event:
            self.update()

    # SHOW HIDE SCALA MAIN COUNT
    def setScalaCount(self, count):
        if count < 1:
            count = 1
        self.scalaCount = count

        if not self.use_timer_event:
            self.update()

    # SET MINIMUM VALUE
    def setMinValue(self, min):
        if self.value < min:
            self.value = min
        if min >= self.maxValue:
            self.minValue = self.maxValue - 1
        else:
            self.minValue = min

        if not self.use_timer_event:
            self.update()

    # SET MAXIMUM VALUE
    def setMaxValue(self, max):
        if self.value > max:
            self.value = max
        if max <= self.minValue:
            self.maxValue = self.minValue + 1
        else:
            self.maxValue = max

        if not self.use_timer_event:
            self.update()

    # SET OUTER CIRCLE RADIUS
    def setOuterCircleRadius(self, value):
        self.outer_circle_radius = value

        if not self.use_timer_event:
            self.update()

    # SET SCALE ANGLE
    def setScaleStartAngle(self, value):
        # Value range in DEG: 0 - 360
        self.scale_angle_start_value = value

        if not self.use_timer_event:
            self.update()

    # SET SCALE SIZE
    def setTotalScaleAngleSize(self, value):
        self.scale_angle_size = value

        if not self.use_timer_event:
            self.update()

    # SET GAUGE COLOR OUTER RADIUS
    def setGaugeColorOuterRadiusFactor(self, value):
        self.gauge_color_outer_radius_factor = float(value) / 1000

        if not self.use_timer_event:
            self.update()

    # SET GAUGE COLOR INNER RADIUS
    def setGaugeColorInnerRadiusFactor(self, value):
        self.gauge_color_inner_radius_factor = float(value) / 1000

        if not self.use_timer_event:
            self.update()

    # SET SCALE POLYGON COLOR
    def set_scale_polygon_colors(self, color_array):
        if 'list' in str(type(color_array)):
            self.scale_polygon_colors = color_array
        elif color_array == None:
            self.scale_polygon_colors = [[.0, Qt.transparent]]
        else:
            self.scale_polygon_colors = [[.0, Qt.transparent]]

        if not self.use_timer_event:
            self.update()
            self.update()

    # GET MAXIMUM VALUE
    def get_value_max(self):
        return self.maxValue

    # CREATE PIE
    def create_polygon_pie(self, outer_radius, inner_radius, start, length, bar_graph=True):
        polygon_pie = QPolygonF()
        n = 360     # angle steps size for full circle
        # changing n value will causes drawing issues
        w = 360 / n   # angle per step
        # create outer circle line from "start"-angle to "start + length"-angle
        x = 0
        y = 0

        # todo enable/disable bar graf here
        if not self.enableBarGraph and bar_graph:
            length = int(
                round((length / (self.maxValue - self.minValue)) * (self.value - self.minValue)))

        # add the points of polygon
        for i in range(length + 1):
            t = w * i + start - self.angle_offset
            x = outer_radius * math.cos(math.radians(t))
            y = outer_radius * math.sin(math.radians(t))
            polygon_pie.append(QPointF(x, y))

        # add the points of polygon
        for i in range(length + 1):
            t = w * (length - i) + start - self.angle_offset
            x = inner_radius * math.cos(math.radians(t))
            y = inner_radius * math.sin(math.radians(t))
            polygon_pie.append(QPointF(x, y))

        # close outer line
        polygon_pie.append(QPointF(x, y))
        return polygon_pie

    def draw_filled_polygon(self, outline_pen_with=0):
        if self.scale_polygon_colors is not None:
            painter_filled_polygon = QPainter(self)
            # painter_filled_polygon.setRenderHint(QPainter.Antialiasing)
            painter_filled_polygon.setRenderHint(QPainter.HighQualityAntialiasing)

            painter_filled_polygon.translate(
                self.width() / 2, self.height() / 2)

            painter_filled_polygon.setPen(Qt.NoPen)
            self.pen.setWidth(outline_pen_with)
            if outline_pen_with > 0:
                painter_filled_polygon.setPen(self.pen)

            colored_scale_polygon = self.create_polygon_pie(
                ((self.widget_diameter / 2) - (self.pen.width() / 2)) *
                self.gauge_color_outer_radius_factor,
                (((self.widget_diameter / 2) - (self.pen.width() / 2))
                 * self.gauge_color_inner_radius_factor),
                self.scale_angle_start_value, self.scale_angle_size)

            gauge_rect = QRect(QPoint(0, 0), QSize(
                int(self.widget_diameter / 2 - 1), int(self.widget_diameter - 1)))
            grad = QConicalGradient(QPointF(0, 0), - self.scale_angle_size - self.scale_angle_start_value +
                                    self.angle_offset - 1)

            for eachcolor in self.scale_polygon_colors:
                grad.setColorAt(eachcolor[0], eachcolor[1])

            painter_filled_polygon.setBrush(grad)
            painter_filled_polygon.drawPolygon(colored_scale_polygon)

    # BIG SCALE MARKERS
    def draw_big_scaled_marker(self):
        my_painter = QPainter(self)
        # my_painter.setRenderHint(QPainter.Antialiasing)
        my_painter.setRenderHint(QPainter.HighQualityAntialiasing)

        my_painter.translate(self.width() / 2, self.height() / 2)

        self.pen = QPen(self.bigScaleMarker)
        self.pen.setWidth(2)

        my_painter.setPen(self.pen)

        my_painter.rotate(self.scale_angle_start_value - self.angle_offset)
        steps_size = (float(self.scale_angle_size) / float(self.scalaCount))
        # scale_line_outer_start = self.widget_diameter // 2 - 1
        scale_line_outer_start = self.widget_diameter // 2 + self.scale_length
        scale_line_length = int((self.widget_diameter / 2) -
                                (self.widget_diameter / 20) + 2)

        for i in range(self.scalaCount + 1):
            # if i >= 10:
            #     my_painter.setPen(QPen(Qt.red, 2))
            my_painter.drawLine(scale_line_length, 0,
                                scale_line_outer_start, 0)
            my_painter.rotate(steps_size)

    def create_scale_marker_values_text(self):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.HighQualityAntialiasing)
        # painter.setRenderHint(QPainter.Antialiasing)

        painter.translate(self.width() / 2, self.height() / 2)

        font = QFont(self.scale_fontname, self.scale_fontsize, QFont.Bold)
        fm = QFontMetrics(font)

        pen_shadow = QPen()

        pen_shadow.setBrush(self.ScaleValueColor)
        painter.setPen(pen_shadow)

        text_radius_factor = 0.8

        if not self.enable_inner_value_text:
            text_radius_factor = 1.235

        text_radius = self.widget_diameter / 2 * text_radius_factor

        scale_per_div = int((self.maxValue - self.minValue) / self.scalaCount)

        angle_distance = (float(self.scale_angle_size) /
                          float(self.scalaCount))
        for i in range(self.scalaCount + 1):
            text = str(int(self.minValue + scale_per_div * i))
            w = fm.width(text) + 1
            h = fm.height()
            painter.setFont(QFont(self.scale_fontname,
                            self.scale_fontsize, QFont.Bold))
            angle = angle_distance * i + \
                float(self.scale_angle_start_value - self.angle_offset)
            x = text_radius * math.cos(math.radians(angle))
            y = text_radius * math.sin(math.radians(angle))

            painter.drawText(int(x - w / 2), int(y - h / 2), int(w),
                             int(h), Qt.AlignCenter, text)

    # FINE SCALE MARKERS
    def create_fine_scaled_marker(self):
        my_painter = QPainter(self)

        my_painter.setRenderHint(QPainter.Antialiasing)
        # my_painter.setRenderHint(QPainter.HighQualityAntialiasing)

        my_painter.translate(self.width() / 2, self.height() / 2)

        my_painter.setPen(QPen(self.fineScaleColor, 1))
        my_painter.rotate(self.scale_angle_start_value - self.angle_offset)
        steps_size = (float(self.scale_angle_size) /
                      float(self.scalaCount * self.scala_subdiv_count))
        scale_line_outer_start = self.widget_diameter // 2 + self.scale_length
        # scale_line_outer_start = self.widget_diameter // 2 - 1
        scale_line_length = int(
            (self.widget_diameter / 2) - (self.widget_diameter / 40))
        for i in range((self.scalaCount * self.scala_subdiv_count) + 1):
            my_painter.drawLine(scale_line_length, 0,
                                scale_line_outer_start, 0)
            my_painter.rotate(steps_size)

    # VALUE TEXT
    def create_values_text(self):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.HighQualityAntialiasing)

        painter.translate(self.width() / 2, self.height() / 2)

        font = QFont(self.value_fontname, self.value_fontsize, QFont.Bold)
        fm = QFontMetrics(font)

        pen_shadow = QPen()

        pen_shadow.setBrush(self.DisplayValueColor)
        painter.setPen(pen_shadow)

        text_radius = self.widget_diameter / 2 * self.text_radius_factor

        text = str(int(self.value))
        w = fm.width(text) + 1
        h = fm.height()
        painter.setFont(QFont(self.value_fontname,
                        self.value_fontsize, QFont.Bold))

        angle_end = float(self.scale_angle_start_value +
                          self.scale_angle_size - 360)
        angle = (angle_end - self.scale_angle_start_value) / \
            2 + self.scale_angle_start_value

        x = text_radius * math.cos(math.radians(angle))
        y = text_radius * math.sin(math.radians(angle))
        # print(w, h, x, y, text)
        painter.drawText(int(x - w / 2), int(y - h / 2), int(w),
                         int(h), Qt.AlignCenter, text)

    # UNITS TEXT
    def create_units_text(self):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.HighQualityAntialiasing)
        # painter.setRenderHint(QPainter.Antialiasing)

        painter.translate(self.width() / 2, self.height() / 2)
        font = QFont(self.value_fontname, int(
            self.value_fontsize / 1.5), QFont.Bold)
        fm = QFontMetrics(font)

        pen_shadow = QPen()

        pen_shadow.setBrush(self.DisplayValueColor)
        painter.setPen(pen_shadow)

        text_radius = self.widget_diameter / 2 * self.text_radius_factor

        text = str(self.units)
        w = fm.width(text) + 1
        h = fm.height()
        painter.setFont(QFont(self.value_fontname, int(
            self.value_fontsize / 2.5), QFont.Bold))

        angle_end = float(self.scale_angle_start_value +
                          self.scale_angle_size + 180)
        angle = (angle_end - self.scale_angle_start_value) / \
            2 + self.scale_angle_start_value

        x = text_radius * math.cos(math.radians(angle))
        y = text_radius * math.sin(math.radians(angle))
        # print(w, h, x, y, text)
        painter.drawText(int(x - w / 2), int(y - h / 2), int(w), int(h), Qt.AlignCenter, text)

    # CENTER POINTER
    def draw_big_needle_center_point(self, diameter=30):
        painter = QPainter(self)
        # painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.HighQualityAntialiasing)

        painter.translate(self.width() / 2, self.height() / 2)
        painter.setPen(Qt.NoPen)

        colored_scale_polygon = self.create_polygon_pie(
            ((self.widget_diameter / 10) - (self.pen.width() / 2)),
            0,
            self.scale_angle_start_value, 360, False)

        grad = QConicalGradient(QPointF(0, 0), 0)

        # todo definition scale color as array here
        for eachcolor in self.needle_center_bg:
            grad.setColorAt(eachcolor[0], eachcolor[1])
        painter.setBrush(grad)
        painter.drawPolygon(colored_scale_polygon)
        # return painter_filled_polygon

    def draw_outer_circle(self):
        painter = QPainter(self)
        # painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.HighQualityAntialiasing)

        painter.translate(self.width() / 2, self.height() / 2)
        painter.setPen(QPen(Qt.white, 2))
        painter.setBrush(QColor(50, 50, 50, 60))
        # radialGradient = QRadialGradient(QPointF(0, 0), self.width())
        #
        # for eachcolor in self.outer_circle_bg:
        #     radialGradient.setColorAt(eachcolor[0], eachcolor[1])
        #
        # painter.setBrush(radialGradient)

        points = QPolygonF()
        outer = (self.widget_diameter / 2) - (self.pen.width()) + self.outer_circle_radius

        start = 0
        end = 360

        if self.enable_outer_half_circle:
            start = 135
            end = 406

        # for i in range(0, 360):
        for i in range(start, end):
            x = outer * math.cos(math.radians(i))
            y = outer * math.sin(math.radians(i))
            points.append(QPointF(x, y))

        painter.drawPolygon(points)  # 원 그리기

    # CREATE OUTER COVER
    def draw_circle(self, diameter=30):
        painter = QPainter(self)
        # painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.HighQualityAntialiasing)

        painter.translate(self.width() / 2, self.height() / 2)
        painter.setPen(Qt.NoPen)
        colored_scale_polygon = self.create_polygon_pie(
            ((self.widget_diameter / 2) - (self.pen.width())),
            (self.widget_diameter / 6),
            self.scale_angle_start_value / 10, 360, False)

        # radialGradient = QRadialGradient(QPointF(0, 0), self.width())
        #
        # for eachcolor in self.outer_circle_bg:
        #     radialGradient.setColorAt(eachcolor[0], eachcolor[1])

        # painter.setBrush(radialGradient)
        # painter.setBrush(QColor(30, 30, 30))
        painter.drawPolygon(colored_scale_polygon)

    # NEEDLE POINTER
    def draw_needle(self):
        painter = QPainter(self)
        # painter.setRenderHint(QtGui.QPainter.HighQualityAntialiasing)
        # painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.HighQualityAntialiasing)

        painter.translate(self.width() / 2, self.height() / 2)
        painter.setPen(Qt.NoPen)
        painter.setBrush(self.NeedleColor)
        painter.rotate(((self.value - self.value_offset - self.minValue) * self.scale_angle_size /
                        (self.maxValue - self.minValue)) + 90 + self.scale_angle_start_value)

        painter.drawConvexPolygon(self.value_needle[0])

    # EVENTS
    # ON WINDOW RESIZE
    def resizeEvent(self, event):
        self.rescale_method()

    # ON PAINT EVENT
    def paintEvent(self, event):
        if self.enable_outer_circle:
            self.draw_outer_circle()

        self.draw_circle()

        # colored pie area
        if self.enable_filled_Polygon:
            self.draw_filled_polygon()

        # draw scale marker lines
        if self.enable_fine_scaled_marker:
            self.create_fine_scaled_marker()
        if self.enable_big_scaled_marker:
            self.draw_big_scaled_marker()

        # draw scale marker value text
        if self.enable_scale_text:
            self.create_scale_marker_values_text()

        # Display Value
        if self.enable_value_text:
            self.create_values_text()
            self.create_units_text()

        # draw needle 1
        if self.enable_Needle_Polygon:
            self.draw_needle()

        # Draw Center Point
        if self.enable_CenterPoint:
            self.draw_big_needle_center_point(diameter=int(self.widget_diameter / 6))



# if __name__ == '__main__':
#     app = QApplication([])
#     window = AnalogGaugeWidget()
#     window.show()
#     app.exec_()
