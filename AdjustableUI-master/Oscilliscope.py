from RsInstrument import *
from test import *
import pyautogui as p
import keyboard


def Oscilloscope():
    global instr
    while True:
        address = p.password(text='Only IP', mask='', default='eg.\t192.168.0.2')  # 'TCPIP::10.65.1.116::inst0::INSTR'
        try:
            instr = RsInstrument('TCPIP::' + address + '::inst0::INSTR', True, False)
            break
        except:
            print("Couldn't connect...")
            # print('Your instrument is probably OFF...')
        if keyboard.is_pressed('q'):
            break

    # Declare all variables
    instr.write('SYSTem:DISPlay:UPDate ON')

    scal_str = 'CHAN1:SCAL {}'
    range_str = 'CHAN1:RANG {}'
    tim_scal_str = 'TIM:SCAL {}'
    tim_range_str = 'TIM:RANG {}'
    trig_level_str = 'TRIG1:LEV1 {}'
    curs1_left_posn_str = 'CURS1:X1P {}'
    curs1_right_posn_str = 'CURS1:X2P {}'
    curs1_top_posn_str = 'CURS1:Y1P {}'
    curs1_bottom_posn_str = 'CURS1:Y2P {}'
    curs2_left_posn_str = 'CURS2:X1P {}'
    curs2_right_posn_str = 'CURS2:X2P {}'
    curs2_top_posn_str = 'CURS2:Y1P {}'
    curs2_bottom_posn_str = 'CURS2:Y2P {}'
    osc_area_array = []
    comp_area_array = []
    new_array_area1 = []
    new_array_area2 = []
    new_array_area3 = []
    new_array_area4 = []
    cummulative_array_area = []

    index = 0
    sum = 0
    sum34 = 0
    sum35 = 0
    left1 = 0
    right1 = 0
    left2 = 0
    right2 = 0
    final_area1 = 0
    final_area2 = 0
    final_area3 = 0
    final_area4 = 0
    start_time = datetime.now()
    previous_time = datetime.now()

    # Infinite while loop started
    while True:

        instr.write('SYSTem:DISPlay:UPDate ON')
        instr.write('MEAS1:ENAB ON')
        instr.write('MEAS1:CAT AMPT')
        instr.write('MEAS1:SOUR C1W1')
        instr.write('MEAS1:MAIN AREA')
        meas_area = instr.query_str('MEAS1:ARES?')  # Gets Area from Oscilloscope

        area_list = meas_area.split(',')  # Splits the Area List as measured area is the first item
        measured_area = float(area_list[0])  # This is the area as reported by the oscilloscope
        instr.query_str('*OPC?')
        instr.write('EXP:WAV:INCX ON')
        data = instr.query_str('CHAN1:WAV:DATA:VAL?')  # This is where we get the waveform from Oscilloscope
        instr.query_str('*OPC?')
        instr.write('*OPC')

        num_array1 = convert_string_to_data(data)  # The data comes as a string. Here it is converted to a array
        num_array_dict1 = Convert(num_array1)
        xax1 = [float(x) for x in list(num_array_dict1.keys())]
        yax1 = [float(x) for x in list(num_array_dict1.values())]
        xax_array1 = np.array(xax1)
        yax_array1 = np.array(yax1)

        left_xax_array1 = xax_array1[0:int(len(xax_array1) / 2)]
        right_xax_array1 = xax_array1[int(len(xax_array1) / 2):]
        left_yax_array1 = yax_array1[0:int(len(yax_array1) / 2)]
        right_yax_array1 = yax_array1[int(len(yax_array1) / 2):]

        left_minimum = np.min(left_yax_array1)
        right_minimum = np.min(right_yax_array1)
        left_ab = left_yax_array1 + abs(0.95 * left_minimum)
        right_ab = right_yax_array1 + abs(0.95 * right_minimum)
        # print("Left Min:",left_minimum,"Right Min:",right_minimum)

        left_maxi = np.max(left_yax_array1)
        right_maxi = np.max(right_yax_array1)
        area1 = np.trapz(yax_array1, xax_array1)

        left_yax_array1[left_yax_array1 < 0] = 0
        right_yax_array1[right_yax_array1 < 0] = 0
        left_ab[left_ab < 0] = 0
        right_ab[right_ab < 0] = 0

        left_area_a1 = np.trapz(left_yax_array1, left_xax_array1)
        left_area_ab1 = np.trapz(left_ab, left_xax_array1)
        right_area_a1 = np.trapz(right_yax_array1, right_xax_array1)
        right_area_ab1 = np.trapz(right_ab, right_xax_array1)
        time_diff = datetime.now() - previous_time
        ##print(datetime.now())
        # print(previous_time)

        delta_t_str = str(time_diff)
        delta_t = float(delta_t_str[6:])
        # print(delta_t)

        if left_area_a1 < 0:
            sum34 = sum34
        else:
            sum34 = sum34 + left_area_a1 * delta_t * 455600
        # print(left_area_a1)
        previous_time = datetime.now()
        # print(sum34)

        left11, right11 = zero_crossing(left_xax_array1, left_yax_array1)
        left12, right12 = zero_crossing(left_xax_array1, left_ab)
        left21, right21 = zero_crossing(right_xax_array1, left_yax_array1)
        left22, right22 = zero_crossing(right_xax_array1, left_ab)
        # print("left1:",left11,"Right1",right11)
        # print("left2:", left12, "Right2", right12)

        instr.write('CURS1:FUNC PAIR')
        instr.write('CURS1:STAT ON')
        instr.write('CURS2:FUNC PAIR')
        instr.write('CURS2:STAT ON')
        # instr.write('CURS3:FUNC HOR')
        # instr.write('CURS3:STAT ON')

        instr.write(curs1_left_posn_str.format(left11))
        instr.write(curs1_right_posn_str.format(right11))
        instr.write(curs1_top_posn_str.format(left_maxi))
        instr.write(curs1_bottom_posn_str.format(left_minimum))
        instr.write(curs2_left_posn_str.format(left21))
        instr.write(curs2_right_posn_str.format(right21))
        # instr.write(curs2_top_posn_str.format(right_maxi))
        # instr.write(curs2_bottom_posn_str.format(right_minimum))

        new_array_area1.append(left_area_ab1 * 1640000)  # 1left a+b
        new_array_area2.append(left_area_a1 * 1640000)  # 1left a
        new_array_area3.append(right_area_ab1 * 1640000)  # 2left a+b
        new_array_area4.append(right_area_a1 * 1640000)  # 2left a       

