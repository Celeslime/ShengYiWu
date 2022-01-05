from matplotlib import pyplot as plt
import numpy as np
K= np.array([0.000000,0.010000,0.020000,0.030000,0.040000,0.050000,0.060000,0.070000,0.080000,0.090000,0.100000,0.110000,0.120000,0.130000,0.140000,0.150000,0.160000,0.170000,0.180000,0.190000,0.200000,0.210000,0.220000,0.230000,0.240000,0.250000,0.260000,0.270000,0.280000,0.290000,0.300000,0.310000,0.320000,0.330000,0.340000,0.350000,0.360000,0.370000,0.380000,0.390000,0.400000,0.410000,0.420000,0.430000,0.440000,0.450000,0.460000,0.470000,0.480000,0.490000,0.500000,0.510000,0.520000,0.530000,0.540000,0.550000,0.560000,0.570000,0.580000,0.590000,0.600000,0.610000,0.620000,0.630000,0.640000,0.650000,0.660000,0.670000,0.680000,0.690000,0.700000,0.710000,0.720000,0.730000,0.740000,0.750000,0.760000,0.770000,0.780000,0.790000,0.800000,0.810000,0.820000,0.830000,0.840000,0.850000,0.860000,0.870000,0.880000,0.890000,0.900000,0.910000,0.920000,0.930000,0.940000,0.950000,0.960000,0.970000,0.980000,0.990000,1.000000,1.010000,1.020000,1.030000,1.040000,1.050000,1.060000,1.070000,1.080000,1.090000,1.100000,1.110000,1.120000,1.130000,1.140000,1.150000,1.160000,1.170000,1.180000,1.190000,1.200000,1.210000,1.220000,1.230000,1.240000,1.250000,1.260000,1.270000,1.280000,1.290000,1.300000,1.310000,1.320000,1.330000,1.340000,1.350000,1.360000,1.370000,1.380000,1.390000,1.400000,1.410000,1.420000,1.430000,1.440000,1.450000,1.460000,1.470000,1.480000,1.490000,1.500000,1.510000,1.520000,1.530000,1.540000,1.550000,1.560000,1.570000,1.580000,1.590000,1.600000,1.610000,1.620000,1.630000,1.640000,1.650000,1.660000,1.670000,1.680000,1.690000,1.700000,1.710000,1.720000,1.730000,1.740000,1.750000,1.760000,1.770000,1.780000,1.790000,1.800000,1.810000,1.820000,1.830000,1.840000,1.850000,1.860000,1.870000,1.880000,1.890000,1.900000,1.910000,1.920000,1.930000,1.940000,1.950000,1.960000,1.970000,1.980000,1.990000,2.000000,2.010000,2.020000,2.030000,2.040000,2.050000,2.060000,2.070000,2.080000,2.090000,2.100000,2.110000,2.120000,2.130000,2.140000,2.150000,2.160000,2.170000,2.180000,2.190000,2.200000,2.210000,2.220000,2.230000,2.240000,2.250000,2.260000,2.270000,2.280000,2.290000,2.300000,2.310000,2.320000,2.330000,2.340000,2.350000,2.360000,2.370000,2.380000,2.390000,2.400000,2.410000,2.420000,2.430000,2.440000,2.450000,2.460000,2.470000,2.480000,2.490000,2.500000,2.510000,2.520000,2.530000,2.540000,2.550000,2.560000,2.570000,2.580000,2.590000,2.600000,2.610000,2.620000,2.630000,2.640000,2.650000,2.660000,2.670000,2.680000,2.690000,2.700000,2.710000,2.720000,2.730000,2.740000,2.750000,2.760000,2.770000,2.780000,2.790000,2.800000,2.810000,2.820000,2.830000,2.840000,2.850000,2.860000,2.870000,2.880000,2.890000,2.900000,2.910000,2.920000,2.930000,2.940000,2.950000,2.960000,2.970000,2.980000,2.990000,3.000000,3.010000,3.020000,3.030000,3.040000,3.050000,3.060000,3.070000,3.080000,3.090000,3.100000,3.110000,3.120000,3.130000,3.140000,3.150000,3.160000,3.170000,3.180000,3.190000,3.200000,3.210000,3.220000,3.230000,3.240000,3.250000,3.260000,3.270000,3.280000,3.290000,3.300000,3.310000,3.320000,3.330000,3.340000,3.350000,3.360000,3.370000,3.380000,3.390000,3.400000,3.410000,3.420000,3.430000,3.440000,3.450000,3.460000,3.470000,3.480000,3.490000,3.500000,3.510000,3.520000,3.530000,3.540000,3.550000,3.560000,3.570000,3.580000,3.590000,3.600000,3.610000,3.620000,3.630000,3.640000,3.650000,3.660000,3.670000,3.680000,3.690000,3.700000,3.710000,3.720000,3.730000,3.740000,3.750000,3.760000,3.770000,3.780000,3.790000,3.800000,3.810000,3.820000,3.830000,3.840000,3.850000,3.860000,3.870000,3.880000,3.890000,3.900000,3.910000,3.920000,3.930000,3.940000,3.950000,3.960000,3.970000,3.980000,3.990000,4.000000,4.010000,4.020000,4.030000,4.040000,4.050000,4.060000,4.070000,4.080000,4.090000,4.100000,4.110000,4.120000,4.130000,4.140000,4.150000,4.160000,4.170000,4.180000,4.190000,4.200000,4.210000,4.220000,4.230000,4.240000,4.250000,4.260000,4.270000,4.280000,4.290000,4.300000,4.310000,4.320000,4.330000,4.340000,4.350000,4.360000,4.370000,4.380000,4.390000,4.400000,4.410000,4.420000,4.430000,4.440000,4.450000,4.460000,4.470000,4.480000,4.490000,4.500000,4.510000,4.520000,4.530000,4.540000,4.550000,4.560000,4.570000,4.580000,4.590000,4.600000,4.610000,4.620000,4.630000,4.640000,4.650000,4.660000,4.670000,4.680000,4.690000,4.700000,4.710000,4.720000,4.730000,4.740000,4.750000,4.760000,4.770000,4.780000,4.790000,4.800000,4.810000,4.820000,4.830000,4.840000,4.850000,4.860000,4.870000,4.880000,4.890000,4.900000,4.910000,4.920000,4.930000,4.940000,4.950000,4.960000,4.970000,4.980000,4.990000,5.000000,5.010000,5.020000,5.030000,5.040000,5.050000,5.060000,5.070000,5.080000,5.090000,5.100000,5.110000,5.120000,5.130000,5.140000,5.150000,5.160000,5.170000,5.180000,5.190000,5.200000,5.210000,5.220000,5.230000,5.240000,5.250000,5.260000,5.270000,5.280000,5.290000,5.300000,5.310000,5.320000,5.330000,5.340000,5.350000,5.360000,5.370000,5.380000,5.390000,5.400000,5.410000,5.420000,5.430000,5.440000,5.450000,5.460000,5.470000,5.480000,5.490000,5.500000,5.510000,5.520000,5.530000,5.540000,5.550000,5.560000,5.570000,5.580000,5.590000,5.600000,5.610000,5.620000,5.630000,5.640000,5.650000,5.660000,5.670000,5.680000,5.690000,5.700000,5.710000,5.720000,5.730000,5.740000,5.750000,5.760000,5.770000,5.780000,5.790000,5.800000,5.810000,5.820000,5.830000,5.840000,5.850000,5.860000,5.870000,5.880000,5.890000,5.900000,5.910000,5.920000,5.930000,5.940000,5.950000,5.960000,5.970000,5.980000,5.990000,6.000000,6.010000,6.020000,6.030000,6.040000,6.050000,6.060000,6.070000,6.080000,6.090000,6.100000,6.110000,6.120000,6.130000,6.140000,6.150000,6.160000,6.170000,6.180000,6.190000,6.200000,6.210000,6.220000,6.230000,6.240000,6.250000,6.260000,6.270000,6.280000,6.290000,6.300000,6.310000,6.320000,6.330000,6.340000,6.350000,6.360000,6.370000,6.380000,6.390000,6.400000,6.410000,6.420000,6.430000,6.440000,6.450000,6.460000,6.470000,6.480000,6.490000,6.500000,6.510000,6.520000,6.530000,6.540000,6.550000,6.560000,6.570000,6.580000,6.590000,6.600000,6.610000,6.620000,6.630000,6.640000,6.650000,6.660000,6.670000,6.680000,6.690000,6.700000,6.710000,6.720000,6.730000,6.740000,6.750000,6.760000,6.770000,6.780000,6.790000,6.800000,6.810000,6.820000,6.830000,6.840000,6.850000,6.860000,6.870000,6.880000,6.890000,6.900000,6.910000,6.920000,6.930000,6.940000,6.950000,6.960000,6.970000,6.980000,6.990000,])

