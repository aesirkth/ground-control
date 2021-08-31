GENERATED FILE DO NOT EDIT

# fc - Description
## All messages
<table>
<thead>
<tr>
<th>ID</th>
<th>sender</th>
<th>receiver</th>
<th>name</th>
</tr>
</thead>
<tbody>
<tr>
<td>255</td>
<td>local</td>
<td>local</td>
<td>local_timestamp</td>
</tr>
<tr>
<td>16</td>
<td>ground_station</td>
<td>flight_controller</td>
<td>time_sync</td>
</tr>
<tr>
<td>17</td>
<td>ground_station</td>
<td>flight_controller</td>
<td>set_state</td>
</tr>
<tr>
<td>18</td>
<td>ground_station</td>
<td>flight_controller</td>
<td>set_parachute_output</td>
</tr>
<tr>
<td>19</td>
<td>ground_station</td>
<td>flight_controller</td>
<td>set_data_logging</td>
</tr>
<tr>
<td>20</td>
<td>ground_station</td>
<td>flight_controller</td>
<td>dump_flash</td>
</tr>
<tr>
<td>21</td>
<td>ground_station</td>
<td>flight_controller</td>
<td>handshake</td>
</tr>
<tr>
<td>32</td>
<td>flight_controller</td>
<td>ground_station</td>
<td>return_time_sync</td>
</tr>
<tr>
<td>33</td>
<td>flight_controller</td>
<td>ground_station</td>
<td>return_power_mode</td>
</tr>
<tr>
<td>34</td>
<td>flight_controller</td>
<td>ground_station</td>
<td>return_radio_equipment</td>
</tr>
<tr>
<td>35</td>
<td>flight_controller</td>
<td>ground_station</td>
<td>return_parachute_output</td>
</tr>
<tr>
<td>36</td>
<td>flight_controller</td>
<td>ground_station</td>
<td>onboard_battery_voltage</td>
</tr>
<tr>
<td>37</td>
<td>flight_controller</td>
<td>ground_station</td>
<td>return_data_logging</td>
</tr>
<tr>
<td>38</td>
<td>flight_controller</td>
<td>ground_station</td>
<td>return_dump_flash</td>
</tr>
<tr>
<td>39</td>
<td>flight_controller</td>
<td>ground_station</td>
<td>return_handshake</td>
</tr>
<tr>
<td>80</td>
<td>flight_controller</td>
<td>ground_station</td>
<td>ms_since_boot</td>
</tr>
<tr>
<td>81</td>
<td>flight_controller</td>
<td>ground_station</td>
<td>GNSS_data</td>
</tr>
<tr>
<td>82</td>
<td>flight_controller</td>
<td>ground_station</td>
<td>ms_raw</td>
</tr>
<tr>
<td>83</td>
<td>flight_controller</td>
<td>ground_station</td>
<td>bmp_raw</td>
</tr>
<tr>
<td>84</td>
<td>flight_controller</td>
<td>ground_station</td>
<td>imu_raw</td>
</tr>
<tr>
<td>85</td>
<td>flight_controller</td>
<td>ground_station</td>
<td>position</td>
</tr>
<tr>
<td>86</td>
<td>flight_controller</td>
<td>ground_station</td>
<td>differential_pressure</td>
</tr>
</tbody>
</table>

### 255 - local_timestamp <br> local &rarr; local
#### fields
<table>
<thead>
<tr>
<th>name</th>
<th>type</th>
<th>native type</th>
<th>info</th>
</tr>
</thead>
<tbody>
<tr>
<td>timestamp</td>
<td>uint</td>
<td>uint32</td>
<td>N/A</td>
</tr>
</tbody>
</table>

### 16 - time_sync <br> ground_station &rarr; flight_controller
#### fields
<table>
<thead>
<tr>
<th>name</th>
<th>type</th>
<th>native type</th>
<th>info</th>
</tr>
</thead>
<tbody>
<tr>
<td>system_time</td>
<td>uint</td>
<td>uint32</td>
<td>N/A</td>
</tr>
</tbody>
</table>

