import datetime

import requests
from PIL import Image
import io

def zpl_a_imagen(zpl_code, filename="etiqueta_actual.png"):
    url = "http://api.labelary.com/v1/printers/8dpmm/labels/2.95276x0.590551/0/"
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

def updatelabel(station, partNo, leak, serialnum):
    """Envía una solicitud de impresión a la impresora Zebra."""
    NivelCambio = Get_levelChange(partNo)

    currDate = datetime.datetime.now()
    currDate = currDate.strftime("%d%m%y%H%M%S")
    formatDate = currDate[0:2] + "/" + currDate[2:4] + "/" + currDate[4:6]
    ID_fabricante = "ZAR"
    line = station
    serialnum = str(serialnum).zfill(7)
    QR = f"{ID_fabricante}{currDate}{line}{partNo}-{serialnum}"

    command = f"""^XA
    ^MMT
    ^PW599
    ^LL128
    ^LS0
    ^FO482,16^GFA,561,960,12,:Z64:eJxV0z1uwzAMBWAKKqBM5ZqhiHqEHiCIrtQxQxCrN9NRdASOGgSrj/RPHA/OB8eybD6S6P2Yxs4whmxOY8ybB4680I/Goy5m3DC19XYsDOuCqRC59an2M9li3/Uci+3UKM3EthtXbEa+rf/iurM7U1bTYiqxu/xUP526JHX36hqxgWtcuXlh3V2iugXYSxK4B7y1r0mChNnDoSx2YsbK0NWc4cqdmjrujqS7xkYPNe++LBb1TWuSUYubOhyNQqR6gq8nD0/1dCF6rD5H+OxR5Kl8qb8cPI7OV/h+caO4zWR+8GIcZI6I9M0zdXOeit+dsoP1+ebuFheU8mUtsJnVKCjOV5QZT/AN73/j+kn0G5p+I8sn5Z8g6iAfLv+w+mL+ZtG6IWVXkPhqXyiq+a8jG6TfFiOrmJvmYk5/ltGTglDSjHy9afM8NUcvSABJaL5OmJDKXXN3LaiFs/VJjp2sT9A/OW39gxNM1lfx0G/owwl92Nb+xIwEOfStDYA79POxz9/6P+oX9XVexmte/JjTNkfH+Xqbu+M87nP6D25wEWg=:F482
    ^FO12,16^GFA,365,972,12,:Z64:eJy90rFKBDEQANAJG0wjt6bzqr1P8NjmhIX8yoJfIJYKu53NNXYWfswK4pX+Qo6Dsw0oGCEkJtnsJoV72ugU4RWTzDCZxvShAKD5D2sg31pNWEI+WkyYT7iDInoR3aauo6Fm0V3vjfU2uLPdfA62R5GYtM1B88QCiCRtmAkx5hZ6v9ham+BHo9BHsHuHJZ6h6KMfLBJrMAZnw1/o4mm0yt6jiRotiYzOJRksUhfRPDUT+eCOydF/umNTkeaY31heez94X2pmfewsrnQTDacr1LmcV3yB6Qlq3V2Od1VN52vnLd5XnFJvDvtq90bvg1eLcol8rbvnm7OyzLznvqzfSXPuzZLe2KGevwAudf68:54B9
    ^FT92,96^BXN,4,200,0,0,1,_,1^FH^FD{QR}
    ^FS^FT190,106^A0N,20,20^FH^CI28^FDSN:^FS^CI27
    ^FT359,83^A0N,23,23^FH\^CI28^FD{leak}
    ^FS^CI27^FT34,111^A0N,14,15^FH^CI28^FDMADE IN MEXICO^FS^CI27
    ^FT190,83^A0N,23,23^FH\^CI2x`8^FDRAD ASSY
    ^FS^CI27^FT190,60^A0N,25,25^FH^CI28^FDZAR        {NivelCambio}^FS^CI27
    ^FT190,37^A0N,31,30^FH\^CI28^FD{partNo}
    ^FS^CI27^FT225,106^A0N,20,20^FH^CI28^FD{serialnum}
    ^FS^CI27^FT297,106^A0N,20,20^FH^CI28^FDDATE:^FS^CI27
    ^FT357,106^A0N,20,20^FH\^CI28^FD{formatDate}
    ^FS^CI27^FT317,83^A0N,23,23^FH^CI28^FD2
    ^FS^CI27
    ^PQ1,,,Y
    ^XZ"""
    zpl_a_imagen(command)




updatelabel("3","5QM121251R","0.25", "9")





