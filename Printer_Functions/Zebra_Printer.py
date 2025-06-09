import datetime
import socket
import time

import select
from PySide6.QtCore import QThread, Signal, QTimer, QThreadPool, QRunnable, Slot


class PrinterCommandTask(QRunnable):
    """Ejecuta comandos a la impresora en un hilo separado sin bloquear la UI."""

    def __init__(self, host, port, command, response_size, timeout, callback, expect_response=True):
        super().__init__()
        self.host = host
        self.port = port
        self.command = command
        self.response_size = response_size
        self.timeout = timeout
        self.callback = callback
        self.expect_response = expect_response  # Nuevo parámetro

    def run(self):
        """Ejecuta la comunicación con la impresora Zebra en un hilo de QThreadPool."""
        try:
            with socket.create_connection((self.host, self.port), timeout=self.timeout) as sock:
                sock.sendall(self.command.encode('utf-8'))

                if self.expect_response:
                    response = sock.recv(self.response_size).decode('utf-8')
                    self.callback(response if response else "Error: No se recibió respuesta de la impresora.")
                else:
                    self.callback("Comando enviado sin esperar respuesta.")  # Opcional
        except socket.timeout as e:
            print(f"Timeout: {e}")
            self.callback("TIMEOUT")
        except socket.error as e:
            print(f"Error de red: {e}")
            self.callback(f"Error de red: {e}")
        except Exception as e:
            print(f"Otro error: {e}")
            self.callback(f"Otro error: {e}")