### 17 - set_state <br> ground_station &rarr; flight_controller
#### fields
<table>
<thead>
<tr>
<th>name</th>
<th>type</th>
<th>native type</th>
<th>info</th>
</tr>
</thead>
<tbody>
<tr>
<td>state</td>
<td>enum</td>
<td>uint8</td>
<td>enum=flight_state</td>
</tr>
</tbody>
</table>

### 18 - set_parachute_output <br> ground_station &rarr; flight_controller
#### bits
<table>
<thead>
<tr>
<th>bit</th>
<th>name</th>
</tr>
</thead>
<tbody>
<tr>
<td>0</td>
<td>is_parachute_armed</td>
</tr>
<tr>
<td>1</td>
<td>is_parachute1_en</td>
</tr>
<tr>
<td>2</td>
<td>is_parachute2_en</td>
</tr>
</tbody>
</table>

### 19 - set_data_logging <br> ground_station &rarr; flight_controller
#### bits
<table>
<thead>
<tr>
<th>bit</th>
<th>name</th>
</tr>
</thead>
<tbody>
<tr>
<td>0</td>
<td>is_logging_en</td>
</tr>
</tbody>
</table>

### 20 - dump_flash <br> ground_station &rarr; flight_controller
#### bits
<table>
<thead>
<tr>
<th>bit</th>
<th>name</th>
</tr>
</thead>
<tbody>
<tr>
<td>0</td>
<td>dump_sd</td>
</tr>
<tr>
<td>1</td>
<td>dump_usb</td>
</tr>
</tbody>
</table>

### 21 - handshake <br> ground_station &rarr; flight_controller
*empty*
### 32 - return_time_sync <br> flight_controller &rarr; ground_station
*empty*
### 33 - return_power_mode <br> flight_controller &rarr; ground_station
*empty*
### 34 - return_radio_equipment <br> flight_controller &rarr; ground_station
#### bits
<table>
<thead>
<tr>
<th>bit</th>
<th>name</th>
</tr>
</thead>
<tbody>
<tr>
<td>0</td>
<td>is_fpv_en</td>
</tr>
<tr>
<td>1</td>
<td>is_tm_en</td>
</tr>
</tbody>
</table>

### 35 - return_parachute_output <br> flight_controller &rarr; ground_station
#### bits
<table>
<thead>
<tr>
<th>bit</th>
<th>name</th>
</tr>
</thead>
<tbody>
<tr>
<td>0</td>
<td>is_parachute_armed</td>
</tr>
<tr>
<td>1</td>
<td>is_parachute1_en</td>
</tr>
<tr>
<td>2</td>
<td>is_parachute2_en</td>
</tr>
</tbody>
</table>

### 36 - onboard_battery_voltage <br> flight_controller &rarr; ground_station
#### fields
<table>
<thead>
<tr>
<th>name</th>
<th>type</th>
<th>native type</th>
<th>info</th>
</tr>
</thead>
<tbody>
<tr>
<td>battery_1</td>
<td>scaledFloat</td>
<td>uint16</td>
<td>scale=100</td>
</tr>
<tr>
<td>battery_2</td>
<td>scaledFloat</td>
<td>uint16</td>
<td>scale=100</td>
</tr>
</tbody>
</table>

### 37 - return_data_logging <br> flight_controller &rarr; ground_station
#### bits
<table>
<thead>
<tr>
<th>bit</th>
<th>name</th>
</tr>
</thead>
<tbody>
<tr>
<td>0</td>
<td>is_logging_en</td>
</tr>
</tbody>
</table>

### 38 - return_dump_flash <br> flight_controller &rarr; ground_station
#### bits
<table>
<thead>
<tr>
<th>bit</th>
<th>name</th>
</tr>
</thead>
<tbody>
<tr>
<td>0</td>
<td>dump_sd</td>
</tr>
<tr>
<td>1</td>
<td>dump_usb</td>
</tr>
</tbody>
</table>

