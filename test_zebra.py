from datetime import datetime

import requests
from PIL import Image
import io
from Printer_Functions.Zebra_Printer import ZebraPrinterThread as Printer
def _updateLabel_BARCODE(code: str, label: int):
    # Obtiene los valores actuales de la Etiqueta
    partNo, serialNumber, station, year, month, day, format_date, leak_rate = _extract_label_data(code)
    print(station)
    BGR = "X58"
    Supplier = "ZAR"
    levelChange = Get_levelChange(partNo)
    serial = int(serialNumber, 36)
    serial = str(serial).zfill(5)
    date = f"{code[36:38]}/{code[38:40]}/{code[42:44]}"

    mode43 = mod43_check_char(f"{BGR} {Supplier}{year}{month}{day}{serialNumber}{station}")
    aditional_data = f"{format_date} {leak_rate}"
    DMC = f"#{partNo}    ###*{BGR} {Supplier}{year}{month}{day}{serialNumber}{station}{mode43}*={aditional_data}"

    command = f"""^XZ
    ^XA
    ^MMT
    ^PW599
    ^LL80
    ^LS0
    ^FT168,32^A0N,30,38^FH\^CI28^FD{partNo}^FS^CI27
    ^FO22,11^GFA,269,488,8,:Z64:eJyd0TEOgjAUBuBCE7rJwKITG6xGD4C34RiFuHIAnDiKL3oAjyCJBxDiwtD0+WgbIzDpW76k6f+a9yrRFMg/1Cw2KpZNHGZ2H6WxdcJhagHUN0PsRzl1K0jGWOgUpZWPAumRQ4xHz+Ze3OW4vbdy+t9SzhekkngRZo6ycyqrp0Ijt2o+GJVwhvTkz/tis0J3vvDR3GmTgNfzzboN1lxAG22rk59CK/b1ZpeTad0nZJBXURKCzrFBLUE/x49Y9n0D0QFG8g==:F85E
    ^FT89,73^BXN,2,200,32,32,1,_,1
    ^FH\^FD{DMC}^FS
    ^FT168,47^A0N,14,15^FH\^CI28^FDZAR^FS^CI27
    ^FT239,47^A0N,14,15^FH\^CI28^FD{levelChange}^FS^CI27
    ^FT168,60^A0N,14,15^FH\^CI28^FDRAD ASSY^FS^CI27
    ^FO521,8^GFA,401,512,8,:Z64:eJw9kcFtBCEMRf+IA7e4gWhdR6QRk5LmOJHQLqlgSwoVpISEEjgSCS35ZjcZAW/wt5D9Dfx/l9uEG6MYdYw2w02mMLgSZV4uTPC8Xyog38APEzdJaB04S1pqALrPS1WgGS3miis+2/n4q1SKp/LIaHyh2iu21TaWphmR7MYA17eCQN6MEf72UqHk1xvZIZ9Hg3Bd79TrQZGS7GdjkD1YL+RmjH7XPybqze+ShJRdsjSWdfg/Fu2uyOGKRm+s4ezz08pmg+TTihaDpEnV9HxCbKpYjfKBVbGZj4dgq96YtPqO6pMW1+lOluLaQmckL83luys+s6Rk7iC6hMJigwMKm9B34JV+SwZtgnU3t2OMZtmwFpsXtjHm/OQxz2WMPAdNv4BfaHyoLA==:26A2
    ^FT416,54^A0N,14,15^FH\^CI28^FDSN:^FS^CI27
    ^FT470,54^A0N,14,15^FH\^CI28^FD{serial}^FS^CI27
    ^FT416,21^A0N,14,15^FH\^CI28^FDDEVICE:^FS^CI27
    ^FT472,21^A0N,14,15^FH\^CI28^FD{station}^FS^CI27
    ^FT293,58^A0N,20,20^FH\^CI28^FDX58^FS^CI27
    ^FT416,70^A0N,14,15^FH\^CI28^FDDATE:^FS^CI27
    ^FT464,70^A0N,14,15^FH\^CI28^FD{date}^FS^CI27
    ^FT168,73^A0N,14,15^FH\^CI28^FDMADE IN MEXICO^FS^CI27
    ^PQ1,,,N
    ^XZ"""

    if label == 1:
        _convert_ZPL(command, "old_label.png")
    if label == 2:
        _convert_ZPL(command, "new_label.png")
def _extract_label_data(code: str):
        try:
            numero_parte = code[1:12].strip()
            año = code[26]
            mes = code[27]
            dia = code[28]
            numero_serie = code[29:32]
            cabina = code[32].strip()
            fecha_formateada = code[36:50]
            rate_fuga = float(code[51:].strip())
        except (IndexError, ValueError):
            numero_parte = año = mes = dia = numero_serie = cabina = fecha_formateada = rate_fuga = None

        return numero_parte, numero_serie, cabina, año, mes, dia, fecha_formateada, rate_fuga
def _convert_ZPL(zpl_code: str, filename="old_label.png"):
        url = "http://api.labelary.com/v1/printers/8dpmm/labels/2.95276x0.390551/0/"
        headers = {"Accept": "image/png", "Content-Type": "application/x-www-form-urlencoded"}

        response = requests.post(url, headers=headers, data=zpl_code.encode('utf-8'))

        if response.status_code == 200:
            img = Image.open(io.BytesIO(response.content))
            img.save(filename)
            print(f"Etiqueta guardada como {filename}")
            return img
        else:
            print("Error al generar la imagen:", response.text)
            return None
def Get_levelChange(partNo):
        niveles_cambio = {
            "5QM121251P": "07S",
            "5QM121251R": "06S",
            "5QM121251Q": "07S"
        }
        return niveles_cambio.get(partNo, "###")  # Retorna un valor por defecto si no encuentra la clave
def mod43_check_char(s_value: str) -> str:
        char_set = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ-. $/+%"
        s_value = s_value.strip().upper()
        total = 0

        for char in s_value:
            index = char_set.find(char)
            if index == -1:
                raise ValueError(f"Carácter inválido para MOD43: {char}")
            total += index

        check_char = char_set[total % 43]
        return check_char
#_updateLabel_BARCODE("#5QM121251R    ###*X58 ZAR83P0012$*=25042025161245 0.15",1)
partNo = "01052025031200"
ndate = datetime.strptime(partNo, "%d%m%Y%H%M%S")
print(ndate)