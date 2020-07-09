import os
qp = [24, 32, 40]
for value in qp:
    script = 'cmd /c "ffmpeg -i "input.avi" -c:v libx265 -x265-params "qp=' + \
                str(value) + '" output_qp' + str(value) + '.265"'
    print(script)
    os.system(script)