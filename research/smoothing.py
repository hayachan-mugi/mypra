from scipy import signal

#Savitzky-Golyでは、測定値をいくつに分割するかを dn で設定し（窓の数は len(Y)/dn になります)、多項式次数を poly で設定します
# paramSG   = [ dn , poly ]
paramSG = [50, 5]
#Savitzky-Golyによりノイズ除去を行います
def SGs(y,dn,poly):
    # y as np.array, dn as int, poly as int
    n = len(y) // dn
    if n % 2 == 0:
        N = n+1
    elif n % 2 == 1:
        N = n
    else:
        print("window length can't set as odd")
    SGsmoothed = signal.savgol_filter(y, window_length=N, polyorder=poly)
    return SGsmoothed

    smth= SGs(fix, paramSG[0], paramSG[1])