### 39 - return_handshake <br> flight_controller &rarr; ground_station
*empty*
### 80 - ms_since_boot <br> flight_controller &rarr; ground_station
#### fields
<table>
<thead>
<tr>
<th>name</th>
<th>type</th>
<th>native type</th>
<th>info</th>
</tr>
</thead>
<tbody>
<tr>
<td>ms_since_boot</td>
<td>uint</td>
<td>uint32</td>
<td>N/A</td>
</tr>
</tbody>
</table>

### 81 - GNSS_data <br> flight_controller &rarr; ground_station
#### fields
<table>
<thead>
<tr>
<th>name</th>
<th>type</th>
<th>native type</th>
<th>info</th>
</tr>
</thead>
<tbody>
<tr>
<td>gnss_time</td>
<td>float</td>
<td>float</td>
<td>N/A</td>
</tr>
<tr>
<td>altitude</td>
<td>scaledFloat</td>
<td>int32</td>
<td>scale=10</td>
</tr>
<tr>
<td>heading</td>
<td>int</td>
<td>int16</td>
<td>N/A</td>
</tr>
<tr>
<td>horiz_speed</td>
<td>scaledFloat</td>
<td>int16</td>
<td>scale=10</td>
</tr>
<tr>
<td>fix_status</td>
<td>enum</td>
<td>uint8</td>
<td>enum=fix_status</td>
</tr>
<tr>
<td>n_satellites</td>
<td>uint</td>
<td>uint8</td>
<td>N/A</td>
</tr>
<tr>
<td>h_dop</td>
<td>scaledFloat</td>
<td>uint16</td>
<td>scale=10</td>
</tr>
</tbody>
</table>

### 82 - ms_raw <br> flight_controller &rarr; ground_station
#### fields
<table>
<thead>
<tr>
<th>name</th>
<th>type</th>
<th>native type</th>
<th>info</th>
</tr>
</thead>
<tbody>
<tr>
<td>pressure</td>
<td>float</td>
<td>float</td>
<td>N/A</td>
</tr>
<tr>
<td>temperature</td>
<td>float</td>
<td>float</td>
<td>N/A</td>
</tr>
</tbody>
</table>

### 83 - bmp_raw <br> flight_controller &rarr; ground_station
#### fields
<table>
<thead>
<tr>
<th>name</th>
<th>type</th>
<th>native type</th>
<th>info</th>
</tr>
</thead>
<tbody>
<tr>
<td>pressure</td>
<td>float</td>
<td>float</td>
<td>N/A</td>
</tr>
<tr>
<td>temperature</td>
<td>float</td>
<td>float</td>
<td>N/A</td>
</tr>
</tbody>
</table>

### 84 - imu_raw <br> flight_controller &rarr; ground_station
#### fields
<table>
<thead>
<tr>
<th>name</th>
<th>type</th>
<th>native type</th>
<th>info</th>
</tr>
</thead>
<tbody>
<tr>
<td>imu_id</td>
<td>uint</td>
<td>uint8</td>
<td>N/A</td>
</tr>
<tr>
<td>accel_x</td>
<td>float</td>
<td>float</td>
<td>N/A</td>
</tr>
<tr>
<td>accel_y</td>
<td>float</td>
<td>float</td>
<td>N/A</td>
</tr>
<tr>
<td>accel_z</td>
<td>float</td>
<td>float</td>
<td>N/A</td>
</tr>
<tr>
<td>gyro_x</td>
<td>float</td>
<td>float</td>
<td>N/A</td>
</tr>
<tr>
<td>gyro_y</td>
<td>float</td>
<td>float</td>
<td>N/A</td>
</tr>
<tr>
<td>gyro_z</td>
<td>float</td>
<td>float</td>
<td>N/A</td>
</tr>
<tr>
<td>magnet_x</td>
<td>float</td>
<td>float</td>
<td>N/A</td>
</tr>
<tr>
<td>magnet_y</td>
<td>float</td>
<td>float</td>
<td>N/A</td>
</tr>
<tr>
<td>magnet_z</td>
<td>float</td>
<td>float</td>
<td>N/A</td>
</tr>
</tbody>
</table>