X= np.array([988.000000,991.103560,994.207120,997.310680,1000.414240,1003.517800,1006.621360,1009.724920,1012.828480,1015.932040,1019.035600,1022.139160,1025.242720,1028.346280,1031.449840,1034.553400,1037.656960,1040.760520,1043.864080,1046.967640,1050.071200,1053.174760,1056.278320,1059.381880,1062.485440,1065.589000,1068.692560,1071.796120,1074.899680,1078.003240,1081.106800,1084.210360,1087.313920,1090.417480,1093.521040,1096.624600,1099.728160,1102.831720,1105.935280,1109.038840,1112.142400,1115.245960,1118.349520,1121.453080,1124.556640,1127.660200,1130.763760,1133.867320,1136.970880,1140.074440,1143.178000,1146.281560,1149.385120,1152.488680,1155.592240,1158.695800,1161.799360,1164.902920,1168.006480,1171.110040,1174.213600,1177.317160,1180.420720,1183.524280,1186.627840,1189.731400,1192.834960,1195.938520,1199.042080,1202.145640,1205.249200,1208.352760,1211.456320,1214.559880,1217.663440,1220.767000,1223.870560,1226.974120,1230.077680,1233.181240,1236.284800,1239.388360,1242.491920,1245.595480,1248.699040,1251.802600,1254.906160,1258.009720,1261.113280,1264.216840,1267.320400,1270.423960,1273.527520,1276.631080,1279.734640,1282.838200,1285.941760,1289.045320,1292.148880,1295.252440,1298.356000,1301.459560,1304.563120,1307.666680,1310.770240,1313.873800,1316.977360,1320.080920,1323.184480,1326.288040,1329.391600,1332.495160,1335.598720,1338.702280,1341.805840,1344.909400,1348.012960,1351.116520,1354.220080,1357.323640,1360.427200,1363.530760,1366.634320,1369.737880,1372.841440,1375.945000,1379.048560,1382.152120,1385.255680,1388.359240,1391.462800,1394.566360,1397.669920,1400.773480,1403.877040,1406.980600,1410.084160,1413.187720,1416.291280,1419.394840,1422.498400,1425.601960,1428.705520,1431.809080,1434.912640,1438.016200,1441.119760,1444.223320,1447.326880,1450.430440,1453.534000,1456.637560,1459.741120,1462.844680,1465.948240,1469.051800,1472.155360,1475.258920,1478.362480,1481.466040,1484.569600,1487.673160,1490.776720,1493.880280,1496.983840,1500.087400,1503.190960,1506.294520,1509.398080,1512.501640,1515.605200,1518.708760,1521.812320,1524.915880,1528.019440,1531.123000,1534.226560,1537.330120,1540.433680,1543.537240,1546.640800,1549.744360,1552.847920,1555.951480,1559.055040,1562.158600,1565.262160,1568.365720,1571.469280,1574.572840,1577.676400,1580.779960,1583.883520,1586.987080,1590.090640,1593.194200,1596.297760,1599.401320,1602.504880,1605.608440,1608.712000,1611.815560,1614.919120,1618.022680,1621.126240,1624.229800,1627.333360,1630.436920,1633.540480,1636.644040,1639.747600,1642.851160,1645.954720,1649.058280,1652.161840,1655.265400,1658.368960,1661.472520,1664.576080,1667.679640,1670.783200,1673.886760,1676.990320,1680.093880,1683.197440,1686.301000,1689.404560,1692.508120,1695.611680,1698.715240,1701.818800,1704.922360,1708.025920,1711.129480,1714.233040,1717.336600,1720.440160,1723.543720,1726.647280,1729.750840,1732.854400,1735.957960,1739.061520,1742.165080,1745.268640,1748.372200,1751.475760,1754.579320,1757.682880,1760.786440,1763.890000,1766.993560,1770.097120,1773.200680,1776.304240,1779.407800,1782.511360,1785.614920,1788.718480,1791.822040,1794.925600,1798.029160,1801.132720,1804.236280,1807.339840,1810.443400,1813.546960,1816.650520,1819.754080,1822.857640,1825.961200,1829.064760,1832.168320,1835.271880,1838.375440,1841.479000,1844.582560,1847.686120,1850.789680,1853.893240,1856.996800,1860.100360,1863.203920,1866.307480,1869.411040,1872.514600,1875.618160,1878.721720,1881.825280,1884.928840,1888.032400,1891.135960,1894.239520,1897.343080,1900.446640,1903.550200,1906.653760,1909.757320,1912.860880,1915.964440,1919.068000,1922.171560,1925.275120,1928.378680,1931.482240,1934.585800,1937.689360,1940.792920,1943.896480,1947.000040,1950.103600,1953.207160,1956.310720,1959.414280,1962.517840,1965.621400,1968.724960,1971.828520,1974.932080,1978.035640,1981.139200,1984.242760,1987.346320,1990.449880,1993.553440,1996.657000,1999.760560,2002.864120,2005.967680,2009.071240,2012.174800,2015.278360,2018.381920,2021.485480,2024.589040,2027.692600,2030.796160,2033.899720,2037.003280,2040.106840,2043.210400,2045.784803,2047.825394,2049.327517,2050.820329,2052.303831,2053.778022,2055.242902,2056.698472,2058.686302,2060.124802,2061.553991,2062.973870,2064.384438,2066.335026,2067.728524,2069.112712,2071.041574,2072.408692,2073.766500,2075.673638,2077.014376,2078.345803,2080.231215,2081.545573,2083.417020,2084.714308,2086.571789,2087.852007,2089.695522,2090.958671,2092.788219,2094.034299,2095.849881,2097.078891,2098.880507,2100.092448,2101.880098,2103.661542,2104.848653,2106.616131,2108.377401,2109.539684,2111.286989,2113.028086,2114.165540,2115.892672,2117.613596,2118.726222,2120.433180,2122.133931,2123.828475,2124.908513,2126.589091,2128.263462,1480.814292,1478.989399,1475.916875,1474.057842,1472.183292,1469.672512,1467.765374,1465.842719,1463.904546,1462.577774,1460.610117,1459.886987,1457.891398,1455.880291,1454.488345,1453.720214,1451.667209,1450.877353,1448.796416,1447.984835,1446.519954,1445.688200,1444.200043,1443.348116,1442.486878,1441.616330,1440.083171,1439.192449,1438.292417,1437.383074,1435.804913,1434.875397,1433.936570,1433.652595,1432.696698,1431.731491,1430.756973,1430.443514,1429.451926,1428.451028,1428.115844,1427.097876,1426.748725,1425.713688,1426.031803,1424.981248,1424.605717,1423.538093,1423.148596,1422.752892,1422.350981,1421.942863,1420.834892,1421.108005,1419.984516,1419.550018,1419.809165,1419.363804,1418.209280,1418.454461,1417.990479,1416.812678,1417.043893,1416.561290,1416.784746,1416.291280,1416.506977,1415.285727,1414.773639,1414.975371,1414.452421,1414.646393,1414.112581,1414.298794,1413.754120,1413.932574,1414.107926,1413.547733,1413.715325,1412.408726,1413.304103,1411.983539,1412.874260,1412.281480,1412.425796,1412.567008,1411.958710,1412.092163,1412.222513,1411.598697,1411.721288,1411.086610,1411.201442,1411.313170,1410.662974,1411.527315,1411.629733,1411.729047,1411.060230,1411.151785,1411.240236,1411.325584,1411.407828,1411.486969,1410.788668,1410.860050,1411.705770,1411.772497,1411.055574,1411.114542,1411.954055,1412.008367,1411.272823,1411.319377,1412.152683,1412.194581,1412.233375,1412.269066,1412.301654,1412.331137,1413.156684,1413.181513,1412.400968,1413.221859,1413.237377,1413.249791,1414.067579,1413.265309,1413.268413,1414.081545,1414.079993,1414.075338,1414.885367,1414.876057,1414.863642,1414.848125,1414.829503,1415.633325,1415.610049,1416.412319,1416.384387,1415.521597,1416.319212,1416.281969,1417.078032,1417.036134,1417.830646,1417.784092,1418.577052,1418.525843,1418.471531,1418.414115,1418.353596,1419.140348,1419.075173,1419.860374,1419.790544,1420.574193,1420.499707,1421.281804,1421.202664,1421.983209,1421.899413,1421.812513,1421.722510,1422.498400,1423.274290,1423.178080,1423.952418,1423.851552,1424.624339,1424.518818,1425.290052,1425.179876,1425.949559,1425.834727,1426.602858,1427.370989,1427.249950,1428.016530,1427.890835,1428.655863,1428.525514,1429.288989,1429.153984,1429.015876,1429.776248,1429.633484,1430.392305,1431.151125,1431.002154,1431.759423,1431.605797,1432.361514,1433.117231,1432.957397,1433.711562,1434.465727,1434.299687,1435.052300,1434.881604,1435.632666,1436.383727,1436.206825,1436.956334,1437.705844,1437.522734,1438.270692,1439.018650,1438.829333,1439.575739,1440.322145,1440.126621,1440.871475,1441.616330,1441.414598,1442.157901,1442.901203,1443.644506,1444.387809,1444.176767,1444.918517,1445.660268,1446.402019,1446.183218,1446.923417,1447.663616,1447.438608,1448.177255,1448.915903,1449.654550,1449.421783,1450.158878,1450.895974,1450.657000,1451.392544,1452.128087,1452.863631,1452.616898,1453.350890,1454.084882,1454.818874,1454.564382,1455.296822,1456.029262,1456.761702,1457.494143,1458.226583,1457.961228,1458.692117,1459.423005,1460.153893,1460.884782,1460.610117,1461.339453,1462.068790,1462.798127,1462.515703,1463.243487,1463.971272,1464.699057,1464.408874,1465.135107,1465.861340,1466.587573,1467.313806,1468.040039,1468.766272,1469.492506,1469.188357,1469.913038,1470.637719,1471.362400,1472.087082,1471.773622,1472.496752,1473.219881,1473.943011,1474.666140,1474.343370,1476.112399,1476.835528,1477.558658,1477.229681,1477.951258,1478.672836,1479.394414,1480.115991,1479.777703,1480.497729,1481.217755,1481.937781,1482.657807,1483.377833,1484.097859,1484.817885,1485.537911,1486.257937,1485.902579,1486.621053,1487.339527,1488.058001,1488.776476,1489.494950,1489.128730,])
plt.plot(K,X,color='green')
Y= np.array([0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,0.500000,1.034376,1.039423,1.045724,1.050812,1.055919,1.061044,1.066188,1.071351,1.076532,1.080475,1.085691,1.089662,1.094912,1.100180,1.104195,1.108223,1.113541,1.117596,1.122949,1.127032,1.131128,1.135236,1.139357,1.143490,1.147636,1.151794,1.155964,1.160147,1.164343,1.168550,1.172771,1.177003,1.181249,1.184175,1.188442,1.192721,1.197013,1.199974,1.204287,1.208613,1.211599,1.215947,1.218948,1.223318,1.226334,1.230726,1.233758,1.238171,1.241219,1.245654,1.248717,1.251787,1.256252,1.259338,1.263825,1.266926,1.270033,1.273146,1.277674,1.280803,1.283938,1.288497,1.291647,1.294804,1.297967,1.301136,1.304311,1.308930,1.312121,1.315318,1.318521,1.321730,1.324946,1.328168,1.331396,1.334631,1.337871,1.341118,1.344371,1.349105,1.350896,1.355648,1.357446,1.360730,1.364020,1.367317,1.370620,1.373929,1.377244,1.380565,1.383893,1.387227,1.390567,1.393914,1.397266,1.399101,1.402463,1.405831,1.409205,1.412586,1.415973,1.417823,1.421219,1.424622,1.428030,1.431445,1.433308,1.436732,1.440162,1.443599,1.445471,1.448917,1.452369,1.455827,1.457709,1.461177,1.464650,1.466538,1.470021,1.473511,1.475405,1.478904,1.482409,1.484309,1.487823,1.491344,1.493250,1.496780,1.500316,1.502229,1.505774,1.509326,1.511244,1.514805,1.516727,1.520298,1.523874,1.525802,1.529388,1.531320,1.534915,1.538516,1.540454,1.544064,1.546005,1.549625,1.551569,1.555198,1.557145,1.560784,1.564429,1.566382,1.570036,1.571992,1.575656,1.577615,1.581288,1.583250,1.586933,1.588898,1.592590,1.594558,1.598259,1.600231,1.603941,1.605916,1.607891,1.611614,1.613591,1.617323,1.619305,1.623046,1.625030,1.628781,1.630768,1.634528,1.636518,1.638509,1.642281,1.644275,1.648056,1.650053,1.653844,1.655844,1.657844,1.661647,1.663650,1.667463,1.669469,1.671475,1.675300,1.677309,1.681144,1.683156,1.685168,1.689015,1.691030,1.693046,1.696905,1.698924,1.702792,1.704814,1.706835,1.710717,1.712741,1.714766,1.718660,1.720687,1.722715,1.726621,1.728652,1.730683,1.734602,1.736636,1.738669,1.742600,1.744638,1.746675,1.750618,1.752658,1.754698,1.758654,1.760698,1.762741,1.766709,1.768756,1.770802,1.774783,1.776832,1.778882,1.780931,1.784928,1.786980,1.789033,1.793042,1.795097,1.797153,1.799209,1.803233,1.805292,1.807351,1.809410,1.813449,1.815511,1.817573,1.821626,1.823691,1.825756,1.827821,1.831889,1.833957,1.836025,1.838093,1.842176,1.844248,1.846319,1.848390,1.852489,1.854564,1.856638,1.858712,1.862827,1.864904,1.866982,1.869059,1.873189,1.875270,1.877351,1.879431,1.883577,1.885660,1.887744,1.889828,1.891912,1.896076,1.898163,1.900250,1.902336,1.904423,1.908606,1.910696,1.912786,1.914876,1.919074,1.921167,1.923260,1.925353,1.927446,1.931664,1.933760,1.935856,1.937952,1.940048,1.944284,1.946383,1.948482,1.950582,1.952681,1.956935,1.959038,1.961140,1.963243,1.965345,1.967447,1.971724,])
plt.plot(K,1000*Y,color='red')
Z= np.array([0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050000,0.050530,0.051595,0.053200,0.054814,0.056438,0.058070,0.059713,0.061364,0.062482,0.064151,0.065828,0.067516,0.069212,0.070367,0.072081,0.073804,0.074981,0.076721,0.078470,0.079669,0.081436,0.083212,0.084432,0.086225,0.087460,0.089270,0.090519,0.092346,0.093608,0.095453,0.096729,0.098591,0.099881,0.101760,0.103064,0.104960,0.106279,0.107603,0.109524,0.110863,0.112208,0.114153,0.115512,0.116877,0.118848,0.120227,0.121612,0.123607,0.125007,0.126413,0.127825,0.129852,0.131278,0.132710,0.517425,0.519840,0.522879,0.525308,0.527743,0.530806,0.533255,0.535710,0.538172,0.540640,0.543114,0.544963,0.547448,0.549939,0.552436,0.554302,0.556810,0.558684,0.561203,0.563085,0.565615,0.567504,0.570045,0.571942,0.573842,0.575745,0.578307,0.580218,0.582132,0.584049,0.586630,0.588556,0.590484,0.592415,0.594350,0.596287,0.598228,0.600171,0.602118,0.604068,0.606021,0.607978,0.609937,0.611899,0.613182,0.615149,0.617119,0.619093,0.621069,0.622358,0.624339,0.626323,0.628311,0.629604,0.631596,0.633591,0.634888,0.636888,0.638891,0.640191,0.642198,0.644209,0.645512,0.647527,0.648832,0.650852,0.652158,0.654183,0.656211,0.657520,0.659552,0.660863,0.662900,0.664213,0.666254,0.667568,0.668882,0.670930,0.672246,0.674298,0.675615,0.677673,0.678991,0.681053,0.682373,0.683694,0.685762,0.687083,0.688405,0.690480,0.691803,0.693882,0.695207,0.696532,0.698617,0.699943,0.701270,0.702596,0.704689,0.706017,0.707345,0.709444,0.710774,0.712103,0.714209,0.715540,0.716871,0.718202,0.720315,0.721648,0.722981,0.724313,0.726434,0.727769,0.729103,0.730437,0.731771,0.733901,0.735237,0.736573,0.737909,0.739244,0.741384,0.742721,0.744059,0.745396,0.746733,0.748882,0.750221,0.751560,0.752899,0.754238,0.755577,0.756915,0.759077,0.760417,0.761758,0.763098,0.764439,0.765779,0.767119,0.769293,0.770635,0.771977,0.773319,0.774661,0.776003,0.777345,0.778687,0.780029,0.781371,0.783562,0.784905,0.786249,0.787592,0.788936,0.790280,0.791623,0.792967,0.794310,0.795654,0.796997,0.798341,0.800552,0.801897,0.803242,0.804587,0.805932,0.807277,0.808622,0.809967,0.811312,0.812658,0.814003,0.815348,0.816693,0.818038,0.819383,0.820728,0.822073,0.823418,0.824763,0.826108,0.827453,0.829699,0.831045,0.832392,0.833739,0.835085,0.836432,0.837779,0.839125,0.840472,0.841818,0.843165,0.844512,0.845858,0.847205,0.848552,0.849898,0.851245,0.852591,0.853938,0.855285,0.856631,0.857978,0.859325,0.860671,0.862018,0.863365,0.864711,0.866058,0.867404,0.868751,0.870098,0.871444,0.872791,0.874138,0.874531,0.875876,0.878177,0.878566,0.879911,0.881256,0.882601,0.883946,0.885292,0.886637,0.887982,0.889327,0.890672,0.892017,0.893362,0.894707,0.896052,0.897397,0.898742,0.900087,0.901432,0.902778,0.904123,0.905468,0.906813,0.908158,0.909503,0.909853,0.911196,0.912540,0.914883,0.915227,0.916570,0.917914,0.919257,0.920601,0.921944,0.923288,0.924632,0.925975,0.927319,0.928662,0.930006,0.931349,0.932693,0.934036,0.935380,0.935697,0.937039,0.938381,0.939723,0.941065,0.942407,0.943749,0.945091,0.946433,0.947775,0.949117,0.950459,0.951800,0.953142,0.954484,0.954777,0.956117,0.957458,0.958798,0.960138,0.961479,0.962819,0.964160,0.965500,0.966840,0.968181,0.969521,0.970862,0.971132,0.972471,0.973810,0.975149,0.976488,0.977827,0.979165,0.980504,0.981843,0.983182,0.984521,0.985860,])
plt.plot(K,1000*Z,color='blue')
plt.ylim(0,)
plt.show()