class ZebraPrinterThread(QThread):
    status_signal = Signal(str, int)  # Señal para el estado (mensaje, código)
    error_signal = Signal(str)  # Señal para errores

    def __init__(self, host, port=4100, interval=1000):  # Intervalo en ms
        super().__init__()
        self.host = host
        self.port = port
        self.interval = interval  # Tiempo entre verificaciones
        self.threadpool = QThreadPool.globalInstance()
        self.running = True  # Bandera para detener el hilo
        self.request_receive = True  # Marca que se está imprimiendo

    def run(self):
        """Inicia el temporizador para verificar la impresora sin bloquear la GUI."""
        self.timer = QTimer()
        self.timer.setInterval(self.interval)
        self.timer.timeout.connect(self.check_printer_status)
        self.timer.start()
        self.exec()  # Inicia el loop del hilo


    def stop(self):
        """Detiene el hilo y el temporizador correctamente."""
        self.running = False
        if self.timer:
            self.timer.stop()
        self.quit()
        self.wait()

    def _send_command(self, command, response_size=82, timeout=1):
        """Envía un comando de forma asincrónica usando un hilo de QThreadPool."""
        task = PrinterCommandTask(self.host, self.port, command, response_size, timeout, self._handle_response, self.request_receive)
        self.threadpool.start(task)

    def _handle_response(self, response):
        """Maneja la respuesta del socket sin bloquear la UI."""
        if response == "TIMEOUT":
            self.status_signal.emit("DESCONECTADA", 5)
            self.error_signal.emit("Timeout al comunicarse con la impresora")
        elif "Error de red" in response or "Otro error" in response:
            self.error_signal.emit(response)
        else:
            lines = response.splitlines()
            try:
                if len(lines) >= 2 and len(lines[0].split(",")) > 3 and len(lines[1].split(",")) > 3:
                    S1, S2 = lines[0].split(","), lines[1].split(",")
                    status, code = self.check_error(S1, S2)
                    self.status_signal.emit(status, code)
                else:
                    pass
                    #raise ValueError("Formato inesperado de respuesta.")
            except Exception as e:
                self.status_signal.emit("Respuesta inválida", 6)
                self.error_signal.emit(str(e))

    def check_printer_status(self):
        #print(self.printing_in_progress)
        """Obtiene el estado de la impresora de forma asíncrona solo si no se está imprimiendo."""
        #if self.running and not self.printing_in_progress:
        if self.running and self.request_receive:
            self._send_command("~HS")  # Comando para obtener el estado
    def check_error(self, m_string1, m_string2):
        """Analiza los estados de la impresora Zebra."""
        if m_string1[1] == "1":
            return "SIN ETIQUETA", 1
        elif m_string1[2] == "1" and m_string1[1] == "0" and m_string2[2] == "0":
            return "PAUSADA", 2
        elif m_string2[2] == "1":
            return "ABIERTA", 3
        elif m_string2[3] == "1":
            return "VERIFICAR RIBBON", 4
        return "CONECTADA", 0

    def Print_Request(self, partNo, serialNo, device, leak, date):
        Create_DMC = self.createDMC(partNo, serialNo, device, leak, date)
        DMC = Create_DMC[0]
        BGR = Create_DMC[1]
        serial = str(serialNo).zfill(5)

        fecha = datetime.datetime.strptime(date, "%d%m%Y%H%M%S")
        fecha_formateada = fecha.strftime("%d/%m/%y %H:%M:%S")

        _date = fecha_formateada[0:8]
        levelChange = self.Get_levelChange(partNo)

        curr_label_last = f"""^XA
        ~TA000
        ~JSN
        ^LT0
        ^MNW
        ^MTT
        ^PON
        ^PMN
        ^LH0,0
        ^JMA
        ^PR4,8
        ~SD30
        ^JUS
        ^LRN
        ^CI27
        ^PA0,1,1,0
        ^XZ
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
        ^FT472,21^A0N,14,15^FH\^CI28^FD{device}^FS^CI27
        ^FT293,58^A0N,20,20^FH\^CI28^FDX58^FS^CI27
        ^FT416,70^A0N,14,15^FH\^CI28^FDDATE:^FS^CI27
        ^FT464,70^A0N,14,15^FH\^CI28^FD{_date}^FS^CI27
        ^FT168,73^A0N,14,15^FH\^CI28^FDMADE IN MEXICO^FS^CI27
        ^PQ1,,,N
        ^XZ
        """
        curr_label =f"""^XA
        ~TA000
        ~JSN
        ^LT0
        ^MNW
        ^MTT
        ^PON
        ^PMN
        ^LH0,0
        ^JMA
        ^PR4
        ~SD30
        ^JUS
        ^LRN
        ^CI27
        ^PA0,1,1,0
        ^XZ
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
        ^FT472,21^A0N,14,15^FH\^CI28^FD{device}^FS^CI27
        ^FT249,60^A0N,14,15^FH\^CI28^FD{BGR}^FS^CI27
        ^FT464,70^A0N,14,15^FH\^CI28^FD{_date}^FS^CI27
        ^FT168,73^A0N,14,15^FH\^CI28^FDMADE IN MEXICO^FS^CI27
        ^FT416,70^A0N,14,15^FH\^CI28^FDDATE:^FS^CI27
        ^FT416,21^A0N,14,15^FH\^CI28^FDDEVICE:^FS^CI27
        ^PQ1,,,N
        ^XZ
        """
        self.request_receive = False
        self._send_command(curr_label)
        QTimer.singleShot(500, self.reset_flag)

    def reset_flag(self):
        self.request_receive = True

    def calibrate_label(self):
        """Envía un comando para calibrar la etiqueta."""
        self._send_command("~JC")
        self.error_signal.emit("Calibración enviada con éxito")

    def calibrate_speed(self):
        """Envía un comando para setear la velocidad de impresion."""
        speed = f"""^XA
        ^PR4
        ^XZ"""

        self._send_command(speed)
        self.error_signal.emit("Velocidad enviada con éxito")

    def calibrate_stroke(self):
        """Envía un comando para setear intensidad de impresion."""
        stroke = """^XA
        ~SD28
        ^XZ"""

        self._send_command(stroke)
        self.error_signal.emit("Intensidad enviada con éxito")

    def calibrate_temp(self):
        """Envía un comando para setear la temperatura de impresion."""
        temp = """^XA
        ^MT25
        ^XZ
        """
        self._send_command(temp)
        self.error_signal.emit("Temperatura enviada con éxito")
    @Slot()
    def Get_levelChange(self, partNo):
        niveles_cambio = {
            "5QM121251P": "08S",
            "5QM121251R": "07S",
            "5QM121251Q": "08S"
        }
        return niveles_cambio.get(partNo, "###")  # Retorna un valor por defecto si no encuentra la clave
    @Slot()
    def base10to36(self, data: int) -> str:
        dato = ''
        chars = '0123456789abcdefghijklmnopqrstuvwxyz'
        if data == 0:
            return '0'
        while data > 0:
            data, rem = divmod(data, 36)
            dato = chars[rem] + dato
        dato = dato.upper()
        print("base_36: ", dato)
        return dato
    @Slot()
    def MOD43CheckChar(self, dni: int) -> str:
        charSet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ-. $/+%"
        modulo = dni % 43
        letra = charSet[modulo]
        print(letra)
        return letra
    @Slot()
    def DayCheckChar(self, data: int) -> str:
        dato = self.base10to36(data)
        print("Dia: ", dato)
        return dato
    @Slot()
    def MonthCheckChar(self, dni: int) -> str:
        charSet = " 0123456789AB"
        letra = charSet[dni]
        print("Mes: ",letra)
        return letra
    @Slot()
    def YearCheckChar(self, dni: int) -> str:
        charSet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        modulo = dni - 2017
        letra = charSet[modulo]
        print("Año: ",letra)
        return letra
    @Slot()
    def CorrelativeNum(self, data: int) -> str:
        dato = self.base10to36(data)
        result = '0' * (3 - len(dato)) + dato
        print("Numero de Serie: ",result)
        return result
    @Slot()
    def mod43_check_char(self, s_value: str) -> str:
        char_set = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ-. $/+%"
        s_value = s_value.strip().upper()
        total = 0

        for char in s_value:
            index = char_set.find(char)
            if index == -1:
                raise ValueError(f"Carácter inválido para MOD43: {char}")
            total += index

        check_char = char_set[total % 43]
        print("Modulo 43: ", check_char)
        return check_char
    @Slot()
    def createDMC(self, partNo, serialNum, device, leak, date, BGR = "X58"):
        # Obtenemos el dia, mes y año actual
        day = int(date[0:2])
        month = int(date[2:4])
        year = int(date[4:8])

        # Convierte datos a base 36
        get_year = self.YearCheckChar(year)
        get_month = self.MonthCheckChar(month)
        get_day = self.DayCheckChar(day)
        get_numCorrelative = self.CorrelativeNum(serialNum)

        # define el BGR del componente
        Supplier = "ZAR"
        line = device
        leak = f"{leak:.2f}"

        mode43 = self.mod43_check_char(f"{BGR} {Supplier}{get_year}{get_month}{get_day}{get_numCorrelative}{line}")
        BGR_Data = f"{BGR} {Supplier}{get_year}{get_month}{get_day}{get_numCorrelative}{line}{mode43}"
        aditional_data = f"{date} {leak}"
        DMC_actual = f"#{partNo}    ###*{BGR} {Supplier}{get_year}{get_month}{get_day}{get_numCorrelative}{line}{mode43}*={aditional_data}"
        print(DMC_actual)
        return DMC_actual, BGR_Data