### 85 - position <br> flight_controller &rarr; ground_station
#### fields
<table>
<thead>
<tr>
<th>name</th>
<th>type</th>
<th>native type</th>
<th>info</th>
</tr>
</thead>
<tbody>
<tr>
<td>altitude</td>
<td>float</td>
<td>float</td>
<td>N/A</td>
</tr>
<tr>
<td>longitude</td>
<td>float</td>
<td>float</td>
<td>N/A</td>
</tr>
<tr>
<td>latitude</td>
<td>float</td>
<td>float</td>
<td>N/A</td>
</tr>
</tbody>
</table>

### 86 - differential_pressure <br> flight_controller &rarr; ground_station
#### fields
<table>
<thead>
<tr>
<th>name</th>
<th>type</th>
<th>native type</th>
<th>info</th>
</tr>
</thead>
<tbody>
<tr>
<td>differential_pressure</td>
<td>float</td>
<td>float</td>
<td>N/A</td>
</tr>
</tbody>
</table>

## Enums
### flight_state
<table>
<thead>
<tr>
<th>name</th>
<th>value</th>
</tr>
</thead>
<tbody>
<tr>
<td>sleeping</td>
<td>0</td>
</tr>
<tr>
<td>idle</td>
<td>1</td>
</tr>
<tr>
<td>ready</td>
<td>2</td>
</tr>
<tr>
<td>burning</td>
<td>3</td>
</tr>
<tr>
<td>ascending</td>
<td>4</td>
</tr>
<tr>
<td>descending</td>
<td>5</td>
</tr>
<tr>
<td>drogue</td>
<td>6</td>
</tr>
<tr>
<td>main_chute</td>
<td>7</td>
</tr>
<tr>
<td>landed</td>
<td>8</td>
</tr>
</tbody>
</table>

### fix_status
<table>
<thead>
<tr>
<th>name</th>
<th>value</th>
</tr>
</thead>
<tbody>
<tr>
<td>no_fix</td>
<td>0</td>
</tr>
<tr>
<td>fix_2D</td>
<td>1</td>
</tr>
<tr>
<td>fix_3D</td>
<td>2</td>
</tr>
</tbody>
</table>

### nodes
<table>
<thead>
<tr>
<th>name</th>
<th>value</th>
</tr>
</thead>
<tbody>
<tr>
<td>local</td>
<td>0</td>
</tr>
<tr>
<td>ground_station</td>
<td>1</td>
</tr>
<tr>
<td>flight_controller</td>
<td>2</td>
</tr>
</tbody>
</table>

