"""
  Copyright 2023 abnoname
  
  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
"""

import open3e.Open3Ecodecs
from open3e.Open3Ecodecs import *

dataIdentifiers = {
    # HMU Führungsgerät Interner CAN-BUS: 1
    # Heat Management Unit 
    "name": "HMU",
    "dids" : 
    {
        256 : None,
        257 : None,
        258 : None,
        259 : None,
        260 : None,
        261 : None,
        262 : None,
        263 : None,
        264 : None,
        265 : None,
        266 : None,
        268 : None,
        271 : None,
        272 : None,
        273 : None,
        274 : None,
        275 : None,
        277 : None,
        278 : None,
        279 : None,
        281 : None,
        282 : None,
        283 : None,
        284 : None,
        286 : None,
        288 : None,
        290 : None,
        318 : None,
        331 : None,
        334 : None,
        335 : None,
        336 : None,
        337 : None,
        360 : None,
        364 : None,
        365 : None,
        373 : None,
        377 : None,
        381 : O3EInt8(4, "CentralHeatingPump"),
        382 : None,
        386 : None,
        392 : None,
        396 : None,
        401 : O3EInt16(5, "MixerOneCircuitPump", signed=True),
        402 : O3EInt16(5, "MixerTwoCircuitPump", signed=True),
        403 : O3EInt16(5, "MixerThreeCircuitPump", signed=True),
        404 : O3EInt16(5, "MixerFourCircuitPump", signed=True),
        405 : None,
        406 : None,
        407 : None,
        408 : None,
        417 : None,
        424 : None,
        426 : None,
        428 : None,
        430 : None,
        432 : None,
        434 : None,
        436 : None,
        438 : None,
        475 : None,
        476 : None,
        477 : None,
        478 : None,
        491 : None,
        497 : None,
        500 : None,
        503 : None,
        504 : RawCodec(10, "DomesticHotWaterSetpointMetaData"),
        505 : None,
        506 : None,
        507 : None,
        508 : None,
        510 : None,
        513 : None,
        514 : None,
        515 : None,
        516 : None,
        517 : None,
        518 : None,
        519 : None,
        520 : None,
        521 : None,
        522 : None,
        524 : None,
        525 : None,
        526 : None,
        527 : None,
        528 : None,
        531 : None,
        534 : None,
        535 : None,
        537 : None,
        538 : None,
        544 : None,
        545 : None,
        548 : None,
        565 : None,
        567 : None,
        568 : None,
        569 : None,
        570 : None,
        572 : None,
        573 : None,
        576 : None,
        580 : None,
        581 : None,
        592 : None,
        593 : None,
        596 : None,
        597 : None,
        600 : None,
        602 : None,
        603 : None,
        604 : None,
        607 : None,
        616 : None,
        618 : None,
        619 : None,
        621 : None,
        622 : None,
        623 : None,
        625 : None,
        627 : RawCodec(12, "CentralHeatingOneCircuitName"),
        628 : RawCodec(12, "CentralHeatingTwoCircuitName"),
        629 : RawCodec(12, "CentralHeatingThreeCircuitName"),
        630 : RawCodec(12, "CentralHeatingFourCircuitName"),
        631 : RawCodec(12, "CentralHeatingFiveCircuitName"),
        632 : RawCodec(12, "CentralHeatingSixCircuitName"),
        633 : RawCodec(12, "CentralHeatingSevenCircuitName"),
        634 : RawCodec(12, "CentralHeatingEightCircuitName"),
        645 : None,
        646 : None,
        647 : None,
        648 : None,
        649 : None,
        650 : None,
        651 : None,
        652 : None,
        653 : None,
        654 : None,
        691 : None,
        692 : None,
        693 : None,
        694 : None,
        695 : None,
        696 : None,
        697 : None,
        726 : None,
        727 : None,
        728 : None,
        729 : None,
        730 : None,
        731 : None,
        732 : None,
        761 : None,
        762 : None,
        763 : None,
        764 : None,
        765 : None,
        766 : None,
        767 : None,
        768 : None,
        769 : None,
        770 : None,
        771 : None,
        772 : None,
        773 : None,
        774 : None,
        775 : None,
        776 : None,
        777 : None,
        778 : None,
        779 : None,
        780 : None,
        781 : None,
        782 : None,
        783 : None,
        784 : None,
        785 : None,
        786 : None,
        787 : None,
        788 : None,
        873 : None,
        874 : O3EInt16(2, "LegionellaProtectionTargetTemperatureSetpoint"),
        875 : None,
        876 : None,
        877 : None,
        878 : None,
        880 : None,
        881 : None,
        882 : None,
        883 : None,
        884 : None,
        885 : None,
        886 : None,
        887 : None,
        896 : None,
        897 : None,
        900 : None,
        901 : None,
        902 : None,
        903 : None,
        906 : None,
        908 : None,
        912 : None,
        915 : None,
        917 : None,
        918 : None,
        919 : None,
        920 : None,
        921 : None,
        924 : None,
        925 : None,
        927 : None,
        928 : None,
        929 : None,
        930 : None,
        931 : None,
        933 : None,
        934 : None,
        935 : None,
        936 : None,
        937 : None,
        938 : None,
        939 : None,
        940 : None,
        950 : None,
        951 : None,
        952 : None,
        953 : None,
        954 : None,
        960 : None,
        961 : O3EInt8(1, "SecurityAlgorithmNumber"),
        962 : None,
        964 : None,
        987 : None,
        988 : None,
        989 : None,
        990 : None,
        1004 : None,
        1006 : RawCodec(3, "TargetQuickMode"),
        1007 : RawCodec(3, "CurrentQuickMode"),
        1008 : RawCodec(3, "MixerOneCircuitTargetQuickMode"),
        1009 : RawCodec(3, "MixerTwoCircuitTargetQuickMode"),
        1010 : RawCodec(3, "MixerThreeCircuitTargetQuickMode"),
        1011 : RawCodec(3, "MixerFourCircuitTargetQuickMode"),
        1024 : RawCodec(3, "MixerOneCircuitCurrentQuickMode"),
        1025 : RawCodec(3, "MixerTwoCircuitCurrentQuickMode"),
        1026 : RawCodec(3, "MixerThreeCircuitCurrentQuickMode"),
        1027 : RawCodec(3, "MixerFourCircuitCurrentQuickMode"),
        1042 : None,
        1043 : None,
        1044 : None,
        1047 : None,
        1084 : None,
        1085 : None,
        1087 : None,
        1093 : None,
        1096 : None,
        1097 : RawCodec(16, "ElectricityPrice"),
        1098 : None,
        1100 : None,
        1101 : None,
        1102 : None,
        1103 : None,
        1104 : None,
        1105 : None,
        1118 : None,
        1125 : None,
        1128 : None,
        1136 : None,
        1138 : None,
        1139 : None,
        1165 : None,
        1166 : None,
        1167 : None,
        1172 : None,
        1175 : None,
        1176 : None,
        1177 : None,
        1178 : None,
        1190 : None,
        1191 : None,
        1192 : None,
        1193 : None,
        1194 : None,
        1195 : None,
        1196 : None,
        1197 : None,
        1198 : None,
        1199 : None,
        1210 : None,
        1211 : None,
        1214 : None,
        1215 : None,
        1216 : None,
        1217 : None,
        1218 : None,
        1220 : None,
        1221 : None,
        1222 : None,
        1223 : None,
        1224 : None,
        1226 : None,
        1227 : None,
        1228 : None,
        1229 : None,
        1230 : None,
        1231 : None,
        1232 : None,
        1233 : None,
        1234 : None,
        1235 : None,
        1236 : None,
        1237 : None,
        1238 : None,
        1239 : None,
        1240 : None,
        1263 : None,
        1264 : None,
        1265 : None,
        1266 : None,
        1286 : None,
        1287 : None,
        1288 : None,
        1289 : None,
        1290 : None,
        1294 : None,
        1311 : None,
        1313 : None,
        1314 : None,
        1315 : None,
        1316 : None,
        1333 : None,
        1335 : None,
        1336 : None,
        1337 : None,
        1339 : None,
        1340 : None,
        1341 : None,
        1342 : None,
        1343 : None,
        1344 : None,
        1345 : None,
        1346 : None,
        1347 : None,
        1348 : None,
        1349 : None,
        1350 : None,
        1351 : None,
        1352 : None,
        1353 : None,
        1354 : None,
        1355 : None,
        1356 : None,
        1357 : None,
        1358 : None,
        1359 : None,
        1360 : None,
        1361 : None,
        1362 : None,
        1363 : None,
        1364 : None,
        1367 : None,
        1371 : None,
        1372 : None,
        1373 : None,
        1383 : None,
        1384 : None,
        1385 : None,
        1389 : None,
        1390 : None,
        1391 : None,
        1392 : None,
        1393 : None,
        1394 : None,
        1395 : None,
        1396 : None,
        1397 : None,
        1398 : None,
        1411 : None,
        1415 : None,
        1416 : None,
        1417 : None,
        1418 : None,
        1419 : None,
        1420 : None,
        1421 : None,
        1422 : None,
        1431 : None,
        1432 : None,
        1434 : None,
        1435 : None,
        1436 : None,
        1467 : None,
        1468 : None,
        1469 : None,
        1470 : None,
        1471 : None,
        1472 : None,
        1473 : None,
        1492 : None,
        1493 : None,
        1494 : None,
        1503 : None,
        1504 : None,
        1505 : None,
        1529 : None,
        1533 : None,
        1535 : None,
        1536 : None,
        1537 : None,
        1538 : None,
        1539 : None,
        1540 : None,
        1541 : None,
        1549 : None,
        1550 : None,
        1551 : None,
        1553 : None,
        1554 : None,
        1555 : None,
        1556 : None,
        1557 : None,
        1558 : None,
        1559 : None,
        1560 : None,
        1561 : None,
        1562 : None,
        1573 : None,
        1585 : None,
        1593 : None,
        1594 : None,
        1595 : None,
        1596 : None,
        1598 : None,
        1599 : None,
        1600 : None,
        1601 : None,
        1604 : None,
        1605 : None,
        1606 : None,
        1608 : None,
        1609 : None,
        1610 : None,
        1611 : None,
        1612 : None,
        1613 : None,
        1614 : None,
        1627 : None,
        1628 : None,
        1629 : None,
        1630 : None,
        1643 : None,
        1644 : None,
        1645 : None,
        1646 : None,
        1659 : None,
        1660 : None,
        1661 : None,
        1662 : None,
        1663 : None,
        1667 : None,
        1668 : None,
        1669 : None,
        1670 : None,
        1694 : None,
        1695 : None,
        1696 : None,
        1697 : None,
        1706 : None,
        1719 : None,
        1721 : None,
        1728 : None,
        1729 : None,
        1730 : None,
        1731 : None,
        1732 : None,
        1749 : None,
        1750 : None,
        1751 : None,
        1752 : None,
        1753 : None,
        1754 : None,
        1759 : None,
        1760 : None,
        1761 : None,
        1762 : None,
        1763 : None,
        1764 : None,
        1765 : None,
        1777 : None,
        1778 : None,
        1779 : None,
        1780 : None,
        1781 : None,
        1782 : None,
        1783 : None,
        1784 : None,
        1785 : None,
        1786 : None,
        1787 : None,
        1788 : None,
        1791 : None,
        1792 : None,
        1793 : None,
        1794 : None,
        1795 : None,
        1796 : None,
        1797 : None,
        1798 : None,
        1799 : None,
        1800 : None,
        2158 : None,
        2166 : None,
        2167 : None,
        2168 : None,
        2169 : None,
        2229 : None,
        2230 : None,
        2231 : None,
        2235 : None,
        2236 : None,
        2237 : None,
        2241 : None,
        2257 : None,
        2320 : None,
        2337 : None,
        2338 : None,
        2339 : None,
        2344 : None,
        2353 : None,
        2382 : None,
        2426 : None,
        2427 : None,
        2428 : None,
        2429 : None,
        2445 : None,
        2446 : None,
        2449 : None,
        2450 : None,
        2451 : None,
        2457 : None,
        2458 : None,
        2459 : None,
        2460 : None,
        2461 : None,
        2462 : None,
        2463 : None,
        2464 : None,
        2465 : None,
        2466 : None,
        2467 : None,
        2468 : None,
        2469 : None,
        2470 : None,
        2471 : None,
        2472 : None,
        2473 : None,
        2474 : None,
        2475 : None,
        2490 : None,
        2491 : None,
        2497 : None,
        2534 : None,
        2535 : None,
        2536 : None,
        2551 : None,
        2552 : None,
        2553 : None,
        2564 : None,
        2576 : None,
        2577 : None,
        2583 : None,
        2584 : None,
        2635 : None,
        2636 : None,
        2637 : None,
        2758 : None,
        2777 : RawCodec(6, "PrimaryBootLoaderVersion"),
        2778 : None,
        2779 : None,
        2780 : None,
        2809 : None,
        2810 : None,
        2826 : None,
        2827 : None,
        2828 : None,
        2830 : None,
        2855 : None,
        2856 : None,
        2857 : None,
        2858 : None,
        2937 : None,
        2938 : None,
    }
}
