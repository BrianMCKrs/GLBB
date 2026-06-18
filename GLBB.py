### Menghitung GLBB
import math as math
import matplotlib.pyplot as plt

print('Apakah anda ingin menghitung GLBB? (Ya/Tidak)')
jawab = input()
print(' ')
if jawab.lower() == 'ya':
    print('Pilih rumus untuk menghitung Persamaan GLBB (\033[4m1\033[0m), Persamaan Jarak GLBB(\033[4m2\033[0m), atau Persamaan kecepatan sebagai fungsi jarak (\033[4m3\033[0m)')
    glbb = input()
    print(' ')
    if glbb.lower() == '1':
        print('Pilih rumus untuk menghitung kecepatan awal (\033[4mv0_1\033[0m), kecepatan akhir (\033[4mvt_1\033[0m), percepatan (\033[4ma_1\033[0m), waktu (\033[4mt_1\033[0m)')
        rumus1 = input()
        if rumus1.lower() == 'vt_1':
            a_11 = float(input('Percepatan dalam m/s/s: '))
            v0_11 = float(input('Kecepatan awal dalam m/s: '))
            t_11 = float(input('Waktu dalam s: '))
            vt_11 = v0_11 + a_11*t_11
            print('Kecepatan akhir adalah', round(vt_11, 2), 'm/s')
            print('Tampilkan dalam plot? (Ya/Tidak)')
            plotting11 = input()
            if plotting11.lower() == 'ya':
                plt.plot([0,vt_11],[0,vt_11],label = 'vt (m/s)')
                plt.axis((0,vt_11,0,vt_11))
                plt.xlabel('t (s)')
                plt.ylabel('v (m/s)')
                plt.legend(loc = 'upper left')
                plt.grid()
                plt.show()
                print('Gambar sudah ditampilkan')
            else: 
                print('Terima Kasih')
        elif rumus1.lower() == 'a_1':
            vt_12 = float(input('Kecepatan akhir dalam m/s: '))
            v0_12 = float(input('Kecepatan awal dalam m/s: '))
            t_12 = float(input('Waktu dalam s: '))
            a_12 = (vt_12/t_12) + v0_12
            print('Percepatnnya adalah', round(a_12, 2), 'm/s/s')
            print('Tampilkan dalam plot? (Ya/Tidak)')
            plotting12 = input()
            if plotting12.lower() == 'ya':
                plt.plot([0,a_12],[a_12,a_12],label = 'v (m/s)')
                plt.axis((0,a_12,0,a_12+3))
                plt.xlabel('t (s)')
                plt.ylabel('a (m/s)')
                plt.legend(loc = 'upper left')
                plt.grid()
                plt.show()
                print('Gambar sudah ditampilkan')
            else: 
                print('Terima Kasih')
        elif rumus1.lower() == 'v0_1':
            vt_13 = float(input('Kecepatan akhir dalam m/s: '))
            t_13 = float(input('Waktu dalam s: '))
            a_13 = float(input('Percepatan dalam m/s/s: '))
            v0_13 = vt_13 - a_13*t_13
            print('Kecepatan akhir adalah', round(v0_13, 2), 'm/s')
            print('Tampilkan dalam plot? (Ya/Tidak)')
            plotting13 = input()
            if plotting13.lower() == 'ya':
                plt.plot([vt_13,v0_13],[vt_13,v0_13],label = 'v (m/s)')
                plt.axis((v0_13,vt_13,v0_13,vt_13))
                plt.xlabel('t (s)')
                plt.ylabel('v (m/s)')
                plt.legend(loc = 'upper left')
                plt.grid()
                plt.show()
                print('Gambar sudah ditampilkan')
            else: 
                print('Terima Kasih')
        elif rumus1.lower() == 't_1':
            vt_14 = float(input('Kecepatan akhir dalam m/s: '))
            a_14 = float(input('Percepatan dalam m/s/s: '))
            v0_14 = float(input('Kecepatan awal dalam m/s: '))
            t_14 = vt_14/a_14 + v0_14
            print('Waktu yang ditempuh adalah', round(t_14, 2), 's')
            print('Tampilkan dalam plot? (Ya/Tidak)')
            plotting14 = input()
            if plotting14.lower() == 'ya':
                plt.plot([0,t_14],[0,t_14],label = 'v (m/s)')
                plt.axis((0,t_14,0,t_14))
                plt.xlabel('t (s)')
                plt.ylabel('v (m/s)')
                plt.legend(loc = 'upper left')
                plt.grid()
                plt.show()
                print('Gambar sudah ditampilkan')
            else: 
                print('Terima Kasih')
        else:
            print('Anda tidak menghitung GLBB')
    elif glbb.lower() == '2':
        print('Pilih rumus untuk menghitung kecepatan awal (\033[4mv0_2\033[0m), jarak (\033[4mx_2\033[0m), atau percepatan (\033[4ma_2\033[0m)')
        rumus2 = input()
        print(' ')
        if rumus2.lower() == 'x_2':
            v0_21 = float(input('Kecepatan awal dalam m/s: '))
            t_21 = float(input('Waktu dalam s: '))
            a_21 = float(input('Percepatan dalam m/s/s: '))
            s_21 = v0_21*t_21 + (1/2)*(a_21*t_21**2)
            print('Jarak yang ditempuh adalah', round(s_21, 2), 'm')
            print('Tampilkan dalam plot? (Ya/Tidak)')
            plotting21 = input()
            if plotting21.lower() == 'ya':
                plt.plot([0,s_21-(s_21*70/100),s_21-(s_21*60/100),s_21-(s_21*40/100),s_21-(s_21*15/100),s_21-(s_21*5/100),s_21],
                         [0,s_21-(s_21*92/100),s_21-(s_21*88/100),s_21-(s_21*74/100),s_21-(s_21*54/100),s_21-(s_21*25/100),s_21],label = 'v (m/s)')
                plt.axis((0,s_21,0,s_21))
                plt.xlabel('t (s)')
                plt.ylabel('s (m)')
                plt.legend(loc = 'upper left')
                plt.grid()
                plt.show()
                print('Gambar sudah ditampilkan')
            else: 
                print('Terima Kasih')
        elif rumus2.lower() == 'v0_2':
            s_22 = float(input('Jarak dalam m: '))
            t_22 = float(input('Waktu dalam s: '))
            a_22 = float(input('Percepatan dalam m/s/s: '))
            v0_22 = s_22/t_22 + (1/2)*(a_22 * t_22**2)
            print('Kecepatan awal adalah', round(v0_22, 2), 'm/s')
            print('Tampilkan dalam plot? (Ya/Tidak)')
            plotting22 = input()
            if plotting22.lower() == 'ya':
                plt.plot([v0_22,s_22/t_22],[s_22/t_22,v0_22],label = 'v (m/s)')
                plt.axis((s_22/t_22,v0_22 + 1,s_22/t_22,v0_22 + 1))
                plt.xlabel('t (s)')
                plt.ylabel('v (m/s)')
                plt.legend(loc = 'upper left')
                plt.grid()
                plt.show()
                print('Gambar sudah ditampilkan')
            else: 
                print('Terima Kasih')
        elif rumus2.lower() == 'a_2':
            s_23 = float(input('Jarak dalam m: '))
            t_23 = float(input('Waktu dalam s: '))
            v0_23 = float(input('Kecepatan awal dalam m/s: '))
            a_23 = v0_23*t_23 + (1/2)*(s_23/t_23**2)
            print('Percepatannya adalah', round(a_23, 2), 'm/s/s')
            print('Tampilkan dalam plot? (Ya/Tidak)')
            plotting23 = input()
            if plotting23.lower() == 'ya':
                plt.plot([0,a_23],[a_23,a_23],label = 'v (m/s)')
                plt.axis((0,a_23,0,a_23 + 1))
                plt.xlabel('t (s)')
                plt.ylabel('a (m/s)')
                plt.legend(loc = 'upper left')
                plt.grid()
                plt.show()
                print('Gambar sudah ditampilkan')
            else: 
                print('Terima Kasih')
        else:
            print('Anda tidak menghitung GLBB')
    elif glbb.lower() == '3':
        print('Pilih rumus untuk menghitung kecepatan awal (\033[4mv0_3\033[0m), jarak (\033[4mx_3\033[0m), kecepatan akhir (\033[4mvt_3\033[0m), atau percepatan (\033[4ma_3\033[0m)')
        rumus3 = input()
        print(' ')
        if rumus3.lower() == 'vt_3':
            a_31 = float(input('Percepatan dalam m/s/s: '))
            v0_31 = float(input('Kecepatan awal dalam m/s: '))
            s_31 = float(input('Jarak dalam m: '))
            vt_31 = math.sqrt(2*a_31*s_31) + v0_31
            print('Kecepatan akhir adalah', round(vt_31, 2), 'm/s')
            print('Tampilkan dalam plot? (Ya/Tidak)')
            plotting31 = input()
            if plotting31.lower() == 'ya':
                plt.plot([0,vt_31],[0,vt_31],label = 'v (m/s)')
                plt.axis((0,vt_31,0,vt_31))
                plt.xlabel('t (s)')
                plt.ylabel('v (m/s)')
                plt.legend(loc = 'upper left')
                plt.grid()
                plt.show()
                print('Gambar sudah ditampilkan')
            else: 
                print('Terima Kasih')
        elif rumus3.lower() == 'a_3':
            vt_32 = float(input('Kecepatan akhir dalam m/s: '))
            v0_32 = float(input('Kecepatan awal dalam m/s: '))
            s_32 = float(input('Jarak dalam m: '))
            a_32 = vt_32/(math.sqrt(s_32)) + v0_32
            print('Jarak yang ditempuh adalah', round(a_32, 2), 'm/s/s')
            print('Tampilkan dalam plot? (Ya/Tidak)')
            plotting32 = input()
            if plotting32.lower() == 'ya':
                plt.plot([0,a_32],[a_32,a_32],label = 'v (m/s)')
                plt.axis((0,a_32,0,a_32 + 3))
                plt.xlabel('t (s)')
                plt.ylabel('a (m/s)')
                plt.legend(loc = 'upper left')
                plt.grid()
                plt.show()
                print('Gambar sudah ditampilkan')
            else: 
                print('Terima Kasih')
        elif rumus3.lower() == 'v0_3':
            vt_33 = float(input('Kecepatan akhir dalam m/s: '))
            s_33 = float(input('Jarak dalam m: '))
            a_33 = float(input('Percepatan dalam m/s/s: '))
            v0_33 = math.sqrt(2*a_33*s_33) - vt_33
            print('Kecepatan awal adalah', round(v0_33, 2), 'm/s')
            print('Tampilkan dalam plot? (Ya/Tidak)')
            plotting33 = input()
            if plotting33.lower() == 'ya':
                plt.plot([v0_33,a_33/vt_33],[v0_33,a_33/vt_33],label = 'v (m/s)')
                plt.axis((v0_33,a_33/vt_33,v0_33,a_33/vt_33))
                plt.xlabel('t (s)')
                plt.ylabel('v (m/s)')
                plt.legend(loc = 'upper left')
                plt.grid()
                plt.show()
                print('Gambar sudah ditampilkan')
            else: 
                print('Terima Kasih')
        elif rumus3.lower() == 'x_3':
            v0_34 = float(input('Kecepatan awal dalam m/s: '))
            vt_34 = float(input('Kecepatan akhir dalam m/s: '))
            a_34 = float(input('Percepatan dalam m/s/s: '))
            s_34 = vt_34/(math.sqrt(a_34)) + v0_34
            print('Jarak yang ditempuh adalah', round(s_34, 2), 'm')
            print('Tampilkan dalam plot? (Ya/Tidak)')
            plotting34 = input()
            if plotting34.lower() == 'ya':
                plt.plot([0,s_34-(s_34*70/100),s_34-(s_34*60/100),s_34-(s_34*40/100),s_34-(s_34*15/100),s_34-(s_34*5/100),s_34],
                         [0,s_34-(s_34*92/100),s_34-(s_34*88/100),s_34-(s_34*74/100),s_34-(s_34*54/100),s_34-(s_34*25/100),s_34],label = 'v (m/s)')
                plt.axis((0,s_34,0,s_34))
                plt.xlabel('t (s)')
                plt.ylabel('s (m)')
                plt.legend(loc = 'upper left')
                plt.grid()
                plt.show()
                print('Gambar sudah ditampilkan')
            else: 
                print('Terima Kasih')
        else:
            print('Anda tidak menghitung GLBB')
else:
    print('\033[4mTerima Kasih!\033[0m')

### Link

### Grafik
### https://www.ophysics.com/k4.html