### fields
<table>
<thead>
<tr>
<th>name</th>
<th>value</th>
</tr>
</thead>
<tbody>
<tr>
<td>timestamp</td>
<td>0</td>
</tr>
<tr>
<td>system_time</td>
<td>1</td>
</tr>
<tr>
<td>state</td>
<td>2</td>
</tr>
<tr>
<td>is_parachute_armed</td>
<td>3</td>
</tr>
<tr>
<td>is_parachute1_en</td>
<td>4</td>
</tr>
<tr>
<td>is_parachute2_en</td>
<td>5</td>
</tr>
<tr>
<td>is_logging_en</td>
<td>6</td>
</tr>
<tr>
<td>dump_sd</td>
<td>7</td>
</tr>
<tr>
<td>dump_usb</td>
<td>8</td>
</tr>
<tr>
<td>is_fpv_en</td>
<td>9</td>
</tr>
<tr>
<td>is_tm_en</td>
<td>10</td>
</tr>
<tr>
<td>battery_1</td>
<td>11</td>
</tr>
<tr>
<td>battery_2</td>
<td>12</td>
</tr>
<tr>
<td>ms_since_boot</td>
<td>13</td>
</tr>
<tr>
<td>gnss_time</td>
<td>14</td>
</tr>
<tr>
<td>altitude</td>
<td>15</td>
</tr>
<tr>
<td>heading</td>
<td>16</td>
</tr>
<tr>
<td>horiz_speed</td>
<td>17</td>
</tr>
<tr>
<td>fix_status</td>
<td>18</td>
</tr>
<tr>
<td>n_satellites</td>
<td>19</td>
</tr>
<tr>
<td>h_dop</td>
<td>20</td>
</tr>
<tr>
<td>pressure</td>
<td>21</td>
</tr>
<tr>
<td>temperature</td>
<td>22</td>
</tr>
<tr>
<td>imu_id</td>
<td>23</td>
</tr>
<tr>
<td>accel_x</td>
<td>24</td>
</tr>
<tr>
<td>accel_y</td>
<td>25</td>
</tr>
<tr>
<td>accel_z</td>
<td>26</td>
</tr>
<tr>
<td>gyro_x</td>
<td>27</td>
</tr>
<tr>
<td>gyro_y</td>
<td>28</td>
</tr>
<tr>
<td>gyro_z</td>
<td>29</td>
</tr>
<tr>
<td>magnet_x</td>
<td>30</td>
</tr>
<tr>
<td>magnet_y</td>
<td>31</td>
</tr>
<tr>
<td>magnet_z</td>
<td>32</td>
</tr>
<tr>
<td>longitude</td>
<td>33</td>
</tr>
<tr>
<td>latitude</td>
<td>34</td>
</tr>
<tr>
<td>differential_pressure</td>
<td>35</td>
</tr>
</tbody>
</table>

### messages
<table>
<thead>
<tr>
<th>name</th>
<th>value</th>
</tr>
</thead>
<tbody>
<tr>
<td>local_timestamp</td>
<td>0</td>
</tr>
<tr>
<td>time_sync</td>
<td>1</td>
</tr>
<tr>
<td>set_state</td>
<td>2</td>
</tr>
<tr>
<td>set_parachute_output</td>
<td>3</td>
</tr>
<tr>
<td>set_data_logging</td>
<td>4</td>
</tr>
<tr>
<td>dump_flash</td>
<td>5</td>
</tr>
<tr>
<td>handshake</td>
<td>6</td>
</tr>
<tr>
<td>return_time_sync</td>
<td>7</td>
</tr>
<tr>
<td>return_power_mode</td>
<td>8</td>
</tr>
<tr>
<td>return_radio_equipment</td>
<td>9</td>
</tr>
<tr>
<td>return_parachute_output</td>
<td>10</td>
</tr>
<tr>
<td>onboard_battery_voltage</td>
<td>11</td>
</tr>
<tr>
<td>return_data_logging</td>
<td>12</td>
</tr>
<tr>
<td>return_dump_flash</td>
<td>13</td>
</tr>
<tr>
<td>return_handshake</td>
<td>14</td>
</tr>
<tr>
<td>ms_since_boot</td>
<td>15</td>
</tr>
<tr>
<td>GNSS_data</td>
<td>16</td>
</tr>
<tr>
<td>ms_raw</td>
<td>17</td>
</tr>
<tr>
<td>bmp_raw</td>
<td>18</td>
</tr>
<tr>
<td>imu_raw</td>
<td>19</td>
</tr>
<tr>
<td>position</td>
<td>20</td>
</tr>
<tr>
<td>differential_pressure</td>
<td>21</td>
</tr>
</tbody>
</table>

### categories
<table>
<thead>
<tr>
<th>name</th>
<th>value</th>
</tr>
</thead>
<tbody>
<tr>
<td>none</td>
<td>0</td>
</tr>
</tbody>
</table>
